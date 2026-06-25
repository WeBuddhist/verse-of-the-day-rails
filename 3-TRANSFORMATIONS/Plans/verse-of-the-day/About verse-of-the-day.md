# About — verse-of-the-day

The **verse-of-the-day** Plan. Deliberately **simple**: one verse per day,
rendered in the six app languages, with a little metadata. We dropped the
template's heavy per-language stream folders (`requirements.md` / `termbase.md` /
`schedule.md` × 6) — overkill for a daily verse. The whole plan is just:

```
verse-of-the-day/
├── About verse-of-the-day.md   ← this file
├── selection-criteria.md       ← which verses qualify
├── discovery-by-feeling.md     ← emotion / cultivation themes
├── occasions.md                ← holiday calendar
├── log.md                      ← the master calendar (date → verse), the index
└── days/
    └── day-NNN-<slug>.md        ← ONE file per day, all six languages + metadata
```

## The unit of work: one day = one file (or one row)

Each day is a single `days/day-NNN-<slug>.md` card holding **all six renderings
plus metadata** — see [`days/day-001-friendship-dhp328.md`](days/day-001-friendship-dhp328.md)
for the shape. `log.md` is the running index (date → `source_ref`, theme, status).

*(Alternative if you'd rather not have per-day files: the whole thing can live as
one table — columns `date · source_ref · theme · en · zh · bo · hi · ne · mn ·
status`. Per-day files win when you want the Pāli source, notes, and the rail
link alongside; the table wins for pure compactness. We're using per-day files +
the log index; say the word to switch to table-only.)*

## What each day card holds

1. **source_ref** — the citation shown with the verse (e.g. **Dhp 328**), per `vault-annex.md` §2. A verse with no resolvable citation does not ship.
2. **source_link / context_packages** — the `2-RAILS/Verses/<slug>.md` rail it was generated from (and through it, the `1-SOURCES/` block).
3. **source (original)** — the Pāli / Chinese / Tibetan, for display under the verse.
4. **six renderings** — en, zh, bo, hi, ne, mn (see language notes below).
5. **theme · speaks_to · occasions** — for calendar variety, the "where are you right now?" feature, and holiday overrides.
6. **review_status** — per-language sign-off state.

## Language notes (folded in from the old per-stream contracts)

- **Modern, plain language** throughout — no scholarly/classical register, no glossary needed (audience: Tier 3/4 practitioners; "feel like home").
- **en** — anchored on Bhikkhu Sujato (CC0); already modern.
- **zh** — **modern Traditional Chinese** for Taiwan / Hong Kong / Singapore (not Simplified/mainland register).
- **bo / hi / ne / mn** — WeBuddhist's own modern renderings from the rail's meaning; **bo and mn carry the highest risk** and need native dharma-reviewer sign-off.
- **No em dashes in the English.**
- Keep faithful to the original's intent (grammar/structure), not just the gist — see the rail's flagged rendering choices.

## Rules

- Each verse must trace to a `2-RAILS/Verses/<slug>.md` rail (`status: complete`). The rail grounds the meaning; the day card prescribes the modern wording.
- A day is `draft` when generated, `complete` only after the rail is signed off **and** a native-speaker dharma reviewer approves the renderings. Only `complete` days publish. The LLM never sets `complete`.
- Curate per [`selection-criteria.md`](selection-criteria.md); log every day in [`log.md`](log.md); keep canon rotation and theme spacing balanced.
