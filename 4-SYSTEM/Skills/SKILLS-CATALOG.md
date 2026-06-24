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

### `root-text-frontmatter` **[exists]**
Generates complete YAML frontmatter for a root-text file in `1-SOURCES/Text/` by extracting metadata from its title, colophon, and opening content.
→ [`root-text-frontmatter/SKILL.md`](root-text-frontmatter/SKILL.md)

### `translation-frontmatter` **[exists]**
Generates complete YAML frontmatter for a translation file in `1-SOURCES/Translations/`, including translator, target language, and `translation_basis`.
→ [`translation-frontmatter/SKILL.md`](translation-frontmatter/SKILL.md)

### `reference-frontmatter` **[exists]**
Generates complete YAML frontmatter for a secondary-literature or reference file in `1-SOURCES/References/`.
→ [`reference-frontmatter/SKILL.md`](reference-frontmatter/SKILL.md)

---

## Rails-building skills (context preparation for translation)

These skills populate `2-RAILS/` with the structured context that translation and QA skills consume.

### `verse-rail` **[exists]**
**Purpose:** Build a **translation-grounded** verse rail for one verse of any canon — the WeBuddhist anthology's adaptation of `verse-context`, used because no commentaries are imported. Grounds the rail in the authoritative translation(s) the vault holds (Sujato / Patton / 84000) rather than a commentary tradition (which About Rails permits).
**Inputs:** Source block id(s) in `1-SOURCES/Text/`; aligned translation block(s) in `1-SOURCES/Translations/`; the `source_ref` label.
**Outputs:** One file at `2-RAILS/Verses/<text-slug>-<verse>.md` containing: source transclusion, authoritative rendering(s), a precise English disambiguated meaning (every claim cited), and theme/selection notes. `grounding: translation` (or `hybrid` if a commentary is later added).
→ [`verse-rail/SKILL.md`](verse-rail/SKILL.md)

### `local-wiki-article` **[exists]**
**Purpose:** Create or update a Local-Wiki article for one key term.
**Inputs:** Commentary passages that explain or define the term (via block citations from `1-SOURCES/`).
**Outputs:** One file at `2-RAILS/Local-Wiki/<term>_(<disambiguator>).md` containing: cited commentary explanations in the original language, and a short contextual definition drafted from those citations (also in the original language).
→ [`local-wiki-article/SKILL.md`](local-wiki-article/SKILL.md)

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

### `translation-qa` **[planned]**
**Purpose:** Review a translated section against the MQM translation error taxonomy, the track requirements, and the source rails.
**Inputs:** Translated section(s); `requirements.md`; `termbase.md`; relevant `2-RAILS/` files.
**Outputs:** Appended entries in `3-TRANSFORMATIONS/Translations/<track-name>/qa-report.md`. Each entry records: the segment, MQM error category, severity (critical / major / minor), and a suggested correction.
→ `translation-qa/SKILL.md` *(to be written)*

### `style-consistency-check` **[planned]**
**Purpose:** Catch style drift over long texts — creeping changes in register, sentence length, verse formatting, list handling, term gloss style.
**Inputs:** All translated files in `3-TRANSFORMATIONS/Translations/<track-name>/`; `requirements.md`; termbase.
**Outputs:** A style-drift section appended to `qa-report.md`, with span references back to the offending passages.
→ `style-consistency-check/SKILL.md` *(to be written)*

---

## Utility skills

### `source-property-extractor` **[exists]**
Extracts structured metadata (author, date, edition, language, publisher) from a source file and writes it to the frontmatter.
→ [`source-property-extractor/SKILL.md`](source-property-extractor/SKILL.md)

### `property-creator` **[exists]**
Creates or updates Obsidian frontmatter properties on a file.
→ [`property-creator/SKILL.md`](property-creator/SKILL.md)

---

## System skills

These skills operate on the vault's own structure — creating new skills, maintaining registrations, and auditing integrity. They are meta-level tools for contributors, not pipeline steps.

### `create-skill` **[exists]**
**Purpose:** Scaffold a new skill completely and correctly in a single pass — creates the SKILL.md, registers it in SKILLS-CATALOG.md, creates the slash command file, and optionally adds it to the CLAUDE.md quick-reference table.
**Inputs:** Skill name, purpose sentence, catalog section, inputs/outputs description, and whether it belongs in the CLAUDE.md §12 table.
**Outputs:** `4-SYSTEM/Skills/<skill-name>/SKILL.md`, a new catalog entry, `.claude/commands/<skill-name>.md`, and optionally a new §12 table row in `4-SYSTEM/CLAUDE.md`.
→ [`create-skill/SKILL.md`](create-skill/SKILL.md)

---

## Maintenance skills

These skills check and report on vault integrity. They are read-only and safe to run on a schedule. They never modify vault content — they produce reports for human action.

### `vault-audit` **[exists]**
**Purpose:** Read-only weekly audit of the vault. Checks that every skill folder is registered in the catalog and has a command file; that 2-RAILS and 3-TRANSFORMATIONS files have required frontmatter; that no 3-TRANSFORMATIONS file references 1-SOURCES directly; that no complete output depends on a draft rail; that 0-INBOX/temp/ has no stale files; and that no internal wiki links are dead.
**Inputs:** None — operates on the vault as a whole.
**Outputs:** One dated report at `0-INBOX/vault-audit-<YYYY-MM-DD>.md` with checkboxed issues per category.
→ [`vault-audit/SKILL.md`](vault-audit/SKILL.md)

---

## Archived / removed (not used in this anthology vault)

These template skills assume a single commentary-bearing text and don't apply to a translation-grounded anthology; moved to `Skills/_archived/` (see `0-INBOX/vault-audit-2026-06-24.md`):

`add-toc`, `commentary-frontmatter`, `format-commentary`, `format-root-text`, `glossary-combine`, `glossary-extract-raw`, `glossary-select`, `interlinear-gloss`, `json-to-commentary`, `section-summary-combined`, `section-summary-raw`, `structural-outline-ingest`, `verse-context`.
