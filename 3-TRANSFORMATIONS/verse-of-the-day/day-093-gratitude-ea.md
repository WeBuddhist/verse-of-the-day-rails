---
day: 93
date: 2026-09-24
source_ref: "EĀ 增壹阿含經 (卷11) · AN 2.32 parallel"
canon: Chinese
theme: gratitude
speaks_to: [grateful, lonely, hopeful]
occasions: []
source_rail: 2-RAILS/Verses/ea-repay-kindness.md
context_packages: [2-RAILS/Verses/ea-repay-kindness.md]
status: draft
review_status:
  en: clean-for-review
  zh: clean-for-review
  hi: clean-for-review
  ne: needs-native-review
  bo: escalate-native-review
  mn: escalate-native-review
---

# Day 93 — Gratitude (EĀ 卷11)

Rail: [[2-RAILS/Verses/ea-repay-kindness]] · own translation from CBETA Chinese source (CC BY-NC-SA), grounded on the Pali parallel AN 2.32 (Sujato, CC0) — which anchors the first claim only.
Short prose teaching, **quoted in full**. Meaning: gratitude is not measured by the size of the favour, and the small one is where it shows.

> **Output languages: six** (en · zh · bo · hi · ne · mn). Ladakhi (`lbj`) discontinued by Evan, 2026-08-03. The rule docs still say seven (the decision was "stop going forward only"); **do not add an `lbj` line back to this card on the strength of them.**

## Source (Chinese, Ekottarika Āgama — verbatim)

> 若有眾生知反復者，此人可敬，小恩尚不忘，何況大恩！ (`zh-ekottarika-agama.md#^pT02p0600a0602`)

Pali parallel (AN 2.32, `pi-anguttara-nikaya.md#^an2-32-2-5`): *Sappuriso ca kho, bhikkhave, kataññū hoti katavedī.* — Sujato: "The true person is grateful and thankful." **Anchors the first claim only**; the small/great comparison is the Chinese text's own.

## Renderings (one short line each)

> **Note on zh:** the verbatim CBETA classical Chinese above is **the source**; the shipped `zh` rendering is **modern Traditional Chinese** like every other language, per the vault's standing rule (CLAUDE.md hard rule 5, `verse-rail` "Source-language output ships modern", `translation-qa` rule 8, `vault-annex.md` §4). **Do not "correct" it back to the classical text.**

- **en** — Anyone who repays kindness is worthy of respect: if even a small kindness is not forgotten, how much more a great one.
- **zh** — 凡是懂得報恩的人，都值得尊敬；連小小的恩惠都不會忘記，更不用說大的恩惠了。
- **bo** — ⚑ དྲིན་ལན་ལོག་འཇལ་ཤེས་པའི་མི་སུ་ཡིན་ཡང་བཀུར་བར་འོས་པ་རེད། དྲིན་ཆུང་ཆུང་ཡང་བརྗེད་མི་སྲིད་ན། དྲིན་ཆེན་པོ་ལྟ་ཅི་སྨོས།
- **hi** — जो भी उपकार का बदला जानता है, वह आदर के योग्य है; जब छोटा उपकार भी नहीं भूला जाता, तो बड़े की तो बात ही क्या।
- **ne** — जो पनि गुन तिर्न जान्दछ, त्यो आदरको योग्य हुन्छ; सानो गुन पनि बिर्सिन्न भने, ठूलोको कुरै छाडिदिनुहोस्।
- **mn** — ⚑ Хүний сайныг хариулж мэддэг хэн ч бай хүндлэлд зохино; бага сайныг ч мартдаггүй бол ихийг хэлэх ч хэрэггүй.

## QA — pre-review (against 2-RAILS/Verses/ea-repay-kindness.md)

