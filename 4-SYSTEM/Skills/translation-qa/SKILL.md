---
name: translation-qa
description: Use this skill whenever a verse-of-the-day's draft renderings are ready and need pre-review QA before a human reviewer sees them — even if the user just says "check the drafts," "QA day 20," or "is this ready for review" without naming translation-qa. For one verse's seven language renderings (en · zh · bo · hi · ne · mn · lbj Ladakhi, or any subset), critiques each against its rail's disambiguated meaning and flagged rendering choices, back-translates to catch drift, checks terminology and register, revises the draft, and flags low-confidence spots for the reviewer. On Chinese- or Tibetan-source cards it also back-translates the modern zh/bo against the verbatim source. Raises draft quality and cuts reviewer load — it does NOT replace native dharma-reviewer sign-off (especially bo/mn/lbj).
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
- **The day card** — `3-TRANSFORMATIONS/verse-of-the-day/<day>.md`
  with the draft renderings (en, zh, bo, hi, ne, mn).
- **Termbase** — [`3-TRANSFORMATIONS/verse-of-the-day/termbase.md`](../../../3-TRANSFORMATIONS/verse-of-the-day/termbase.md): locked key-term renderings per language. The terminology check (step 4) compares each rendering's key terms against it; flag mismatches and ⚑ (unratified) rows.
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
4. **Terminology — standard dharma term, not paraphrase.** Each key Buddhist term
   must use the **established, standard rendering** in that language (per
   `termbase.md`), not an everyday paraphrase. Real misses caught this way:
   *mettā* must be "loving-kindness / 慈 / मैत्री," **not** "love / प्रेम";
   *puñña* = "merit," not "good deed"; the five aggregates take their standard
   names (form, feeling, perception, **volition, consciousness** — not "will,
   awareness"). Flag invented/inconsistent renderings; add a termbase row rather
   than coining per-verse.
5. **Ecumenical wording (WeBuddhist is for all Buddhists).** Render *bodhicitta*
   as **"the awakening mind," never "Great Vehicle mind"** (大乘 reads sectarian).
   *Bodhisattva* is acceptable (pan-Buddhist); frame such lines as universal.
   Flag any sectarian phrasing.
6. **Register & locale.** Modern, plain, audience-appropriate ("feel like home",
   not scholarly). **zh = modern Traditional Chinese, Taiwan/HK/SG.** **No em
   dashes in the English.** **Not classical/Literary register — in ANY language,
   including on a card whose source is that same language.** Our readers are
   cultural Buddhists with a casual practice, not scholars: a Tibetan or Chinese
   reader gets plain modern prose for the same reason an English reader gets
   modern English rather than Middle English. See rule 8.
7. **Real quote, whole, within the card (~125 chars).** The rendering is a
   *complete* quote (a verse or one self-contained sentence), never a summary,
   stitch, or gist. If it reads like a paraphrase-to-fit, that is a **critical**
   finding — the fix is a shorter source, not tighter wording. Check it fits the
   ~125-char card in every language.
8. **Source-language cards ship MODERN language, and get an extra back-translation
   check.** (Rewritten 2026-09 — this rule previously said the opposite, that `zh`/`bo`
   *must be* the verbatim source. It does not say that any more. **Do not revert a
   modern `zh`/`bo` rendering to the classical source text.**)
   - For a **Chinese-source** verse the shipped `zh` is **modern Traditional
     Chinese** (Taiwan/HK/SG); for a **Tibetan-source** verse the shipped `bo` is
     **modern Tibetan**. Both are freshly rendered from the rail's Disambiguated
     Meaning, exactly like the other five languages.
   - **Why:** our readers are cultural Buddhists with a casual practice, not
     scholars, and the card must be *instantly* understandable. An English reader
     isn't handed Middle English to decode; a Tibetan or Chinese reader is owed the
     same plain-language treatment **even when the quote comes from their own
     canon.** Full reasoning in `verse-rail`'s "Source-language output ships
     modern" section and `vault-annex.md` §4.
   - **The extra check this rule now carries.** The verbatim source still appears in
     the card's `## Source` block, and on a source-language card it is a **second
     ground truth**: back-translate the modern `zh`/`bo` **against the verbatim
     source itself**, not only against the English, and record that in the QA note.
     Drift away from the original is a **critical** finding. This replaces the old
     rule's built-in guarantee — a copied source could not be mistranslated, a
     modern rendering can be.
   - Also confirm each classical→modern substitution the rail lists is faithful, and
     that the result is *genuinely* modern rather than a half-classical middle
     register. Flag the register question explicitly for the native reviewer.
   - Native-review stakes **rise** on these cards: `bo` is now WeBuddhist-authored
     prose rather than quoted Kangyur, so it stays `escalate-native-review`.
   - 84000 English is reference-only and must never appear as the shipped text.
   - **Backfill debt:** only Days 76, 78, 79 follow this rule. Roughly 23
     Tibetan-source and 27 Chinese-source cards before Day 76 still ship classical
     text; they predate the rule and are not precedent.
9. **Fluency.** Natural in the target language; reads as something a person would
   actually say.

## Severity

- **critical** — wrong meaning, fabricated content, or a doctrinal distortion. Must be fixed (or escalated) before review.
- **major** — a nuance, key term, or structural intent distorted.
- **minor** — register, fluency, or style polish.

## Outputs

1. **Revised renderings** written back into the day card (status stays `draft`).
2. **A QA note** appended to the day card. Use the house format (one `##`
   section, one `###` per language):

```markdown
## QA — pre-review (against 2-RAILS/Verses/<slug>.md)

### en
- Back-translation: "<EN back-translation of the revised rendering>"
- Findings: <faithfulness vs rail; term/ecumenical/length checks; "No em dash ✓">
- Net: clean for review.

### zh (Traditional)
- Back-translation: "<EN back-translation of the modern zh>"
- Findings: <faithfulness; term/register checks; Taiwan/HK/SG register ✓>. **If the source IS Chinese:** state that this is our modern rendering (not the source), list the classical→modern substitutions, and record the back-translation **against the verbatim source**.
- Net: clean for review.

### hi
- Back-translation / findings. Net: clean for review.

### ne
- Back-translation / confidence flags. Net: needs native review.

### bo ⚑
- Back-translation (approx) / confidence flags. **If the source IS Tibetan:** state that this is our modern rendering (not the verbatim Degé), list the classical→modern substitutions, back-translate **against the verbatim source**, and flag the register question explicitly.
- Net: escalate to native Tibetan dharma reviewer.

### mn ⚑
- Back-translation (approx) / confidence flags. Net: escalate to native Mongolian dharma reviewer.

### lbj (Ladakhi) ⚑
- Back-translation (approx) / confidence flags. Ladakhi ships in **Devanagari** (Evan, 2026-09), so `lbj` can never be a copy of the `bo` line. The real trap is the opposite one: it shares its script with `hi`/`ne` but is a **Tibetic** language, so its vocabulary is mostly cognate with Tibetan while only the script matches Hindi. **Flag any sign the rendering has drifted into Hindi** (Indo-Aryan words or grammar), and note which Devanagari orthography convention was assumed for Ladakhi.
- Net: escalate to native Ladakhi dharma reviewer.
```

`review_status` in the card frontmatter mirrors the Nets: en/zh/hi default
`clean-for-review` when faithful, ne `needs-native-review`, bo/mn/**lbj**
`escalate-native-review` (use `blocked` if a gate fails, e.g. non-buddhavacana).

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
- [ ] Back-translation recorded for **each of the seven languages** (en · zh · bo · hi · ne · mn · lbj).
- [ ] Findings tagged by MQM category + severity; critical/major fixed or flagged.
- [ ] Terminology checked against glossary; register/locale rules enforced (zh Traditional, no em-dash English).
- [ ] **No rendering is in classical register** — including the source language's own rendering on a Chinese- or Tibetan-source card.
- [ ] **On a source-language card:** the modern `zh`/`bo` was back-translated **against the verbatim source** (not only the English), the rail's classical→modern substitutions were each checked, and the register question was flagged for the native reviewer.
- [ ] `lbj` is genuinely Ladakhi, not a copy of the `bo` line, and is set to `escalate-native-review`.
- [ ] Confidence flags listed for the reviewer; `status` still `draft`.

---

## Improve this skill (friction log)

**Always run this as the final step, after the task is done.** The goal is that the next agent to use this skill struggles less than you did.

1. **Recall the friction.** Walk back through the run and list every point where you were confused, guessed, backtracked, hit an error, re-read a file to figure something out, or wished this SKILL.md had told you something up front. That list is your friction log for this run.
2. **Diagnose each item.** For each friction point, decide: was it caused by *this skill* being unclear, incomplete, missing a worked example, or missing a gotcha or edge case? Or was it a one-off specific to this task? Only skill-level gaps get fixed here — ignore the one-offs.
3. **Fix the skill.** Edit *this* `SKILL.md` so the next agent avoids the same wall: add the missing instruction, a short worked example, a "gotcha" note, or a Completion-check item; tighten wording that misled you. Keep every existing hard rule and gate intact — **never weaken a gate or dedupe/verbatim/buddhavacana rule to reduce friction.** If a rule itself was the source of friction, add a clarifying note or example rather than removing it, and call it out for a human in your summary.
4. **Record the change.** In your final summary to the user, note in one line per change what friction you hit and what you changed (e.g. "kept mistyping the bo block id -> added a 'verify the exact ^block anchor first' gotcha"). If you hit no real friction, say so explicitly and change nothing.
