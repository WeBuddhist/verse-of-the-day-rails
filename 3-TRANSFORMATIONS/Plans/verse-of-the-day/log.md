# Verse of the Day — Log

The running record of every verse of the day: which verse ran on which date,
its theme and canon, and a link to its day card. This is the source of truth for
the calendar-level rules in [`selection-criteria.md`](selection-criteria.md) §3 —
**no near-term repeats**, **roughly equal canon rotation**, **theme spacing**,
and **occasion overrides**. Add a row each day; check the recent rows before
selecting the next verse.

Status legend: `draft` = generated, not yet reviewed · `complete` = rail signed
off + all six renderings reviewed, ready/published.

| Date | Day | source_ref | Canon | Theme | speaks_to | Day card | Status |
|------|-----|-----------|-------|-------|-----------|----------|--------|
| 2026-06-24 | 1 | Dhp 328 | Pali | friendship | lonely, loving-kindness, hopeful | [[days/day-001-friendship-dhp328]] | draft |
| 2026-06-25 | 2 | SĀ 1 | Chinese Āgama | impermanence | grieving, craving, equanimity | [[days/day-002-impermanence-sa1]] | draft |
| 2026-06-26 | 3 | Dhp 5 | Pali | non-hatred | angry, resentful, loving-kindness | [[days/day-003-nonhatred-dhp5]] | draft |
| 2026-06-27 | 4 | SĀ 379 | Chinese Āgama | four-noble-truths | doubtful, aspiration, hopeful | [[days/day-004-fournobletruths-sa379]] | draft |
| 2026-06-28 | 5 | Dhp 1 | Pali | mind | overwhelmed, restless, hopeful | [[days/day-005-mind-dhp1]] | draft |
| 2026-06-29 | 6 | SĀ 770 | Chinese Āgama | right-view | doubtful, hopeful, aspiration | [[days/day-006-rightview-sa770]] | draft |
| 2026-06-30 | 7 | Dhp 223 | Pali | overcoming-anger | angry, irritated, patience | [[days/day-007-anger-dhp223]] | draft |

## Running balance (update as the log grows)

- **Canon mix so far (7 days):** Pali 4 · Chinese Āgama 3 · Tibetan Kangyur 0 → **Tibetan is the standing gap** (the Udānavarga still needs a translation reference — Rockhill PD or 84000 when published — before it can be railed well). Prioritise a Tibetan verse once that's resolved.
- **Recent themes (avoid clustering):** friendship, impermanence, non-hatred, four-noble-truths, mind, right-view, overcoming-anger. Day 8 should avoid these; under-used Door-B themes (compassion, gratitude, generosity, equanimity) are open.
- **Last occasion verse:** SĀ 379 (Day 4) is tagged Dhamma Day / Āsāḷha Pūjā — reuse on that occasion rather than in normal rotation if the dates align.

## Convention

1. Build the verse's rail (`2-RAILS/Verses/<slug>.md`) and its day card (`days/day-NNN-...md`) first.
2. Add a row here with the date it runs as verse of the day.
3. Set the day card's `date:` and this row's date to match.
4. Don't reuse a verse within the no-repeat window; keep the canon mix moving toward balance; don't run the same theme on consecutive days.
5. Flip Status to `complete` only after rail sign-off + native review of all renderings.