### en
- Back-translation: n/a (source language of the rail's Disambiguated Meaning).
- Findings: both claims present. **"Repays kindness"** for `知反復` per rail flag (a) — the Chinese term is about *reciprocating*, stronger than "is grateful"; "repay a debt" avoided, which would make it transactional. **"Worthy of respect"** for `可敬` per flag (b), not "admirable." **The `何況` construction ships as a genuine *a fortiori* ("how much more")** per flag (c) — this is the easiest error on the card, since "let alone" or "still less" would invert the logic and say the great kindness is *forgotten*. **"Kindness" for `恩`** per flag (d), not "grace" or "gift." **The negative mirror is absent** per the rail's central ⚑ flag — the source continues into the ungrateful person at length, and including it would make this a warning instead of praise ✓. 118 chars. No em dash ✓.
- Net: clean for review.

### zh (Traditional)
- Back-translation: "Anyone who understands how to repay kindness is worthy of respect; if even the smallest kindness is not forgotten, still less need one mention a great kindness."
- Findings: **our modern Traditional rendering, not the verbatim CBETA text** (per the note above). Back-translated **against the verbatim source** as rule 8 requires: `若有眾生知反復者` → `凡是懂得報恩的人`; `此人可敬` → `都值得尊敬`; `小恩尚不忘` → `連小小的恩惠都不會忘記`; `何況大恩` → `更不用說大的恩惠了`. Classical→modern substitutions: the Literary conditional-existential `若有眾生…者` → `凡是…的人`; `知反復` → `懂得報恩`, which is the ordinary modern word for the same act; the demonstrative-plus-bare-adjective `此人可敬` → the modern predicate `都值得尊敬`; the classical adverb `尚` unpacked into the modern `連…都`; and bare literary `何況` → the standard modern *a fortiori* `更不用說…了`. Taiwan/HK/SG register.
- Confidence note: `更不用說…了` is the correct modern construction but is idiomatically closer to "needless to say" than to "how much more" — a reviewer should confirm the *a fortiori* force survives and does not flatten into a throwaway.
- Net: clean for review.

### hi
- Back-translation: "Whoever knows how to return a favour is worthy of respect; when even a small favour is not forgotten, then what to say of a great one."
- Findings: बदला जानता है carries `知反復`'s reciprocating sense per rail flag (a). आदर के योग्य for `可敬` per flag (b). तो बात ही क्या is the natural Hindi *a fortiori* and preserves the logic per flag (c) ✓. उपकार for `恩` — confirm with the reviewer whether उपकार (a favour done) or कृतज्ञता (the feeling) is wanted; the rail asks for the act, so उपकार is used deliberately.
- Net: clean for review.

### ne
- Back-translation: "Whoever knows how to repay a debt of kindness is worthy of respect; if even a small kindness is not forgotten, leave aside the matter of a great one."
- Confidence flags: (i) गुन तिर्न is the natural Nepali for repaying kindness but तिर्न is literally "to pay" — confirm it does not read as settling a financial debt, which rail flag (a) explicitly warns against; (ii) **कुरै छाडिदिनुहोस् is the weakest point on this line** — it is an imperative aside ("leave the matter aside") where the other languages have a clean *a fortiori*, and it may read oddly on a card; a reviewer should probably replace it; (iii) confirm the register of the whole line matches earlier Nepali cards, which have mixed familiar and polite forms.
- Net: needs native review.

### bo ⚑
- Back-translation (approx): "Anyone who knows how to return kindness is worthy of being honoured. If even a small kindness cannot be forgotten, what need is there to speak of a great one?"
- Findings: source is **Chinese**, not Tibetan, so this is a fresh rendering from the rail's meaning rather than a modernisation of a Tibetan source. `དྲིན་ལན་ལོག་འཇལ` is the standard Tibetan phrase for repaying kindness and carries the reciprocating sense of `知反復` per flag (a). `བཀུར་བར་འོས་པ` for `可敬` per flag (b). `ལྟ་ཅི་སྨོས` is the standard Tibetan *a fortiori* and preserves the logic per flag (c) ✓.
- Confidence flags: (i) confirm `དྲིན་ལན་ལོག་འཇལ` is not too formal or literary for a daily card, and whether a plainer modern phrasing exists. (ii) `བརྗེད་མི་སྲིད་ན` renders "is not forgotten" as "cannot possibly be forgotten," slightly stronger than the source's `尚不忘` — confirm this is acceptable or should be softened. (iii) Confirm `སུ་ཡིན་ཡང` is the natural way to render the source's open `若有眾生` ("if there is anyone") without sounding like a legal formula. (iv) **`དྲིན` has no `termbase.md` row** — this is the vault's second gratitude card and the term still is not locked; worth adding a row.
- Net: escalate to native Tibetan dharma reviewer.

### mn ⚑
- Back-translation (approx): "Whoever knows how to return another's kindness deserves respect; if even a small kindness is not forgotten, there is no need to speak of a great one."
- Confidence flags: (i) сайныг хариулах renders `知反復` as "returning good" — confirm this is the established Mongolian idiom for repaying kindness rather than a calque. (ii) **хүндлэлд зохино may be too formal/bureaucratic** for `可敬`; confirm a warmer construction. (iii) ихийг хэлэх ч хэрэггүй carries the *a fortiori* — confirm it reads as "how much more" rather than dismissively as "no need to discuss." (iv) As with Tibetan, **no termbase row exists for gratitude/kindness-received**; flagged as a gap rather than guessed at.
- Net: escalate to native Mongolian dharma reviewer.

## Why this card was selected

Chosen directly against the failures of the last three batches. It is **self-applying** — it names no person, place, scene or event, it addresses anyone (`若有眾生`, "if there is anyone"), and a reader knows on one read what it is saying to them. It is **one idea** (a single claim about where gratitude shows; the *a fortiori* reinforces rather than adds). It is **warm** — it praises a quality rather than correcting a fault, which is why the source's long negative mirror about ungrateful people is deliberately left out. Like Day 92, it has **no image at all**, which is worth recording: the screen that matters is whether the meaning lands, not whether the card is vivid.
