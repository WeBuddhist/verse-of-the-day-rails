# Screening brief — Verse of the Day, Days 129–133 candidate hunt

You are finding candidate verses for WeBuddhist's Verse of the Day.
Vault root on this machine: `$HOME/mnt/verse-of-the-day-rails/`
Sources: `1-SOURCES/Text/` (ground truth) and `1-SOURCES/Translations/` (reference only).
Already-shipped digest (day | source_ref | theme): `0-INBOX/day129-133/shipped-digest.txt`

## HARD GATES — a candidate failing any of these is dead, do not report it
1. **Buddhavacana spoken BY the Buddha**, not about him. No disciples, gods (Śakra, Brahmā, devas),
   kings, brahmins, bodhisattvas, Mañjuśrī, past buddhas, or narrator voice. VERIFY the speaker by
   reading the surrounding frame in the source, not by assuming.
2. **Verbatim and whole.** A complete verse/stanza, or ONE self-contained sentence, quoted in full.
   Never stitch, summarise or gist. Copy the exact characters from `1-SOURCES/Text/` — never from memory.
   Report the exact `^block-id` anchor and confirm the anchor holds the words you quote (off-by-one
   block errors have burned this vault before).
3. **Fits ~125 characters in English** (126 is fine; 140+ is not). Give the count.
4. **In scope:** discourse/verse only. No tantra, no Vinaya, no scholastic literature.
5. **Not already used.** Check the shipped digest for the same source_ref AND the same subject.

## TASTE SCREENS — these are where candidates actually die. All are curator rulings.
- **A. No first-person Buddha.** If the shipped line has the Buddha speaking as "I"/"me"/"my", it is out.
  Not rescuable by rewording. (Killed SĀ 963.)
- **B. The word "Buddha" must not appear in the card text.** Also avoid Dharma/Sangha/nirvāṇa as the
  card's subject. The card is for the reader's own life, not devotional.
- **C. Dharma, not general life advice.** Test: could this sentence sit in a secular self-help book with
  nothing lost? If yes, it is not a card. (Killed AN 2.33 on parenting.)
- **D. No culture-specific deity or Vedic frame.** Brahmā, Śakra, Māra etc. as the verse's load-bearing
  image fails — the audience spans East Asian and Tibetan practitioners. (Killed Toh 315.)
- **E. Not bleak. Not sober.** A verse whose opening clause is fear, death, violence or universal
  suffering fails even if it resolves later. Screen the OPENING CLAUSE, not just the overall logic.
  (Killed Dhp 129.) Do not propose a sober card.
- **F. No "withdraw affection" surface reading.** A casual reader must not hear "do not love anyone."
  (Killed Dhp 212 / Udānavarga 5.)
- **G. Concrete and self-applying.** No chains of abstract negations ("the unborn, the unmade"),
  no technical jargon, no glossary needed. A simile only works if the quote names its own referent.
  Third-person description of what a wise one is like fails — the reader should not have to make an
  inference step to reach themselves.
- **H. Not a proclamation of attainment.** "My births are ended, the task is done" reports a finished
  state instead of pointing a way. Out.
- **I. Not an over-exposed greatest hit.** Reach for under-circulated material.
- **J. Verify boundary and grammatical person BEFORE reporting.** Read the source AROUND the line, not
  the line alone. Confirm it starts a stanza/sentence rather than sitting mid-run, and confirm the
  grammatical subject is not carried from an earlier line. This check is the single most common
  late-stage failure; resolve it now, not at build time.

## CARD TYPES — label every candidate with one
1 teaching/instruction · 2 observation/how-things-work · 3 encouragement/permission · 4 consolation ·
5 reframe/paradox · 6 simile/image · 7 blessing (Buddha wishes the reader well) · 8 aspiration (a wish
the reader makes).
Recent run: 122 teaching · 123 blessing · 124 reframe · 125 teaching · 126 reframe · 127 encouragement ·
128 aspiration. **Day 129 must not be an aspiration card and must not be about generosity or giving.**
Variety matters more than volume — eight candidates in two types will be rejected.

## OUTPUT FORMAT — one block per candidate, and report AT MOST your 6 best
```
### <short slug>
- source_ref: <e.g. SĀ 379 / 中阿含經 卷12 / MN 21>
- file + anchor: 1-SOURCES/Text/<file>.md#^<id>
- VERBATIM (copy exactly from source):
- speaker verified: <how you know the Buddha is speaking — quote the frame line>
- boundary check: <why this is a whole stanza/sentence, not a mid-run fragment>
- person check: <no first-person Buddha; grammatical subject is X>
- proposed English (~125 chars): "<...>"
- char count: <n>
- theme: <tag> | card type: <1-8> | speaks_to: <felt states>
- dedupe: <nearest shipped card + why this is different ground>
- honest weaknesses: <state every doubt; a flagged candidate is still worth offering, a hidden flaw is not>
```
Report nothing rather than padding. A candidate you could not verify verbatim does not get reported.
