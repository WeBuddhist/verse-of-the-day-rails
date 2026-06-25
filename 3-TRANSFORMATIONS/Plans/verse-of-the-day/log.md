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
| 2026-07-01 | 8 | Dhp 50 | Pali | self-reflection | resentful, overwhelmed, equanimity | [[days/day-008-self-reflection-dhp50]] | draft |
| 2026-07-02 | 9 | SĀ 803 | Chinese Āgama | mindfulness-of-breathing | anxious, restless, overwhelmed | [[days/day-009-breath-sa803]] | draft |
| 2026-07-03 | 10 | Iti 27 | Pali | loving-kindness | lonely, grieving, loving-kindness | [[days/day-010-loving-kindness-iti27]] | draft |
| 2026-07-04 | 11 | SĀ 33 | Chinese Āgama | not-self | grasping, afraid, equanimity | [[days/day-011-not-self-sa33]] | draft |
| 2026-07-05 | 12 | Dhp 100 | Pali | speech | overwhelmed, restless, hopeful | [[days/day-012-speech-dhp100]] | draft |

## Running balance (update as the log grows)

- **Canon mix so far (12 days):** Pali 7 · Chinese Āgama 5 · Tibetan Kangyur 0 → **Tibetan is still the standing gap** (Udānavarga needs a translation reference — Rockhill PD or 84000 when published — before it can be railed well). Days 8–12 leaned Chinese where possible; the next openings should go Tibetan as soon as a translation reference is resolved, then keep Chinese roughly level with Pali.
- **Recent themes (avoid clustering):** self-reflection, mindfulness-of-breathing, loving-kindness, not-self, speech (Days 8–12) on top of friendship, impermanence, non-hatred, four-noble-truths, mind, right-view, overcoming-anger (Days 1–7). Day 13 should avoid all of these; still-open themes: compassion, gratitude, generosity, contentment, patience-as-its-own-card, joy/muditā.
- **Freshness (Days 8–12):** all five are fresh, lesser-known picks — none from the presumed-used greatest-hits in [`previously-used.md`](previously-used.md). Days 1–7 still contain greatest-hits (Dhp 1/5/223/328) flagged for re-pick once the real used-list is imported.
- **Last occasion verse:** SĀ 379 (Day 4) is tagged Dhamma Day / Āsāḷha Pūjā — reuse on that occasion rather than in normal rotation if the dates align.

## Convention

1. Build the verse's rail (`2-RAILS/Verses/<slug>.md`) and its day card (`days/day-NNN-...md`) first.
2. Add a row here with the date it runs as verse of the day.
3. Set the day card's `date:` and this row's date to match.
4. Don't reuse a verse within the no-repeat window; keep the canon mix moving toward balance; don't run the same theme on consecutive days.
5. Flip Status to `complete` only after rail sign-off + native review of all renderings.
