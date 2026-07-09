#!/usr/bin/env python3
"""
cbeta_sutra.py — general CBETA TEI P5 → 1-SOURCES markdown converter for
**verse texts and Mahāyāna sūtras** (anything with 品/juan + <lg>/<l> verse and
<p> prose). Complements cbeta_agama.py (which was written for the Āgama
<cb:div type="jing"> prose structure and does NOT capture <lg> verses).

Used to import (2026-07):
  - Chinese Dharmapada 法句經 (T210)         -> zh-dharmapada.md
  - Diamond 金剛經 (T235), Lotus 妙法蓮華經 (T262), Amitābha 佛說阿彌陀經 (T366),
    Bequeathed Teachings 佛遺教經 (T389), Vimalakīrti 維摩詰所說經 (T475),
    Eight Realizations 八大人覺經 (T779)     -> zh-<slug>.md

License of output source: CBETA CC BY-NC-SA 3.0 TW (non-commercial, ShareAlike,
attribution to CBETA + Taishō). Cleared for WeBuddhist's non-profit use; keep
separate from CC0 Pali in output licensing (vault-annex §7).

How to get the XML (sparse checkout — only the volumes you need):
  cd /tmp && git clone --filter=blob:none --no-checkout --depth 1 \\
      https://github.com/cbeta-org/xml-p5 cbeta
  cd cbeta && git sparse-checkout init --cone
  git sparse-checkout set T/T08 T/T09 T/T12 T/T14 T/T17   # volumes for the texts
  git checkout
  # Taishō vol → path: T235=T/T08, T262=T/T09, T366/T389=T/T12, T475=T/T14, T779=T/T17

CLI:
  python cbeta_sutra.py --xml T/T14/T14n0475.xml --slug vimalakirti \\
      --title "Vimalakīrti Sūtra (維摩詰所說經, T475)" --taisho T475 \\
      --vehicle Mahayana --out 1-SOURCES/Text/zh-vimalakirti.md

Block scheme: each <lg> and <p> becomes a citable block anchored by its CBETA
xml:id (^lg… / ^p…); each 品/juan becomes a heading. Notes/anchors/lb dropped;
<caesura/> dropped (existing punctuation suffices); <g> gaiji best-effort.
"""
from __future__ import annotations
import argparse, re
import xml.etree.ElementTree as ET

XMLID = '{http://www.w3.org/XML/1998/namespace}id'
def ln(t): return t.split('}')[-1]

def text_of(el):
    out = []
    if el.text: out.append(el.text)
    for ch in el:
        t = ln(ch.tag)
        if t in ('note', 'anchor'):
            pass                      # apparatus / id targets: skip
        elif t == 'caesura':
            pass                      # internal pause; keep source punctuation
        elif t == 'g':
            if ch.text: out.append(ch.text)   # gaiji best-effort
        else:
            out.append(text_of(ch))
        if ch.tail: out.append(ch.tail)
    return ''.join(out)

def clean(s): return re.sub(r'\s+', '', s).strip()

def convert(xml, slug, title, taisho, vehicle, out):
    root = ET.parse(xml).getroot()
    body = next(e for e in root.iter() if ln(e.tag) == 'body')
    blocks = []
    def walk(el):
        for ch in el:
            t = ln(ch.tag)
            if t == 'juan':
                head = next((clean(text_of(d)) for d in ch.iter() if ln(d.tag) == 'jhead'), None)
                blocks.append(('h', head or 'juan')); walk(ch)
            elif t == 'div':
                head = next((clean(text_of(d)) for d in ch.iter() if ln(d.tag) in ('mulu', 'head')), '')
                if head: blocks.append(('h2', head))
                walk(ch)
            elif t == 'lg':
                x = ch.get(XMLID); tx = clean(text_of(ch))
                if tx and x: blocks.append(('b', x, tx))
            elif t == 'p':
                x = ch.get(XMLID); tx = clean(text_of(ch))
                if tx and x: blocks.append(('b', x, tx))
            else:
                walk(ch)
    walk(body)

    canon = "Chinese (Taishō, Mahāyāna)" if vehicle.lower().startswith("maha") else "Chinese (Taishō)"
    vline = "vehicle: Mahāyāna\n" if vehicle.lower().startswith("maha") else ""
    fm = f"""---
title: {title}
author: Buddha (buddhavacana); Chinese canon
language: Literary Chinese
script: Han (Traditional)
file_type: root-text
lang_tag: zh
verse_id_format: cbeta-pid
canon: {canon}
{vline}source_description: CBETA TEI P5 ({taisho}); Taishō Tripiṭaka.
source_url: "https://github.com/cbeta-org/xml-p5"
taisho: {taisho}
license: CC BY-NC-SA 3.0 TW
license_url: "https://creativecommons.org/licenses/by-nc-sa/3.0/tw/"
rights_holder: CBETA + Taishō (non-commercial, ShareAlike, attribution)
commercial_use: false
derivatives_allowed: true
attribution_required: true
usage_status: cleared (non-profit use; see vault-annex §7)
grounding_note: "Own modern renderings produced in-vault from the Chinese source; meaning cross-checked against a Pali parallel (for Dharmapada/Āgama) or a standard reference translation (for Mahāyāna sūtras). Quote one self-contained sentence in full."
status: draft
---

# {title}

> CBETA source (CC BY-NC-SA). Verses anchored by line-group id (`^lg…`); prose by paragraph id (`^p…`); chapters/fascicles as headings. Modern translations produced in-vault; quote a self-contained sentence in full. No structure fabricated.
"""
    lines = [fm]; nb = 0
    for b in blocks:
        if b[0] == 'h':  lines.append(f"\n## {b[1]}\n")
        elif b[0] == 'h2': lines.append(f"\n### {b[1]}\n")
        else: lines.append(f"{b[2]} ^{b[1]}\n"); nb += 1
    open(out, 'w').write('\n'.join(lines))
    return nb

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--xml", required=True)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--taisho", required=True)
    ap.add_argument("--vehicle", default="")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    n = convert(a.xml, a.slug, a.title, a.taisho, a.vehicle, a.out)
    print(f"{a.out}  blocks={n}")
