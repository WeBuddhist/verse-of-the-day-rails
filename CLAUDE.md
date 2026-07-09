# CLAUDE.md — verse-of-the-day-rails (WeBuddhist Verse of the Day)

**New session: start here, then open [`4-SYSTEM/CLAUDE.md`](4-SYSTEM/CLAUDE.md) — the full operational guide.** This root file exists so the guidance is auto-loaded; `4-SYSTEM/CLAUDE.md` (and the folder READMEs it points to) is the canonical, detailed version. If the two ever disagree, the detailed files win.

**What this vault is.** A "Railroads" anthology that produces WeBuddhist's **Verse of the Day**: one short, authentic **buddhavacana** verse per day, grounded in a cited source and rendered in six languages (**en · zh · bo · hi · ne · mn**), drawn from the **Pali Canon, Chinese canon, and Tibetan Kangyur** (discourse/verse only — no tantra, Vinaya, or scholastic). Authority is the human source + authoritative translations, never the model's parametric knowledge.

**Before doing anything:** open [`4-SYSTEM/Skills/SKILLS-CATALOG.md`](4-SYSTEM/Skills/SKILLS-CATALOG.md) and use the matching skill — don't improvise. The verse-of-the-day pipeline is **`verse-selection` → `verse-rail` → build the day card → `translation-qa` → add the `log.md` row.**

**To add daily verses,** read the quickstart in `4-SYSTEM/CLAUDE.md` §1b and the track docs in [`3-TRANSFORMATIONS/verse-of-the-day/`](3-TRANSFORMATIONS/verse-of-the-day/) — `About verse-of-the-day.md` (day-card template), `selection-criteria.md` (gates + balance), `termbase.md` (locked terms), `log.md` (what's used + running balance), `previously-used.md` (dedupe). Hard rules in brief:

1. **Buddhavacana spoken *by* the Buddha, not *about* him** (no praise-of-the-Buddha, no words of disciples/gods/kings).
2. **Real quote kept whole** — a complete verse or ONE self-contained sentence, quoted in full (never summarise/stitch/gist); **verified verbatim from `1-SOURCES/`, never from memory**; must **fit the ~125-char card** in all six languages.
3. **Ecumenical wording** — *bodhicitta* = "the awakening mind," never "Great Vehicle"; use standard `termbase.md` terms, not paraphrase (*mettā* = loving-kindness, not "love").
4. **No em dashes in English**; **zh = modern Traditional**; on Chinese/Tibetan-source cards the **zh/bo IS the verbatim source**; **84000 English is reference-only**.
5. **Dedupe material** (log + previously-used + rails + days); **themes may repeat but never two days running**; keep the three canons balanced; **draw from the full breadth** (Pali verse *and* prose Nikāyas, Chinese Dharmapada + Āgamas + Mahāyāna sūtras, Tibetan Udānavarga + Kangyur Mahāyāna sūtras) — not just the Dhammapada; Mahāyāna should appear regularly.
6. All cards stay **`status: draft`**; only a native dharma reviewer (esp. bo + mn) sets `complete`.

**Key locations:** sources `1-SOURCES/` · rails `2-RAILS/Verses/` · daily output `3-TRANSFORMATIONS/verse-of-the-day/` · skills, guidelines & converters `4-SYSTEM/`.
