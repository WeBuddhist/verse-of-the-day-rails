# Termbase — locked key-term renderings

The shared **vocabulary contract** for verse-of-the-day: one agreed rendering per
key term, per language, so the same term reads the same way every day and isn't
re-invented. Consumed by [`verse-rail`](../../../4-SYSTEM/Skills/verse-rail/SKILL.md)
(when rendering) and [`translation-qa`](../../../4-SYSTEM/Skills/translation-qa/SKILL.md)
(terminology check).

> **Status — working draft.** English, Chinese, and Hindi entries are solid;
> **Tibetan, Nepali, and especially Mongolian renderings marked ⚑ are proposed
> and need native-reviewer ratification.** Until a native reviewer signs off a
> row, treat it as a strong default, not a lock. Chinese is **Traditional**
> (Taiwan/HK/SG). Seeded from the verses currently in the corpus.

> **⚑ Ladakhi (`lbj`) column — added 2026-09, entirely unratified.** Ladakhi is the
> seventh output language (`vault-annex.md` §4), written in **Tibetan script**. *Script
> history, so it isn't re-litigated:* first assumed Tibetan, then specified as Devanagari,
> then corrected back to **Tibetan script** by Evan — final. Every cell reads `⚑ TBD`: the
> column was added as structure, deliberately **not** filled in by guesswork.
>
> **How to fill it, and the trap to avoid.** Ladakhi shares its script *and* much of its
> written dharma vocabulary with Tibetan, so for many technical terms here (`སེམས`,
> `དྲན་པ`, `བྱམས་པ`, `ཚུལ་ཁྲིམས`…) the Ladakhi cell will legitimately end up **identical**
> to the `བོད་ཡིག` cell. **That does not license copying the Tibetan column across.**
> Ladakhi diverges from Central Tibetan in everyday vocabulary, in pronunciation-driven
> spelling, and in grammar — verb endings, case particles, kinship words. That everyday
> layer is exactly the register this vault ships in, since our renderings are modern and
> plain rather than liturgical, so it is also the layer a blind Tibetan-column copy would
> get wrong. The rows most likely to differ are the ordinary ones (`sahāya`,
> `nipaka`-style plain adjectives), not the doctrinal ones.
>
> **A native Ladakhi dharma reviewer fills this column;** an agent may propose a cell only
> when it can say either what differs from the Tibetan cell, or why matching it is correct
> here. A silent duplicate is not an answer.
>
> Until then, `lbj` renderings on day cards carry `escalate-native-review` and honest
> low-confidence flags, and **Days 1–75 have no `lbj` rendering at all** (backfill owed;
> Days 76–79 were the first).

---

## The friendship distinction (the reason this exists)

Two different words, two different renderings — don't conflate:

| Pāli term | Sense | en | 中文 (Hant) | བོད་ཡིག | हिन्दी | नेपाली | Монгол | ལ་དྭགས་སྐད · Ladakhi (lbj) | Use when |
|---|---|---|---|---|---|---|---|---|---|
| **sahāya** | a companion / friend (plain) | companion, friend | 同伴 / 善友 | གྲོགས / གྲོགས་པོ | साथी | साथी | нөхөр / хамтрагч | ⚑ TBD | the text says *sahāya* (e.g. **Dhp 328**) — a wise, good companion |
| **kalyāṇa-mitta** | spiritual / admirable friend | good friend, spiritual friend | 善知識 | དགེ་བའི་བཤེས་གཉེན | कल्याणमित्र | कल्याणमित्र | буянт нөхөр ⚑ | ⚑ TBD | the text says *kalyāṇa-mitta* (**Dhp 78**, **SN 45.2**) |

**Do not** render *sahāya* with `དགེ་བའི་བཤེས་གཉེན` / 善知識 — that imports a word the verse doesn't use. `གྲོགས(་པོ)` is warm/everyday and fits the modern register; a reviewer may prefer `གྲོགས` or `གྲོགས་བཟང` for a touch more dignity.

---

## Friendship & community

