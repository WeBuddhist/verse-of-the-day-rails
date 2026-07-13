---
name: candidate-tagging
description: Use this skill to bulk-scan one or more source files in 1-SOURCES/Text/ for verse-of-the-day candidates and record them in the candidate pool — even if the user just says "tag Toh 100-120," "scan the Majjhima Nikāya for candidates," or "seed the pool for the Chinese Āgamas" without naming candidate-tagging directly. Produces lightweight, pre-verified entries (buddhavacana confirmed, verbatim quote captured, rough length estimate, speaks_to and/or theme tagged) in candidate-pool/<canon>.md, plus near-miss entries in candidate-pool/rejected.md, so a later, much lighter selection pass never has to re-scan raw source text. This is the deliberate heavy-upfront-cost investment that makes verse-selection cheap afterward — it does not select, schedule, or build a rail for anything (that's verse-selection and verse-rail).
---

# candidate-tagging

Scans source text once, up front, and banks everything a future selection pass would otherwise have to re-derive: whether a passage is genuinely spoken by the Buddha, whether it can be quoted whole without distillation, roughly how long it runs in English, and which felt-states/themes it serves. The payoff is that `verse-selection` (and any future rotation skill built on top of the pool) can filter `candidate-pool/*.md` instead of reading raw `1-SOURCES/` text — the expensive gate-checking work happens once per passage, not once per selection cycle.

This skill produces **candidates for a later pass to claim**, not a scheduled verse. It never sets a `day:`/date, never writes a day card, and never marks anything `complete`.

---

## Inputs

- **Source file(s) to scan** — one or more files (or a named range, e.g. "Toh 100–120," "the Majjhima Nikāya," "files under 40 lines") in `1-SOURCES/Text/`, plus each file's paired translation/reference file in `1-SOURCES/Translations/` if one exists.
- **`discovery-by-feeling.md`** (`3-TRANSFORMATIONS/verse-of-the-day/discovery-by-feeling.md`) — the fixed 24-entry `speaks_to` vocabulary (Door A + Door B). Never invent a `speaks_to` value outside this list.
- **`candidate-pool/theme-checklist.md`** (`3-TRANSFORMATIONS/verse-of-the-day/candidate-pool/theme-checklist.md`) — the self-extending list of recognized core Buddhist teachings to tag `theme:` against.
- **Existing pool state** — `candidate-pool/pali.md`, `candidate-pool/chinese.md`, `candidate-pool/tibetan.md`, `candidate-pool/rejected.md` — check before tagging so the same passage/toh-number/sutta isn't re-added.
- **`log.md`** and every `2-RAILS/Verses/*.md` — the already-claimed set; don't re-tag a passage already built into a rail (it's either already in the pool as `claimed`, or add it as `claimed` if this is the first time it's being backfilled into the pool).
- **`selection-criteria.md` §1–2** — the hard gates and quality bar this skill checks against (same bar as `verse-rail`, just applied earlier).

## Output

Appends entries to `3-TRANSFORMATIONS/verse-of-the-day/candidate-pool/<canon>.md` (`pali.md` / `chinese.md` / `tibetan.md`, matching the scanned file's canon) and/or `3-TRANSFORMATIONS/verse-of-the-day/candidate-pool/rejected.md`. Never creates new pool files beyond these three canons plus `rejected.md` and `theme-checklist.md` without asking first.

---

## Output file format

Each accepted candidate is one record, appended to the matching canon's pool file:

```markdown
### <source_ref / title> — <slug, if a rail-style slug is obvious; otherwise omit>
- link: [[1-SOURCES/Text/<file>.md#^<anchor>]]
- quote: "<verbatim quote text>" (or, if length/compression is unresolved: a note on what's available and that compression is needed, per Rule 6 — never invent a final quote here)
- buddhavacana: confirmed — <terse note: who's speaking, to whom>
- length_est: ~<N> chars EN (rough estimate; mark "(est.)" if reconstructed rather than measured, or "unresolved — flagged for compression at claim time" if it doesn't fit as-is)
- speaks_to: [<0 or more entries from discovery-by-feeling.md's fixed list>]
- theme: <0 or 1 label from theme-checklist.md, or omit the line entirely if none>
- status: unclaimed
```

A rejected or deferred near-miss, appended to `rejected.md`:

```markdown
### <source_ref / title> [— DEFERRED, if genuinely ambiguous rather than a clean reject]
- link: [[1-SOURCES/Text/<file>.md#^<anchor>]]
- reason: <one line — why it was disqualified, or why the call is ambiguous and needs a deeper read later>
```

A file that yields nothing at all gets one line at the bottom of the relevant canon's pool file (not `rejected.md`):

```markdown
### <file> — scanned, no candidates found
```

---

## Rules

1. **Don't tag everything — pass over the obviously irrelevant silently.** Narrative frames ("thus have I heard..."), homage lines, attendee lists, closing dedications, and passages structurally too long with no extractable unit get no entry at all. An entry (accepted, rejected, or deferred) is only for something that was seriously considered.
2. **Reject/defer entries are for near-misses only** — something that looked plausible (short, seemingly Buddha-attributed, on a good topic) but failed on closer inspection, or is genuinely ambiguous. One line of reason. No essay justifying the call.
3. **Never lower the gates to make tagging easier.** Same bar as `verse-rail`'s Rules 9–10 (buddhavacana — spoken *by* the Buddha, never a stanza of praise *about* him; a genuine complete verse or self-contained sentence, never a summary/stitch/gist) — these are checked here, once, not relaxed for convenience.
4. **Verify every verbatim quote against the source directly.** A tagged quote must be copy-exact from `1-SOURCES/`. Never reconstruct a quote from memory or from the paired translation's wording.
5. **`speaks_to` only from `discovery-by-feeling.md`'s fixed list.** `theme` only from `theme-checklist.md`, which may be extended (add a new entry under "Known gaps" when a passage is a clean instance of a real, recognized core teaching not yet listed — don't add vague one-off phrasings). A candidate needs *at least one* of `theme` or `speaks_to` to be pool-worthy; never require both.
6. **Do not do the compression/translation work here.** A rough length estimate is enough — if a passage clearly needs the same compress-without-cutting treatment already used on cards like `toh330-generosity` or `toh125-bodhicitta`, flag it as such and move on; don't draft the final rendering during tagging.
7. **Extracting one unit from a list or repeating refrain is allowed** (same pattern as `toh330-generosity`'s couplet-from-refrain), but confirm the source text itself — not just the paired English translation — actually separates that unit cleanly. English numbered lists sometimes impose structure the source language doesn't have (see `toh150` in `rejected.md` for a worked example of this exact trap); if the source doesn't cleanly separate, defer rather than force it.
8. **This skill never builds a rail, writes a day card, or sets a date/day number.** That's `verse-selection` and `verse-rail`. Claiming a pool entry (updating its `status:` to `claimed (day N, date)`) happens when a rail is actually built from it, not here.
9. **Never touch `1-SOURCES/`.** Read-only against that folder; all writes go to `candidate-pool/`.
10. **A paired translation file is a lead, not proof — verify it actually aligns to the anchor you're citing.** In the Chinese Āgamas especially, a Patton-translation block can be a fuller *parallel* telling rather than a direct translation of the terse Chinese at that exact anchor (found twice: `SĀ 379` and `SĀ 784`/`SĀ 785` — Patton's English there is far more elaborate than the compact or elliptical Chinese). If the translation's length or level of detail looks out of proportion to the source, re-read the Chinese directly before tagging or citing it for grounding; note the mismatch in the entry (accept, reject, or defer) rather than silently using the mismatched wording.
11. **Check a file's typical entry length before committing to a full-file scan.** Different sub-collections vary hugely in per-entry cost — e.g. within the Chinese Āgamas, Saṁyukta sūtras are mostly short and repetitive (cheap to scan), while Madhyama sūtras are individually long, parable-style discourses (one entry can run to what would otherwise be a whole small file). Sample one entry's length first; if entries are much longer than expected, treat the file as its own batch rather than folding it into a "quick" pass, and say so explicitly when reporting back rather than pushing through at inconsistent quality.
12. **Tone/wellbeing is its own gate, distinct from buddhavacana and length.** A passage can be genuinely Buddha-spoken, self-contained, and on a good theme, and still fail — e.g. `selection-criteria.md` §3's rule that graphic or harsh imagery (torture-simile content, viscerally violent similes) stays off the daily card regardless of doctrinal soundness (found at `MĀ 5`, the wood-pile/molten-iron-balls simile). When a passage trips this gate, reject it with that reason named explicitly ("tone/wellbeing gate, not buddhavacana or length") rather than folding it into a generic "didn't fit" note — a future rotation skill may want to distinguish these categories.
14. **Self-contained ≠ intelligible out of context — test both, or you'll pool a dud.** A quote can be one grammatically whole sentence and still be unusable, because the daily card ships **alone** with no room for backstory: if the line only means something to a reader who already knows the surrounding story, it fails. Apply `selection-criteria.md` §2's two-part test (a: grammatically whole; b: understandable out of context) at tag time. **Iconic lines are the trap** — three real examples that were wrongly accepted before this rule existed: *"this earth is my witness"* (Toh 95 — needs the Māra/earth-touching scene), and *"out of compassion I accept your repentance"* (DA 27 — needs the patricide/confession it answers). Both are whole sentences; both are meaningless standalone. Reject such a candidate with the reason *"self-contained but context-dependent — fails §2 out-of-context test."* Keep this separate from the **accessibility** gate (too technical/esoteric for a no-glossary lay reader — e.g. *"the world is painted by mind, yet mind does not see mind,"* Toh 231): that's also a reject, but for a different reason, and should be named as such. When in doubt, read the quote cold, as if you'd never seen the sūtra — if you can't tell what it's saying, defer or reject. **Relatedly, a bare proclamation of the Buddha's or an arahant's own attainment** ("my births are ended, what had to be done is done, there is no more becoming") is authentic buddhavacana but a poor daily card — it reports a finished state rather than teaching or meeting the reader. You may still pool it if it's a clean instance, but tag it `note: proclamation of attainment — weak daily fit` so a selection pass knows to prefer a path-pointing verse (`selection-criteria.md` §2).
15. **A secondary compilation (not a translation) can serve as a lead-generation shortcut for an expensive, un-paired file** — same "lead, not proof" spirit as Rule 10, one level further removed. If someone hands you a curated study digest (topically organized excerpts, possibly with commentary) covering a canon you haven't scanned yet, its numbering scheme almost certainly won't match this vault's source file (different editions renumber sutras differently — see the SĀ/佛光 triple-numbering precedent). Instead of trying to map numbers, grep each citation's distinctive verbatim phrase directly into the actual `1-SOURCES/` file to locate the real anchor, then run the normal gates (buddhavacana, self-containment, tone, length) against what you find there — never against the digest's own wording, and never against commentary. This turned a 14,502-line untouched Ekottarika Āgama file into a ~46-lead targeted pass instead of a blind full-file read (see `chinese.md`'s Ekottarika section for a worked example). Some leads won't grep-locate at all — that's a real outcome (e.g. a verse that turns out to live in a chapter this vault's source copy doesn't include), not a failure to search harder; log it as "not independently located" rather than tagging from the digest's memory.

