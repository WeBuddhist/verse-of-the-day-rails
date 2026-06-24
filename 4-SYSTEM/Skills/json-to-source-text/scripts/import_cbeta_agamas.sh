#!/usr/bin/env bash
#
# import_cbeta_agamas.sh — clone CBETA TEI P5 and import the four Chinese
# Āgamas into 1-SOURCES/Text/ via the cbeta_agama converter.
#
# LICENSE: CBETA is CC BY-NC-SA 3.0 TW — NON-COMMERCIAL, ShareAlike, attribute
# CBETA + Taishō. Only use if WeBuddhist's use stays non-commercial. Imported
# source-only (Literary Chinese); modern translations are produced in-vault.
# See vault-annex §7. Run from the vault root.
set -euo pipefail

VAULT="$(cd "$(dirname "$0")/../../../.." && pwd)"
CONV="$VAULT/4-SYSTEM/Skills/json-to-source-text/converters/cbeta_agama.py"
WORK="$VAULT/0-INBOX/raw-data/cbeta-xml-p5"
TMP="$VAULT/0-INBOX/temp"; mkdir -p "$TMP"

if [ ! -d "$WORK" ]; then
  echo "Cloning CBETA xml-p5 (sparse: Taishō vols 1–2)…"
  git clone --depth 1 --filter=blob:none --sparse \
    https://github.com/cbeta-org/xml-p5.git "$WORK"
  git -C "$WORK" sparse-checkout set T/T01 T/T02
fi

imp () { # <xml-rel> <slug> <title> <abbr>
  python3 "$CONV" --xml "$WORK/$1" --slug "$2" --title "$3" --abbr "$4" \
    --out "$TMP/zh-$2.md"
  echo "  -> review $TMP/zh-$2.md then move to 1-SOURCES/Text/"
}

imp T/T01/T01n0001.xml digha-agama      "Dīrgha Āgama (長阿含經)"      da
imp T/T01/T01n0026.xml madhyama-agama   "Madhyama Āgama (中阿含經)"    ma
imp T/T02/T02n0099.xml samyukta-agama   "Saṁyukta Āgama (雜阿含經)"    sa
imp T/T02/T02n0125.xml ekottarika-agama "Ekottarika Āgama (增壹阿含經)" ea

cat <<'NOTE'

Done. Review in 0-INBOX/temp/, then:  mv 0-INBOX/temp/zh-*-agama.md 1-SOURCES/Text/

LIMITATIONS:
  - Source-only: no paired translation (none exists under a clean license).
    Produce modern renderings in-vault, under review.
  - Gaiji (rare missing glyphs) appear as 〔CB…〕 placeholders — resolve via the
    CBETA gaiji table if a specific verse needs one.
  - ShareAlike: any output derived from these inherits CC BY-NC-SA. Keep Āgama-
    derived verses' licensing separate from the CC0 Pali.
NOTE
