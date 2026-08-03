---
day: 88
date: 2026-09-19
source_ref: "DĀ 22 (種德經, Soṇadaṇḍa parallel) · DN 4 parallel"
canon: Chinese
theme: threefold-training
speaks_to: [aspiration, doubtful, hopeful]
occasions: []
source_rail: 2-RAILS/Verses/da-22-ethics-and-wisdom.md
context_packages: [2-RAILS/Verses/da-22-ethics-and-wisdom.md]
status: draft
review_status:
  en: clean-for-review
  zh: clean-for-review
  hi: clean-for-review
  ne: needs-native-review
  bo: escalate-native-review
  mn: escalate-native-review
---

# Day 88 — Ethics and Wisdom (DĀ 22)

Rail: [[2-RAILS/Verses/da-22-ethics-and-wisdom]] · own translation from CBETA Chinese source (CC BY-NC-SA), grounded on the Pali parallel DN 4 (Sujato, CC0).
Short prose teaching, **quoted in full**. Meaning: neither hand can wash itself, and good conduct and clear seeing work the same way.

> **Output languages: six** (en · zh · bo · hi · ne · mn). Ladakhi (`lbj`) discontinued by Evan, 2026-08-03. The rule docs still say seven (the decision was "stop going forward only"); **do not add an `lbj` line back to this card on the strength of them.**

## Source (Chinese, Dīrgha Āgama — verbatim)

> 如人洗手，左右相須，左能淨右，右能淨左。此亦如是，有慧則有戒，有戒則有慧，戒能淨慧，慧能淨戒。 (`zh-digha-agama.md#^pT01p0096b1608`)

Pali parallel (DN 4, `pi-digha-nikaya.md#^dn4-22-2` / `^dn4-22-5` / `^dn4-22-6`): *Yattha sīlaṁ tattha paññā, yattha paññā tattha sīlaṁ. … hatthena vā hatthaṁ dhoveyya … sīlaparidhotā paññā, paññāparidhotaṁ sīlaṁ.*

## Renderings (one short line each)

> **Note on zh:** the verbatim CBETA classical Chinese above is **the source**; the shipped `zh` rendering is **modern Traditional Chinese** like every other language, per the vault's standing rule (CLAUDE.md hard rule 5, `verse-rail` "Source-language output ships modern", `translation-qa` rule 8, `vault-annex.md` §4). **Do not "correct" it back to the classical text.**

- **en** — Hands wash each other, left cleaning right, right cleaning left. So too ethics and wisdom go together, each cleansing the other.
- **zh** — 就像兩隻手互相清洗，左手洗淨右手，右手洗淨左手；持戒與智慧也是如此，兩者相伴而行，彼此洗淨。
- **bo** — ⚑ ལག་པ་གཉིས་ཀྱིས་ཕན་ཚུན་འཁྲུ་བ་བཞིན། གཡོན་པས་གཡས་པ་འཁྲུ། གཡས་པས་གཡོན་པ་འཁྲུ། དེ་བཞིན་ཚུལ་ཁྲིམས་དང་ཤེས་རབ་གཉིས་མཉམ་དུ་འགྲོ་ཞིང་། ཕན་ཚུན་གཙང་མ་བཟོ་གི་རེད།
- **hi** — जैसे दोनों हाथ एक दूसरे को धोते हैं, बायाँ दायें को और दायाँ बायें को; वैसे ही शील और प्रज्ञा साथ चलते हैं और एक दूसरे को निर्मल करते हैं।
- **ne** — जसरी दुई हातले एक अर्कालाई धुन्छन्, देब्रेले दायाँलाई र दायाँले देब्रेलाई; त्यसै गरी शील र प्रज्ञा सँगै हिँड्छन् र एक अर्कालाई निर्मल पार्छन्।
- **mn** — ⚑ Хоёр гар бие биенээ угаадаг шиг, зүүн нь баруунаа, баруун нь зүүнээ; ёс журам ба билиг ухаан ч хамт явж, бие биенээ цэвэрлэдэг.

## QA — pre-review (against 2-RAILS/Verses/da-22-ethics-and-wisdom.md)

