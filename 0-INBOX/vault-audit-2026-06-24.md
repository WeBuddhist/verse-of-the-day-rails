# Vault Audit — fit for purpose (2026-06-24)

Auditing the vault against its **actual** intent: a multi-canon **buddhavacana
anthology** producing **verse of the day** (translation-grounded, no
commentaries) — *not* the single-text, commentary-centric vault the Railroads
template was built for. Findings categorized: **UPDATE**, **REMOVE/ARCHIVE**,
**KEEP**, **CONTENT**.

---

## A. UPDATE — to match the anthology intent

| # | File | Issue | Fix |
|---|------|-------|-----|
| A1 | `README.md` | Still the template stub: "[text-slug]-rails… Replace every [text-slug]… This vault serves [name of text]." | Rewrite as the WeBuddhist VOTD anthology. **(done)** |
| A2 | `4-SYSTEM/CLAUDE.md` | "[name of text]" placeholder; assumes one text + commentaries. | State the anthology; point to `verse-rail` + `grounding: translation`; note no commentaries; multi-source addressing in annex §2. **(done)** |
| A3 | `4-SYSTEM/Guidelines/0-VAULT-Structure.md` §1 "One Vault Per Text" | Directly contradicts our model. | Add an exception note → annex §0 (anthology). **(done)** |
| A4 | `source-formatting.md` (referenced by 3 skills, **missing**) | Dangling reference. | Create a concise one documenting our 4 addressing schemes; point to annex §2. **(done)** |
| A5 | `2-RAILS/About Rails.md` | Heavily commentary-centric; our rails are translation-grounded. | Add a top note: this anthology grounds rails in translations (`verse-rail`), per About Rails' own "or a translation passage". **(done)** |
| A6 | `verse-rail` command file | Skill has no `.claude/commands/verse-rail.md` (path was write-protected). | Human to add it (vault-audit flags 24 skills / 23 commands). |

## B. REMOVE / ARCHIVE — not needed for this vault

The vault has **0 commentaries** and **0 section summaries**, and we've decided
(this session) to ground rails in translations, not commentary. These skills
therefore have no applicability here:

| Skill | Why it doesn't fit |
|-------|--------------------|
| `json-to-commentary` (+ `tipitaka_org_atthakatha` converter) | We import no commentaries. |
| `commentary-frontmatter` | Pairs with commentary import. |
| `section-summary-raw` | Needs commentaries + a single-text TOC. |
| `section-summary-combined` | Same. |
| `verse-context` | Commentary-centric; **superseded by `verse-rail`** for this anthology. |

**Borderline** (single-text structural / bilingual-glossary chain — keep only if a
translation-consistency workflow will use them; otherwise archive):
`add-toc`, `structural-outline-ingest`, `interlinear-gloss`,
`glossary-extract-raw`, `glossary-combine`, `glossary-select`,
`format-root-text`, `format-commentary`.

> Recommendation: **archive** rather than delete — move to
> `4-SYSTEM/Skills/_archived/` and remove their catalog entries — so the template
> lineage is preserved but the working skill set reflects this vault.

## C. KEEP — core to the anthology

- `verse-rail` (core), `local-wiki-article` (usable, translation-grounded later).
- `json-to-source-text` + our converters (`suttacentral_bilara`, `cbeta_agama`,
  `openpecha_kangyur`, `suttacentral_agama_en`, `tei_84000_en`) + import scripts.
- Frontmatter/util: `root-text-frontmatter`, `translation-frontmatter`,
  `reference-frontmatter`, `source-property-extractor`, `property-creator`,
  `epub-to-markdown`.
- System: `create-skill`, `vault-audit`.
- The `Adaptations/` transformation category is unused but valid — keep.

## D. CONTENT — size / corpus

- `1-SOURCES/` is **212 MB**, dominated by the giant Tibetan Perfection-of-Wisdom
  / Avataṃsaka texts: `bo-toh8` (38 MB), `bo-toh44` (13 MB), `bo-toh287` (9.5 MB),
  `bo-toh9` (9.5 MB), `bo-toh10` (7.1 MB) — ~77 MB in five files. These are
  authentic buddhavacana but **not daily-verse material** (huge prose).
  **Recommendation:** trim the mega-texts (move out, or exclude from import) to
  slim the repo; keep the verse-rich and short sūtras. Pairs with the note in
  `vault-annex.md` §1.
- `0-INBOX/` is clean (16 KB — just the two Dhammapada sample JSONs). The bulk
  source clones lived in `/tmp` during import, not the vault. Good.

## E. Integrity (vault-audit checks)

- Frontmatter present on rails; citation chain intact (rails cite `1-SOURCES/`).
- No `3-TRANSFORMATIONS` file cites `1-SOURCES` directly.
- All sources `status: draft` (correct — human marks complete).
- 1 skill (`verse-rail`) lacks a command file (A6).

---

## Proposed actions

**Done now (safe, non-destructive):** A1–A5.

**Needs your go-ahead (destructive / judgment):**
1. **Archive the commentary-centric skills** (B, the first five) — clearly unused.
2. **Decide on the borderline skills** (B borderline) — archive or keep.
3. **Trim the giant Perfection-of-Wisdom Tibetan texts** (D) — ~77 MB.
