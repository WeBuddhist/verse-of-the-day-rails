# Import runbook — Pali Canon from SuttaCentral (CC0)

How to bulk-import buddhavacana source texts from SuttaCentral's `bilara-data`
into `1-SOURCES/`. SuttaCentral's Pāli root (Mahāsaṅgīti) and Bhikkhu Sujato's
English are **CC0 / public domain** — cleared for commercial use and derivatives
(see `vault-annex.md` §7).

> **Why a local clone, not in-agent fetching.** The canon is thousands of
> small JSON files. Fetching them one at a time through an agent is impractical.
> Clone the data repo once and run the converter locally — minutes, not hours.

---

## 1. Get the data (once)

```bash
cd 0-INBOX/raw-data
git clone --depth 1 https://github.com/suttacentral/bilara-data.git
```

Layout that matters:

```
bilara-data/
  root/pli/ms/sutta/                 # Pāli root text
    kn/dhp/dhp1-20_root-pli-ms.json  #   Khuddaka: Dhammapada (by vagga)
    mn/mn1_root-pli-ms.json          #   Majjhima: one file per sutta
    ...
  translation/en/sujato/sutta/       # Sujato English (CC0), same paths/ids
    kn/dhp/dhp1-20_translation-en-sujato.json
```

Root and translation files share **segment ids** (`dhp1:1`, `mn1:1.2`), so they
merge by id. Sujato's English covers DN, MN, SN, AN in full, plus much of KN.

---

## 2. Verse collections (priority for verse-of-the-day)

Use the `suttacentral_bilara` converter. It pairs root + translation files
**in order** and emits a Pāli root file and an English translation file with
`verse_id_format: verse` and CC0 licensing frontmatter.

Driver (imports one whole text from its split vagga files, in numeric order):

```bash
ROOT=0-INBOX/raw-data/bilara-data/root/pli/ms/sutta/kn/dhp
TR=0-INBOX/raw-data/bilara-data/translation/en/sujato/sutta/kn/dhp

# sort vagga files by their starting verse number
roots=$(ls $ROOT/dhp*_root-pli-ms.json | sort -t/ -k99 -V)
trs=$(ls $TR/dhp*_translation-en-sujato.json | sort -V)

python3 4-SYSTEM/Skills/json-to-source-text/converters/suttacentral_bilara.py \
  --slug dhammapada --title "Dhammapada" --uid-hint dhp \
  --root $roots --tr $trs \
  --out-text 0-INBOX/temp/pi-dhammapada.md \
  --out-tr   0-INBOX/temp/en-dhammapada-sujato.md
```

Repeat per verse collection (each is the same shape):

| Text | bilara dir (`.../kn/<x>`) | slug |
| ---- | ------------------------- | ---- |
| Dhammapada | `dhp` | `dhammapada` |
| Sutta Nipāta | `snp` | `sutta-nipata` |
| Udāna | `ud` | `udana` |
| Itivuttaka | `iti` | `itivuttaka` |
| Theragāthā | `thag` | `theragatha` |
| Therīgāthā | `thig` | `therigatha` |

Review the output in `0-INBOX/temp/`, then move the pair to
`1-SOURCES/Text/pi-<slug>.md` and `1-SOURCES/Translations/en-<slug>-sujato.md`.

---

## 3. Prose Nikāyas (DN/MN/SN/AN) — segment scheme

Prose suttas need `verse_id_format: suttacentral-segment` (block ids like
`^mn1-1-2`, from `mn1:1.2`). This is a **second converter mode**, not yet
written — see the next-steps note in `vault-annex.md`. For verse-of-the-day the
verse collections above are the priority; prose suttas are imported as their
verse-bearing passages are needed.

---

## 4. Chinese Āgamas (CBETA) and Tibetan Kangyur

- **Chinese:** SuttaCentral also hosts Āgama root text under `root/zh/`. CBETA
  is the fuller source. Source text is Creative Commons (verify per text);
  English is sparse, so modern Mandarin output is rendered in-vault under review.
- **Tibetan Kangyur:** the Tibetan root is not under copyright, but 84000's
  English is CC BY-NC-ND (**blocked** — see `vault-annex.md` §7). Do not import
  84000 translations until a Khyentse Foundation content-use grant is in place.

---

## 5. After import — checklist

- [ ] Frontmatter has `license`, `commercial_use`, `derivatives_allowed`, `usage_status` (annex §7).
- [ ] `verse_id_format` matches the scheme used.
- [ ] Root and translation files share identical block ids (verse-aligned).
- [ ] File moved from `0-INBOX/temp/` to `1-SOURCES/`.
- [ ] Source row updated in `vault-annex.md` §1 and §7.
- [ ] Run `vault-audit` skill.