| Pāli | en | 中文 (Hant) | བོད་ཡིག | हिन्दी | नेपाली | Монгол | ལ་དྭགས་སྐད · Ladakhi (lbj) |
|---|---|---|---|---|---|---|---|
| nipaka (discerning/prudent) | wise, discerning | 明智 / 審慎 | གཟབ་པ / རྟོག་ལྡན ⚑ | समझदार / विवेकी | विवेकी / बुद्धिमान् | ухаалаг ⚑ | ⚑ TBD |
| sādhuvihārin (of good conduct) | good-hearted, of good conduct | 善行 / 良善 | སྤྱོད་པ་བཟང་བ ⚑ | सदाचारी / भला | असल / सदाचारी | сайн зан үйлтэй ⚑ | ⚑ TBD |
| saṅgha (community) | Sangha, community | 僧伽 / 僧團 | དགེ་འདུན | संघ | संघ | хувраг | ⚑ TBD |

> Note: `nipaka` has no single standard Tibetan/Mongolian term — `བློ་གྲོས་ལྡན` leans "intelligent," not "prudent/discerning." Flagged ⚑ for native choice.

## Mind, mind-states, emotions

| Pāli | en | 中文 (Hant) | བོད་ཡིག | हिन्दी | नेपाली | Монгол | ལ་དྭགས་སྐད · Ladakhi (lbj) |
|---|---|---|---|---|---|---|---|
| citta / mano (mind) | mind, heart | 心 | སེམས | मन / चित्त | मन | сэтгэл | ⚑ TBD |
| sati (mindfulness) | mindfulness | 正念 | དྲན་པ | स्मृति / सजगता | सजगता | ухаарал ⚑ (proposed; *ухамсар* = "consciousness," wrong — confirm vs дурсал / санах) | ⚑ TBD |
| ānāpānasati (mindfulness of breathing) | mindfulness of breathing | 出入息念 / 安那般那念 | དབུགས་འབྱུང་རྔུབ་ཀྱི་དྲན་པ | आनापान-स्मृति | आनापान-स्मृति | амьсгалын ухаарал ⚑ | ⚑ TBD |
| vera / avera (hatred / non-hatred) | hatred / non-hatred | 仇恨 / 無瞋 | ཞེ་སྡང / ཞེ་སྡང་མེད་པ | वैर / अवैर | घृणा / अवैर | үзэн ядалт / үзэн ядалтгүй | ⚑ TBD |
| kodha / akkodha (anger / non-anger) | anger / non-anger | 瞋 / 不瞋 | ཁྲོ་བ / མི་ཁྲོ་བ | क्रोध / अक्रोध | क्रोध / अक्रोध | уур / уургүй | ⚑ TBD |

## Path & core terms

