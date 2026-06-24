# About — verse-of-the-day

Cross-language brief for the **verse-of-the-day** Plan. Written in English regardless of which languages the plan publishes (per `3-TRANSFORMATIONS/About Transformations.md` §3).

## Purpose

Deliver one short verse (2–4 lines) per day, drawn from authentic buddhavacana in `1-SOURCES/` (Pali Canon, Chinese Āgamas, Tibetan Kangyur), rendered in **modern, plain language** for the WeBuddhist app. Each day's verse is grounded against its source rail and carries a citation; nothing publishes un-sourced.

## Audience

Regular (Tier 3) and casual (Tier 4) WeBuddhist practitioners. They are not scholars — a verse must be **immediately understandable** with no glossary. See the per-stream `requirements.md` for language-specific register.

## Per-session shape (shared by all language streams)

Each `days/day-N.md` contains:

1. **source_ref** — the citation label shown with the verse, using the standard abbreviations in `vault-annex.md` §2 (e.g. **Dhp 16**, **SN 56.11**, **SĀ 262**). Displayed to the practitioner.
2. **source_link** — the exact block link the label resolves to, e.g. `[[1-SOURCES/Text/pi-dhammapada.md#^16]]`. Guarantees the displayed "Dhp 16" is grounded in the real source.
3. **verse** — the modern-language verse for this stream's language (2–4 lines).
4. **source_original** — the original-language text (Pāli / Chinese / Tibetan), for display under the verse.
5. **theme** — one-word tag (Mind, Anger, Contentment…) for calendar variety.
6. **context_packages** — the `2-RAILS/` file(s) the rendering was generated from.
7. **review_status** — per-stream sign-off state.

Every published verse of the day **must** show its `source_ref` label — a verse with no resolvable citation does not ship (it would be indistinguishable from a "fake Buddha quote").

## Languages (one stream each)

`en/`, `bo/`, `zh/`, `hi/`, `ne/`, `mn/`. Streams progress independently. English leads (CC0 sources are already modern English); bo / ne / mn carry the highest rendering risk and require native dharma-reviewer sign-off before publish.

## Source-rail dependencies

Each verse must trace to a `2-RAILS/Verses/<id>.md` package whose `status: complete`. The rail grounds the meaning; the stream prescribes the modern wording. Modernizing classical source text (Literary Chinese, classical Tibetan) is permitted only with reviewer sign-off, per `vault-annex.md` §4.

## Status rules

A day is `draft` when generated, `complete` only when a native-speaker dharma reviewer signs off. Only `complete` days are published. The LLM never sets `complete`.
