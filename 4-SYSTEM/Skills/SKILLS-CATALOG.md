# Skills Catalog

This file catalogues every skill available in a Railroads vault, grouped by workflow phase. Each entry names the skill, states its purpose, describes its inputs and outputs, and points to the SKILL.md that operationalises it.

Skills that already exist are marked **[exists]**. Skills that are planned but not yet written are marked **[planned]**.

The pipeline reads top-to-bottom: source ingestion populates `1-SOURCES/`, the rails-building skills turn those sources into `2-RAILS/` context (Sections / Verses / Local-Wiki / Bilingual Glossaries), the translation skills consume those rails to produce `3-TRANSFORMATIONS/Translations/<track-name>/`, and the QA skill checks the output back against the rails.

---

## Source ingestion skills

These skills bring raw material into `1-SOURCES/` in a consistent, citation-ready format.

### `epub-to-markdown` **[exists]**
Converts EPUB files (commentaries, reference texts) into formatted Obsidian markdown with block IDs, headings, and frontmatter.
→ [`epub-to-markdown/SKILL.md`](epub-to-markdown/SKILL.md)

### `json-to-source-text` **[exists]**
Converts JSON exports of root texts (e.g. from tipitaka.org or SuttaCentral) into formatted source-text markdown files. Includes example converters for tipitaka.org and English paired translations; new source schemas get their own converter in `json-to-source-text/converters/`.
→ [`json-to-source-text/SKILL.md`](json-to-source-text/SKILL.md)

---

## Candidate pooling skills

These skills bulk-scan `1-SOURCES/` ahead of time and bank pre-verified candidates in `3-TRANSFORMATIONS/verse-of-the-day/candidate-pool/`, so the curation skills below can filter that pool instead of re-scanning raw source text each time.

### `candidate-tagging` **[exists]**
**Purpose:** Bulk-scan one or more source files for verse-of-the-day candidates and record them in the candidate pool (buddhavacana confirmed, verbatim quote, rough length estimate, speaks_to/theme tagged), plus near-misses in a rejected list, so a later selection pass never re-scans raw source text.
**Inputs:** Source file(s) in `1-SOURCES/Text/`; `discovery-by-feeling.md`; `candidate-pool/theme-checklist.md`; existing `candidate-pool/*.md` and `rejected.md`; `log.md` and `2-RAILS/Verses/` (already-claimed set); `selection-criteria.md` §1–2 gates.
**Outputs:** Entries appended to `3-TRANSFORMATIONS/verse-of-the-day/candidate-pool/<canon>.md` and/or `candidate-pool/rejected.md`.
→ [`candidate-tagging/SKILL.md`](candidate-tagging/SKILL.md)

---

## Curation skills (verse-of-the-day selection)

### `verse-selection` **[exists]**
**Purpose:** Select the next verse of the day — reads the `log.md` (already-run rows + running balance) and the curation docs, then proposes the next verse: dedupes against the log/rails/days, rotates the canon toward balance, spaces themes, and honors holiday occasions. The selection step before `verse-rail`.
**Inputs:** `log.md`; `selection-criteria.md`; `occasions.md`; `discovery-by-feeling.md`; `1-SOURCES/`; existing `2-RAILS/Verses/` + `verse-of-the-day/` (dedupe set); the date.
**Outputs:** A selection proposal — `source_ref`, canon, theme/speaks_to, rationale, source link, dedupe result, and the ready-to-paste log row. Hands off to `verse-rail`.
→ [`verse-selection/SKILL.md`](verse-selection/SKILL.md)

---

## Rails-building skills (context preparation for translation)

These skills populate `2-RAILS/` with the structured context that translation and QA skills consume.

### `verse-rail` **[exists]**
**Purpose:** Build a **translation-grounded** verse rail for one verse of any canon — the WeBuddhist anthology's adaptation of `verse-context`, used because no commentaries are imported. Grounds the rail in the authoritative translation(s) the vault holds (Sujato / Patton / 84000) rather than a commentary tradition (which About Rails permits).
**Inputs:** Source block id(s) in `1-SOURCES/Text/`; aligned translation block(s) in `1-SOURCES/Translations/`; the `source_ref` label.
**Outputs:** One file at `2-RAILS/Verses/<text-slug>-<verse>.md` containing: source transclusion, authoritative rendering(s), a precise English disambiguated meaning (every claim cited), and theme/selection notes. `grounding: translation` (or `hybrid` if a commentary is later added).
→ [`verse-rail/SKILL.md`](verse-rail/SKILL.md)

---

## Translation requirements skills

### `requirements-author` **[planned]**
**Purpose:** Author or audit a track's `requirements.md` so it contains everything the `translate-section` skill needs to behave consistently across the whole text.
**Inputs:** The track folder `3-TRANSFORMATIONS/Translations/<track-name>/`; the per-track termbase (if it exists yet); samples of any prior translation in the same target language.
**Outputs:** A complete `3-TRANSFORMATIONS/Translations/<track-name>/requirements.md`, written in the target language.
→ `requirements-author/SKILL.md` *(to be written)*

---

## Translation skills