| Pāli | en | 中文 (Hant) | བོད་ཡིག | हिन्दी | नेपाली | Монгол | ལ་དྭགས་སྐད · Ladakhi (lbj) |
|---|---|---|---|---|---|---|---|
| kusala (wholesome) | wholesome, skillful | 善 | དགེ་བ | कुशल | कुशल | буян / сайн үйл | ⚑ TBD |
| sāsana (teaching) | teaching, instruction | 教法 / 教導 | བསྟན་པ | शिक्षा / अनुशासन | शिक्षा | сургаал | ⚑ TBD |
| dāna (giving) | giving, generosity | 布施 | སྦྱིན་པ | दान | दान | өглөг | ⚑ TBD |
| sacca (truth) | truth | 真實 / 諦 | བདེན་པ | सत्य | सत्य | үнэн | ⚑ TBD |
| anicca (impermanence) | impermanence | 無常 | མི་རྟག་པ | अनित्यता | अनित्यता | хувирамтгай / мөнх бус | ⚑ TBD |
| anattā (not-self) | not-self | 無我 | བདག་མེད | अनात्म | अनात्म | би үгүй ⚑ | ⚑ TBD |
| dukkha (suffering) | suffering, unsatisfactoriness | 苦 | སྡུག་བསྔལ | दुःख | दुःख | зовлон | ⚑ TBD |
| khandha (aggregates) | the aggregates | 蘊 (五蘊) | ཕུང་པོ | स्कन्ध | स्कन्ध | чогц ⚑ | ⚑ TBD |
| nibbāna (liberation) | nibbāna, liberation | 涅槃 | མྱ་ངན་ལས་འདས་པ | निर्वाण | निर्वाण | нирвана | ⚑ TBD |
| puñña (merit) | merit, making merit | 福德 / 作福 | བསོད་ནམས | पुण्य | पुण्य | буян | ⚑ TBD |
| cetovimutti (heart's release) | heart's release, liberation of mind | 心解脫 | སེམས་རྣམ་གྲོལ / རྣམ་གྲོལ | चित्त-विमुक्ति | चित्त-विमुक्ति | сэтгэлийн чөлөөлөл ⚑ | ⚑ TBD |
| sīla (ethics) | ethics, moral conduct | 戒 / 戒律 | ཚུལ་ཁྲིམས | शील | शील | ёс журам / шагшаабад ⚑ | ⚑ TBD |
| samādhi (concentration) | concentration, meditative stillness | 定 / 三摩地 | ཏིང་ངེ་འཛིན | समाधि | समाधि | самади ⚑ | ⚑ TBD |
| paññā (wisdom) | wisdom | 慧 / 智慧 | ཤེས་རབ | प्रज्ञा | प्रज्ञा | билиг ухаан ⚑ | ⚑ TBD |
| khanti (patience) | patience, endurance | 忍 / 忍辱 | བཟོད་པ | क्षमा / सहनशीलता | धैर्य / सहनशीलता | тэвчээр ⚑ | ⚑ TBD |
| appamāda (diligence) | diligence, heedfulness | 不放逸 | བག་ཡོད | अप्रमाद | अप्रमाद | сэрэмж ⚑ | ⚑ TBD |
| viriya (effort, perseverance) | steady effort, perseverance | 精進 | བརྩོན་འགྲུས | प्रयत्न (not वीर्य — see note) | प्रयत्न | хичээл ⚑ | — (discontinued) |
| rakkhati / rakkhā (guarding, looking after) | look after (a person) · keep safe (protection) — **two senses, see note** | 照顧 (look after) / 守護 (keep safe) | ལྟ་རྟོག (look after) / སྲུང་བ (keep safe) | ध्यान रखना / रक्षा | ख्याल राख्नु / रक्षा | ⚑ TBD — see note | — (discontinued) |
| saṃvara (restraint, settled conduct) | steadier conduct (**not** "restraint" on a card) | 律儀 | སྤྱོད་པ་བརྟན་པོ (not སྡོམ་པ on a card) | आचरण | आचरण | ⚑ TBD | — (discontinued) |
| maṅgala (blessing, good fortune) | blessing | 吉祥 | བཀྲ་ཤིས | मंगल | मङ्गल | өлзий ⚑ | — (discontinued) |
| santuṭṭhi (contentment) | contentment | 知足 | ཆོག་ཤེས | संतोष | सन्तोष | ханамж ⚑ | ⚑ TBD |
| saddhā (faith, confidence) | faith, confidence | 信心 | དད་པ | श्रद्धा | श्रद्धा | итгэл ⚑ (confirm vs **сүсэг**, which may be the established Buddhist term for faith-as-devotion) | — (discontinued) |
| saraṇa / saraṇagamana (refuge) | refuge, going for refuge | 皈依 (皈依三寶) | སྐྱབས / སྐྱབས་སུ་འགྲོ་བ | शरण / शरण लेना | शरण / शरण लिनु | ⚑ TBD — **needs a real term**; "итгэлээ авах" was used as a placeholder on Day 86 and is weak | — (discontinued) |
| santi (peace) | peace | 安穩 / 寂靜 | ཞི་བདེ | शांति | शान्ति | ⚑ TBD — амар амгалан used on Days 87 and 92 for two *different* source words; needs disambiguating | — (discontinued) |
| kataññū-katavedī / 恩 (gratitude, kindness received) | grateful and repaying; a kindness received | 恩 / 報恩 | དྲིན / དྲིན་ལན་ལོག་འཇལ | उपकार / कृतज्ञता | गुन / कृतज्ञता | ⚑ TBD — сайныг хариулах used on Day 93, unverified as idiom | — (discontinued) |

> **`santi` row — added 2026-08-03 for Day 92** (`iti-86`). The vault now has three inner-peace cards (Days 24, 67, 92) and this term had never been locked. **Two cautions built into the row.** (1) **Do not conflate `santi` with `samādhi`.** Iti 86's verb is `samayaṁ` ("settled"), a different word from *samādhi*, and its noun is plain `santi`; the *samādhi* row's "concentration / meditative stillness" must **not** be imported into peace contexts. (2) **The Mongolian cell is the live problem:** *амар амгалан* was shipped on Day 87 for `བདེ་བ` and again on Day 92 for `santi` — two different source words given one Mongolian rendering. A reviewer should decide whether that is correct or whether the two need distinguishing. Left `⚑ TBD` rather than locking a rendering that may already be doing double duty.
>
> **`kataññū-katavedī` / `恩` row — added 2026-08-03 for Day 93** (`ea-repay-kindness`), the vault's **second** gratitude card (after Day 41) and the first time the term has had a row. **The English deliberately holds two senses in one row**, because the sources do: the Pali `kataññū-katavedī` names a *quality of person* ("grateful and repaying"), while the Chinese `恩` names *the kindness received* and `知反復` / `報恩` the act of returning it. A card may need either. **The trap to avoid, recorded because it is the easiest error on this material:** render the reciprocating sense without making it transactional — "repays kindness" is right, "repays a debt" is wrong and undoes the teaching. Tibetan and Mongolian cells both need native confirmation; the Tibetan `དྲིན་ལན་ལོག་འཇལ` may be too literary for a daily card.

> **`saddhā` row — added 2026-08-03 for Day 87** (`udv-faith-wealth`, Udānavarga 10 / Snp 1.10). **Two English options are deliberately kept**, and this row does not lock one: **"faith"** matches Sujato at `en-sutta-nipata-sujato.md#^snp1-10-7-1` and is the standard translation; **"confidence"** avoids the theistic connotation English "faith" can carry for a secular-leaning reader, and is the word the calendar already uses for this theme (Day 71's `confidence` tag). Day 87 ships "faith." A reviewer may switch it; if they do, switch the theme tag's English gloss with it for consistency, not the tag itself.
>
> **`saraṇa` row — added 2026-08-03, and it is the weakest row in this file.** Refuge has now appeared on Days 22, 60 and 86 and never had a termbase row, which is how Day 86's Mongolian line ended up with a placeholder that its own QA note flags as needing replacement. The Chinese, Tibetan, Hindi and Nepali cells are solid; **the Mongolian cell is empty on purpose** rather than guessed at. This is the first row a Mongolian reviewer should fill.

> **`viriya` row — added 2026-10 for Day 116** (`t389-steady-effort`, 佛遺教經 T389). **Two things this row exists to prevent.**
> (1) **Do not collapse `viriya` into `appamāda`.** They are different terms and the calendar now ships both within one week — Day 113 renders 不放逸 as **"diligence"**, Day 116 renders 精進 as **"steady effort."** Using one English word for both would erase the distinction three days apart. Keep: *appamāda* = diligence/heedfulness (not letting yourself drift), *viriya* = steady effort (sustained application).
> (2) **The Hindi cell deliberately says प्रयत्न, not वीर्य.** वीर्य is the etymologically correct Sanskrit cognate and is what a scholarly glossary would give, but in modern Hindi it reads primarily as *semen* and must never appear on a card. Nepali follows Hindi for the same reason. The Mongolian cell is ⚑ unratified — candidates a reviewer should weigh: хичээл, хичээл зүтгэл, шамдал. Tibetan `བརྩོན་འགྲུས` is the *pāramitā* name and is solid; confirm only that it is not too formal for a daily card.
>
> **`maṅgala` row — added 2026-10 for Day 114** (`snp-2-4-unshaken`, Snp 2.4 Maṅgalasutta). Overdue: the calendar has shipped **three** blessing cards (Day 104 Toh 292, Day 109 Toh 95, and now Day 114) and this term had never been locked. English is **"blessing"** rather than "auspiciousness" (which reads like a fortune cookie) or "good fortune" (which reads like luck) — the card genre is benediction, something conferred. ⚑ **Two cells need a native call.** (a) Mongolian **өлзий**: confirm it is the established Buddhist term rather than a folk-auspiciousness word, and whether the fuller **өлзий хутаг** is what a card should carry. (b) Tibetan **བཀྲ་ཤིས**: confirm it reads as a conferred blessing here and is not heard as the conventional greeting; also settle `བཀྲ་ཤིས་ཀྱི་མཆོག` vs `བཀྲ་ཤིས་མཆོག` for the superlative `maṅgalamuttamaṁ`.
>
> **⚑ Open cross-language inconsistency found while building Day 115** (`da-2-shelter`), left for a native reviewer rather than silently harmonised: for Chinese `護` (shelter/protection) the **Hindi** line ships **आश्रय** while the **Nepali** line ships **शरण** — and शरण is this file's `saraṇa` row, which the card was deliberately trying *not* to invoke (it would import the going-for-refuge formula). The two lines should agree. Whichever way a reviewer settles it, the `saraṇa` row's scope needs a sentence saying whether it covers plain shelter or only formal refuge. Related: the `saraṇa` row's **Mongolian cell is still empty** — flagged since Day 86 — and Day 115 ships a fresh coinage, `хоргодох газар`, precisely because there is nothing to use.

> **`rakkhati` / `rakkhā` row — added 2026-10 for Days 117 and 119**, and it is the first row in this file to deliberately carry **two renderings for one Pali term**. The reason: the same verb family lands in two different registers three days apart. **Day 117** (SN 47.19, *"Looking after yourself, you look after others"*) needs the *caring* sense — 照顧 / `ལྟ་རྟོག` / ध्यान रखना. **Day 119** (SĀ 1222, *"Guarding what is within you is what truly keeps you safe"*) needs the *protective* sense — 守護 / `སྲུང་བ` / रक्षा. Using one word for both would flatten a real distinction; using them inconsistently would look like drift. **A reviewer should confirm the split is right, or collapse it deliberately — not silently.**
> ⚑ **The Mongolian cell is the live problem and is left empty on purpose.** Day 117 ships `хамгаалах` and its own QA note flags that word as leaning too *defensive* for a card about caring; Day 119 ships `сахих`. Those two may well be the wrong way round. A Mongolian reviewer should settle the pair and fill this cell, not patch one line. Related: the `saraṇa` row's Mongolian cell is **also** still empty (flagged since Day 86), and Day 115 shipped a fresh coinage, `хоргодох газар`, for want of one. **Guarding, sheltering and refuge are now three adjacent Mongolian gaps and are worth settling together.**
>
> **`saṃvara` row — added 2026-10 for Day 118** (`sa-345-owning-a-fault`, 律儀成就). The English cell is written as an instruction rather than a gloss because the obvious translations both fail on a card: **"restraint" reads as self-denial** to a lay reader, and **"the discipline" reads monastic**. Day 118 ships "**becomes steadier**," and the Tibetan cell likewise avoids the technical `སྡོམ་པ` in favour of `སྤྱོད་པ་བརྟན་པོ`. Keep the term distinct from `sīla` / 戒 / `ཚུལ་ཁྲིམས` above: *sīla* is the ethics one undertakes, *saṃvara* is the settled conduct that results.

## Mahāyāna & wisdom terms

| Term | en | 中文 (Hant) | བོད་ཡིག | हिन्दी | नेपाली | Монгол | ལ་དྭགས་སྐད · Ladakhi (lbj) |
|---|---|---|---|---|---|---|---|
| bodhicitta (byang chub sems) | the awakening mind (never "Great Vehicle mind") | 菩提心 | བྱང་ཆུབ་སེམས | बोधिचित्त | बोधिचित्त | бодь сэтгэл ⚑ | ⚑ TBD |
| śūnyatā (stong pa nyid) | emptiness, empty nature | 空性 | སྟོང་པ་ཉིད | शून्यता | शून्यता | хоосон чанар ⚑ | ⚑ TBD |

> **`anukampā` / `anuddayā` row — added 2026-10 for Day 123** (`sn10-2-care-does-not-bind`, SN 10.2). **This row exists to stop a specific silent error.** SN 10.2's stanza is about `anukampā` (fellow-feeling, being moved by another's condition) and `anuddayā` (tenderness, solicitude) — **not** about `karuṇā`. Sujato renders the pair "compassion and empathy"; using "compassion" on the card would silently claim the `karuṇā` row above for a verse that does not use that word, and "empathy" is a modern psychological term that reads clinically. English and Chinese therefore ship the plain pair — **kindness and care** / 善意與關懷 — and the Chinese deliberately avoids 慈悲.
> ⚑ **Three cells are `TBD` because Day 123 had to borrow, and a reviewer should see exactly what was borrowed.** The **Tibetan** line ships `བྱམས་སེམས་དང་གཅེས་སེམས`, and `བྱམས་སེམས` **is the *mettā* row's term** (`བྱམས་པ`) — used only because Tibetan has no ready plain word here. Candidates a reviewer should weigh: `སྙིང་བརྩེ`, `བརྩེ་སེམས`. The **Nepali** line ships सद्भाव / माया, and ⚑ माया reads as "love/affection", which is looser than tenderness-as-care and risks the affection misreading the vault has flagged before (Dhp 212). The **Mongolian** line ships `сайхан санаа` / `халамж`, and ⚑ `халамж` is also a candidate for the `rakkhati` row's caring sense on Day 117 — the two must not end up meaning different things in the same calendar week. **Settle all three cells together.**

## The four noble truths (catu-sacca)

| Term | en | 中文 (Hant) | བོད་ཡིག | हिन्दी | नेपाली | Монгол | ལ་དྭགས་སྐད · Ladakhi (lbj) |
|---|---|---|---|---|---|---|---|
| samudaya (origin) | origin (of suffering) | 集 | ཀུན་འབྱུང་ | समुदय | समुदय | үүсэл ⚑ | ⚑ TBD |
| nirodha (cessation) | cessation | 滅 | འགོག་པ | निरोध | निरोध | зогсолт ⚑ | ⚑ TBD |
| magga (path) | path | 道 | ལམ | मार्ग | मार्ग | зам | ⚑ TBD |

## Ethics — generosity terms

| Term | en | 中文 (Hant) | བོད་ཡིག | हिन्दी | नेपाली | Монгол | ལ་དྭགས་སྐད · Ladakhi (lbj) |
|---|---|---|---|---|---|---|---|
| adinnādāna / a-adinnādāna (taking what is not given / abstaining) | taking what isn't given / giving it up | 不與取 | མ་བྱིན་ལེན | अदत्तादान | अदत्तादान | өгөөгүйг авах ⚑ | ⚑ TBD |
| tyāga / `གཏོང་བ` (giving, liberality — **not** the *dāna* perfection) | giving | 布施 ⚑ | གཞན་ལ་སྟེར་བ ⚑ | देना | दिनु | өглөг ⚑ | — (discontinued) |
| dgra / verī (enemy, adversary) | enemies ⚑ | 敵人 ⚑ | དགྲ་བོ ⚑ | शत्रु ⚑ | शत्रु ⚑ | дайсан ⚑ | — (discontinued) |

> **`tyāga` row — added 2026-08-26 for Day 122** (`toh329-giving-makes-friends`). It exists to stop *tyāga* silently collapsing into the **`dāna` row above**. 84000's note [n11] on Toh 329 records that `གཏོང་བ` (*tyāga*: giving up, sacrifice, liberality) is deliberately distinct from `སྦྱིན་པ` (*dāna*, the bodhisattva perfection). ⚑ **The Chinese and Mongolian cells are flagged because the card ships the *dāna* words anyway** — 布施 and `өглөг` — on the grounds that they are what a cultural Buddhist reader actually knows and the alternatives (慷慨付出 / 樂於施予) read stiff on a card. That is a knowing trade, not an oversight; a reviewer may take the other side. The **Tibetan cell deliberately does not use `སྦྱིན་པ`**, since that is the one language where the substitution would contradict the source's own word.
>
> **`dgra` row — added 2026-08-26 for Day 122.** ⚑ **Every cell is flagged, and the open question is register, not accuracy.** "Enemy" and its equivalents are all faithful to `དགྲ`, but the word is large for a reader whose actual situation is a difficult colleague or a relative who is not speaking to them. The alternative on file across all six languages is a periphrasis in the shape of "those who are set against you," which is relatable but wordier and slightly editorialising. Day 122 ships the plain word in every language so the choice is consistent and can be overturned in one pass. **Related but distinct: Day 103** (AN 5.161) is about someone you *resent*, which is a feeling of yours, not a standing adversary — do not let the two rows' vocabulary merge.


## Brahmavihāras (the four; the "grow" themes)

| Pāli | en | 中文 (Hant) | བོད་ཡིག | हिन्दी | नेपाली | Монгол | ལ་དྭགས་སྐད · Ladakhi (lbj) |
|---|---|---|---|---|---|---|---|
| mettā | loving-kindness | 慈 / 慈愛 | བྱམས་པ | मैत्री | मैत्री | энэрэл хайр ⚑ | ⚑ TBD |
| karuṇā | compassion | 悲 / 慈悲 | སྙིང་རྗེ | करुणा | करुणा | нигүүлсэл | ⚑ TBD |
| anukampā / anuddayā (sympathy, tenderness) | kindness and care (**never "compassion"** — that is karuṇā) | 善意 / 關懷 | ⚑ TBD — see note | भलमनसाहत / परवाह | ⚑ TBD — see note | ⚑ TBD — see note | — (discontinued) |
| muditā | sympathetic joy | 喜 / 隨喜 | དགའ་བ | मुदिता | मुदिता | баясал ⚑ | ⚑ TBD |
| upekkhā | equanimity | 捨 / 平等心 | བཏང་སྙོམས | उपेक्षा | उपेक्षा | тэгш сэтгэл ⚑ | ⚑ TBD |

---

## How to use it

- **Building a rail / rendering** (`verse-rail`): when a key term appears, use its row here. If the verse needs a term not yet listed, add a row (propose renderings, mark ⚑ where unsure) rather than inventing per-verse.
- **QA** (`translation-qa`): the terminology check compares each rendering's key terms against this table; mismatches are flagged.
- **Adding/ratifying:** a native reviewer confirms ⚑ rows for their language; once confirmed, drop the ⚑ — that rendering is then locked for consistency. The whole **Ladakhi (`lbj`)** column awaits a first pass — see the Ladakhi note at the top, and don't fill it by copying the Tibetan column. Keep one sense per row; if a term has two senses (e.g. *sahāya* vs *kalyāṇa-mitta*), give each its own row.
- **Sourcing:** prefer renderings attested in the authoritative translations we hold (Sujato, 84000, Patton) and standard Buddhist dictionaries over fresh coinage.
- **Standard term, not paraphrase:** always use the established dharma-term rendering, never an everyday word — *mettā* = loving-kindness / मैत्री, **not** "love"; *puñña* = merit; aggregates = form/feeling/perception/**volition/consciousness**. Paraphrase is the most common QA miss.
- **Ecumenical (WeBuddhist is for all Buddhists):** render Mahāyāna terms inclusively — **bodhicitta = "the awakening mind," never "Great Vehicle mind"** (大乘 / *theg chen* reads sectarian). *Bodhisattva* is fine. Keep Mahāyāna content; drop sectarian framing.
