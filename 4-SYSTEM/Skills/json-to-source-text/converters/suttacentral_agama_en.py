#!/usr/bin/env python3
"""
suttacentral_agama_en.py — assemble SuttaCentral's (partial) English Āgama
translations into a 1-SOURCES/Translations/ reference layer.

These are CC0 (SuttaCentral bilara LICENSE: all Bilara translations are CC0).
Coverage is partial (e.g. Charles Patton's SĀ/MĀ selections), so this is a
*reference* translation layer, keyed by **sūtra number** so it cross-links to
the CBETA Chinese source (which uses CBETA paragraph ids, a different
segmentation — the shared bridge is the Taishō sūtra number).

Block scheme: `verse_id_format: suttacentral-sutta`; each sūtra is one block
`^<abbr><n>` (e.g. ^sa262), cross-referenced to `zh-<agama>.md#^<abbr><n>-0`.

CLI:
  python suttacentral_agama_en.py --tr-dir <bilara>/translation/en/patton/sutta/sa \\
     --abbr sa --label SĀ --slug samyukta-agama --translator "Charles Patton" \\
     --out 1-SOURCES/Translations/en-samyukta-agama-patton.md
"""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

def yaml_block(meta):
    out=["---"]
    for k,v in meta.items():
        if isinstance(v,bool): out.append(f"{k}: {str(v).lower()}")
        elif isinstance(v,str) and (":" in v or v.startswith(("#","[","&","*"))): out.append(f'{k}: "{v}"')
        else: out.append(f"{k}: {v}")
    out.append("---"); return "\n".join(out)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--tr-dir",required=True); ap.add_argument("--abbr",required=True)
    ap.add_argument("--label",required=True); ap.add_argument("--slug",required=True)
    ap.add_argument("--translator",default="Charles Patton"); ap.add_argument("--out",required=True)
    a=ap.parse_args()

    files=sorted(Path(a.tr_dir).rglob(f"{a.abbr}*_translation-en-*.json"),
                 key=lambda p:[int(n) for n in re.findall(r"\d+",p.stem.split("_")[0])])
    meta={
        "title": f"{a.label} — partial English (reference)",
        "translator": a.translator,
        "language":"English","script":"Roman","file_type":"translation","lang_tag":"en",
        "verse_id_format":"suttacentral-sutta",
        "canon":"Chinese Āgama (Taishō)",
        "root_text": f"1-SOURCES/Text/zh-{a.slug}.md",
        "source_description": f"SuttaCentral bilara-data, {a.translator}'s English {a.label} translation (partial).",
        "source_url":"https://suttacentral.net/",
        "license":"CC0","license_url":"https://creativecommons.org/publicdomain/zero/1.0/",
        "rights_holder": a.translator,
        "commercial_use":True,"derivatives_allowed":True,"attribution_required":False,
        "usage_status":"cleared","coverage":"partial — reference layer","status":"draft",
    }
    out=[yaml_block(meta),"",f"# {a.label} — partial English translation (CC0, {a.translator})\n",
         f"> Partial reference layer ({len(files)} sūtras). Cross-links to the Chinese source by "
         f"sūtra number: each `^{a.abbr}N` ↔ `1-SOURCES/Text/zh-{a.slug}.md#^{a.abbr}N-0`. CC0.\n"]
    for f in files:
        d=json.load(open(f,encoding="utf-8")); uid=f.stem.split("_")[0]
        num=re.sub(rf"^{a.abbr}","",uid)
        fm=[v.strip() for k,v in d.items() if k.split(":")[1].split(".")[0]=="0"]
        title=fm[-1] if fm else ""
        body=" ".join(v.strip() for k,v in d.items() if k.split(":")[1].split(".")[0]!="0" and v.strip())
        body=re.sub(r"\s+"," ",body).strip()
        out.append(f"## {a.label} {num} — {title} ^{a.abbr}{num}\n")
        out.append(f"*Source:* [[1-SOURCES/Text/zh-{a.slug}.md#^{a.abbr}{num}-0|{a.label} {num} (Chinese)]]\n")
        out.append(body+"\n")
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text("\n".join(out)+"\n",encoding="utf-8")
    print(f"Wrote {a.out}: {len(files)} sūtras")

if __name__=="__main__": main()
