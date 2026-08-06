---
ref: ea-ground-of-diligence
source_ref: "EĀ 增壹阿含經 (卷18) · SN 45.150 / AN 10.15 parallels"
canon: Chinese Āgama
unit_type: single
source_text: 1-SOURCES/Text/zh-ekottarika-agama.md
source_block: "^pT02p0635b1202"
grounding: chinese-source
translations: [own-from-source, pali-parallel-reference, sujato]
pali_parallel: "SN 45.150 (Bījasutta, ^sn45-150-1-1) for the earth simile; AN 10.15 (Appamādasutta, ^an10-15-1-2) for the all-good-qualities-are-rooted-in-appamāda formula — neither is an exact parallel, see the flag"
theme: heedfulness-as-ground
card_type: observation
speaks_to: [discouraged, scattered, hopeful]
buddhist_lens: "good qualities felt as scattered and unrelated → appamāda as the single ground they all grow from"
occasions: []
concepts: [appamāda / 不放逸 (diligence, heedfulness), kusala / 善 (wholesome qualities), 道品 (the qualities of the path)]
status: draft
---

## Source Text (CBETA — CC BY-NC-SA)
![[1-SOURCES/Text/zh-ekottarika-agama.md#^pT02p0635b1202]]

**The full passage in that block, verbatim:**
> 猶如山河、石壁、百草、五穀，皆依於地而得長大，然復此地最尊、最上。此亦如是，諸善道品之法，住不放逸之地，使諸善法而得長大。

**The shipped sentence, verbatim:**
> 諸善道品之法，住不放逸之地，使諸善法而得長大。
> *(verbatim substring of `zh-ekottarika-agama.md#^pT02p0635b1202`, quoted whole. The pivot `此亦如是` ("this too is likewise") that opens it in the source is dropped, the same treatment given the list connective `Puna caparaṁ` on `an4-73-speaks-well` and the vocative `汝今，羅雲！` on `ea-mudita`. No wording inside the sentence is altered.)*

## ⚑ Why the earth simile is NOT on the card — a length-gate failure caught at build time
This passage was proposed and approved as a **simile** card (mountains, rivers, grasses and grain all grow from the earth; so every good quality grows from diligence). **It does not fit.** Rendered whole, as `selection-criteria.md` §2 requires — no summarising, no cutting — the two-sentence unit is:

> "Just as mountains, rivers, cliffs, grasses and grain all grow from the earth, and the earth is the highest of all, so every good quality of the path rests on the ground of diligence and grows from it." — **200 characters.**

The card budget is ~125 (126 acceptable). 200 is not a near miss, and the only ways to reach 125 would be to drop `石壁`, `山`, and `然復此地最尊、最上` — i.e. to **distil**, which is barred. The simile half alone (`猶如…而得長大`) is a dangling "just as" clause and fails the self-contained test.

**So the card ships the passage's second sentence alone**, which is a real contiguous complete quote, is intelligible with no simile behind it, and fits at 101 characters. **The consequence, stated honestly: this is no longer a simile card, it is an observation.** The earth image survives only as a trace in the word `地` / "ground."

**Process note for the next batch:** the length should have been resolved *before* the candidate went to the curator. `log.md` already carries this exact lesson from the Toh 149 failure in the 2026-09 batch ("resolve the length **before** putting it in front of the curator, not after"). It recurred here. The alternates offered alongside this card were Lotus T262 (`如為一人，眾多亦然…`, consolation) and Toh 219 (`May every being hold a jewel in their hands`, aspiration); either could replace this card if a reviewer judges the reduced version too plain.

## Authoritative Renderings
### None held for the Ekottarika — `grounding: chinese-source`
No Patton translation exists for the Ekottarika Āgama (the same situation as `ea-mudita`, `ea-repay-kindness`, `ea-trouble-nothing-alive`), so there is no paired English at this anchor. Two Pali passages are cited below as convergent meaning anchors, not as parallels of this exact sentence.

### Bhikkhu Sujato — English, SN 45.150 (CC0) — the earth simile
![[1-SOURCES/Translations/en-samyutta-nikaya-sujato.md#^sn45-150-1-1]]

### Bhikkhu Sujato — English, AN 10.15 (CC0) — the appamāda formula
![[1-SOURCES/Translations/en-anguttara-nikaya-sujato.md#^an10-15-1-2]]

## Traditional Interpretation (commentary)
*No commentary imported.*

## Disambiguated Meaning
Grounded in the Chinese source (`zh-ekottarika-agama.md#^pT02p0635b1202`), with the two Pali passages above as convergent references:

1. **`諸善道品之法`** — "the qualities/factors of the good path," i.e. **all the wholesome qualities a practitioner develops** (善 = *kusala*, termbase: wholesome, skillful · 善 · དགེ་བ · कुशल · कुशल · буян). Not a technical enumeration — the Chinese is a general collective, and it must ship as a general collective, not as a named list.
2. **`住不放逸之地`** — "**stand on / dwell on the ground of 不放逸**." 不放逸 is the standard Chinese rendering of *appamāda* (termbase: diligence, heedfulness · 不放逸 · བག་ཡོད · अप्रमाद · अप्रमाद · сэрэмж ⚑). `地` is literally *earth / ground* — the residue of the dropped simile, and the reason the rendering keeps the word "ground" rather than abstracting to "basis."
3. **`使諸善法而得長大`** — "**causes all good qualities to grow**." `長大` is organic growth, not accumulation.

So: **the many good qualities are not many separate projects; they have one ground, and that ground is not letting yourself drift.** The card states how it works and leaves the reader to draw the encouragement — which is why the card type is `observation`, not `teaching`.

- **⚑ The Pali parallels diverge, and must not be used to overwrite the Chinese.** `SN 45.150` pairs the earth-and-plants simile with **`sīla` (ethics)**, not with *appamāda*: "a mendicant develops the noble eightfold path depending on and grounded on ethics" (`en-samyutta-nikaya-sujato.md#^sn45-150-1-2`). `AN 10.15` gives the *appamāda* formula — "all skillful qualities are rooted in diligence and meet at diligence" (`^an10-15-1-2`) — but its similes are the elephant's footprint and the roof peak, **not the earth**. **The Chinese recension is the one that puts the earth simile together with 不放逸, and this card ships the Chinese.** Do not "correct" the ground to ethics on the strength of SN 45.150.
- **⚑ Rendering choice: 不放逸 ships as "diligence," not "heedfulness."** Both are in the termbase row. "Diligence" is Sujato's word at `^an10-15-1-2`, is already the shipped English on **Day 77**, and passes the collocation test — an English speaker with no Buddhist background says "diligence." "Heedfulness" (shipped on Day 66) reads slightly archaic cold, and Day 66 is *already* flagged in `log.md` for an accessibility problem. Prefer diligence.
- **⚑ Rendering choice: `地` stays as "ground."** It is the only surviving trace of the earth simile and it does real work — "basis" or "foundation" would be more idiomatic and less alive.
- **⚑ Rendering choice: 諸善道品之法 ships as "every good quality of the path," not "the factors of the path."** The latter would read as the seven *bodhyaṅgas* or the eightfold path specifically and would need a gloss, failing the no-glossary screen.
- **⚑ `此亦如是` dropped — a judgement call, flagged for review.** It is the simile's pivot, so dropping it is a slightly stronger move than dropping a vocative or `Puna caparaṁ`. The defence: with the simile itself excluded on the length gate, the pivot has no referent and would leave the card pointing at nothing ("this too is likewise…"), which is exactly the out-of-context failure the screens bar. A reviewer may disagree and pull the card.

## Theme & Selection Notes
Theme: **heedfulness-as-ground.** This **fills a "Known gaps" entry** in `theme-checklist.md` — *heedfulness as the foundation of virtue*, whose recorded Chinese candidate is precisely this passage (EA juan 18, the earth simile). The calendar has `heedfulness` (Day 66, Udānavarga 4) and `diligence` (Day 77, DN 16), but neither says the thing this one says: that the good qualities share a single root.

**Gate checks.** *Buddhavacana* — the block opens `爾時，世尊告諸比丘` ("then the Blessed One said to the monks"). *In scope* — Ekottarika Āgama. *Traceable* — `^pT02p0635b1202`. *License* — CBETA **CC BY-NC-SA** (source); Sujato **CC0** (the two reference passages). *Real quote, kept whole* — one complete sentence, contiguous, connective dropped; **see the length-gate section above for what was excluded and why.** *Length* — en 101, zh 36. *Fresh* — this anchor has never been used. ⚑ Note the pool records this anchor **twice**, as `ea-g` and again under juan 18; dedupe the pool entry at claim time. The pool also carries a standing warning that shortcut-pass Ekottarika anchors may be off by one block — **this one was re-verified directly against `zh-ekottarika-agama.md` and is correct.**

**Screens.** *Arrives already applied* — ⚑ **the weakest screen on this card.** The sentence is a general statement about how good qualities grow, so the reader has a short step to take to "so keep at it." The rendering closes that step as far as the source allows by keeping "in you" out and letting `地`/"ground" do the work; a reviewer may still judge it one inference too many, which is the Dhp 228 objection. *Lands on one read* ✓ — no scene, no proper names, no frame. *One idea in five words* ✓ — "one ground, everything grows." *Warm* ✓ — it neither corrects nor warns; it consolidates. *Dharma, not general life advice* ✓ — 不放逸 and 善道品 are both doctrinal. *No "Buddha" in the card* ✓. *Not sober* ✓.

**Batch spacing.** The other cards in this batch are contentment (112), unshaken mind (114), the teaching as shelter (115) and steady effort (116). ⚑ **This card and Day 116 are adjacent** — both concern sustained application (不放逸 here, 精進 there). They are two days apart, and the subjects differ (*where good qualities come from* vs. *small effort accumulating*), but a reviewer should see them together. Named rather than hidden.

**Shipped-zh policy — modern, not the classical source.** The verbatim CBETA sentence is **the source**; the shipped `zh` is **modern Traditional Chinese**. Substitutions made: `諸善道品之法` → `修道上一切善的品質`; `住…之地` → `都立在…這片土地上`; `使…而得長大` → `也正是從這片土地生長起來的`; 不放逸 is kept, because it is the doctrinal term with a termbase row and it is still legible in modern Chinese. Standing rule — **do not revert the card's zh to the classical text.**

## Concept Links
- `appamāda` / 不放逸 (diligence, heedfulness — cf. Day 66, Day 77) · `kusala` / 善 (wholesome) · `sīla` (the ground SN 45.150 names instead — see the divergence flag) · the earth simile (SN 45.150, excluded here on length)
