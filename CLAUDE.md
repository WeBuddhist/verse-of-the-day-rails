# CLAUDE.md — WeBuddhist Verse of the Day (verse-of-the-day-rails)

**Canonical operational guide for an AI agent in this vault.** Read before touching any file. This file lives at the repo root so it auto-loads. Human-facing overview: [`README.md`](README.md). Deep per-folder rules: each folder's `About …md` and [`4-SYSTEM/Guidelines/vault-annex.md`](4-SYSTEM/Guidelines/vault-annex.md). When this file and a folder README disagree, the folder README wins.

---

## ⚑ Before doing anything — check for a skill first

1. Open [`4-SYSTEM/Skills/SKILLS-CATALOG.md`](4-SYSTEM/Skills/SKILLS-CATALOG.md) and find the skill matching the task.
2. Open its `SKILL.md` in full and follow it exactly — don't improvise.
3. Only if no skill exists, use the general rules below.

A task done without its skill must be redone. This is the most common error in this vault.

---

## What this vault is

A "Railroads" **anthology** producing WeBuddhist's **Verse of the Day**: one short, authentic **buddhavacana** verse per day, grounded in a cited source and rendered in six languages (**en · zh · bo · hi · ne · mn**), drawn from the **Pali Canon, Chinese canon, and Tibetan Kangyur** (discourse/verse only — no tantra, Vinaya, or scholastic). Authority is the human source + authoritative translations, **never the model's parametric knowledge**. It holds **no commentaries**, so rails are **translation-grounded** (the `verse-rail` skill) — with one narrow, human-approved exception: a few Kangyur sūtras 84000 hasn't translated yet (Toh 12, 13, 16, 53, 60) are grounded on the Tibetan Degé source alone (`grounding: source-only`), translated directly without a reference; all hard gates (buddhavacana, verbatim-from-source, in-scope) still apply. See `verse-rail`'s grounding table and [`candidate-pool/kangyur-scan-leads.md`](3-TRANSFORMATIONS/verse-of-the-day/candidate-pool/kangyur-scan-leads.md). Anthology specifics: [`4-SYSTEM/Guidelines/vault-annex.md`](4-SYSTEM/Guidelines/vault-annex.md) §0.

---

## Verse-of-the-Day — pipeline and hard rules (the core of this vault)

