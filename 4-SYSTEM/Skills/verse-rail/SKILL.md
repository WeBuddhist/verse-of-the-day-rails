---
name: verse-rail
description: Use this skill whenever a verse has been selected (by verse-selection or named directly by the user) and needs a rail built before rendering — even if the user just says "build the rail for Dhp 5" or names a sutta/verse directly without saying "rail." Builds a translation-grounded verse-of-the-day rail at 2-RAILS/Verses/<slug>.md for one verse from any canon (Pali, Chinese Āgama, Tibetan Kangyur): transcludes the source block, cites the authoritative translation(s) the vault holds, writes a precise disambiguated meaning, and tags theme + source_ref. This anthology holds no commentaries, so grounding is always translation-based — About Rails explicitly permits this ("a claim may cite a commentary block ID, or a translation passage").
---

# verse-rail (translation-grounded)

Produces the verse-level rail that the verse-of-the-day Plan consumes. The
Plan's six language streams never see the bare verse — they see this rail: the
source text, the authoritative translation(s) we hold, and a precise
disambiguated meaning grounded in them. From a `complete` rail, each stream
writes its own modern rendering.

Key conventions, documented in `vault-annex.md`:

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

## Grounding & licensing by source (what to cite, what to ship)

| Source | `grounding:` | License / handling | Shipped rendering |
|---|---|---|---|
| **Pali** — Dhammapada, Sutta Nipāta, Udāna, Itivuttaka, **DN/MN/SN/AN** | `translation` | Sujato **CC0** — transclude the aligned block | our modern rendering; en anchors on Sujato |
| **Chinese Dharmapada (法句經 T210)** | `parallel-pali` | CBETA **CC BY-NC-SA** | own rendering; **zh = verbatim source**; ground on the Dhp parallel (Sujato) |
| **Chinese Āgamas (DĀ/MĀ/SĀ/EĀ)** | `parallel-pali` or `chinese-source` | CBETA CC BY-NC-SA; Patton CC0 for ~54 paired suttas | own rendering; zh = verbatim source |
| **Chinese Mahāyāna sūtras (T235/262/366/389/475/779…)** | `chinese-source` | CBETA CC BY-NC-SA | own rendering; zh = verbatim source; cross-check a standard translation |
| **Tibetan Udānavarga (Toh 326)** | `parallel-pali` | Degé **Public Domain** | own rendering; **bo = verbatim source**; ground on the Pali Dhp/Udāna parallel |
| **Tibetan Kangyur Mahāyāna sūtras (bo-toh + 84000)** | `source-plus-reference` | Degé **PD** source; **84000 English = reference only (CC BY-NC-ND — never excerpt)** | own rendering from bo; bo = verbatim source; 84000 consulted for meaning only |

- **zh is the verbatim CBETA source** on Chinese-source cards; **bo is the verbatim Degé source** on Tibetan-source cards — they *are* the quote.
- **84000 English is reference-only** — cite it, never ship its wording.
- **Grounding-by-parallel:** name the exact Pali parallel (e.g. Dhp 239) and transclude Sujato as the meaning anchor. The T210 Dharmapada and the Udānavarga are the Chinese/Tibetan Dharmapada — parallel to the Pali; **don't rely on them alone for non-Pali variety, and don't pull Chinese only from T210 or Tibetan only from the Udānavarga** (use the Āgamas and the Kangyur Mahāyāna sūtras too, per `selection-criteria.md` §3).

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
grounding: translation | parallel-pali | source-plus-reference | chinese-source | hybrid
translations: [sujato | patton | 84000-reference | pali-parallel-reference | own-from-source | ...]
pali_parallel: "<if grounding: parallel-pali — e.g. Dhp 239>"
vehicle: "<Mahāyāna — only for Mahāyāna sūtras>"
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
3. **Flag, don't fix, rendering choices.** Where translators differ (e.g. *averena* = "by love" vs "by non-hatred"), note the options. For recurring **key terms**, use the shared [`termbase.md`](../../../3-TRANSFORMATIONS/verse-of-the-day/termbase.md) (e.g. *sahāya* ≠ *kalyāṇa-mitta*); add a row there if a term is missing rather than deciding per-verse.
4. **84000 English is reference-only** (CC BY-NC-ND): cite/point to it, do not reproduce large excerpts in the rail; the shipped verse is the vault's own rendering.
5. **`status: draft` always** — a domain specialist sets `complete`.
6. **One canon's translation per `### Authoritative Renderings` subsection**, each labelled with its license.
7. **Tag `speaks_to:` honestly** with the everyday felt-states the verse genuinely meets (anger, grief, worry, craving, gratitude…), per `discovery-by-feeling.md`. These power the "where are you right now?" discovery feature. Don't over-tag; tag what the verse actually addresses. Observe the wellbeing guardrail for distress-related states.
8. **Verify the source verbatim first — never render from memory.** Grep the exact block from `1-SOURCES/` before writing anything. A mistyped syllable is a fabricated quote (real bug caught this way: Iti 22 is *sukhudrayaṁ*, not *sukhindriyaṁ*). The zh/bo shown on the card must be copy-exact from the source.
9. **Buddhavacana gate — spoken *by* the Buddha, not *about* him.** No praise-of-the-Buddha stanzas (e.g. Toh 323 was blocked for this), no words of disciples/gods/kings. If the passage is *about* the Buddha, reject it. (Udānavarga/Dharmapada/sūtra utterances of the Buddha are fine.)
10. **Real quote, kept whole, that fits the card (~125 chars).** A complete verse or one self-contained sentence, quoted in full — never a summary, stitch, or gist. If it will not fit whole in all six languages, pick a shorter source (see `selection-criteria.md` §2). Prose Nikāya/sūtra sentences are welcome if short.
11. **Ecumenical wording.** WeBuddhist is for all Buddhists: render *bodhicitta* as "the awakening mind," never "Great Vehicle mind"; keep Mahāyāna content in inclusive language; use the standard `termbase.md` rendering of each key term, not paraphrase (e.g. *mettā* = loving-kindness, not "love").
12. **Then build the day card + QA.** After the rail, build `days/day-NNN-<slug>.md` using the template in [`../../../3-TRANSFORMATIONS/verse-of-the-day/About verse-of-the-day.md`](../../../3-TRANSFORMATIONS/verse-of-the-day/About%20verse-of-the-day.md), run [`translation-qa`](../translation-qa/SKILL.md), then add the `log.md` row.

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
