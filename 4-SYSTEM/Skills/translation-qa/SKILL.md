---
name: translation-qa
description: Automated pre-review QA pass on verse-of-the-day renderings, run BEFORE a human reviewer sees them. For one verse's six language renderings (or any subset), critiques each against its rail's disambiguated meaning and flagged rendering choices, back-translates to catch drift, checks terminology and register, produces a revised draft, and flags low-confidence spots for the reviewer. Raises draft quality and cuts reviewer load — it does NOT replace native dharma-reviewer sign-off (especially bo/mn).
---

# translation-qa (pre-review pass)

Run on a day card's renderings once they're drafted and **before** they go to a
native reviewer. The goal: every error the model *can* catch is caught and fixed
here, and the reviewer is handed a clean draft + a triage note pointing at the
genuinely uncertain spots.

**Ground truth is the rail, not parametric knowledge.** Every check and every
correction traces to the rail's *Disambiguated Meaning* and *flagged rendering
choices* (`2-RAILS/Verses/<slug>.md`) — and to the term glossary if one exists.
The skill never introduces content that isn't in the rail.

**It does not sign anything off.** Output stays `status: draft`. Native review
(especially Tibetan and Mongolian) is still required — this makes that review
faster and higher-confidence, not optional.

---

## Inputs

- **The rail** — `2-RAILS/Verses/<slug>.md`: the Disambiguated Meaning (the
  authority for *what the verse means*) and the flagged rendering choices (the
  authority for *how to handle* contested words/structure).
- **The day card** — `3-TRANSFORMATIONS/Plans/verse-of-the-day/days/<day>.md`
  with the draft renderings (en, zh, bo, hi, ne, mn).
- **Term glossary** *(if present)* — locked key-term renderings per language.
- The English rendering (Sujato-anchored) serves as a second meaning anchor.

## The QA pass — per language

For each rendering, evaluate against the rail and record findings:

1. **Accuracy (vs the rail's meaning).** MQM accuracy: *mistranslation*,
   *omission*, *addition*. Every clause of the disambiguated meaning must be
   present, nothing distorted, nothing invented.
2. **Faithfulness to intent.** Does it preserve the structural intent the rail
   flags? (e.g. participial "overcoming…" vs two coordinate commands;
   adjectives vs manner-adverbs; the cause-and-effect a verse turns on.)
3. **Back-translation.** Back-translate the rendering into English and compare
   to the rail's Disambiguated Meaning. Record the back-translation and any
   divergence — divergence is a flag, not an auto-fail.
4. **Terminology.** Key Buddhist terms match the glossary / standard vocabulary
   for that language and are consistent. Flag invented or inconsistent renderings
   (e.g. nibbāna → 涅槃 / myang-'das / निर्वाण should be the agreed form).
5. **Register & locale.** Modern, plain, audience-appropriate ("feel like home",
   not scholarly). **zh = modern Traditional Chinese, Taiwan/HK/SG.** **No em
   dashes in the English.** Not classical/Literary register.
6. **Fluency.** Natural in the target language; reads as something a person would
   actually say.

## Severity

- **critical** — wrong meaning, fabricated content, or a doctrinal distortion. Must be fixed (or escalated) before review.
- **major** — a nuance, key term, or structural intent distorted.
- **minor** — register, fluency, or style polish.

## Outputs

1. **Revised renderings** written back into the day card (status stays `draft`).
2. **A QA note** appended to the day card, per language:

```markdown
### QA — <language> (pre-review, against 2-RAILS/Verses/<slug>.md)
- Back-translation: "<EN back-translation of the revised rendering>"
- Findings:
  - [critical|major|minor] <category>: <issue> → <fix applied / or flag>
- Confidence flags (for reviewer): <span(s) the model is unsure of, and why>
- Net: <clean / needs native review on flagged spans / escalate>
```

## Rules

1. **Trace every correction to the rail or glossary.** No parametric "I think it should be…".
2. **Don't over-correct.** If the draft is faithful, say so; don't churn good wording.
3. **Flag, don't fabricate.** If the right rendering is genuinely uncertain (common for bo/mn), flag it for the reviewer rather than guessing confidently.
4. **Never set `complete`** or imply the rendering is reviewer-approved.
5. **Honour the language rules** (zh Traditional/Taiwan; no em dash in English; modern register) as hard checks, not suggestions.

## Procedure

1. Load the rail's Disambiguated Meaning + flagged choices, and the glossary.
2. For each target rendering: run checks 1–6; back-translate; list findings by severity.
3. Revise the rendering to fix critical/major issues that are determinable from the rail; leave genuinely uncertain spots as confidence flags.
4. Write the revised rendering back to the day card; append the QA note.
5. Keep `status: draft`; summarise in `review_status` which languages are "clean for review" vs "escalate".

## Completion check

- [ ] Every rendering checked against the rail's meaning (not parametric knowledge).
- [ ] Back-translation recorded for each language.
- [ ] Findings tagged by MQM category + severity; critical/major fixed or flagged.
- [ ] Terminology checked against glossary; register/locale rules enforced (zh Traditional, no em-dash English).
- [ ] Confidence flags listed for the reviewer; `status` still `draft`.
