# Occasions — verses for Buddhist holidays

A calendar-aware layer over verse-of-the-day. On a Buddhist holiday, the daily
verse is chosen **for the occasion** (overriding the normal rotation), tied to
the event in the Buddha's life it commemorates.

WeBuddhist is **for all Buddhists**, so the calendar spans Theravāda, East
Asian (Chinese/Japanese/Korean), and Tibetan observances. Many of these mark the
*same* three events (birth, awakening, parinibbāna) on dates that differ by
tradition — that shared core is a feature, not a clash.

> **Dates are lunar and vary by tradition, country, and year.** Don't hardcode
> Gregorian dates here — the app should resolve each observance per the user's
> tradition/region via a calendar service. This doc fixes the *events, themes,
> and verses*; the runtime fixes the dates.

## The major observances

| Occasion | Tradition(s) | Lunar timing | Event in the Buddha's life | Verse themes |
|---|---|---|---|---|
| **Vesak / Visākha Pūjā** | Theravāda | full moon, ~May | birth, awakening **and** parinibbāna (all three) | awakening; impermanence; the whole arc of a Buddha's life |
| **Saga Dawa (Düchen)** | Tibetan | 15th, 4th Tib. month (~May–Jun) | birth, awakening, parinibbāna | same as Vesak; merit/generosity |
| **Buddha's Birthday (浴佛 / Bathing the Buddha)** | East Asian | 8th, 4th lunar month (Apr 8 Japan) | birth | aspiration, the rarity of a Buddha's arising |
| **Bodhi Day (成道會 / Rōhatsu)** | East Asian | 8th, 12th lunar month (Dec 8 Japan) | **awakening** | the house-builder verses; victory over craving |
| **Māgha Pūjā (Saṅgha Day)** | Theravāda | full moon, ~Feb–Mar | the 1,250 arahants gather; the **Ovāda-pāṭimokkha** | "avoid evil, do good, purify the mind" (**Dhp 183–185**) |
| **Chötrul Düchen** | Tibetan | 15th, 1st Tib. month | the Buddha's display of miracles | faith, the marvellous |
| **Āsāḷha Pūjā / Dhamma Day** | Theravāda | full moon, ~Jul | the **first sermon** (Dhammacakkappavattana) | Four Noble Truths; the middle way; turning the wheel |
| **Chökhor Düchen** | Tibetan | 4th, 6th Tib. month | first turning of the wheel (first sermon) | same as Dhamma Day |
| **Nirvana Day (涅槃會)** | East Asian | 15th, 2nd lunar month (Feb 15 Japan) | **parinibbāna** | impermanence; the Buddha's last words |
| **Lhabab Düchen** | Tibetan | 22nd, 9th Tib. month | descent from Tāvatiṃsa (teaching his mother) | gratitude; the gift of the teaching |
| **Vassa (Rains Retreat) / Kathina** | Theravāda | ~Jul–Oct | the retreat the Buddha established | effort, diligence, generosity (Kathina) |
| **Uposatha** (observance days) | all | full & new moon (bi-weekly) | recurring practice day | precepts, mindfulness, renewal |

## Signature verses per occasion (acquire where missing)

The corpus should guarantee a strong verse for each major occasion. Current
state:

- **Māgha Pūjā** → **Dhp 183** (the Ovāda-pāṭimokkha) — ✅ rail exists. (Add 184–185 to complete the set.)
- **Bodhi Day / awakening** → **Dhp 153–154**, the "house-builder" verses (the Buddha's words at awakening: *gahakāraka diṭṭho'si…*) — ⬜ acquire + build rail.
- **Nirvana Day / parinibbāna** → the Buddha's last words, *"vayadhammā saṅkhārā, appamādena sampādetha"* (DN 16; "conditioned things decay — strive with diligence") — ⬜ acquire (DN not verse-indexed yet) + rail.
- **Dhamma Day / first sermon** → the Dhammacakkappavattana (SN 56.11) — ⬜ pick a core line + rail.
- **Vesak / Saga Dawa** → an awakening or whole-life verse (e.g. Dhp 153–154, or an impermanence verse for the parinibbāna aspect).

## How it's wired in

- Each rail can carry an `occasions:` tag:
  ```yaml
  occasions: [magha-puja]      # observances this verse is apt for
  ```
- On an observance date (resolved at runtime per the user's tradition), the
  scheduler selects from verses tagged for that occasion, overriding the normal
  rotation (`selection-criteria.md` §3). Non-holiday days follow the usual rules.
- Tradition-awareness: where an occasion is tradition-specific, the app can match
  the user's tradition; the shared events (Vesak/Saga Dawa/Bodhi/Nirvana) can be
  surfaced to everyone.

## Wellbeing / tone note

Holiday verses follow the same care rules — e.g. on Nirvana Day, the parinibbāna
is framed as the Buddha's serene passing and the call to diligence, not as a
mournful or fearful death. Keep it dignified and steadying.
