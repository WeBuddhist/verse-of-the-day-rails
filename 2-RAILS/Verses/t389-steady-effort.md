---
ref: t389-steady-effort
source_ref: "佛遺教經 T389 (Bequeathed Teachings)"
canon: Chinese (Mahāyāna)
unit_type: single
source_text: 1-SOURCES/Text/zh-bequeathed-teachings.md
source_block: "^pT12p1111c1701"
grounding: chinese-source
translations: [own-from-source]
vehicle: "Mahāyāna"
theme: steady-effort
card_type: encouragement
speaks_to: [discouraged, impatient, hopeful]
buddhist_lens: "my practice is too small to matter → viriya, the small stream that wears through stone"
occasions: []
concepts: [viriya / 精進 (effort, perseverance), 穿石 (wearing through stone — the simile)]
status: draft
---

## Source Text (CBETA — CC BY-NC-SA)
![[1-SOURCES/Text/zh-bequeathed-teachings.md#^pT12p1111c1701]]

**The shipped sentence, verbatim from that block:**
> 汝等比丘，若勤精進則事無難者，是故汝等當勤精進，譬如小水常流則能穿石。
> *(verbatim substring of `zh-bequeathed-teachings.md#^pT12p1111c1701`, quoted whole. The vocative `汝等比丘` ("you monks") that opens it is dropped so the encouragement reads universally, the same treatment given `汝今，羅雲！` on `ea-mudita`. No wording inside the sentence is altered, and nothing is stitched from the following sentence.)*

## ⚑ Data-quality fix required in the candidate pool
`candidate-pool/chinese.md` records **Day 40** (`t389-concentration`, the quote `制之一處，無事不辦`) against this same anchor, `^pT12p1111c1701`. **That record is wrong.** Verified by grep against `zh-bequeathed-teachings.md`: `制之一處，無事不辦` sits at **`^pT12p1111a0801`**, and `^pT12p1111c1701` holds the 精進 passage used here. So this anchor is genuinely unclaimed, and the pool's Day 40 link needs correcting. This is the second instance of the mis-recorded-anchor pattern already flagged at the pool's line 941 — **a systematic anchor audit of the claimed Chinese Mahāyāna rails is worth doing**, since these errors only surface at build time.

## Authoritative Renderings
### None held — `grounding: chinese-source`
The vault holds **no English translation of T389** (same situation as `t389-contentment`, Day 112, and the other Chinese Mahāyāna cards). The Disambiguated Meaning below is derived from the source's own grammar; the sentence is simple and its reading is not contested.

## Traditional Interpretation (commentary)
*No commentary imported.*

## Disambiguated Meaning
Grounded in the Chinese source (`zh-bequeathed-teachings.md#^pT12p1111c1701`):

Three beats, and the middle one is a restatement, not a new claim:

1. **`若勤精進則事無難者`** — "**if you are diligent in 精進, then nothing is difficult**." 精進 is *viriya* (termbase row added with this card: effort, perseverance · 精進 · བརྩོན་འགྲུས · वीर्य / प्रयत्न · वीर्य / प्रयत्न · хичээл ⚑). `勤` adds sustained, unremitting application. `事無難者` is literally "there is no matter that is hard."
2. **`是故汝等當勤精進`** — "**therefore you should be diligent in 精進**." A restatement in the imperative, which is what makes the sentence an encouragement addressed to the reader rather than an observation about effort.
3. **`譬如小水常流則能穿石`** — "**like a small quantity of water that flows constantly and so is able to bore through stone**." `小` (small) and `常` (constant) are the two load-bearing words; `穿` is to pierce or bore through, not merely to erode.

The teaching is about **rate, not size**: the mechanism is continuity, and the smallness of the amount is the point rather than an obstacle. It is the answer to "my practice is too small to be worth anything."

- **⚑ Rendering choice: `是故汝等當勤精進` is compressed, not cut.** Rendered in full — "therefore you should be diligent in effort" — it repeats beat 1 word for word and pushes the card past the budget. The card ships "**so keep at it**," which keeps the imperative and the addressee (the two things the restatement contributes) while not repeating the phrase. Flagged as a compression of a restatement, permitted because no *content* is dropped; a reviewer who wants the repetition restored should expect to lose the simile instead. Contrast **Day 93**, where a structurally similar tail was kept because it carried the teaching, and **`an4-73-speaks-well`**, where an emphasis-only tail was dropped entirely.
- **⚑ Rendering choice: 精進 ships as "steady effort," not "diligence."** Two reasons. (a) `勤` and `常` both carry continuity, and "steady" is where that lands in English. (b) **Day 113 in this same batch ships 不放逸 as "diligence"** — using the same English word for both would collapse two distinct terms two days apart. Keep them apart: *appamāda* = diligence, *viriya* = steady effort. This distinction should go in the termbase, and the new `viriya` row records it.
- **⚑ Rendering choice: `小水` ships as "a small stream," not "a little water."** "A little water flowing constantly can bore through stone" is more literal but reads like a physics claim; "a small stream that runs on" is the image a reader can see. Flagged as a mild concretisation.
- **⚑ Rendering choice: `穿石` ships as "wears through stone."** "Bores through" is closer to `穿` but suggests a drill and an agent; "wears through" is what water does and what an English speaker would say. Collocation screen, the same one applied to `苦`/"bitter" and to Day 106's `chetvā`.
- **Do not import the following sentence.** The block continues `若行者之心數數懈廢，譬如鑽火未熱而息，雖欲得火，火難可得` (the fire-drill simile for repeated slackening). It is the negative mirror, it is discouraging in tone, and it would make the card two similes and two claims. **Excluded**, and it must not later be added as if the card had been truncated.

## Theme & Selection Notes
Theme: **steady-effort**, new tag. Adjacent cards: `effort` (Day 15, Dhp 25), `concentration` (Day 40, the same sūtra, different chapter and a different anchor), `diligence` (Day 77, DN 16) and `heedfulness-as-ground` (Day 113, this batch). None of them is about *smallness accumulating*, which is this card's content and the reason it answers a discouragement none of the others reach.

**Gate checks.** *Buddhavacana* — T389 is the Buddha's bequeathed teaching, addressed throughout to `汝等比丘`; this sentence is his own imperative. *In scope* — Chinese Mahāyāna sūtra, in scope per Evan (log.md). *Traceable* — `^pT12p1111c1701`, re-verified by grep. *License* — CBETA **CC BY-NC-SA**. *Real quote, kept whole* — one complete sentence, vocative dropped, restatement compressed (see flag). *Length* — en 119, zh 40 (the longest zh line in this batch; a reviewer may want it tighter). *Fresh* — this sentence has never been used; see the anchor-error note above for why the pool appeared to say otherwise.

**Screens.** *Arrives already applied* ✓ — second person from the first word, and the imperative is addressed to the reader. *Lands on one read* ✓ — the simile names its own referent (effort) inside the sentence, which is `card-types.md`'s condition for a workable simile. *One idea in five words* ✓ — "small stream wearing through stone." *Warm* ✓ — it lowers a bar and removes a discouragement, which is the `encouragement` type exactly; the negative mirror is deliberately excluded. *Dharma, not general life advice* — ⚑ **a real risk, and worth naming.** "Persistence pays off" is a secular platitude and this sentence can be read that way. What keeps it on the dharma side: 精進 is one of the pāramitās and one of the five faculties, with a termbase row; the sūtra's frame is the Buddha's final instruction on how to practise after he is gone; and `事無難者` is a claim about the path, not about worldly goals. Recorded so a reviewer can disagree knowingly. *No "Buddha" in the card* ✓. *Not sober* ✓.

**Batch spacing.** ⚑ **This card and Day 113 are adjacent** — both concern sustained application (不放逸 there, 精進 here), three days apart. The subjects differ (*where good qualities come from* vs. *small effort accumulating*) and the English terms are deliberately kept distinct, but a reviewer should see them together and may want one held for a later batch. Also note **this batch runs two T389 cards**, Days 112 and 116, from different chapters and different blocks — permitted precedent (Evan, 2026-08-03: same source, distinct quotes), and deliberately placed at the two ends of the batch rather than adjacent.

**Shipped-zh policy — modern, not the classical source.** The verbatim CBETA sentence is **the source**; the shipped `zh` is **modern Traditional Chinese**. Substitutions: the vocative `汝等比丘` dropped; `若勤精進則` → `只要不斷精進，就`; `事無難者` → `沒有難事`; `是故汝等當勤精進` → `所以要持續努力下去`; `譬如` → `就像`; `小水常流` → `小水流不停地流`; `則能穿石` → `也能穿透石頭`. 精進 is kept in the first clause, because it is the doctrinal term with a termbase row, and paraphrased as 努力 in the restatement, which is exactly what the restatement is for. Standing rule — **do not revert the card's zh to the classical text.**

## Concept Links
- `viriya` / 精進 (effort, perseverance — termbase row added with this card, and deliberately distinguished there from *appamāda*) · `appamāda` / 不放逸 (Day 113, Day 77, Day 66 — the neighbouring term) · the fire-drill simile (`若行者之心數數懈廢…`, the same block, excluded as the negative mirror)
