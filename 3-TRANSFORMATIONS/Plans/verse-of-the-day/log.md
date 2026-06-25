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

## Running balance (update as the log grows)

- **Canon mix so far:** Pali 1 · Chinese Āgama 1 · Tibetan Kangyur 0 → **Tibetan next** for balance (needs a verse with a translation reference — Udānavarga still lacks one).
- **Recent themes (avoid clustering):** friendship, impermanence. Day 3 should avoid both; lean uplifting after a sober verse.
- **Last occasion verse:** — (none yet; Māgha Pūjā / Sangha Day is the next natural occasion to plan for).

## Convention

1. Build the verse's rail (`2-RAILS/Verses/<slug>.md`) and its day card (`days/day-NNN-...md`) first.
2. Add a row here with the date it runs as verse of the day.
3. Set the day card's `date:` and this row's date to match.
4. Don't reuse a verse within the no-repeat window; keep the canon mix moving toward balance; don't run the same theme on consecutive days.
5. Flip Status to `complete` only after rail sign-off + native review of all renderings.
