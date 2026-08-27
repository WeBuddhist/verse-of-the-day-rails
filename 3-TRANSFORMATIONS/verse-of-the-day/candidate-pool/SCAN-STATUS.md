# Candidate-tagging scan status — open work

Tracks which source files have had a real `candidate-tagging` pass (sequential read + selection against `1-SOURCES/Text/`), as distinct from files that only have candidates backfilled from already-built rails. Update this when a scan completes or when new source text is imported. See `SKILLS-CATALOG.md` → `candidate-tagging` for the process itself.

## Done — full sequential scan complete

- **Chinese canon** — all four Āgamas (Dīrgha, Madhyama, Saṁyukta, Ekottarika) plus the Chinese Mahāyāna sūtras registered in `vault-annex.md`. See `candidate-pool/chinese.md`.
- **Pali verse collections** — Dhammapada (423 verses), Sutta Nipāta (~72 suttas, 5 vagga), Udāna (80 suttas), Itivuttaka (112 suttas). See `candidate-pool/pali.md`.
- **Tibetan Udānavarga** (Toh 326, 33 chapters) — the first genuine scan of Tibetan source text, not a rail-backfill. See `candidate-pool/tibetan.md`.
- **Tibetan Kangyur, three individual sūtras** — Toh 59 (Sūtra on the Array of Qualities in Mañjuśrī's Pure Realm), Toh 95 (Lalitavistara Sūtra), Toh 231 (Ratnamegha/Jewel Cloud Sūtra) — scanned using leads from Lotsawa House's "Words of the Buddha" quotations page (see `kangyur-scan-leads.md`). One of the three original leads (a Toh 95 verse on saṃsāra) was checked and rejected — it's spoken by cymbals/an omen in context, not the Buddha, despite Lotsawa House listing it. See `candidate-pool/tibetan.md`.

## Not yet done — the big remaining lift

- **Pali prose Nikāyas** — Dīgha Nikāya (34 suttas, ~32,800 lines), Majjhima Nikāya (152 suttas, ~54,100 lines), Saṁyutta Nikāya (1,819 suttas, ~79,800 lines), Aṅguttara Nikāya (1,408 suttas, ~78,200 lines). Combined ≈ 245,000 lines — roughly **17× everything scanned in the pass above**. A full sequential read-every-line scan at that scale isn't practical in one sitting; when this is picked up, consider Rule 11 of the `candidate-tagging` skill (sample first, then decide scan strategy) and likely a sampling or targeted approach (e.g. well-known/oft-cited suttas first) rather than line-by-line reading of all four texts.
- **Tibetan Kangyur sūtras** — roughly 226 individual `bo-toh<N>.md` files remain beyond the Udānavarga, Toh 59/95/231 (now scanned, above), and the handful already covered via rail-backfill or the earlier 3-file live test (Toh 143, 149, 150). Each file is a separate sūtra of varying length; this also hasn't had a real scan pass. See [`kangyur-scan-leads.md`](kangyur-scan-leads.md) for a prioritized shortlist (sourced from Lotsawa House's "Words of the Buddha" quotations page) and its note on five Toh numbers (12, 13, 16, 53, 60) that 84000 hasn't translated yet, so they can't be imported with a paired reference translation the way this vault's pipeline expects.

Existing rails already drawn from a few of these files (see `2-RAILS/Verses/` — e.g. mn19-thought, sn1-1, an2-32-gratitude) don't count as a scan of the source text itself; they're one-off selections made without a bulk pre-tagging pass.

**Why this matters:** the Pali/Tibetan candidate pools are strong for the verse collections but still shallow on the prose Nikāyas and the bulk of the Kangyur relative to how thoroughly the Chinese canon has been covered. `verse-selection` can keep drawing on what's here in the meantime — this file is a reminder to eventually close the gap, not a blocker.

## When picking this back up

1. Re-read `4-SYSTEM/Skills/candidate-tagging/SKILL.md` in full.
2. Check `log.md`'s running balance and `theme-checklist.md`'s open gaps first, so the scan is looking for something.
3. Given the scale, parallel sub-agents per source file (or per chunk of a large file) are more practical than one sequential pass — see this session's approach for the verse collections as a template (each sub-agent reads its assigned range, returns candidates in the standard format, one person compiles into the pool file to avoid write conflicts).
4. Update this file's "Done" / "Not yet done" lists when a chunk completes.

---

## Update 2026-10 — the Kangyur sūtras have now had a real scan (partial but substantial)

This file has listed the ~229 individual Tibetan Kangyur sūtra files as **unscanned** since the vault began. That is no longer accurate. State as of 2026-10:

- **Sub-12 kB band: EXHAUSTED.** Every file read. The productive ones are already claimed (Toh 300 → Day 80, Toh 327 → Day 82, Toh 249 → Day 86, Toh 329 → Day 97, Toh 183 → Day 100, Toh 292 → Day 104, Toh 95 → Day 109, Toh 182 → Day 111). The last three unexamined files (Toh 250, 309, 27) were read and all fail; recorded in `rejected.md`.
- **12–27 kB band: SCANNED IN FULL (46 files).** Yield: **two** candidates — Toh 269 (fearlessness) and Toh 259 (the golden rule). Both banked in `candidate-pool/tibetan.md`. Every file that yielded nothing is listed in `rejected.md`.
- **27–45 kB band: FILTER-SCREENED, NOT SCANNED (21 files).** Screened for second-person address, blessing/aspiration optatives, warm-keyword verses, simile-plus-"you", and imperatives — not read sequentially. Yield: **one** candidate, Toh 219 (the jewel-in-every-hand aspiration). Treat these as partially covered: a sequential read could still turn something up, but the shapes this card format wants have been checked.
- **Above 45 kB: NOT TOUCHED.** The largest Kangyur files remain genuinely unscanned.

