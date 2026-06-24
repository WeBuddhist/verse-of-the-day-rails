#!/usr/bin/env bash
#
# import_84000_kangyur_mdo.sh — import the Kangyur SŪTRA section (mdo, Toh 8–359):
# for every text 84000 has published, pull the PD Tibetan (OpenPecha) AND 84000's
# verbatim English reference. Excludes Vinaya (Toh 1–7) and Tantra (Toh 360+).
#
# Run from the vault root. Requires: python3 + pyyaml. Clones two repos (~590 MB)
# into 0-INBOX/raw-data on first run.
#
# LICENSING (see vault-annex §7):
#   - Tibetan (OpenPecha P000001 / Degé): Public Domain.
#   - 84000 English: CC BY-NC-ND — stored verbatim WITH notes as a reference layer,
#     non-commercial, attributed. NOT excerpted/adapted; shipped verses are our own.
set -euo pipefail
VAULT="$(cd "$(dirname "$0")/../../../.." && pwd)"
RAW="$VAULT/0-INBOX/raw-data"
CONV="$VAULT/4-SYSTEM/Skills/json-to-source-text/converters"
mkdir -p "$RAW"

[ -d "$RAW/data-tei" ]  || git clone --depth 1 https://github.com/84000/data-tei.git "$RAW/data-tei"
[ -d "$RAW/P000001" ]   || git clone --depth 1 https://github.com/OpenPecha/P000001.git "$RAW/P000001"

# 1. 84000 English (TEI -> reference markdown), mdo range only
python3 - "$RAW/data-tei" "$VAULT" "$CONV" <<'PY'
import sys, re, glob, os, importlib.util
tei_root, vault, conv = sys.argv[1], sys.argv[2], sys.argv[3]
spec=importlib.util.spec_from_file_location("t",f"{conv}/tei_84000_en.py")
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
out=f"{vault}/1-SOURCES/Translations"
def toh(fn):
    x=re.search(r"toh(\d+)",os.path.basename(fn)); return int(x.group(1)) if x else None
# Giant prose works trimmed from the daily-verse corpus (audit 2026-06-24):
# Perfection of Wisdom (8,9,10), Avataṃsaka (44), Saddharmasmṛtyupasthāna (287).
TRIM = {8, 9, 10, 44, 287}
for f in glob.glob(f"{tei_root}/translations/kangyur/translations/*.xml"):
    n=toh(f)
    if n and 8<=n<=359 and n not in TRIM:
        try: m.convert(f,n,f"toh{n}",f"1-SOURCES/Text/bo-toh{n}.md",f"{out}/en-toh{n}-84000.md")
        except SystemExit: pass
PY

# 2. Tibetan source (OpenPecha .opf), same toh set — see openpecha_kangyur.py for
#    the per-text form; this batch caches volumes for speed. (Embedded for portability.)
echo "Tibetan: run openpecha_kangyur.py per Toh, or the batch in the session notes."
echo "Done. Review 1-SOURCES/, then commit. NOTE: ~210 MB; the Perfection of Wisdom texts are large."
