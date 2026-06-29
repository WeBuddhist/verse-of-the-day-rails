# Verse-of-the-Day — Selection Criteria

How a verse is chosen for the verse-of-the-day calendar. Two layers: **hard gates** (a verse either qualifies or it doesn't) and **quality judgment** (among qualifying verses, which make good daily cards), plus **calendar-level balance** rules that apply across the whole stream.

This governs curation for the `verse-of-the-day` Plan. A selected verse must have a `complete` rail (`2-RAILS/Verses/<slug>.md`) before it can be scheduled.

> **Brand grounding** (per `knowledge-base 10_ORG/11_Strategy/🌟North_Star.md`). WeBuddhist's mission — *do a little less harm, a little more good, know your own mind* — is itself **Dhp 183**; that verse is the corpus anchor. The platform rule is that **every daily session includes a verified canonical quote** (this work is the "Reliability" half; relatability is the other half). Audience = **already-Buddhist practitioners** across traditions, served in modern language ("Sacred, Not Precious" — it should *feel like home*, not like a wellness app). Metric: **Daily Active Buddhists (DABs)**.

---

## 1. Hard gates (all required)

A candidate is ineligible unless it meets **every** gate:

1. **Authentic buddhavacana.** The words of the Buddha. *Not* verses attributed to disciples (e.g. Theragāthā/Therīgāthā), not commentary, not later composition.
2. **In scope.** Within the canon boundaries set in `vault-annex.md`: Pali Sutta Piṭaka (4 Nikāyas + the KN verse texts), Chinese Āgamas, Kangyur **mdo/sūtra** section. **Excluded:** Vinaya, Abhidhamma/scholastic, and **tantra** (WeBuddhist is for all Buddhists).
3. **Traceable.** Resolves to a real source block in `1-SOURCES/` and carries a citation label (`source_ref`, e.g. *Dhp 5*, *SĀ 1*). No un-sourced or paraphrased "fake Buddha quotes."
4. **License-cleared** for our use (see `vault-annex.md` §7).
5. **Backed by a `complete` rail.** Meaning is grounded and reviewer-approved before scheduling.

---

## 2. Quality criteria (judgment among eligible verses)

- **Form — short & self-contained.** A 2–4 line verse that lands **without** needing its backstory or surrounding context. Long, list-heavy, or syntactically dependent passages are poor daily cards.
- **Find a source that is already short — translate it in full.** The default move is to pick a source short enough to render *complete and faithful*: a 2–4 line verse (gāthā) **or a short prose statement that stands on its own**. **Prose is fine as long as it is short.** What to avoid is taking a *long* discourse and summarising it down to fit — that introduces editorial choice and drifts toward paraphrase rather than translation, which weakens the "authentic, faithfully rendered buddhavacana" promise. So hunt for self-contained short passages (verse-rich sources like the Dhammapada, Udāna, Sutta Nipāta, and the Itivuttaka gāthās are good ground, but a short prose line from any sutta works too). Only as a last resort distil a longer text, and if you do, label the card honestly as a distilled summary, not a verbatim quote.
- **Length cap (app card space).** Each rendering must fit the app's limited card space: aim for **one short sentence** — roughly **≤ 20 words / ≤ 120 characters in English**, and comparably brief in every language (CJK / Indic / Tibetan / Cyrillic scripts pack differently, so judge by line length on the card, not character count alone). Avoid multi-clause chains and multi-sentence renderings; distil prose suttas (and even three-part progressions) to the single essential line. When a teaching is a list or a progression, render the gist, not every item. *(If the design team gives a hard per-field character limit, record it here and treat it as the cap.)*
- **Accessibility (Tier 3 / Tier 4).** A regular or casual lay learner grasps it in modern language with **no glossary**. Avoid dense technical enumerations (e.g. lists of dhammas), obscure proper names, or verses whose point depends on a technical term.
- **Universality — non-sectarian.** Resonates across traditions and across the four tiers. Avoid tradition-specific or sectarian-divisive content. The verse should feel like *everyone's* Dharma.
- **Tone & wellbeing.** Aligned with Buddhist values; non-manipulative; genuinely nourishing as a once-a-day touchpoint. See the tone rule in §3.
- **Translatability.** Survives rendering into all six languages (en, bo, zh, hi, ne, mn) without depending on Pali/Chinese wordplay, meter, or a pun that won't carry.
- **Relatability to lived experience.** Prefer verses that speak to a real human moment — anger, worry, grief, craving, gratitude, loneliness — over abstract or purely doctrinal stanzas. Each rail is tagged `speaks_to:` with the everyday felt-states it meets (see [`discovery-by-feeling.md`](discovery-by-feeling.md)), powering both the daily card and a "where are you right now?" discovery feature. Over the corpus, ensure every common felt-state has verses that *meet the person where they are* and *point the way through*.
- **Freshness — avoid the over-exposed.** The canon's "greatest hits" (Dhp 1, 5, 183, 223, 328, the first sermon, the Heart/Diamond Sūtra gāthās, the Metta Sutta opening) are the ones WeBuddhist has most likely *already published* and that circulate everywhere. **Prefer fresh, lesser-known verses** from the breadth of the corpus (423 Dhammapada verses + thousands of suttas) that are still accessible and relatable. Treat the famous handful as *presumed-used* unless confirmed otherwise, and always check [`previously-used.md`](previously-used.md) (historical) alongside [`log.md`](log.md). Selection's job is to surface the *under-circulated* gems, not re-serve the obvious ones.

---

## 3. Calendar-level balance (across the whole stream)

These apply to the *sequence* of verses, not a single pick:

- **Canon rotation — roughly equal.** Aim over time for balanced representation of the **Pali Canon, Chinese Āgamas, and Tibetan Kangyur**. This is a deliberate "for all Buddhists" signal. (Early on the mix will skew Pali while Chinese/Tibetan rails are built; correct toward balance as they mature — don't let it stay Pali-only.)
- **Tone — lean uplifting, sober sparingly.** The default daily tone is **encouraging or contemplative**. Sobering teachings (impermanence, mortality, the cost of unwholesome action) are part of the Dharma and **are** included — but used deliberately and occasionally, framed gently, and the harshest/graphic verses (e.g. vivid hell-realm imagery) are kept off the daily card. Rough target: a clear majority of cards uplifting/steadying, the sobering ones spaced out.
- **Theme variety — emergent tags.** Themes are tagged freely on each rail (`theme:` in frontmatter) rather than chosen from a fixed list. The curation rule is simply: **avoid clustering** — don't run the same theme (or near-duplicate verse) on consecutive days or within a short window. Let the tag set grow naturally; review it periodically for gaps.
- **No near-term repeats.** A verse isn't reused within a long window (set per the schedule); near-identical paired verses (e.g. Dhp 1 & 2) aren't run back-to-back.
- **Occasion override.** On a Buddhist holiday, the daily verse is chosen for the occasion (overriding rotation), per [`occasions.md`](occasions.md) — multi-tradition (Vesak/Saga Dawa, Māgha Pūjā, Bodhi Day, Dhamma Day, Nirvana Day, etc.).

---

## 4. Selection workflow

1. **Pick a candidate** that meets the §1 gates.
2. **Judge it against §2** — short, accessible, universal, right tone, translatable. If it needs its backstory to make sense, reject (or note it for a different feature).
3. **Tag the theme** (emergent) and check §3 balance against recent cards: canon mix, tone spacing, theme clustering.
4. **Ensure the rail exists and is `complete`** (`2-RAILS/Verses/<slug>.md`, built via the `verse-rail` skill). If not, build it first.
5. **Schedule** it in the stream's `schedule.md` with its `source_ref` and theme.
6. **Reviewer sign-off** before publish (per the Plan's review gate).

---

## 5. Quick checklist (per candidate)

- [ ] Buddhavacana, in-scope, license-cleared.
- [ ] Resolves to a `source_ref` + has a `complete` rail.
- [ ] Short and self-contained — no backstory required.
- [ ] Understandable by a lay reader in modern language, no glossary.
- [ ] Non-sectarian; resonates across traditions/tiers.
- [ ] Tone fits (uplifting/contemplative by default; sober only if deliberately spaced).
- [ ] Translates cleanly into all six languages.
- [ ] Canon mix, theme spacing, and no-repeat rules checked against recent cards.

---

## 6. Worked examples (from current rails)

- **Dhp 1 (mind)** — ✅ short, iconic, universal, uplifting-contemplative. Note: pairs with Dhp 2; don't run consecutively.
- **Dhp 183 (the path)** — ✅ self-contained ethical summary; broadly resonant; gentle.
- **Dhp 223 (overcoming anger)** — ✅ practical, four-fold, encouraging.
- **SĀ 1 (impermanence)** — ⚠️ prose, not a verse: pick the single impermanence→liberation line for the card; sober theme, so space it out (§3).