**Pipeline:** `candidate-tagging` (optional, run ahead of time in bulk against `1-SOURCES/` to seed `3-TRANSFORMATIONS/verse-of-the-day/candidate-pool/`) → `verse-selection` → `verse-rail` → build the day card → `translation-qa` → add the `log.md` row. Read, in [`3-TRANSFORMATIONS/verse-of-the-day/`](3-TRANSFORMATIONS/verse-of-the-day/): **`About verse-of-the-day.md`** (day-card template), **`selection-criteria.md`** (gates + balance), **`termbase.md`** (locked terms), **`log.md`** (what's used + running balance), **`previously-used.md`** (dedupe), **`candidate-pool/`** (pre-tagged candidates — check here before scanning `1-SOURCES/` raw).

**Hard rules — a card that breaks any of these must be redone:**
1. **Buddhavacana spoken *by* the Buddha, not *about* him** — no praise-of-the-Buddha stanzas, no words of disciples/gods/kings.
2. **Real quote, kept whole** — a complete verse or ONE self-contained sentence, quoted in full; never summarise / stitch / gist. **Verify the source verbatim from `1-SOURCES/` first — never render Pāli/Chinese/Tibetan from memory** (a mistyped syllable is a fabricated quote).
3. **Fits the app card (~125 chars)** in all six languages; if it won't fit whole, pick a shorter source.
4. **Ecumenical wording** (for all Buddhists) — *bodhicitta* = "the awakening mind," never "Great Vehicle"; use standard `termbase.md` terms, not paraphrase (*mettā* = loving-kindness, not "love"; aggregates = form/feeling/perception/volition/consciousness).
5. **No em dashes in English**; **zh = modern Traditional**; on Chinese/Tibetan-source cards the **zh/bo rendering IS the verbatim source**; **84000 English is reference-only, never shipped.**
6. **Dedupe the material** (log + previously-used + rails + days); **themes may repeat but never two days running**; keep the three canons roughly balanced.
7. All cards stay **`status: draft`**; only a native dharma reviewer (esp. bo + mn) sets `complete`.

**Source breadth — do NOT default to the Dhammapada.** Rotate across: Pali verse collections (Dhp, Snp, Ud, Iti gāthās) **and prose Nikāyas** (DN/MN/SN/AN, Sujato CC0) · Chinese Dharmapada (T210), the four Āgamas, **and Chinese Mahāyāna sūtras** (`zh-diamond-sutra`, `zh-lotus-sutra`, `zh-amitabha-sutra`, `zh-bequeathed-teachings`, `zh-vimalakirti`, `zh-eight-realizations`) · Tibetan **Udānavarga** (Toh 326) **and Kangyur Mahāyāna sūtras** (`bo-toh<N>` + `en-toh<N>-84000`). **Mahāyāna must appear regularly**, worded ecumenically. Grounding & licensing per canon: the table in the [`verse-rail`](4-SYSTEM/Skills/verse-rail/SKILL.md) skill.

**Importing more source text:** CBETA → [`4-SYSTEM/Skills/json-to-source-text/converters/cbeta_sutra.py`](4-SYSTEM/Skills/json-to-source-text/converters/cbeta_sutra.py) (verse/sūtra) or `cbeta_agama.py` (Āgama prose); sparse-clone only the Taishō volume you need (see the converter docstring). Register in `vault-annex.md` (corpus table + §7 licensing). **Open item:** populate `previously-used.md` with WeBuddhist's real prior-published verses when available.

**Open item — import the five reference-less Kangyur sūtras (Toh 12, 13, 16, 53, 60):** approved for `source-only` use (Evan, 2026-07-13), but **not yet imported** — no `bo-toh<N>.md` exists for them. Before any can be scanned or railed: import the raw Tibetan from OpenPecha's Degé Kangyur (`P000001`) and register each in `vault-annex.md` (corpus table + §7 licensing). Scope note: T12 (~907k chars) and T60 (~520k chars) are large imports; 13/16/53 are smaller. Details and rationale in [`3-TRANSFORMATIONS/verse-of-the-day/candidate-pool/kangyur-scan-leads.md`](3-TRANSFORMATIONS/verse-of-the-day/candidate-pool/kangyur-scan-leads.md); grounding mechanics in `verse-rail` (`grounding: source-only`).

**Open item — candidate-tagging coverage gap:** the Chinese Āgamas/sūtras, Pali verse collections (Dhp/Snp/Ud/Iti), and the Tibetan Udānavarga have all had a real `candidate-tagging` scan. The Pali prose Nikāyas (DN/MN/SN/AN, ~245,000 lines combined) and the ~229 individual Tibetan Kangyur sūtra files have **not** — this is a much bigger lift than everything scanned so far and needs a dedicated future pass (likely parallel sub-agents, not one sequential read). See [`3-TRANSFORMATIONS/verse-of-the-day/candidate-pool/SCAN-STATUS.md`](3-TRANSFORMATIONS/verse-of-the-day/candidate-pool/SCAN-STATUS.md) for exact status and how to resume.

---

## Structure, citation chain, write permissions

```
0-INBOX/            # scratch — not authoritative
1-SOURCES/          # human ground truth — read-only (metadata via skills only)
  Text/  Translations/
2-RAILS/Verses/     # translation-grounded verse rails (the only active rail type)
3-TRANSFORMATIONS/
  verse-of-the-day/ # the one output track (day cards + curation docs + log)
4-SYSTEM/           # skills, guidelines, converters — read-only (human-owned)
```

**One-way citation chain — never skip a link:** `1-SOURCES/ → 2-RAILS/ → 3-TRANSFORMATIONS/`. A rail cites `1-SOURCES/` only; a day card cites its rail (`source_rail` / `context_packages`), not `1-SOURCES/` directly (it may quote the verbatim source line for display). If a claim can't be cited, don't make it.

**Write permissions:** `0-INBOX/` yes (scratch) · `1-SOURCES/` **no** (frozen; metadata only, via skills) · `2-RAILS/` yes · `3-TRANSFORMATIONS/` yes · `4-SYSTEM/` **no** (rule changes need a human).

---

## Conventions

- **Filenames:** lowercase, hyphenated, no diacritics; language-tag suffix (`-pi -sk -bo -zh -en -hi -ne -mn`). Rails in `2-RAILS/Verses/` are named by source slug (`dhp-5.md`, `sa-803.md`, `toh-282.md`). Full tag list: [`1-SOURCES/About Sources.md`](1-SOURCES/About%20Sources.md) §12.
- **Block IDs** are the verse-level link: `[verse] ^id`; link `[[1-SOURCES/Text/<file>.md#^id]]`, transclude `![[…#^id]]`. Per-source `verse_id_format` in each source file's frontmatter; details in `About Sources.md` §5.
- **Status lifecycle:** `draft` (LLM + QA done) → `complete` (rail signed off **and** native review of all six renderings). Per-language `review_status`: `clean-for-review` / `needs-native-review` / `escalate-native-review` / `blocked`. bo + mn always need native review. The LLM never sets `complete`.
- **No parametric knowledge; no consensus flattening** (flag divergences with ⚑).

---

## Skills quick-reference

| Task | Skill |
|------|-------|
| Bulk-tag verse candidates from source text ahead of time | `candidate-tagging` |
| Select the next day's verse (rotation + dedupe) | `verse-selection` |
| Build a verse rail (translation-grounded) | `verse-rail` |
| Pre-review QA of a verse's six renderings | `translation-qa` |
| Import source text (SuttaCentral / CBETA / OpenPecha) | `json-to-source-text` (+ converters, incl. `cbeta_sutra.py`) |
| Ingest an EPUB | `epub-to-markdown` |
| Create a new skill (full registration) | `create-skill` |
| Audit vault integrity | `vault-audit` |

Commentary/section/glossary skills from the template (`verse-context`, `section-summary-*`, `local-wiki-article`, `glossary-*`, …) are **not used** here and have been removed (see SKILLS-CATALOG.md's "Removed" section).

---

## Where the detail lives

- [`3-TRANSFORMATIONS/verse-of-the-day/About verse-of-the-day.md`](3-TRANSFORMATIONS/verse-of-the-day/About%20verse-of-the-day.md) — day-card template + language notes.
- [`3-TRANSFORMATIONS/verse-of-the-day/selection-criteria.md`](3-TRANSFORMATIONS/verse-of-the-day/selection-criteria.md) — gates, freshness, source diversity, vehicle representation, theme rule.
- [`4-SYSTEM/Guidelines/vault-annex.md`](4-SYSTEM/Guidelines/vault-annex.md) — corpus table, addressing, licensing register (§7).
- [`1-SOURCES/About Sources.md`](1-SOURCES/About%20Sources.md) · [`2-RAILS/About Rails.md`](2-RAILS/About%20Rails.md) · [`3-TRANSFORMATIONS/About Transformations.md`](3-TRANSFORMATIONS/About%20Transformations.md) — per-folder rules.
