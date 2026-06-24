#!/usr/bin/env python3
"""
openpecha_kangyur.py — extract one Kangyur work (by Tohoku no.) from the
OpenPecha Degé Kangyur (P000001, .opf format) into a 1-SOURCES/ Tibetan file.

Source: OpenPecha/P000001 (Esukhia digital Degé Kangyur). The Tibetan root is a
mechanical reproduction of a public-domain woodblock edition → **Public Domain**.
See vault-annex §7.

The .opf format stores clean base text per volume (base/vNNN.txt) plus annotation
layers. We use:
  - index.yml      : maps work_id "T<N>" (Tohoku) -> character span(s) per volume
  - Pagination.yml : maps char spans -> Degé page images (the canonical citation)

Output scheme: verse_id_format `derge-page`. The work is segmented by **Degé
folio page** (faithful, citable — fine verse numbering comes later from aligning
with 84000). Each page becomes a block `^p<imgnum>`. No verse structure is
fabricated. Intra-line wrap newlines are removed; Tibetan punctuation kept.

CLI:
  python openpecha_kangyur.py --opf /path/P000001.opf --work T326 \\
     --slug udanavarga --title "Udānavarga (ched du brjod pa'i tshoms), Toh 326" \\
     --out 1-SOURCES/Text/bo-udanavarga.md
"""
from __future__ import annotations
import argparse, re
from pathlib import Path
import yaml


def yaml_block(meta: dict) -> str:
    out = ["---"]
    for k, v in meta.items():
        if isinstance(v, bool):
            out.append(f"{k}: {str(v).lower()}")
        elif isinstance(v, str) and (":" in v or v.startswith(("#", "[", "&", "*"))):
            out.append(f'{k}: "{v.replace(chr(34), "")}"')
        else:
            out.append(f"{k}: {v}")
    out.append("---")
    return "\n".join(out)


def find_spans(index_path, work_id):
    idx = yaml.safe_load(open(index_path, encoding="utf-8"))
    spans = []
    for a in idx["annotations"].values():
        if a.get("work_id") == work_id and a.get("span"):
            spans = a["span"]
        for p in (a.get("parts") or {}).values():
            if p.get("work_id") == work_id:
                spans = p["span"]
    return spans


def pages_for(opf, vol, start, end):
    pg = yaml.safe_load(open(f"{opf}/layers/v{vol:03d}/Pagination.yml", encoding="utf-8"))
    items = []
    for ann in pg["annotations"].values():
        s = ann["span"]["start"]; e = ann["span"]["end"]
        if e <= start or s >= end:
            continue
        items.append((max(s, start), min(e, end), ann.get("imgnum"), ann.get("reference", "")))
    return sorted(items)


def convert(opf, work, slug, title, out_path):
    spans = find_spans(f"{opf}/index.yml", work)
    if not spans:
        raise SystemExit(f"work {work} not found in index.yml")

    meta = {
        "title": title,
        "author": "Buddha (buddhavacana); Kangyur (mdo / sūtra section)",
        "language": "Classical Tibetan",
        "script": "Tibetan (Unicode)",
        "file_type": "root-text",
        "lang_tag": "bo",
        "verse_id_format": "derge-page",
        "canon": "Tibetan Kangyur (Degé)",
        "tohoku": work.lstrip("T"),
        "source_description": "OpenPecha P000001 (Esukhia digital Degé Kangyur); BDRC W22084.",
        "source_url": "https://github.com/OpenPecha/P000001",
        "license": "public-domain",
        "license_url": "https://creativecommons.org/publicdomain/mark/1.0/",
        "rights_holder": "Public domain (Degé woodblock); digitisation by Esukhia/OpenPecha",
        "commercial_use": True,
        "derivatives_allowed": True,
        "attribution_required": False,
        "usage_status": "cleared",
        "status": "draft",
    }
    out = [yaml_block(meta), "", f"# {title}\n",
           "> Public-domain Degé Kangyur Tibetan (mdo section). Segmented by Degé folio page "
           "(`^p<imgnum>`). Modern translations are produced in-vault; 84000's English may be "
           "consulted as a verbatim reference (vault-annex §7). No verse structure is fabricated here.\n"]

    total_pages = 0
    for sp in spans:
        vol = sp["vol"]; start = sp["start"]; end = sp["end"]
        base = open(f"{opf}/base/v{vol:03d}.txt", encoding="utf-8").read()
        out.append(f"## Degé Kangyur vol. {vol} (Tohoku {work.lstrip('T')})\n")
        for s, e, imgnum, ref in pages_for(opf, vol, start, end):
            txt = base[s:e].replace("\n", "").strip()
            if not txt:
                continue
            total_pages += 1
            out.append(f"{txt} ^p{imgnum}\n")
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_path).write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote {out_path}: {total_pages} page-blocks across {len(spans)} span(s)")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--opf", required=True, help="path to P000001.opf")
    ap.add_argument("--work", required=True, help="Tohoku work id, e.g. T326")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    convert(args.opf, args.work, args.slug, args.title, args.out)


if __name__ == "__main__":
    main()