**⚑ The finding that should govern the next pass, and it matters more than the coverage numbers.** Three candidates from 67 files is about **one per twenty**, and the limiting factor is **not** length, licensing, or buddhavacana — it is the *self-applying* and *warmth* screens. Kangyur Mahāyāna prose is overwhelmingly third-person doctrinal exposition, name-recitation merit, or framed narrative; its best lines sit inside scenes. It reliably speaks *to* the reader warmly in only three shapes:
1. **protection / fearlessness sūtras**,
2. **Buddha-prescribed formulas the reader says or does**,
3. **the *anumodanā* blessing clusters** (Toh 292/312/313/95 — already mined).

**So the next Tibetan pass should grep those three shapes directly across all 229 `bo-toh*.md` files rather than continuing file-by-file by size.** Search terms that worked: `འཇིགས་པ` / `མི་འཇིགས` / `སྐྲག` (fear); `ཁྱོད` / `ཁྱེད་ཅག` plus an imperative (`བྱོས` / `གྱིས` / `མཛོད` / `ཤིག`); `ང་སྨྲའོ` (first-person Buddha speech); `ཤོག` / `གྱུར་ཅིག` / `བདེ་ལེགས` / `བཀྲ་ཤིས` (optatives — but check the speaker every time, since most are spoken by bodhisattvas, gods, kings, or the reader and fail gate 1).

**Also still open, unchanged by this pass:** (1) the Pali prose Nikāyas have had **one** scan (2026-08-03) whose filter required a literal second-person pronoun in Sujato's English, so it provably missed impersonal-voice and bare-imperative material — a second pass targeting those two classes is owed. (2) `zh-samyukta-agama.md` (25,078 lines) has only ever had its 39 Patton-paired sūtras looked at, and is by far the largest unmined Chinese source.

---

## Update 2026-08-26 — the Kangyur has now had its FIRST FULL SCAN (all 229 files)

Supersedes the coverage claims above. During the Days 124–127 selection pass, **all 229 `bo-toh*.md` files were scanned**, split four ways and worked in parallel, with **speakers verified in the Degé rather than in the 84000 English**. Yield: **three cards from first-time sources** — **Toh 302** (Day 124; in `rejected.md` only for a *different* line), **Toh 55** (Day 125) and **Toh 93** (Day 127), the last two appearing in **neither `rejected.md` nor `candidate-pool/tibetan.md`**. Method that worked: use the paired `en-toh<N>-84000.md` as a searchable index into the Tibetan, then pin every survivor back to grep-verified Degé.

**Residue — what is honestly still unscanned.** The ~23 files **above 45 kB**, which were filter-screened but not read: **Toh 11, 51, 56, 113, 124, 145, 147, 175, 232, 238** and the rest of that band. A 4-pada stanza rarely fits the 126-char budget whole, so the judgement there has to be by eye rather than by filter. **Toh 340** (*The Hundred Deeds*, 1.57 MB) should be **permanently skipped** — it is avadāna and fails gate 1 by construction.

**⚑⚑ THE FINDING THAT INVALIDATES THE INDEX METHOD IF USED CARELESSLY: 84000's English can be clean where the Degé is not.** **Toh 113** (Lotus) carries what reads as a perfect card in 84000 — *"the power of love is the residence, patience and gentleness the robe"* — with no first person anywhere. **The Degé reads `བྱམས་པའི་སྟོབས་ནི་ང་ཡི་གནས།`; 84000 dropped the possessive `ང་ཡི` ("my").** Under the first-person screen the verse is dead. **Anyone working this corpus through the English index must re-check the Degé for `ང་` / `བདག་` before believing any clean-looking line.** This is a fifth confirmed case of 84000 diverging from the Degé.

**The shape that actually yields here, confirmed twice in one batch:** Buddha-spoken **imperative verse runs addressed to a single named youth** (Toh 55 → Candraprabha; Toh 302 → Upāli's retinue). The three shapes the previous update recommended — protection/fearlessness, aspiration formulas, benediction clusters — are now **grep-exhausted and dedupe-poor**: they light up reliably and almost every hit is either a non-Buddha speaker or already shipped. **Work the youth-address vein first next time.**

**Gate-1 traps verified and recorded, so future greps do not re-surface them as finds:** Toh 312 blessing cluster (= Days 104/107/109) · Toh 99 *"look upon beings with loving eyes"* (past buddha Vimalanetra, past-life frame) · **Toh 61 *"do not waste the freedom you have now"* (spoken by nonvirtuous friends, quoted as bad advice — the most convincing false positive in the corpus)** · Toh 96 / Toh 218 / Toh 248 fear passages (Mañjuśrī, a bodhisattva, third-person description) · Toh 112's 806 `གྱུར་ཅིག` aspirations (all the brahmin Samudrareṇu) · Toh 47, 181, 257, 124, 56 aspiration series (Śakra, Pūrṇa, a nāga king, a brahmin youth, a yakṣa) · Toh 325 (jātaka, nāga speakers) · **Toh 160's "ten resolves" — 84000 prints ten warm second-person imperatives, but the Tibetan is one enumeration of noun phrases each ending in `དང་`; the imperatives are a translation artifact.**

**Chinese is now the deficit canon (Pali 43 · Chinese 39 · Tibetan 39) and its scan status is the bottleneck.** `zh-samyukta-agama.md` (1.8 MB, only its 39 Patton-paired sūtras ever scanned) and `zh-madhyama-agama.md` (2.0 MB, 15 sūtras scanned) are the large unmined seams, and **the CBETA `<lg>` gāthā blocks were dropped at import from both**, so they currently hold no verse content at all. **A converter re-run to recover those gāthās is the highest-value unblocking task in the vault.**
