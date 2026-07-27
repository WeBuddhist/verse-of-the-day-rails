---
day: 83
date: 2026-09-14
source_ref: "法句經 T210 (安寧品) · Dhp 201 parallel"
canon: Chinese
theme: peace-beyond-winning
speaks_to: [resentful, irritated, equanimity]
occasions: []
source_rail: 2-RAILS/Verses/t210-peace-beyond-winning.md
context_packages: [2-RAILS/Verses/t210-peace-beyond-winning.md]
status: draft
review_status:
  en: clean-for-review
  zh: clean-for-review
  hi: clean-for-review
  ne: needs-native-review
  bo: escalate-native-review
  mn: escalate-native-review
  lbj: escalate-native-review
---

# Day 83 — Peace Beyond Winning (法句經 T210)

Rail: [[2-RAILS/Verses/t210-peace-beyond-winning]] · own translation from CBETA Chinese source (CC BY-NC-SA), grounded on the Pali parallel Dhp 201 (Sujato, CC0).
Short verse, **quoted in full**. Meaning: both winning and losing cost you something, so put down the scorekeeping and the peace is already there.

## Source (Chinese, T210 — verbatim)

> 勝則生怨、負則自鄙，去勝負心，無爭自安。 (`zh-dharmapada.md#^lgT04p0567b1801`)

## Renderings (one short line each)

> **Note on zh:** the verbatim CBETA text above is **the source**; the shipped `zh` rendering is **modern Traditional Chinese** (Taiwan/HK/SG) like every other language, per the vault's standing rule (CLAUDE.md hard rule 5, `verse-rail` "Source-language output ships modern", `translation-qa` rule 8, `vault-annex.md` §4). **Do not "correct" it back to the classical text.**

- **en** — Winning breeds resentment, losing breeds self-contempt. Let go of the win-lose mind, and with nothing to contend, be at peace.
- **zh** — 贏了會招來怨恨，輸了會看不起自己；放下勝負之心，無所爭執，自然安穩。
- **bo** — ⚑ རྒྱལ་ན་ཞེ་སྡང་སློང་། ཕམ་ན་རང་ཉིད་ལ་བརྙས་སེམས་སྐྱེ། རྒྱལ་ཕམ་གྱི་བློ་དོར་ན་རྩོད་པ་མེད་པར་རང་བཞིན་གྱིས་བདེ།
- **hi** — जीतने से वैर उपजता है, हारने से आत्म-तिरस्कार। जीत-हार का भाव छोड़ दो, तो कोई झगड़ा नहीं और मन स्वयं शान्त।
- **ne** — जित्दा वैर जन्मिन्छ, हार्दा आत्म-अपमान। जित-हारको भाव छोड, कुनै झगडा रहँदैन र मन आफै शान्त हुन्छ।
- **mn** — ⚑ Хожвол хорсол төрнө, хожигдвол өөрийгөө басамжилна. Хожих-хожигдох сэтгэлийг тавь, тэмцэл үгүй бол сэтгэл өөрөө амар.
- **lbj** — ⚑ རྒྱལ་ན་ཞེ་སྡང་སློང་། ཕམ་ན་རང་ལ་བརྙས་སེམས་སྐྱེ། རྒྱལ་ཕམ་གྱི་བློ་བོར་ན། རྩོད་པ་མེད་དེ་རང་བཞིན་གྱིས་བདེ།

## QA — pre-review (against 2-RAILS/Verses/t210-peace-beyond-winning.md)

### en
- Back-translation: "Winning breeds resentment, losing breeds self-contempt. Let go of the win-lose mind, and with nothing to contend, be at peace."
- Findings: all four phrases present in order. `勝負心` kept as a **single idea** ("the win-lose mind") per rail flag (a), not split into two desires. `自鄙` shipped as **self-contempt**, the Chinese reading, not the Pali parallel's "sleeps badly" — the flagged divergence, deliberately not flattened. `自安` rendered so the peace is what remains rather than something manufactured (flag b). `怨` kept interpersonal per flag (c). 126 chars — one over the ~125 design benchmark, which Evan confirmed acceptable (2026-09). No em dash ✓.
- Net: clean for review.

