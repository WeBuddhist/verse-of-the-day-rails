---
name: verse-selection
description: Select the next verse(s) of the day for the WeBuddhist anthology. Reads the log (what's already run + the running balance) and the curation docs, then proposes the next verse — deduping against everything already used, rotating the canon toward balance, spacing themes, and honoring holiday occasions. The selection step that precedes verse-rail. It picks and proposes; it does not build the rail or invent un-sourced verses.
---

# verse-selection

Operationalises the calendar-level rules in `selection-criteria.md` §3 so
rotation and no-repeat are **systematic, not manual**. Given a date (or "the
next slot"), it proposes the verse to run, with the rationale, and the log row
to add. Then hand off to `verse-rail`.

Pipeline position: **`verse-selection` → `verse-rail` → `translation-qa` → log.**

---

## Inputs

- **Log** — `3-TRANSFORMATIONS/Plans/verse-of-the-day/log.md`: the rows already run (the dedupe list) and the **running-balance** section (canon mix, recent themes, last occasion).
- **Selection criteria** — `selection-criteria.md`: the hard gates (§1) and the quality + balance rules (§2–3).
- **Occasions** — `occasions.md`: holiday calendar + the verse themes each calls for.
- **Discovery-by-feeling** — `discovery-by-feeling.md`: the theme / felt-state set, for coverage.
- **Corpus** — `1-SOURCES/Text/` (+ paired translations) to pick from.
- **Already-used set** — the dedupe key: the log's `source_ref` column, **plus** `previously-used.md` (verses published *before/outside* this vault), **plus** existing rail files in `2-RAILS/Verses/` and cards in `days/`.
- The **date** to fill (defaults to the next empty slot).

## Procedure

1. **Occasion check first.** If the date is a Buddhist holiday (`occasions.md`, resolved per tradition), the occasion **overrides** normal rotation: select a verse tagged for that occasion. Skip to step 5.
2. **Read the running balance.** From the log: which canon is under-represented (target it) and **what theme ran on the immediately preceding day** (don't repeat it back-to-back — but themes from two or more days ago are open to reuse).
3. **Choose the target canon** = the most under-represented of Pali / Chinese Āgama / Tibetan Kangyur, to move the mix toward equal rotation.
4. **Pick a candidate** from that canon's sources that (a) passes the **hard gates** (§1), (b) passes **quality** (§2: a source **already short enough to translate in full** — a verse or a short prose line, *not* a summary of a long passage; prose is fine if it is short — plus self-contained, accessible, relatable), (c) has a **theme** that isn't the previous day's (no back-to-back repeats; otherwise themes may recur freely, and filling gaps in `speaks_to` coverage is a plus), and (d) is **fresh** — *not* one of the over-exposed "greatest hits" (§2 Freshness). Reach into the breadth of the corpus for under-circulated verses; the famous handful are presumed-used.
5. **Dedupe — mandatory.** Reject the candidate if its `source_ref` (or rail filename) appears in **`log.md`, `previously-used.md`, `2-RAILS/Verses/`, or `days/`** within the no-repeat window. Also avoid near-identical paired verses (e.g. Dhp 1 & 2) close together, and treat presumed-used greatest-hits as rejected unless confirmed fresh. If rejected, return to step 4.
6. **Propose** (output below). On acceptance, the workflow continues: `verse-rail` builds/confirms the rail → render + `translation-qa` → add the log row and update the running balance.

## Output — selection proposal

```markdown
## Verse-of-the-day selection — <date>
- **Proposed:** <source_ref> (<canon>) — "<short gloss / first line>"
- **Theme / speaks_to:** <theme> · <felt-states>
- **Why now:** canon = <target> (balance was <P·C·T>); theme avoids recent <…>; [occasion: <name>] if applicable.
- **Source:** [[1-SOURCES/Text/<file>.md#^<id>]]
- **Dedupe:** ✓ not in log / rails / days (checked <N> prior entries).
- **Rail:** exists at `2-RAILS/Verses/<slug>.md` · OR needs building (→ verse-rail).
- **Log row to add:** `| <date> | <day#> | <source_ref> | <canon> | <theme> | <speaks_to> | [[days/<card>]] | draft |`
```

## Rules

1. **Gates are hard.** Never propose an un-sourced, out-of-scope (tantra/Vinaya/scholastic), or unlicensed verse.
2. **Dedupe is mandatory** and checks the log **and** existing rails/days — not just the log.
3. **Move the canon mix toward balance**; don't pick the over-represented canon without a stated reason (e.g. an occasion demands it).
4. **Don't repeat a theme back-to-back** (on consecutive days); themes may recur after a gap. Prefer under-covered felt-states.
5. **Occasions override** normal rotation on holidays.
6. **Propose, don't auto-publish.** A curator confirms the pick; the skill updates the log only once the verse is finalized. It does **not** build the rail (that's `verse-rail`).

## Completion check

- [ ] Occasion checked for the date.
- [ ] Target canon chosen from the running balance (toward equal rotation).
- [ ] Candidate passes §1 gates + §2 quality + fills a non-recent theme.
- [ ] Dedupe run against log + `2-RAILS/Verses/` + `days/`.
- [ ] Proposal includes rationale, source link, and the ready-to-paste log row.
