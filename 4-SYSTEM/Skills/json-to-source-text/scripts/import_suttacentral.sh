#!/usr/bin/env bash
#
# import_suttacentral.sh — clone SuttaCentral bilara-data (CC0) and import
# Pali verse collections into 1-SOURCES/ via the suttacentral_bilara converter.
#
# Confirmed workflow: clone the data repo locally, then run this script.
# Run from the vault root:  bash 4-SYSTEM/Skills/json-to-source-text/scripts/import_suttacentral.sh
#
# Currently supports the FLAT RANGE-FILE collections (Dhammapada). The nested
# vagga-subfolder collections (Sutta Nipata, Udana, Itivuttaka, Theragatha,
# Therigatha) need the converter's nested mode — see TODO at the bottom.
set -euo pipefail

VAULT="$(cd "$(dirname "$0")/../../../.." && pwd)"
CONV="$VAULT/4-SYSTEM/Skills/json-to-source-text/converters/suttacentral_bilara.py"
WORK="$VAULT/0-INBOX/raw-data/bilara-data"
TMP="$VAULT/0-INBOX/temp"
mkdir -p "$TMP"

# 1. Clone (sparse: only the KN root + Sujato English) if not present
if [ ! -d "$WORK" ]; then
  echo "Cloning SuttaCentral bilara-data (sparse)…"
  git clone --depth 1 --filter=blob:none --sparse \
    https://github.com/suttacentral/bilara-data.git "$WORK"
  git -C "$WORK" sparse-checkout set \
    root/pli/ms/sutta/kn translation/en/sujato/sutta/kn
else
  echo "Using existing clone at $WORK"
fi

# 2. Import a flat range-file collection.  Args: <uid-dir> <slug> <title>
import_flat() {
  local dir="$1" slug="$2" title="$3"
  local R="$WORK/root/pli/ms/sutta/kn/$dir"
  local T="$WORK/translation/en/sujato/sutta/kn/$dir"
  local roots trs
  roots=$(ls "$R"/${dir}*_root-pli-ms.json | sort -t/ -k99 -V)
  trs=$(ls "$T"/${dir}*_translation-en-sujato.json | sort -t/ -k99 -V)
  echo "Importing $title …"
  python3 "$CONV" --slug "$slug" --title "$title" --uid-hint "$dir" \
    --root $roots --tr $trs \
    --out-text "$TMP/pi-$slug.md" \
    --out-tr   "$TMP/en-$slug-sujato.md"
  echo "  -> review $TMP/pi-$slug.md then move to 1-SOURCES/Text/ and 1-SOURCES/Translations/"
}

# 3. Import a nested collection (vagga subfolders, per-sutta files).
#    Args: <uid-dir> <slug> <title>
import_nested() {
  local dir="$1" slug="$2" title="$3"
  echo "Importing $title (nested) …"
  python3 "$CONV" --nested --slug "$slug" --title "$title" \
    --root "$WORK/root/pli/ms/sutta/kn/$dir" \
    --tr   "$WORK/translation/en/sujato/sutta/kn/$dir" \
    --out-text "$TMP/pi-$slug.md" \
    --out-tr   "$TMP/en-$slug-sujato.md"
  echo "  -> review $TMP/pi-$slug.md then move to 1-SOURCES/"
}

# ── buddhavacana verse collections of the Khuddaka Nikāya ──
import_flat   dhp dhammapada   "Dhammapada"     # verses, continuous numbering
import_nested snp sutta-nipata "Sutta Nipāta"   # suttas, segment scheme
import_nested ud  udana        "Udāna"
import_nested iti itivuttaka   "Itivuttaka"

# NOTE: Theragāthā (thag) and Therīgāthā (thig) are intentionally NOT imported.
# They are verses of named elder monks/nuns, not words of the Buddha, so they
# do not belong in this buddhavacana anthology (see vault-annex §1).

cat <<'NOTE'

Done. Review output in 0-INBOX/temp/, then move each pair:
  mv 0-INBOX/temp/pi-<slug>.md           1-SOURCES/Text/
  mv 0-INBOX/temp/en-<slug>-sujato.md    1-SOURCES/Translations/

NEXT SOURCES (not yet supported by this converter):
  - Pali prose Nikāyas (DN/MN/SN/AN): verse-bearing suttas, segment scheme.
  - Chinese Āgamas (CBETA) and Tibetan Kangyur (84000 — license-blocked, see annex §7).
NOTE