### `translate-section` **[planned]**
**Purpose:** Translate a small batch of TOC nodes into the target language.
**Inputs:** `requirements.md`, `termbase.md`, `audience.md` for the track; relevant section and verse packages from `2-RAILS/`; Local-Wiki articles as needed.
**Outputs:** Updated translation file(s) in `3-TRANSFORMATIONS/Translations/<track-name>/`. Each file's frontmatter lists the rail files it was generated from.
**Rules:** Translate small batches only — one or a few TOC nodes at a time. Every keyword rendering must match the per-track termbase. Introduce no new rendering without first adding it to the termbase and feeding it back into the consolidated bilingual glossary.
→ `translate-section/SKILL.md` *(to be written)*

---

## Translation QA skills

### `translation-qa` **[exists]**
**Purpose:** Automated **pre-review** QA pass on a verse-of-the-day's renderings, run before a native reviewer sees them — critiques each language against its rail's *Disambiguated Meaning* and flagged choices, back-translates to catch drift, checks terminology + register (zh Traditional/Taiwan; no em-dash English), produces a revised draft, and flags low-confidence spots for the reviewer. Raises draft quality and cuts reviewer load; does **not** replace native sign-off (esp. bo/mn).
**Inputs:** The verse's rail (`2-RAILS/Verses/<slug>.md`); the day card's draft renderings; the term glossary if present.
**Outputs:** Revised renderings (still `status: draft`) + a per-language QA note (back-translation, MQM findings by severity, confidence flags) appended to the day card.
→ [`translation-qa/SKILL.md`](translation-qa/SKILL.md)

### `style-consistency-check` **[planned]**
**Purpose:** Catch style drift over long texts — creeping changes in register, sentence length, verse formatting, list handling, term gloss style.
**Inputs:** All translated files in `3-TRANSFORMATIONS/Translations/<track-name>/`; `requirements.md`; termbase.
**Outputs:** A style-drift section appended to `qa-report.md`, with span references back to the offending passages.
→ `style-consistency-check/SKILL.md` *(to be written)*

---

## System skills

These skills operate on the vault's own structure — creating new skills, maintaining registrations, and auditing integrity. They are meta-level tools for contributors, not pipeline steps.

### `create-skill` **[exists]**
**Purpose:** Scaffold a new skill completely and correctly in a single pass — creates the SKILL.md, registers it in SKILLS-CATALOG.md, creates the slash command file, and optionally adds it to the CLAUDE.md quick-reference table.
**Inputs:** Skill name, purpose sentence, catalog section, inputs/outputs description, and whether it belongs in the CLAUDE.md "Skills quick-reference" table.
**Outputs:** `4-SYSTEM/Skills/<skill-name>/SKILL.md`, a new catalog entry, `.claude/commands/<skill-name>.md`, and optionally a new row in `CLAUDE.md`'s "Skills quick-reference" table.
→ [`create-skill/SKILL.md`](create-skill/SKILL.md)

---

## Maintenance skills

These skills check and report on vault integrity. They are read-only and safe to run on a schedule. They never modify vault content — they produce reports for human action.

### `vault-audit` **[exists]**
**Purpose:** Read-only weekly audit of the vault. Checks that every skill folder is registered in the catalog and has a command file (and the reverse — no orphaned command files pointing at a deleted skill); that 2-RAILS and 3-TRANSFORMATIONS files have required frontmatter; that no 3-TRANSFORMATIONS file references 1-SOURCES directly; that no complete output depends on a draft rail; that 0-INBOX/temp/ has no stale files; that no internal wiki links are dead; and that 2-RAILS/Verses/ filenames follow convention with a rail on file for every day card.
**Inputs:** None — operates on the vault as a whole.
**Outputs:** One dated report at `0-INBOX/vault-audit-<YYYY-MM-DD>.md` with checkboxed issues per category.
→ [`vault-audit/SKILL.md`](vault-audit/SKILL.md)

---

---

## Removed (not used in this anthology vault)

Template skills that assume a single commentary-bearing text, or manual-frontmatter helpers made redundant by the auto-frontmatter converters; their `4-SYSTEM/Skills/<name>/` folders have been **deleted outright** (there is no `Skills/_archived/` folder — an earlier version of this note said they were moved there, but they were removed instead; see `0-INBOX/vault-audit-2026-06-24.md`). Their `.claude/commands/<name>.md` files have been deleted as of the 2026-07-09 audit, since a command pointing at a deleted `SKILL.md` is dead:

`add-toc`, `commentary-frontmatter`, `format-commentary`, `format-root-text`, `glossary-combine`, `glossary-extract-raw`, `glossary-select`, `interlinear-gloss`, `json-to-commentary`, `local-wiki-article`, `property-creator`, `reference-frontmatter`, `root-text-frontmatter`, `section-summary-combined`, `section-summary-raw`, `source-property-extractor`, `structural-outline-ingest`, `translation-frontmatter`, `verse-context`.

If any of these are reinstated later, use `create-skill` to rebuild them correctly rather than restoring the old folders — the SKILL.md template and registration steps have moved on since these were written.

