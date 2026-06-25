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

---

## The friendship distinction (the reason this exists)

Two different words, two different renderings — don't conflate:

| Pāli term | Sense | en | 中文 (Hant) | བོད་ཡིག | हिन्दी | नेपाली | Монгол | Use when |
|---|---|---|---|---|---|---|---|---|
| **sahāya** | a companion / friend (plain) | companion, friend | 同伴 / 善友 | གྲོགས / གྲོགས་པོ | साथी | साथी | нөхөр / хамтрагч | the text says *sahāya* (e.g. **Dhp 328**) — a wise, good companion |
| **kalyāṇa-mitta** | spiritual / admirable friend | good friend, spiritual friend | 善知識 | དགེ་བའི་བཤེས་གཉེན | कल्याणमित्र | कल्याणमित्र | буянт нөхөр ⚑ | the text says *kalyāṇa-mitta* (**Dhp 78**, **SN 45.2**) |

**Do not** render *sahāya* with `དགེ་བའི་བཤེས་གཉེན` / 善知識 — that imports a word the verse doesn't use. `གྲོགས(་པོ)` is warm/everyday and fits the modern register; a reviewer may prefer `གྲོགས` or `གྲོགས་བཟང` for a touch more dignity.

---

## Friendship & community

| Pāli | en | 中文 (Hant) | བོད་ཡིག | हिन्दी | नेपाली | Монгол |
|---|---|---|---|---|---|---|
| nipaka (discerning/prudent) | wise, discerning | 明智 / 審慎 | གཟབ་པ / རྟོག་ལྡན ⚑ | समझदार / विवेकी | विवेकी / बुद्धिमान् | ухаалаг ⚑ |
| sādhuvihārin (of good conduct) | good-hearted, of good conduct | 善行 / 良善 | སྤྱོད་པ་བཟང་བ ⚑ | सदाचारी / भला | असल / सदाचारी | сайн зан үйлтэй ⚑ |
| saṅgha (community) | Sangha, community | 僧伽 / 僧團 | དགེ་འདུན | संघ | संघ | хувраг |

> Note: `nipaka` has no single standard Tibetan/Mongolian term — `བློ་གྲོས་ལྡན` leans "intelligent," not "prudent/discerning." Flagged ⚑ for native choice.

## Mind, mind-states, emotions

| Pāli | en | 中文 (Hant) | བོད་ཡིག | हिन्दी | नेपाली | Монгол |
|---|---|---|---|---|---|---|
| citta / mano (mind) | mind, heart | 心 | སེམས | मन / चित्त | मन | сэтгэл |
| sati (mindfulness) | mindfulness | 正念 | དྲན་པ | स्मृति / सजगता | सजगता | ⚑ (sati term to confirm — *ухамсар* = "consciousness," likely wrong) |
| vera / avera (hatred / non-hatred) | hatred / non-hatred | 仇恨 / 無瞋 | ཞེ་སྡང / ཞེ་སྡང་མེད་པ | वैर / अवैर | घृणा / अवैर | үзэн ядалт / үзэн ядалтгүй |
| kodha / akkodha (anger / non-anger) | anger / non-anger | 瞋 / 不瞋 | ཁྲོ་བ / མི་ཁྲོ་བ | क्रोध / अक्रोध | क्रोध / अक्रोध | уур / уургүй |

## Path & core terms

| Pāli | en | 中文 (Hant) | བོད་ཡིག | हिन्दी | नेपाली | Монгол |
|---|---|---|---|---|---|---|
| kusala (wholesome) | wholesome, skillful | 善 | དགེ་བ | कुशल | कुशल | буян / сайн үйл |
| sāsana (teaching) | teaching, instruction | 教法 / 教導 | བསྟན་པ | शिक्षा / अनुशासन | शिक्षा | сургаал |
| dāna (giving) | giving, generosity | 布施 | སྦྱིན་པ | दान | दान | өглөг |
| sacca (truth) | truth | 真實 / 諦 | བདེན་པ | सत्य | सत्य | үнэн |
| anicca (impermanence) | impermanence | 無常 | མི་རྟག་པ | अनित्यता | अनित्यता | хувирамтгай / мөнх бус |
| anattā (not-self) | not-self | 無我 | བདག་མེད | अनात्म | अनात्म | би үгүй ⚑ |
| dukkha (suffering) | suffering, unsatisfactoriness | 苦 | སྡུག་བསྔལ | दुःख | दुःख | зовлон |
| khandha (aggregates) | the aggregates | 蘊 (五蘊) | ཕུང་པོ | स्कन्ध | स्कन्ध | чогц ⚑ |
| nibbāna (liberation) | nibbāna, liberation | 涅槃 | མྱ་ངན་ལས་འདས་པ | निर्वाण | निर्वाण | нирвана |

## Brahmavihāras (the four; the "grow" themes)

| Pāli | en | 中文 (Hant) | བོད་ཡིག | हिन्दी | नेपाली | Монгол |
|---|---|---|---|---|---|---|
| mettā | loving-kindness | 慈 / 慈愛 | བྱམས་པ | मैत्री | मैत्री | энэрэл хайр ⚑ |
| karuṇā | compassion | 悲 / 慈悲 | སྙིང་རྗེ | करुणा | करुणा | нигүүлсэл |
| muditā | sympathetic joy | 喜 / 隨喜 | དགའ་བ | मुदिता | मुदिता | баясал ⚑ |
| upekkhā | equanimity | 捨 / 平等心 | བཏང་སྙོམས | उपेक्षा | उपेक्षा | тэгш сэтгэл ⚑ |

---

## How to use it

- **Building a rail / rendering** (`verse-rail`): when a key term appears, use its row here. If the verse needs a term not yet listed, add a row (propose renderings, mark ⚑ where unsure) rather than inventing per-verse.
- **QA** (`translation-qa`): the terminology check compares each rendering's key terms against this table; mismatches are flagged.
- **Adding/ratifying:** a native reviewer confirms ⚑ rows for their language; once confirmed, drop the ⚑ — that rendering is then locked for consistency. Keep one sense per row; if a term has two senses (e.g. *sahāya* vs *kalyāṇa-mitta*), give each its own row.
- **Sourcing:** prefer renderings attested in the authoritative translations we hold (Sujato, 84000, Patton) and standard Buddhist dictionaries over fresh coinage.
