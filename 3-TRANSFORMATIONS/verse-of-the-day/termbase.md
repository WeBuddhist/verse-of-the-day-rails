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

## Mahāyāna & wisdom terms

| Term | en | 中文 (Hant) | བོད་ཡིག | हिन्दी | नेपाली | Монгол | ལ་དྭགས་སྐད · Ladakhi (lbj) |
|---|---|---|---|---|---|---|---|
| bodhicitta (byang chub sems) | the awakening mind (never "Great Vehicle mind") | 菩提心 | བྱང་ཆུབ་སེམས | बोधिचित्त | बोधिचित्त | бодь сэтгэл ⚑ | ⚑ TBD |
| śūnyatā (stong pa nyid) | emptiness, empty nature | 空性 | སྟོང་པ་ཉིད | शून्यता | शून्यता | хоосон чанар ⚑ | ⚑ TBD |

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

## Brahmavihāras (the four; the "grow" themes)

| Pāli | en | 中文 (Hant) | བོད་ཡིག | हिन्दी | नेपाली | Монгол | ལ་དྭགས་སྐད · Ladakhi (lbj) |
|---|---|---|---|---|---|---|---|
| mettā | loving-kindness | 慈 / 慈愛 | བྱམས་པ | मैत्री | मैत्री | энэрэл хайр ⚑ | ⚑ TBD |
| karuṇā | compassion | 悲 / 慈悲 | སྙིང་རྗེ | करुणा | करुणा | нигүүлсэл | ⚑ TBD |
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