---

## Procedure

1. Confirm the batch of source files to scan (explicit file list, a named range, or a selection rule like "shortest N files"). Check each against existing pool entries and `rejected.md` first — skip anything already tagged.
2. For each file: read it in full, along with its paired `1-SOURCES/Translations/` file if one exists.
3. Walk the file looking for buddhavacana-attributed passages (direct Buddha-speech, or a sutta framed as the Buddha's teaching) that could plausibly be short and self-contained. Pass over everything else silently (Rule 1).
4. For each passage seriously considered: check the buddhavacana gate (who's speaking, to whom), the in-scope gate (mdo/sūtra, not tantra/vinaya/abhidhamma), and whether a genuinely short, whole, self-contained unit exists (a full short verse, one sentence, or one cleanly-separable item from a list/refrain — verify per Rule 7).
5. Estimate rough English length. If it looks like it needs compression to fit (~125 chars), don't compress it now — flag it (Rule 6).
6. Decide: accept (write the record to the matching canon's pool file), reject (one-line entry in `rejected.md`), or defer (one-line entry in `rejected.md`, marked DEFERRED) per Rule 2.
7. Tag `speaks_to` (Rule 5) and/or `theme` (Rule 5), extending `theme-checklist.md` if a new, clearly-recognized core teaching turns up.
8. If a file yields nothing at all, add the one-line "scanned, no candidates found" marker to the matching pool file.
9. Report back a short summary: files scanned, candidates accepted, near-misses rejected/deferred, and any files that came up empty.

---

## Completion check

- [ ] Every accepted entry has: link, verbatim quote (or an honest "compression needed" note, never a placeholder), buddhavacana note, length estimate, at least one of speaks_to/theme, `status: unclaimed`.
- [ ] Every accepted quote passes BOTH self-containment tests (Rule 14): grammatically whole AND intelligible out of context; iconic-but-context-dependent lines rejected (not pooled), with the reason named vs. the separate accessibility gate.
- [ ] Every rejected/deferred entry has a one-line reason; DEFERRED used only for genuine ambiguity, not as a way to avoid a call.
- [ ] No entry exists for material that was obviously irrelevant at a glance (Rule 1 respected).
- [ ] No new `speaks_to` value invented outside `discovery-by-feeling.md`; any new `theme` value was added to `theme-checklist.md`, not just used inline.
- [ ] Files yielding nothing are marked "scanned, no candidates found," not silently skipped.
- [ ] `1-SOURCES/` untouched.

---

## Improve this skill (friction log)

**Always run this as the final step, after the task is done.** The goal is that the next agent to use this skill struggles less than you did.

1. **Recall the friction.** Walk back through the run and list every point where you were confused, guessed, backtracked, hit an error, re-read a file to figure something out, or wished this SKILL.md had told you something up front. That list is your friction log for this run.
2. **Diagnose each item.** For each friction point, decide: was it caused by *this skill* being unclear, incomplete, missing a worked example, or missing a gotcha or edge case? Or was it a one-off specific to this task? Only skill-level gaps get fixed here — ignore the one-offs.
3. **Fix the skill.** Edit *this* `SKILL.md` so the next agent avoids the same wall: add the missing instruction, a short worked example, a "gotcha" note, or a Completion-check item; tighten wording that misled you. Keep every existing hard rule and gate intact — **never weaken a gate or dedupe/verbatim/buddhavacana rule to reduce friction.** If a rule itself was the source of friction, add a clarifying note or example rather than removing it, and call it out for a human in your summary.
4. **Record the change.** In your final summary to the user, note in one line per change what friction you hit and what you changed (e.g. "kept mistyping the bo block id -> added a 'verify the exact ^block anchor first' gotcha"). If you hit no real friction, say so explicitly and change nothing.
