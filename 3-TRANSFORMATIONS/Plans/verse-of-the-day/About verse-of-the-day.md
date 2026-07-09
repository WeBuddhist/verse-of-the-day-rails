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
├── termbase.md                 ← locked key-term renderings per language
├── previously-used.md          ← verses published before/outside this vault (dedupe)
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

## Day-card format (copy this template)

This is the exact shape every `days/day-NNN-<slug>.md` uses. Match it.

```markdown
---
day: <N>
date: <YYYY-MM-DD>
source_ref: "<citation, e.g. Dhp 328 · or 法句經 T210 (述千品) · Dhp 103 parallel>"
canon: <Pali | Chinese | Chinese (Mahāyāna) | Tibetan Kangyur | Tibetan Kangyur (Mahāyāna)>
theme: <emergent-tag>
speaks_to: [<felt-states>]
occasions: []
source_rail: 2-RAILS/Verses/<slug>.md
context_packages: [2-RAILS/Verses/<slug>.md]
status: draft
review_status:
  en: clean-for-review        # en/zh/hi default clean-for-review when faithful
  zh: clean-for-review
  hi: clean-for-review
  ne: needs-native-review     # ne always needs native review
  bo: escalate-native-review  # bo + mn always escalate (highest risk)
  mn: escalate-native-review
---

# Day <N> — <Theme> (<Source>)

Rail: [[2-RAILS/Verses/<slug>]] · <one-line grounding: e.g. "grounded in Sujato (CC0)" / "own translation from CBETA Chinese source (CC BY-NC-SA); Mahāyāna" / "own translation from the Degé Kangyur (Public Domain); 84000 English as reference only">.
Short <verse|sentence>, **quoted in full**. Meaning: <one plain line>.

## Source (<language>)

<For Pali: transclude — ![[1-SOURCES/Text/pi-....md#^id]] (or the en-sujato block).
 For Chinese/Tibetan: quote the VERBATIM source line + its anchor:>
> <verbatim source> (`<file>#^<id>`)

## Renderings (one short line each)

- **en** — <one short line>
- **zh** — <verbatim source if the source IS Chinese; else our modern Traditional rendering>
- **bo** — ⚑ <verbatim source if the source IS Tibetan; else our rendering>
- **hi** — <our rendering>
- **ne** — <our rendering>
- **mn** — ⚑ <our rendering>

## QA — pre-review (against 2-RAILS/Verses/<slug>.md)

### en
- Back-translation: "<literal back-translation>"
- Findings: <faithfulness vs source/parallel; term checks; "No em dash ✓">
- Net: clean for review.

### zh (Traditional)
- <if verbatim source: "the verbatim CBETA source; the quote itself."; else back-translation + findings>
- Net: clean for review.

### hi
- Back-translation / findings. Net: clean for review.

### ne
- Back-translation / confidence flags. Net: needs native review.

### bo ⚑
- Back-translation (approx) / confidence flags. Net: escalate to native Tibetan dharma reviewer.

### mn ⚑
- Back-translation (approx) / confidence flags. Net: escalate to native Mongolian dharma reviewer.
```

Notes on the fields: **source_ref** is the citation shown with the verse (a card with no resolvable citation does not ship); for grounding-by-parallel picks, append `· Dhp N parallel`. **source_rail / context_packages** point to the rail (and through it to `1-SOURCES/`). The **⚑** on bo/mn flags them for native ratification. `review_status` values used: `clean-for-review`, `needs-native-review`, `escalate-native-review`, `blocked`.

## Language notes (folded in from the old per-stream contracts)

- **Modern, plain language** throughout — no scholarly/classical register, no glossary needed (audience: Tier 3/4 practitioners; "feel like home").
- **en** — anchored on Bhikkhu Sujato (CC0); already modern.
- **zh** — **modern Traditional Chinese** for Taiwan / Hong Kong / Singapore (not Simplified/mainland register).
- **bo / hi / ne / mn** — WeBuddhist's own modern renderings from the rail's meaning; **bo and mn carry the highest risk** and need native dharma-reviewer sign-off.
- **No em dashes in the English.**
- **Ecumenical wording — WeBuddhist is for all Buddhists.** Keep Mahāyāna *content* but render it in inclusive language: **bodhicitta → "the awakening mind," never "Great Vehicle mind"** (大乘 / *theg chen* reads sectarian). *Bodhisattva* is fine (pan-Buddhist); frame such lines as universal instructions. Use the standard, established dharma-term rendering in each language (see `termbase.md`) rather than paraphrase — e.g. *mettā* = "loving-kindness / मैत्री," not "love"; render the five aggregates with their standard names (form, feeling, perception, volition, consciousness).
- **Real quote, kept whole — no distillation.** Each rendering is a *full* real quote: a complete verse, or a single self-contained sentence, translated in full. **Never** summarise a passage, stitch partial lines, or reduce a teaching to its "gist" to save space. Keep renderings short by *choosing a short source*, not by cutting — if a source only fits by distilling, don't use it (pick a genuinely short verse instead). Target ≈ ≤ 20 words / ≤ 120 chars in English where the quote allows, but faithfulness wins over the target. See the hard rule in [`selection-criteria.md`](selection-criteria.md) §2.
- Keep faithful to the original's intent (grammar/structure), not just the gist — see the rail's flagged rendering choices.

## Rules

- Each verse must trace to a `2-RAILS/Verses/<slug>.md` rail (`status: complete`). The rail grounds the meaning; the day card prescribes the modern wording.
- A day is `draft` when generated, `complete` only after the rail is signed off **and** a native-speaker dharma reviewer approves the renderings. Only `complete` days publish. The LLM never sets `complete`.
- Curate per [`selection-criteria.md`](selection-criteria.md); log every day in [`log.md`](log.md); keep canon rotation and theme spacing balanced.
