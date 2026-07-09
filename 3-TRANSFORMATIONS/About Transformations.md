# 3-TRANSFORMATIONS — Prescriptive outputs

This folder holds the vault's **AI-generated outputs**. Where `2-RAILS/` records what the source *means* (grounded, cited), this folder records what a *particular output* does with it.

> **This vault has one transformation: [`verse-of-the-day/`](verse-of-the-day/).** The generic Railroads template shipped three output *categories* — `Translations/`, `Adaptations/`, `Plans/` — each with per-track `requirements.md` / `termbase.md` / `audience.md` / language-stream contracts. **None of that applies here** and it has been removed. This anthology produces a single daily-verse stream, so its plan sits directly under `3-TRANSFORMATIONS/` (no `Plans/` wrapper). If you ever add a genuinely different output, give it its own subfolder then.

---

## The one track: `verse-of-the-day/`

One short buddhavacana verse per day, rendered in six languages (en · zh · bo · hi · ne · mn), grounded in a rail. Structure:

```
verse-of-the-day/
├── About verse-of-the-day.md   ← the track's own README + day-card template
├── selection-criteria.md       ← hard gates + quality + calendar-balance rules
├── termbase.md                 ← locked key-term renderings per language
├── discovery-by-feeling.md     ← emotion / cultivation themes (speaks_to)
├── occasions.md                ← holiday calendar (occasion overrides)
├── previously-used.md          ← verses published before/outside the vault (dedupe)
├── log.md                      ← the master calendar (date → verse) + running balance
└── days/
    ├── day-NNN-<slug>.md        ← ONE card per day: 6 renderings + metadata + QA
    └── _superseded/             ← replaced/blocked cards, kept for the record
```

**Pipeline (each step is a skill in `4-SYSTEM/Skills/`):**
`verse-selection` → `verse-rail` (in `2-RAILS/Verses/`) → build the day card → `translation-qa` → add the `log.md` row.

The **hard rules, source pools, grounding-by-canon, ecumenical wording, and day-card template** live in `verse-of-the-day/About verse-of-the-day.md`, `selection-criteria.md`, and the three pipeline skills — and are summarised in the root [`CLAUDE.md`](../CLAUDE.md). Read those before adding verses.

---

## Citation chain (into every day card)

A day card cites its rail; the rail cites `1-SOURCES/`. The card never reaches past the rail to `1-SOURCES/` for its *meaning* (though it quotes the verbatim source line for display).

```yaml
source_rail: 2-RAILS/Verses/<slug>.md
context_packages: [2-RAILS/Verses/<slug>.md]
```

- A card must trace to a rail; a rail must trace to a real `1-SOURCES/` block. No un-sourced "fake Buddha quotes."
- Renderings use the locked `termbase.md` terms; add a termbase row rather than coining per-verse.

---

## Status lifecycle

| Status | Meaning |
|---|---|
| `draft` | LLM-generated + `translation-qa` pass done; not yet human-reviewed |
| `complete` | rail signed off **and** a native dharma reviewer approved all six renderings |

Per-language `review_status` (`clean-for-review` / `needs-native-review` / `escalate-native-review` / `blocked`) tracks each rendering. **bo and mn always need native review.** Only a human sets `complete`; the LLM never does. Only `complete` cards publish.

---

## Where to look next

- [`verse-of-the-day/About verse-of-the-day.md`](verse-of-the-day/About%20verse-of-the-day.md) — the track README + day-card template.
- [`verse-of-the-day/selection-criteria.md`](verse-of-the-day/selection-criteria.md) — gates, freshness, source diversity, vehicle representation, theme rule.
- [`../CLAUDE.md`](../CLAUDE.md) — the canonical agent guide (pipeline + hard rules + source breadth).
- [`../2-RAILS/About Rails.md`](../2-RAILS/About%20Rails.md) — the descriptive context this folder consumes.