### zh (Traditional)
- Back-translation: "Winning invites resentment, losing makes you look down on yourself; put down the win-lose mind, with nothing to fight over, and you are naturally at ease."
- Findings: **our own modern Traditional rendering**, not the verbatim source (per the note above). Back-translated **against the verbatim source** as rule 8 requires: all four phrases map one-to-one — 勝則生怨 → 贏了會招來怨恨, 負則自鄙 → 輸了會看不起自己, 去勝負心 → 放下勝負之心, 無爭自安 → 無所爭執，自然安穩. Modernised: the classical `則` conditional becomes 了…會; `自鄙` unpacked to 看不起自己, which a modern reader parses instantly where the classical compound would not; `自安` becomes 自然安穩, keeping the "of itself" force per flag (b). 勝負之心 keeps the compound intact per flag (a). Taiwan/HK/SG register.
- Net: clean for review.

### hi
- Back-translation: "Winning gives rise to enmity, losing to self-contempt. Give up the sense of winning and losing, then there is no quarrel and the mind is peaceful of itself."
- Findings: वैर for `怨` matches the termbase's *vera* row ✓ and keeps it interpersonal (flag c). जीत-हार का भाव holds the compound as one idea (flag a). मन स्वयं शान्त carries `自安`'s "of itself" (flag b).
- Net: clean for review.

### ne
- Back-translation: "When winning, enmity is born; when losing, self-humiliation. Give up the sense of winning and losing, no quarrel remains and the mind becomes peaceful by itself."
- Confidence flags: confirm आत्म-अपमान is the natural Nepali for self-contempt rather than something stronger like self-hatred; confirm झगडा is the right register for `爭` (contention) rather than a word for a physical fight.
- Net: needs native review.

### bo ⚑
- Back-translation (approx): "If you win, you provoke enmity; if you lose, contempt for yourself arises. If you drop the mind of winning and losing, then with no contention there is natural ease."
- Confidence flags: our rendering (source is Chinese, not Tibetan). `ཞེ་སྡང` is the termbase rendering for hatred/enmity ✓ — confirm it is right for `怨` (resentment others hold toward you) rather than a word for one's own anger. Confirm `བརྙས་སེམས` carries self-contempt. Confirm `རྒྱལ་ཕམ་གྱི་བློ` reads as one compound idea per flag (a), and that `རང་བཞིན་གྱིས་བདེ` carries `自安`'s "of itself."
- Net: escalate to native Tibetan dharma reviewer.

### mn ⚑
- Back-translation (approx): "If you win, rancour arises; if you lose, you belittle yourself. Set down the winning-and-losing mind; with no struggle, the mind is at ease of itself."
- Confidence flags: confirm хорсол is the right word for `怨` as interpersonal resentment rather than bitterness generally; confirm басамжилна carries self-contempt directed inward; confirm "сэтгэл өөрөө амар" keeps the "of itself" sense.
- Net: escalate to native Mongolian dharma reviewer.

### lbj (Ladakhi) ⚑
- Back-translation (approx): "If you win, you provoke enmity; if you lose, contempt for yourself arises. If you cast off the win-lose mind, there is no contention and natural ease."
- Findings: **Tibetan script** — settled 2026-09 after this field was briefly specified as Devanagari and then corrected back; the Devanagari draft of this line has been discarded. Differs from the `bo` line in two spots: **`བོར`** for "cast off" rather than `bo`'s `དོར`, and **`རང་ལ`** rather than `bo`'s fuller `རང་ཉིད་ལ`. `ཞེ་སྡང` and `རྒྱལ་ཕམ་གྱི་བློ` are shared with `bo` — the compound must stay one idea in both, per the rail's flag (a).
- Confidence flags — **lowest confidence of any language on this card.** Ladakhi is the newest output language and its entire `termbase.md` column is still `⚑ TBD`, so there is no ratified vocabulary to check against. Because Ladakhi shares script *and* much dharma vocabulary with `bo`, the differentiation above is unavoidably thin, and the reviewer's real job is the layer I cannot reach: everyday word choice, pronunciation-driven spelling, verb endings, and case particles. Treat this line as a draft to rewrite, not to approve.
- Net: escalate to native Ladakhi dharma reviewer.
