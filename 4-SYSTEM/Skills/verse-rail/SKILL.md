---
name: verse-rail
description: Build a translation-grounded verse-of-the-day rail at 2-RAILS/Verses/<slug>.md for one verse from any canon (Pali, Chinese Āgama, Tibetan Kangyur). Transcludes the source block, cites the authoritative translation(s) the vault holds, writes a precise disambiguated meaning, and tags theme + source_ref. Use this INSTEAD of `verse-context` for the WeBuddhist buddhavacana anthology, which has no commentaries imported — `verse-context` requires a commentary tradition; this skill grounds rails in translations, which About Rails explicitly permits ("a claim may cite a commentary block ID, or a translation passage").
---

# verse-rail (translation-grounded)

Produces the verse-level rail that the verse-of-the-day Plan consumes. The
Plan's six language streams never see the bare verse — they see this rail: the
source text, the authoritative translation(s) we hold, and a precise
disambiguated meaning grounded in them. From a `complete` rail, each stream
writes its own modern rendering.

This is the anthology's adaptation of `verse-context`. Differences, both
deliberate and documented in `vault-annex.md`:

- **Grounding is translation, not commentary.** The anthology imported no
  commentaries. The grounding source is the authoritative translation(s):
  Sujato (Pali, CC0), 84000 (Tibetan, CC BY-NC-ND reference), Patton (Āgama,
  CC0). If a commentary is later imported for a verse, add a Traditional
  Interpretation section and flip `grounding:` to `hybrid`.
- **Filenames are text-qualified.** Multi-text anthology, so `dhp-5.md`,
  `sa-262.md`, `snp-1-8.md` — not the single-text `5.md`.
- **Disambiguated meaning is English.** The output is modern translation into
  six languages; the rail's job is to fix the meaning the renderings target.
  The original-language source is transcluded directly above it.

---

## Inputs

- **Verse** — its source block id(s) in `1-SOURCES/Text/<file>.md`.
- **Translation(s)** — the authoritative rendering(s) in `1-SOURCES/Translations/`
  whose block ids align to the source (by verse number or sūtra number).
- **source_ref label** — the citation shown with the verse (e.g. `Dhp 5`,
  `SĀ 262`, `Snp 1.8`), per `vault-annex.md` §2.

## Output

`2-RAILS/Verses/<slug>.md`, where `<slug>` is text-slug + verse id (`dhp-5`,
`sa-262`, `snp-1-8`, `udv-...`). Update in place if it exists.

## Output format

```markdown
---
ref: <slug>
source_ref: "<label, e.g. Dhp 5>"
canon: Pali | Chinese Āgama | Tibetan Kangyur
unit_type: single | group
source_text: 1-SOURCES/Text/<file>.md
source_block: "^<id>"
grounding: translation | hybrid
translations: [sujato | patton | 84000 | ...]
theme: <one-word tag>
speaks_to: [<everyday felt-states this verse meets, e.g. angry, lonely>]
buddhist_lens: "<one-line: hindrance/wholesome-state → skillful turn>"
occasions: [<Buddhist holidays this verse suits, if any — see occasions.md>]
concepts: [term (gloss), ...]
status: draft
---

## Source Text
![[1-SOURCES/Text/<file>.md#^<id>]]

## Authoritative Renderings
### <Translator> — <language> (<license>)
![[1-SOURCES/Translations/<file>.md#^<id>]]

## Traditional Interpretation (commentary)
*No commentary imported.* (Slot — see vault-annex §3 if one is added.)

## Disambiguated Meaning
<Precise English restatement of what the verse means, grounded in the source +
the cited translation. Flag rendering choices (don't fix them — that's each
stream's termbase). Every claim cites a 1-SOURCES translation/source block.>
(1-SOURCES/Translations/<file>.md#^<id>)

## Theme & Selection Notes
<Theme; whether self-contained; why it suits verse of the day.>

## Concept Links
<stubs for Local-Wiki terms, when built>
```

## Rules

1. **Transclude source and translation — never copy.** `![[…#^id]]`.
2. **Ground every claim in the disambiguated meaning** to a `1-SOURCES/` block (translation or source). No parametric claims. If it can't be cited, leave it out and keep `status: draft`.
3. **Flag, don't fix, rendering choices.** Where translators differ (e.g. *averena* = "by love" vs "by non-hatred"), note the options. For recurring **key terms**, use the shared [`termbase.md`](../../../3-TRANSFORMATIONS/Plans/verse-of-the-day/termbase.md) (e.g. *sahāya* ≠ *kalyāṇa-mitta*); add a row there if a term is missing rather than deciding per-verse.
4. **84000 English is reference-only** (CC BY-NC-ND): cite/point to it, do not reproduce large excerpts in the rail; the shipped verse is the vault's own rendering.
5. **`status: draft` always** — a domain specialist sets `complete`.
6. **One canon's translation per `### Authoritative Renderings` subsection**, each labelled with its license.
7. **Tag `speaks_to:` honestly** with the everyday felt-states the verse genuinely meets (anger, grief, worry, craving, gratitude…), per `discovery-by-feeling.md`. These power the "where are you right now?" discovery feature. Don't over-tag; tag what the verse actually addresses. Observe the wellbeing guardrail for distress-related states.

## Procedure

1. Confirm the source block id exists in `1-SOURCES/Text/`. If not, fix the source first.
2. Identify the aligned translation block(s) we hold.
3. Transclude source; transclude/cite translation(s).
4. Write the disambiguated meaning from source + translation, citing each claim; flag rendering choices.
5. Add theme + selection notes; stub concept links.
6. Fill frontmatter; `status: draft`. Write to `2-RAILS/Verses/<slug>.md`.

## Completion check

- [ ] Source + translation transcluded (not copied), block ids resolve.
- [ ] Disambiguated meaning grounded, every claim cited; rendering choices flagged.
- [ ] `source_ref`, `canon`, `grounding`, `theme` set; `status: draft`.
- [ ] 84000 text referenced, not bulk-reproduced.
