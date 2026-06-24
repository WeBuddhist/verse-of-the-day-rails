#!/usr/bin/env python3
"""
cbeta_agama.py — converter for CBETA TEI P5 XML (Chinese Āgamas) into a
1-SOURCES/ Chinese source-text file.

Source: cbeta-org/xml-p5 (https://github.com/cbeta-org/xml-p5).
License: CC BY-NC-SA 3.0 TW — NON-COMMERCIAL, ShareAlike, attribution to CBETA +
Taishō. See vault-annex §7. This converter emits frontmatter recording that.

TEI structure used:
  <cb:juan n="001"> ... <cb:jhead><title>雜阿含經</title>卷第一</cb:jhead>  -> fascicle marker
  <byline cb:type="Translator">…譯</byline>                               -> translator
  <cb:div type="jing"> <cb:mulu n="1" type="經">1</cb:mulu>
       <head>（一）</head> <p xml:id="pT02p0001a0602">如是我聞：</p> … </cb:div>  -> one sūtra
  <lb n="0001a01"/> <pb/>  -> Taishō line/page refs (dropped from text)
  <note> <anchor>          -> apparatus (dropped)
  <g ref="#CB…"/>          -> gaiji / missing glyph (best-effort)

Output scheme (vault-annex §2, a per-source variant): verse_id_format
`cbeta-pid`. Each <p> becomes a block whose id is its CBETA xml:id (a stable,
citable Taishō page/column/line anchor, e.g. ^pT02p0001a0602). Each sūtra is a
`###` heading anchored `^sa<n>-0`; each fascicle a `##` heading.

CLI:
  python cbeta_agama.py --xml T/T02/T02n0099.xml --slug samyukta-agama \\
      --title "Saṁyukta Āgama (雜阿含經)" --abbr sa --out 1-SOURCES/Text/zh-samyukta-agama.md
"""
from __future__ import annotations
import argparse, re
import xml.etree.ElementTree as ET
from pathlib import Path

XML_ID = "{http://www.w3.org/XML/1998/namespace}id"


def ln(tag: str) -> str:
    return tag.split("}")[-1]


def text_of(elem) -> str:
    """Reading text of an element, dropping notes/anchors/apparatus; collapse line-wrap whitespace."""
    parts = []

    def walk(e):
        t = ln(e.tag)
        if t in ("note", "anchor"):
            if e.tail:                  # skip the note's content, but keep reading text after it
                parts.append(e.tail)
            return
        if t == "g":                    # gaiji: use ref code as a visible placeholder
            ref = e.get("ref", "")
            parts.append("〔" + ref.lstrip("#") + "〕" if ref else "")
            if e.tail:
                parts.append(e.tail)
            return
        if e.text:
            parts.append(e.text)
        for c in e:
            walk(c)
        if e.tail:
            parts.append(e.tail)

    walk(elem)
    s = "".join(parts)
    return re.sub(r"\s+", "", s)        # Chinese has no word spaces; strip line wraps


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


def convert(xml_path, slug, title, abbr, out_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    body = next(e for e in root.iter() if ln(e.tag) == "body")

    translator = ""
    for e in root.iter():
        if ln(e.tag) == "byline" and (e.get("{http://www.cbeta.org/ns/1.0}type") == "Translator"
                                       or "Translator" in (e.get("type") or "")):
            translator = text_of(e)
            break

    meta = {
        "title": title,
        "author": "Buddha (buddhavacana); Chinese Āgama",
        "translator_classical": translator or "(see Taishō)",
        "language": "Literary Chinese",
        "script": "Han (Traditional)",
        "file_type": "root-text",
        "lang_tag": "zh",
        "verse_id_format": "cbeta-pid",
        "canon": "Chinese Āgama (Taishō)",
        "source_description": f"CBETA TEI P5 ({Path(xml_path).name}); Taishō Tripiṭaka.",
        "source_url": "https://github.com/cbeta-org/xml-p5",
        "license": "CC-BY-NC-SA-3.0-TW",
        "license_url": "http://creativecommons.org/licenses/by-nc-sa/3.0/tw/",
        "rights_holder": "CBETA; Taishō Tripiṭaka (大正藏, Daizō Shuppan)",
        "commercial_use": False,
        "derivatives_allowed": True,
        "share_alike": True,
        "attribution_required": True,
        "attribution_text": "Source: CBETA (cbeta.org), Taishō Tripiṭaka. CC BY-NC-SA 3.0.",
        "usage_status": "cleared-noncommercial",
        "status": "draft",
    }

    out = [yaml_block(meta), "", f"# {title}\n",
           f"> Source text in Literary Chinese (classical). Modern-language renderings are produced "
           f"in-vault under review (vault-annex §4). CC BY-NC-SA — non-commercial, ShareAlike.\n"]

    cur_juan = None
    sutta_n = 0
    # document-order walk of the body
    for e in body.iter():
        t = ln(e.tag)
        if t == "juan" and e.get("fun") == "open":
            n = e.get("n", "").lstrip("0") or "?"
            cur_juan = n
            out.append(f"## 卷 {n} (Fascicle {n}) ^juan-{n}-0\n")
        elif t == "div" and (e.get("type") == "jing"):
            sutta_n += 1
            # heading text: the <head> child, plus mulu number if present
            head_txt = ""
            mulu_n = ""
            for c in e:
                if ln(c.tag) == "head":
                    head_txt = text_of(c)
                if ln(c.tag) == "mulu":
                    mulu_n = c.get("n", "")
            label = head_txt or f"({sutta_n})"
            out.append(f"### {abbr.upper()} {mulu_n or sutta_n} {label} ^{abbr}{mulu_n or sutta_n}-0\n")
            # paragraphs
            for p in e.iter():
                if ln(p.tag) != "p":
                    continue
                pid = p.get(XML_ID) or ""
                txt = text_of(p)
                if not txt:
                    continue
                if pid:
                    out.append(f"{txt} ^{pid}\n")
                else:
                    out.append(f"{txt}\n")
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    Path(out_path).write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote {out_path}: {sutta_n} sūtras")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--xml", required=True)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--abbr", required=True, help="sutra-id prefix, e.g. sa / ma / da / ea")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    convert(args.xml, args.slug, args.title, args.abbr, args.out)


if __name__ == "__main__":
    main()
