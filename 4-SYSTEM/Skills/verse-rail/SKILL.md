---
name: verse-rail
description: Use this skill whenever a verse has been selected (by verse-selection or named directly by the user) and needs a rail built before rendering — even if the user just says "build the rail for Dhp 5" or names a sutta/verse directly without saying "rail." Builds a translation-grounded verse-of-the-day rail at 2-RAILS/Verses/<slug>.md for one verse from any canon (Pali, Chinese Āgama, Tibetan Kangyur): transcludes the source block, cites the authoritative translation(s) the vault holds, writes a precise disambiguated meaning, and tags theme + source_ref. This anthology holds no commentaries, so grounding is translation-based — About Rails explicitly permits this ("a claim may cite a commentary block ID, or a translation passage") — with one narrow, human-approved exception (grounding: source-only) for a few Kangyur sūtras 84000 hasn't translated yet, grounded on the Tibetan source alone; see the grounding table.
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
| **Tibetan Kangyur, no 84000 translation yet (Toh 12, 13, 16, 53, 60 only)** | `source-only` | Degé **PD** source; **no reference translation exists** | own rendering translated directly from bo; bo = verbatim source; **no reference to consult** — see the source-only note below |

- **zh is the verbatim CBETA source** on Chinese-source cards; **bo is the verbatim Degé source** on Tibetan-source cards — they *are* the quote.
- **84000 English is reference-only** — cite it, never ship its wording.
- **Grounding-by-parallel:** name the exact Pali parallel (e.g. Dhp 239) and transclude Sujato as the meaning anchor. The T210 Dharmapada and the Udānavarga are the Chinese/Tibetan Dharmapada — parallel to the Pali; **don't rely on them alone for non-Pali variety, and don't pull Chinese only from T210 or Tibetan only from the Udānavarga** (use the Āgamas and the Kangyur Mahāyāna sūtras too, per [`selection-criteria.md`](../../../3-TRANSFORMATIONS/verse-of-the-day/selection-criteria.md) §3).
- **`source-only` — the reference-less exception (Toh 12, 13, 16, 53, 60 only).** These five Kangyur sūtras have no 84000 translation and no Pali parallel to anchor on, so — by explicit human decision (Evan, 2026-07-13; recorded in [`candidate-pool/kangyur-scan-leads.md`](../../../3-TRANSFORMATIONS/verse-of-the-day/candidate-pool/kangyur-scan-leads.md)) — a rail may be built grounding on the Tibetan Degé source **alone**, with the Disambiguated Meaning translated directly from the bo with no reference translation to consult. This is a bounded exception, **not a general license**: it applies only to these five texts, and only after each is imported and registered. Everything else is unchanged and still fully enforced — the buddhavacana gate, verbatim-from-source, in-scope (mdo, not tantra/Vinaya/scholastic), ecumenical wording, and the ~125-char fit. Because there is no reference to catch a misreading, take **extra** care with the Tibetan: leave `status: draft`, and in `## Traditional Interpretation` / `## Theme & Selection Notes` flag explicitly that this rail is source-only and needs a native-Tibetan reviewer to confirm the meaning before it can move toward `complete`. Set `review_status: escalate-native-review` for bo. Do **not** use this grounding value for any text that *does* have an 84000 reference — that stays `source-plus-reference`.

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
grounding: translation | parallel-pali | source-plus-reference | source-only | chinese-source | hybrid
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
9. **Buddhavacana gate — spoken *by* the Buddha, not *about* him.** No praise-of-the-Buddha stanzas (e.g. Toh 323 was blocked for this), no words of disciples/gods/kings. If the passage is *about* the Buddha, reject it. (Udānavarga/Dharmapada/sūtra utterances of the Buddha are fine.) Also skip **bare proclamations of the Buddha's/an arahant's own attainment** ("my births are ended, the task is done, no more becoming") — authentic, but they report a finished state rather than teach or speak to the reader, so they're a poor daily card; see `selection-criteria.md` §2.
10. **Real quote, kept whole, that fits the card (~125 chars).** A complete verse or one self-contained sentence, quoted in full — never a summary, stitch, or gist. If it will not fit whole in all six languages, pick a shorter source (see `selection-criteria.md` §2). Prose Nikāya/sūtra sentences are welcome if short. The quote must also be **intelligible out of context**: a whole sentence that only makes sense with its backstory (e.g. Toh 95 "this earth is my witness," or a bare "I accept your repentance") is not a valid card even though it's a real quote — the card ships alone. See §2's two-part (whole + out-of-context) test.
11. **Ecumenical wording.** WeBuddhist is for all Buddhists: render *bodhicitta* as "the awakening mind," never "Great Vehicle mind"; keep Mahāyāna content in inclusive language; use the standard `termbase.md` rendering of each key term, not paraphrase (e.g. *mettā* = loving-kindness, not "love").
12. **Then build the day card + QA.** After the rail, build `day-NNN-<slug>.md` using the template in [`../../../3-TRANSFORMATIONS/verse-of-the-day/About verse-of-the-day.md`](../../../3-TRANSFORMATIONS/verse-of-the-day/About%20verse-of-the-day.md), run [`translation-qa`](../translation-qa/SKILL.md), then add the `log.md` row.

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
- [ ] If `grounding: source-only`: text is one of the five approved (Toh 12/13/16/53/60), it's imported + registered, the rail is flagged source-only for native-Tibetan review, and bo `review_status: escalate-native-review`.

---

## Improve this skill (friction log)

**Always run this as the final step, after the task is done.** The goal is that the next agent to use this skill struggles less than you did.

1. **Recall the friction.** Walk back through the run and list every point where you were confused, guessed, backtracked, hit an error, re-read a file to figure something out, or wished this SKILL.md had told you something up front. That list is your friction log for this run.
2. **Diagnose each item.** For each friction point, decide: was it caused by *this skill* being unclear, incomplete, missing a worked example, or missing a gotcha or edge case? Or was it a one-off specific to this task? Only skill-level gaps get fixed here — ignore the one-offs.
3. **Fix the skill.** Edit *this* `SKILL.md` so the next agent avoids the same wall: add the missing instruction, a short worked example, a "gotcha" note, or a Completion-check item; tighten wording that misled you. Keep every existing hard rule and gate intact — **never weaken a gate or dedupe/verbatim/buddhavacana rule to reduce friction.** If a rule itself was the source of friction, add a clarifying note or example rather than removing it, and call it out for a human in your summary.
4. **Record the change.** In your final summary to the user, note in one line per change what friction you hit and what you changed (e.g. "kept mistyping the bo block id -> added a 'verify the exact ^block anchor first' gotcha"). If you hit no real friction, say so explicitly and change nothing.
