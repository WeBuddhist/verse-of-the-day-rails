#!/usr/bin/env python3
"""
tei_84000_en.py — convert an 84000 TEI translation (Kangyur) into a
1-SOURCES/Translations/ reference file (English).

License: 84000 is CC BY-NC-ND. We store the **whole** translation verbatim,
**with its notes**, attributed, non-commercial — the permitted reference use.
We do NOT excerpt or adapt it; the shipped verse is our own. See vault-annex §7.

84000 TEI: <div type="translation"> holds <head type="titleMain">, sections,
<p> paragraphs, <lg>/<l> verses, <ref type="folio" cRef="F.271.a"/> Degé-folio
anchors, and <note place="end"> footnotes.

Output scheme `verse_id_format: derge-folio`: blocks anchored by Degé folio
(`^F271a`), which align to the Tibetan source. Verses kept as <br>-joined lines;
notes kept inline as [n: …] to satisfy the license's "with footnotes" condition.

CLI:
  python tei_84000_en.py --xml <file.xml> --toh 37 --slug benefits-five-precepts \\
     --bo-source 1-SOURCES/Text/bo-toh37.md --out 1-SOURCES/Translations/en-toh37-84000.md
"""
from __future__ import annotations
import argparse, re
import xml.etree.ElementTree as ET
from pathlib import Path

def ln(t): return t.split("}")[-1]

def folio_anchor(cref):
    # "F.271.a" -> "F271a"
    return "F" + re.sub(r"[^0-9ab]", "", cref) if cref else ""

def render(elem, notes):
    """Reading text of a <p>/<l>; fold <ref folio> to a marker token, keep <note> as [n]."""
    parts = []
    cur_folio = [None]
    def walk(e):
        t = ln(e.tag)
        if t == "ref" and e.get("type") == "folio":
            cur_folio[0] = folio_anchor(e.get("cRef", ""))
            if e.tail: parts.append(e.tail)
            return
        if t == "note":
            notes.append(re.sub(r"\s+", " ", "".join(e.itertext())).strip())
            parts.append(f" [n{len(notes)}]")
            if e.tail: parts.append(e.tail)
            return
        if e.text: parts.append(e.text)
        for c in e: walk(c)
        if e.tail: parts.append(e.tail)
    walk(elem)
    return re.sub(r"[ \t]*\n[ \t]*", " ", "".join(parts)).strip(), cur_folio[0]

def yaml_block(meta):
    out=["---"]
    for k,v in meta.items():
        if isinstance(v,bool): out.append(f"{k}: {str(v).lower()}")
        elif isinstance(v,str) and (":" in v or v.startswith(("#","[","&","*"))): out.append(f'{k}: "{v}"')
        else: out.append(f"{k}: {v}")
    out.append("---"); return "\n".join(out)

def convert(xml_path, toh, slug, bo_source, out_path):
    root = ET.parse(xml_path).getroot()
    tdiv = next((e for e in root.iter() if ln(e.tag)=="div" and e.get("type")=="translation"), None)
    if tdiv is None: raise SystemExit(f"no translation div in {xml_path}")

    def head(t):
        h = next((e for e in tdiv.iter() if ln(e.tag)=="head" and e.get("type")==t), None)
        return re.sub(r"\s+"," ","".join(h.itertext())).strip() if h is not None else ""
    title = (head("titleHon")+" "+head("titleMain")).strip() or f"Toh {toh}"

    meta = {
        "title": f"{title} (Toh {toh}, 84000 English — reference)",
        "translator": "84000: Translating the Words of the Buddha",
        "language":"English","script":"Roman","file_type":"translation","lang_tag":"en",
        "verse_id_format":"derge-folio","canon":"Tibetan Kangyur (Degé)","tohoku":str(toh),
        "root_text": bo_source,
        "source_description": f"84000 TEI (data-tei), Toh {toh}. Stored verbatim with notes as a reference layer.",
        "source_url": f"https://84000.co/translation/toh{toh}",
        "license":"CC-BY-NC-ND-3.0","license_url":"https://creativecommons.org/licenses/by-nc-nd/3.0/",
        "rights_holder":"84000: Translating the Words of the Buddha",
        "commercial_use":False,"derivatives_allowed":False,"attribution_required":True,
        "attribution_text":"Translated by 84000: Translating the Words of the Buddha. CC BY-NC-ND.",
        "usage_status":"reference-only (verbatim, with notes; do not excerpt/adapt)","status":"draft",
    }
    out=[yaml_block(meta),"",f"# {title}\n",
         f"> **84000 English, stored verbatim as a reference layer** (CC BY-NC-ND — do not excerpt or "
         f"adapt for output; the shipped verse is our own translation, citing 84000). Tibetan source: "
         f"`{bo_source}`. Folio anchors `^F<folio>` align to the Degé Kangyur.\n"]
    notes=[]
    last=None
    for e in tdiv.iter():
        t=ln(e.tag)
        if t=="p":
            txt,fol=render(e,notes)
            if not txt: continue
            anchor=f" ^{fol}" if fol and fol!=last else ""
            if fol: last=fol
            out.append(txt+anchor+"\n")
        elif t=="lg":
            lines=[]; fol=None
            for l in e:
                if ln(l.tag)=="l":
                    lt,lf=render(l,notes)
                    if lf: fol=lf
                    if lt: lines.append(lt)
            if lines:
                anchor=f" ^{fol}" if fol and fol!=last else ""
                if fol: last=fol
                out.append("<br>".join(lines)+anchor+"\n")
    if notes:
        out.append("\n## Notes (84000)\n")
        for i,n in enumerate(notes,1): out.append(f"[n{i}] {n}\n")
    Path(out_path).parent.mkdir(parents=True,exist_ok=True)
    Path(out_path).write_text("\n".join(out)+"\n",encoding="utf-8")
    print(f"Wrote {out_path}: {sum(1 for x in out if ' ^F' in x)} folio-anchored blocks, {len(notes)} notes")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--xml",required=True); ap.add_argument("--toh",required=True)
    ap.add_argument("--slug",required=True); ap.add_argument("--bo-source",default="")
    ap.add_argument("--out",required=True)
    a=ap.parse_args()
    convert(a.xml,a.toh,a.slug,a.bo_source,a.out)

if __name__=="__main__": main()
