#!/usr/bin/env python3
"""
suttacentral_bilara.py — converter for SuttaCentral *bilara-data* JSON.

SuttaCentral's bilara-data stores each text as flat JSON dicts keyed by
**segment id** (e.g. "dhp1:1", "mn1:1.2"), one dict per layer:

    root/pli/ms/...   — Pāli root text        (segment-id -> Pāli)
    translation/en/sujato/... — Sujato English (segment-id -> English, CC0)

The same segment ids align the layers, so a root file and a translation file
for the same uid range merge cleanly. This converter targets **verse
collections** (Dhammapada and the other Khuddaka verse texts), producing the
`verse_id_format: verse` scheme defined in `4-SYSTEM/Guidelines/vault-annex.md` §2(a):

    - one `##` heading per vagga (chapter), anchored `^vagga-N-0`
    - each canonical verse -> its own block, `^<verse-number>`
    - the verse number is the integer in the segment uid ("dhp17" -> 17)

It emits TWO files from one or more (root, translation) pairs:
    - a Pāli root-text file   -> 1-SOURCES/Text/pi-<slug>.md
    - an English translation  -> 1-SOURCES/Translations/en-<slug>-sujato.md
both carrying the licensing frontmatter required by the annex §7 (CC0).

Segment rules:
    - keys whose sub-part starts with "0"  (e.g. "dhp1:0.3") are front matter:
      the ":0.3" piece carries the vagga title; ":0.4" etc. are vatthu labels.
    - a verse line is any segment present in BOTH the root and the translation
      whose sub-part does NOT start with "0". This naturally drops vatthu
      labels and vagga colophons (which are untranslated, root-only).

CLI:
    python suttacentral_bilara.py --slug dhammapada --title "Dhammapada" \\
        --root r1.json r2.json ... --tr t1.json t2.json ... \\
        --out-text 1-SOURCES/Text/pi-dhammapada.md \\
        --out-tr   1-SOURCES/Translations/en-dhammapada-sujato.md

`--root`/`--tr` take matching ordered lists (one vagga file each). Order
determines vagga numbering.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

VERSE_UID_RE = re.compile(r"^([a-z]+)(\d+)$")   # "dhp17" -> ("dhp", "17")


def load(path: str) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def seg_parts(seg_id: str):
    """'dhp1:0.3' -> ('dhp1', '0.3'); 'dhp17:2' -> ('dhp17', '2')."""
    uid, _, sub = seg_id.partition(":")
    return uid, sub


def is_frontmatter_sub(sub: str) -> bool:
    return sub.split(".")[0] == "0"


def yaml_block(meta: dict) -> str:
    lines = ["---"]
    for k, v in meta.items():
        if isinstance(v, bool):
            lines.append(f"{k}: {str(v).lower()}")
        elif isinstance(v, str) and (":" in v or v.startswith(("#", "[", "*", "&"))):
            esc = v.replace('"', '\\"')
            lines.append(f'{k}: "{esc}"')
        else:
            lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def build(root_files, tr_files, slug, title, *, source_uid_hint=""):
    """Return (text_md, translation_md)."""
    pli_meta = {
        "title": title,
        "author": "Traditional (buddhavacana)",
        "language": "Pāli",
        "script": "Roman-PTS",
        "file_type": "root-text",
        "lang_tag": "pi",
        "verse_id_format": "verse",
        "canon": "Pali Canon (Khuddaka Nikāya)",
        "source_description": "SuttaCentral bilara-data, Mahāsaṅgīti Tipiṭaka (root/pli/ms).",
        "source_url": "https://suttacentral.net/",
        "suttacentral_uid": source_uid_hint or slug,
        "license": "CC0",
        "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
        "rights_holder": "SuttaCentral (Mahāsaṅgīti edition)",
        "commercial_use": True,
        "derivatives_allowed": True,
        "attribution_required": False,
        "usage_status": "cleared",
        "status": "draft",
    }
    en_meta = dict(pli_meta)
    en_meta.update({
        "title": f"{title} (English, Sujato)",
        "author": "Bhikkhu Sujato (translator)",
        "language": "English",
        "script": "Roman",
        "file_type": "translation",
        "lang_tag": "en",
        "root_text": f"1-SOURCES/Text/pi-{slug}.md",
        "translation_basis": "SuttaCentral / Mahāsaṅgīti Pāli",
        "source_description": "Bhikkhu Sujato's English translation from SuttaCentral bilara-data (translation/en/sujato).",
        "rights_holder": "Bhikkhu Sujato",
    })

    text_out = [yaml_block(pli_meta), ""]
    tr_out = [yaml_block(en_meta), ""]
    text_out.append(f"# {title}\n")
    tr_out.append(f"# {title} — English (Bhikkhu Sujato, CC0)\n")

    for vagga_n, (rf, tf) in enumerate(zip(root_files, tr_files), start=1):
        root = load(rf)
        tr = load(tf)

        # vagga title: prefer the translation's ":0.3" piece, else root's
        def fm_title(d):
            cands = {seg_parts(k)[1]: v.strip() for k, v in d.items()
                     if is_frontmatter_sub(seg_parts(k)[1])}
            return cands.get("0.3") or cands.get("0.2") or ""
        pli_title = re.sub(r"^\s*\d+\.\s*", "", fm_title(root)).strip()
        en_title = re.sub(r"^\s*\d+\.\s*", "", fm_title(tr)).strip()

        text_out.append(f"## {vagga_n}. {pli_title} ^vagga-{vagga_n}-0\n")
        tr_out.append(f"## {vagga_n}. {en_title or pli_title} ^vagga-{vagga_n}-0\n")

        # group verse-line segments by verse uid, preserving order
        order = []
        verses = {}
        for seg_id, pli_text in root.items():
            uid, sub = seg_parts(seg_id)
            if is_frontmatter_sub(sub):
                continue
            if seg_id not in tr:            # untranslated -> colophon/label, skip
                continue
            if uid not in verses:
                verses[uid] = {"pli": [], "en": []}
                order.append(uid)
            verses[uid]["pli"].append(pli_text.strip())
            verses[uid]["en"].append(tr[seg_id].strip())

        for uid in order:
            m = VERSE_UID_RE.match(uid)
            vnum = m.group(2) if m else uid
            pli_body = "<br>".join(s for s in verses[uid]["pli"] if s)
            en_body = "<br>".join(s for s in verses[uid]["en"] if s)
            text_out.append(f"{pli_body} ^{vnum}\n")
            tr_out.append(f"{en_body} ^{vnum}\n")

    return "\n".join(text_out) + "\n", "\n".join(tr_out) + "\n"


# ─────────────────────────────────────────────────────────────────────────────
# Nested mode: collections stored as vagga subfolders with one file per sutta
# (Sutta Nipāta, Udāna, Itivuttaka). These are mixed prose+verse suttas, so they
# use the segment-id block scheme (vault-annex §2b): a segment id like
# "snp1.10:1.1" becomes block id "^snp1-10-1-1".
# ─────────────────────────────────────────────────────────────────────────────

def dashify(seg_id: str) -> str:
    return seg_id.replace(":", "-").replace(".", "-")


def _num_key(s: str):
    return [int(n) for n in re.findall(r"\d+", s)]


def _group_label(dirname: str) -> str:
    """Nice section heading from a subfolder name."""
    for pat, word in ((r"^vagga(\d+)$", "Vagga"),
                      (r"^sn(\d+)$", "Saṁyutta"),
                      (r"^an(\d+)$", "Aṅguttara Nipāta")):
        m = re.match(pat, dirname)
        if m:
            return f"{word} {m.group(1)}"
    return dirname


def _meta_nested(slug, title, *, is_tr):
    meta = {
        "title": title if not is_tr else f"{title} (English, Sujato)",
        "author": "Buddha (buddhavacana)" if not is_tr else "Bhikkhu Sujato (translator)",
        "language": "Pāli" if not is_tr else "English",
        "script": "Roman-PTS" if not is_tr else "Roman",
        "file_type": "root-text" if not is_tr else "translation",
        "lang_tag": "pi" if not is_tr else "en",
        "verse_id_format": "suttacentral-segment",
        "canon": "Pali Canon (Khuddaka Nikāya)",
        "source_description": ("SuttaCentral bilara-data, Mahāsaṅgīti Tipiṭaka (root/pli/ms)."
                               if not is_tr else
                               "Bhikkhu Sujato's English from SuttaCentral bilara-data (translation/en/sujato)."),
        "source_url": "https://suttacentral.net/",
        "license": "CC0",
        "license_url": "https://creativecommons.org/publicdomain/zero/1.0/",
        "rights_holder": "SuttaCentral (Mahāsaṅgīti edition)" if not is_tr else "Bhikkhu Sujato",
        "commercial_use": True,
        "derivatives_allowed": True,
        "attribution_required": False,
        "usage_status": "cleared",
        "status": "draft",
    }
    if is_tr:
        meta["root_text"] = f"1-SOURCES/Text/pi-{slug}.md"
    return meta


def build_nested(root_dir, tr_dir, slug, title):
    root_dir, tr_dir = Path(root_dir), Path(tr_dir)
    files = sorted(root_dir.rglob("*_root-pli-ms.json"),
                   key=lambda p: (_num_key(p.parent.name), _num_key(p.stem.split("_")[0])))

    text_out = [yaml_block(_meta_nested(slug, title, is_tr=False)), "", f"# {title}\n"]
    tr_out = [yaml_block(_meta_nested(slug, title, is_tr=True)), "",
              f"# {title} — English (Bhikkhu Sujato, CC0)\n"]

    cur_vagga = None
    for rf in files:
        rel = rf.relative_to(root_dir)
        tf = tr_dir / rel.parent / rf.name.replace("_root-pli-ms.json", "_translation-en-sujato.json")
        root = load(str(rf))
        tr = load(str(tf)) if tf.exists() else {}
        uid = rf.stem.split("_")[0]

        # group heading from the subfolder (skip for flat collections like DN/MN)
        flat = (rf.parent == root_dir)
        if not flat:
            vagga = rf.parent.name
            if vagga != cur_vagga:
                cur_vagga = vagga
                text_out.append(f"## {_group_label(vagga)} ^{vagga}-0\n")
                tr_out.append(f"## {_group_label(vagga)} ^{vagga}-0\n")
        sutta_level = "##" if flat else "###"

        # sutta heading: ref = first 0.x segment, name = last 0.x segment
        def fm(d):
            fmsegs = [(k, v.strip()) for k, v in d.items() if is_frontmatter_sub(seg_parts(k)[1])]
            ref = fmsegs[0][1] if fmsegs else uid
            name = fmsegs[-1][1] if fmsegs else ""
            return ref, name
        r_ref, r_name = fm(root)
        e_ref, e_name = fm(tr)
        anchor = f"^{dashify(uid)}-0"
        text_out.append(f"{sutta_level} {r_name} ({r_ref}) {anchor}\n")
        tr_out.append(f"{sutta_level} {e_name or r_name} ({e_ref or r_ref}) {anchor}\n")

        # content segments (sub not starting with 0), each its own block
        for seg_id, txt in root.items():
            if is_frontmatter_sub(seg_parts(seg_id)[1]):
                continue
            t = txt.strip()
            if t:
                text_out.append(f"{t} ^{dashify(seg_id)}\n")
        for seg_id, txt in tr.items():
            if is_frontmatter_sub(seg_parts(seg_id)[1]):
                continue
            t = txt.strip()
            if t:
                tr_out.append(f"{t} ^{dashify(seg_id)}\n")

    return "\n".join(text_out) + "\n", "\n".join(tr_out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--root", nargs="+", required=True,
                    help="ordered root pli json files; or a single root DIR with --nested")
    ap.add_argument("--tr", nargs="+", required=True,
                    help="ordered translation json files; or a single translation DIR with --nested")
    ap.add_argument("--out-text", required=True)
    ap.add_argument("--out-tr", required=True)
    ap.add_argument("--uid-hint", default="")
    ap.add_argument("--nested", action="store_true",
                    help="treat --root/--tr as collection directories (vagga subfolders, per-sutta files)")
    args = ap.parse_args()

    if args.nested:
        text_md, tr_md = build_nested(args.root[0], args.tr[0], args.slug, args.title)
    else:
        if len(args.root) != len(args.tr):
            ap.error("--root and --tr must have the same number of files (paired by vagga)")
        text_md, tr_md = build(args.root, args.tr, args.slug, args.title,
                               source_uid_hint=args.uid_hint)

    Path(args.out_text).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_tr).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_text).write_text(text_md, encoding="utf-8")
    Path(args.out_tr).write_text(tr_md, encoding="utf-8")
    print(f"Wrote {args.out_text}  and  {args.out_tr}")


if __name__ == "__main__":
    main()