### en
- Back-translation: n/a (source language of the rail's Disambiguated Meaning).
- Findings: the simile and both its applications are present. **"Ethics"** for `戒` per rail flag (a) — this is the `termbase.md` locked rendering *and* Sujato's own word at `^dn4-22-6`, so "virtue" was not used even though it is the commoner translation elsewhere. **"Cleansing"** rather than "purifying" per flag (b), following Sujato and keeping the image domestic. **The card's tightest join, per flag (c):** claims 2 and 3 are compressed into "go together, each cleansing the other" — "go together" is Sujato's wording for `有慧則有戒` (`^dn4-22-2`), "each cleansing the other" carries `戒能淨慧，慧能淨戒`. Both claims survive; this is a compression of wording, not a cut. **The Pali's second simile (foot washing foot) is deliberately absent** — it is not in the Chinese source, per the rail's ⚑ divergence flag; likewise the left/right specification is kept because the Chinese has it and the Pali does not. 125 chars, inside the 126 ceiling. No em dash ✓.
- Net: clean for review.

### zh (Traditional)
- Back-translation: "Just as two hands wash each other, the left hand washes the right clean and the right hand washes the left clean; keeping ethics and wisdom are also like this, the two travel alongside each other and wash each other clean."
- Findings: **our modern Traditional rendering, not the verbatim CBETA text** (per the note above). Back-translated **against the verbatim source** as rule 8 requires: `如人洗手` → `就像兩隻手互相清洗`; `左能淨右，右能淨左` → `左手洗淨右手，右手洗淨左手`; `此亦如是` → `也是如此`; `有慧則有戒，有戒則有慧` → `兩者相伴而行`; `戒能淨慧，慧能淨戒` → `彼此洗淨`. Classical→modern substitutions: the Literary comparative `如人…` → `就像…`; the generic subject `人` dropped and the two hands named, since modern Chinese wants the agent explicit; `相須` → `相伴而行`; the bare verb `淨` → the resultative `洗淨`; `此亦如是` → `也是如此`; the classical conditional `則` construction replaced by a plain statement of co-presence. `持戒` used rather than bare `戒` so the term reads as a practice rather than a rule-book. Taiwan/HK/SG register.
- Confidence note: `兩者相伴而行` is the point where the two source claims are merged, mirroring the English compression in flag (c) — a reviewer should check that a Chinese reader still hears the co-presence claim and not only "they go nicely together."
- Net: clean for review.

### hi
- Back-translation: "Just as both hands wash each other, the left the right and the right the left; in the same way ethics and wisdom walk together and make each other pure."
- Findings: शील and प्रज्ञा both match their `termbase.md` rows. निर्मल करते हैं for `淨` keeps the cleansing sense without the ritual overtone of पवित्र, per rail flag (b). साथ चलते हैं carries the co-presence claim as its own clause, so Hindi keeps claims 2 and 3 slightly more separate than the English does — a small improvement on the compression in flag (c), noted rather than corrected.
- Net: clean for review.

### ne
- Back-translation: "Just as two hands wash each other, the left the right and the right the left; in the same way ethics and wisdom walk together and make each other pure."
- Confidence flags: (i) confirm शील is the natural Nepali Buddhist term here rather than सदाचार; (ii) confirm निर्मल पार्छन् is the right verb for `淨` and does not read as bleaching or laundering; (iii) confirm the left/right clause reads naturally without repeating the verb, or whether Nepali wants धुन्छ restated in each half; (iv) the sentence is long for a card in Nepali — confirm whether it should be split at the semicolon.
- Net: needs native review.

### bo ⚑
- Back-translation (approx): "Like two hands washing each other: the left washes the right, the right washes the left. In the same way, ethics and wisdom go together and make each other clean."
- Findings: source is **Chinese**, not Tibetan, so this is a fresh rendering from the rail's meaning rather than a modernisation of a Tibetan source. `ཚུལ་ཁྲིམས` and `ཤེས་རབ` are the `termbase.md` rows for *sīla* and *paññā*. `འཁྲུ` chosen for the washing (physical, everyday) and `གཙང་མ་བཟོ` for the cleansing effect, keeping flag (b)'s domestic register rather than reaching for `དག་པ`/`རྣམ་དག`, which would pull toward ritual purification.
- Confidence flags: (i) confirm `འཁྲུ` is the natural everyday verb for washing hands rather than a literary form, and that repeating it three times is not clumsy. (ii) `གཙང་མ་བཟོ་གི་རེད` is deliberately plain-modern — confirm it is not too colloquial for a dharma card, and that a reviewer would not prefer `དག་པར་བྱེད`. (iii) Confirm `མཉམ་དུ་འགྲོ` carries the co-presence claim ("where one is, the other is") and not merely "they travel together." (iv) Confirm the left/right pair reads naturally as `གཡོན་པས་གཡས་པ` / `གཡས་པས་གཡོན་པ` without a classifier.
- Net: escalate to native Tibetan dharma reviewer.

### mn ⚑
- Back-translation (approx): "Like two hands washing each other, the left the right and the right the left; ethics and wisdom too go together and clean each other."
- Confidence flags: (i) ёс журам for `戒` is the `termbase.md` first option; the row also offers шагшаабад ⚑ as the more specifically Buddhist term — confirm which belongs on a daily card for a lay reader. (ii) билиг ухаан matches the termbase *paññā* row but is still ⚑ unratified. (iii) Confirm цэвэрлэдэг is right for `淨` and does not read as household cleaning in a way that undercuts the point (the rail wants the image domestic, but not comic). (iv) Confirm the elided verb in "зүүн нь баруунаа, баруун нь зүүнээ" is grammatical in Mongolian or whether угаана must be restated.
- Net: escalate to native Mongolian dharma reviewer.
