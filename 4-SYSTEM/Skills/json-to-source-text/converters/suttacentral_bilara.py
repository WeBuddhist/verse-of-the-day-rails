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


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--root", nargs="+", required=True, help="ordered root pli json files")
    ap.add_argument("--tr", nargs="+", required=True, help="ordered translation json files")
    ap.add_argument("--out-text", required=True)
    ap.add_argument("--out-tr", required=True)
    ap.add_argument("--uid-hint", default="")
    args = ap.parse_args()

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
