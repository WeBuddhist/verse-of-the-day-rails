---
name: verse-selection
description: Use this skill whenever it's time to pick the next verse-of-the-day — even if the user just says "what's next," "fill in the next slot," or gives a date, without naming verse-selection. Reads the log (what's already run + the running balance), the curation docs, and the pre-tagged candidate-pool/ files (filtering to unclaimed entries before ever re-scanning raw source), then proposes the next verse: deduping against everything already used, rotating the canon toward balance, spacing themes, and honoring holiday occasions. Picks and proposes only — it does not build the rail (that's verse-rail) or invent un-sourced verses.
---

# verse-selection

Operationalises the calendar-level rules in `selection-criteria.md` §3 so
rotation and no-repeat are **systematic, not manual**. Given a date (or "the
next slot"), it proposes the verse to run, with the rationale, and the log row
to add. Then hand off to `verse-rail`.

Pipeline position: **`verse-selection` → `verse-rail` → `translation-qa` → log.**

---

## Inputs

- **Log** — [`3-TRANSFORMATIONS/verse-of-the-day/log.md`](../../../3-TRANSFORMATIONS/verse-of-the-day/log.md): the rows already run (the dedupe list) and the **running-balance** section (canon mix, recent themes, last occasion).
- **Selection criteria** — [`selection-criteria.md`](../../../3-TRANSFORMATIONS/verse-of-the-day/selection-criteria.md): the hard gates (§1) and the quality + balance rules (§2–3).
- **Occasions** — [`occasions.md`](../../../3-TRANSFORMATIONS/verse-of-the-day/occasions.md): holiday calendar + the verse themes each calls for.
- **Discovery-by-feeling** — [`discovery-by-feeling.md`](../../../3-TRANSFORMATIONS/verse-of-the-day/discovery-by-feeling.md): the theme / felt-state set, for coverage.
- **Candidate pool — check this FIRST** — [`candidate-pool/`](../../../3-TRANSFORMATIONS/verse-of-the-day/candidate-pool/): pre-tagged, pre-gate-checked candidates banked by the `candidate-tagging` skill, so a selection pass can filter this instead of re-scanning raw `1-SOURCES/` text. One file per canon, each entry already carrying a verbatim quote, buddhavacana note, length estimate, and `speaks_to`/`theme` tags:
  - [`candidate-pool/pali.md`](../../../3-TRANSFORMATIONS/verse-of-the-day/candidate-pool/pali.md) — Dhammapada, Sutta Nipāta, Udāna, Itivuttaka (verse collections).
  - [`candidate-pool/chinese.md`](../../../3-TRANSFORMATIONS/verse-of-the-day/candidate-pool/chinese.md) — all four Āgamas + the Chinese Mahāyāna sūtras.
  - [`candidate-pool/tibetan.md`](../../../3-TRANSFORMATIONS/verse-of-the-day/candidate-pool/tibetan.md) — Udānavarga (Toh 326) + Kangyur sūtras Toh 59, 95, 231.
  - Filter to `status: unclaimed` entries only (skip `claimed`; never pull from `rejected.md`, including its DEFERRED near-misses).
- **Theme gaps** — [`candidate-pool/theme-checklist.md`](../../../3-TRANSFORMATIONS/verse-of-the-day/candidate-pool/theme-checklist.md): its **"Known gaps"** section lists doctrinal themes not yet represented (many newly filled/flagged) — prefer a candidate that fills a flagged gap.
- **Scan coverage** — [`candidate-pool/SCAN-STATUS.md`](../../../3-TRANSFORMATIONS/verse-of-the-day/candidate-pool/SCAN-STATUS.md): what's had a real scan vs. not. The Pali prose Nikāyas (DN/MN/SN/AN) and most of the Tibetan Kangyur are **not yet scanned**, so the pool is shallow there — the raw-source fallback below is expected for those, not a sign the pool is broken.
- **Corpus (fallback when the pool has nothing suitable)** — `1-SOURCES/Text/` (+ paired translations) to pick from when the target canon's pool file has no fitting `unclaimed` entry. **Draw from the whole corpus, not just the verse collections** — see [`selection-criteria.md`](../../../3-TRANSFORMATIONS/verse-of-the-day/selection-criteria.md) §3 for the source-diversity and vehicle-representation rules, worked sutta examples, and the "don't over-rely on X" guidance. Source pools and where to find them in `1-SOURCES/Text/`:
  - *Verse collections:* Dhammapada, Sutta Nipāta, Udāna, Itivuttaka gāthās (Pali, CC0); Chinese Dharmapada 法句經 T210; Tibetan Udānavarga (Toh 326).
  - *Prose Nikāyas:* Dīgha, Majjhima, Saṁyutta, Aṅguttara (Pali, CC0, Sujato-paired) — short, self-contained quotable sentences within longer discourses.
  - *Tibetan Kangyur Mahāyāna sūtras:* `bo-toh<N>.md` + `en-toh<N>-84000.md` (229 texts; 84000 English is reference-only, never shipped).
  - *Chinese beyond T210:* the four Āgamas (DĀ/MĀ/SĀ/EĀ) + Chinese Mahāyāna sūtras (`zh-<slug>.md`, CBETA CC BY-NC-SA).
- **Already-used set** — the dedupe key: the log's `source_ref` column, **plus** [`previously-used.md`](../../../3-TRANSFORMATIONS/verse-of-the-day/previously-used.md) (verses published *before/outside* this vault), **plus** existing rail files in `2-RAILS/Verses/` and cards in `verse-of-the-day/`.
- The **date** to fill (defaults to the next empty slot).

## Procedure

1. **Occasion check first.** If the date is a Buddhist holiday (`occasions.md`, resolved per tradition), the occasion **overrides** normal rotation: select a verse tagged for that occasion. Skip to step 5.
2. **Read the running balance.** From the log: which canon is under-represented (target it) and **what theme ran on the immediately preceding day** (don't repeat it back-to-back — but themes from two or more days ago are open to reuse).
3. **Choose the target canon** = the most under-represented of Pali / Chinese Āgama / Tibetan Kangyur, to move the mix toward equal rotation.
4. **Pick a candidate — check the candidate pool first.** Open the target canon's pool file (`candidate-pool/pali.md` / `chinese.md` / `tibetan.md`) and filter to `status: unclaimed`; among those, prefer an entry whose `theme` fills a **Known gap** in `theme-checklist.md`. Pool entries were already gate-, buddhavacana-, and verbatim-checked by `candidate-tagging`, so you confirm they still satisfy (a)–(d) below but don't re-derive them from raw source. **Only fall back to a fresh scan of `1-SOURCES/Text/`** when the target canon's pool file has no suitable `unclaimed` entry — or when that canon is still under-scanned per `SCAN-STATUS.md` (Pali prose Nikāyas, most of the Kangyur) and you need something the pool doesn't yet hold. Whichever path, the candidate must: (a) pass the **hard gates** (§1); (b) pass **quality** (§2: a source **already short enough to translate in full** — a verse or a short prose line, *not* a summary of a long passage; prose is fine if it is short — plus self-contained, accessible, relatable); (c) have a **theme** that isn't the previous day's (no back-to-back repeats; otherwise themes may recur freely, and filling gaps in `speaks_to`/theme coverage is a plus); and (d) be **fresh** — *not* one of the over-exposed "greatest hits" (§2 Freshness). Reach into the breadth of the corpus for under-circulated verses; the famous handful are presumed-used.
   - **Gotcha — don't select an *open*-flagged entry on your own.** If a pool entry still carries an unresolved human-judgment flag, leave it for the curator rather than proposing it. Two prior flags are now **resolved** and their entries are usable: (1) the Toh 95 / Lalitavistara pre-enlightenment candidates in `tibetan.md` — Evan ruled these count as buddhavacana because the Lalitavistara is the Buddha's *final-lifetime* biography (the life he awoke in), not a past-life Jātaka; pre-awakening words from a *past* life would still fail the gate. (2) Toh 12/13/16/53/60 (`kangyur-scan-leads.md`) — Evan approved using these without a paired reference translation, but they are **not imported yet** and building a rail for them needs a `verse-rail` carve-out from the translation-grounded premise, so they still won't appear in the pool for now; don't be surprised if a wanted theme has no entry there.
5. **Dedupe — mandatory.** Reject the candidate if its `source_ref` (or rail filename) appears in **`log.md`, `previously-used.md`, `2-RAILS/Verses/`, or `verse-of-the-day/`** within the no-repeat window. Also avoid near-identical paired verses (e.g. Dhp 1 & 2) close together, and treat presumed-used greatest-hits as rejected unless confirmed fresh. If rejected, return to step 4.
6. **Propose** (output below). On acceptance, the workflow continues: `verse-rail` builds/confirms the rail → render + `translation-qa` → add the log row and update the running balance.

## Multi-day requests ("make the next N days")

Run the full pipeline **once per day, sequentially** — never batch-select N verses
against a single read of the running balance. After each day's `log.md` row and
running-balance update are committed, re-run step 2 (read the running balance
again) before selecting the next day: the canon target and "previous day's
theme" must reflect the day you just added, not the state before the batch
started. Concretely, for each of the N days in order: steps 1–6 above → hand
off to `verse-rail` → build the day card → `translation-qa` → add the `log.md`
row and update the running balance → only then start the next day. Skipping
the re-read between days is the most common way a multi-day batch ends up with
a canon or theme that doesn't actually rotate within the batch.

## Output — selection proposal

```markdown
## Verse-of-the-day selection — <date>
- **Proposed:** <source_ref> (<canon>) — "<short gloss / first line>"
- **Theme / speaks_to:** <theme> · <felt-states>
- **Why now:** canon = <target> (balance was <P·C·T>); theme avoids recent <…>; [occasion: <name>] if applicable.
- **Source:** [[1-SOURCES/Text/<file>.md#^<id>]]
- **Dedupe:** ✓ not in log / rails / days (checked <N> prior entries).
- **Rail:** exists at `2-RAILS/Verses/<slug>.md` · OR needs building (→ verse-rail).
- **Log row to add:** `| <date> | <day#> | <source_ref> | <canon> | <theme> | <speaks_to> | [[<card>]] | draft |`
```

## Rules

1. **Gates are hard.** Never propose an un-sourced, out-of-scope (tantra/Vinaya/scholastic), or unlicensed verse.
2. **Dedupe is mandatory** and checks the log **and** existing rails/days — not just the log.
3. **Move the canon mix toward balance**; don't pick the over-represented canon without a stated reason (e.g. an occasion demands it).
4. **Don't repeat a theme back-to-back** (on consecutive days); themes may recur after a gap. Prefer under-covered felt-states.
5. **Occasions override** normal rotation on holidays.
6. **Propose, don't auto-publish.** A curator confirms the pick; the skill updates the log only once the verse is finalized. It does **not** build the rail (that's `verse-rail`).
7. **Pool first, raw source second.** Filter the target canon's `candidate-pool/*.md` (`status: unclaimed`) before scanning raw `1-SOURCES/` text; fall back to a raw scan only when the pool has nothing suitable. This reuses `candidate-tagging`'s gate/verbatim work — it does not replace the §1 gates or dedupe, which still apply to every pick, pool or raw.

## Completion check

- [ ] Occasion checked for the date.
- [ ] Target canon chosen from the running balance (toward equal rotation).
- [ ] Target canon's `candidate-pool/*.md` file checked (filtered to `status: unclaimed`) **before** any raw-source scan; theme-checklist "Known gaps" consulted; raw `1-SOURCES/` scan used only as a fallback when the pool had nothing suitable.
- [ ] Candidate passes §1 gates + §2 quality + fills a non-recent theme.
- [ ] Dedupe run against log + `2-RAILS/Verses/` + `verse-of-the-day/`.
- [ ] Proposal includes rationale, source link, and the ready-to-paste log row.
- [ ] For multi-day requests: each day's log row was committed before the next day's running balance was read (no batch-selecting against a stale snapshot).

---

## Improve this skill (friction log)

**Always run this as the final step, after the task is done.** The goal is that the next agent to use this skill struggles less than you did.

1. **Recall the friction.** Walk back through the run and list every point where you were confused, guessed, backtracked, hit an error, re-read a file to figure something out, or wished this SKILL.md had told you something up front. That list is your friction log for this run.
2. **Diagnose each item.** For each friction point, decide: was it caused by *this skill* being unclear, incomplete, missing a worked example, or missing a gotcha or edge case? Or was it a one-off specific to this task? Only skill-level gaps get fixed here — ignore the one-offs.
3. **Fix the skill.** Edit *this* `SKILL.md` so the next agent avoids the same wall: add the missing instruction, a short worked example, a "gotcha" note, or a Completion-check item; tighten wording that misled you. Keep every existing hard rule and gate intact — **never weaken a gate or dedupe/verbatim/buddhavacana rule to reduce friction.** If a rule itself was the source of friction, add a clarifying note or example rather than removing it, and call it out for a human in your summary.
4. **Record the change.** In your final summary to the user, note in one line per change what friction you hit and what you changed (e.g. "kept mistyping the bo block id -> added a 'verify the exact ^block anchor first' gotcha"). If you hit no real friction, say so explicitly and change nothing.
