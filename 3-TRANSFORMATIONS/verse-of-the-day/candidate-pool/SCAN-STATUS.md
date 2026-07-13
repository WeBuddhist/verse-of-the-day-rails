# Candidate-tagging scan status — open work

Tracks which source files have had a real `candidate-tagging` pass (sequential read + selection against `1-SOURCES/Text/`), as distinct from files that only have candidates backfilled from already-built rails. Update this when a scan completes or when new source text is imported. See `SKILLS-CATALOG.md` → `candidate-tagging` for the process itself.

## Done — full sequential scan complete

- **Chinese canon** — all four Āgamas (Dīrgha, Madhyama, Saṁyukta, Ekottarika) plus the Chinese Mahāyāna sūtras registered in `vault-annex.md`. See `candidate-pool/chinese.md`.
- **Pali verse collections** — Dhammapada (423 verses), Sutta Nipāta (~72 suttas, 5 vagga), Udāna (80 suttas), Itivuttaka (112 suttas). See `candidate-pool/pali.md`.
- **Tibetan Udānavarga** (Toh 326, 33 chapters) — the first genuine scan of Tibetan source text, not a rail-backfill. See `candidate-pool/tibetan.md`.

## Not yet done — the big remaining lift

- **Pali prose Nikāyas** — Dīgha Nikāya (34 suttas, ~32,800 lines), Majjhima Nikāya (152 suttas, ~54,100 lines), Saṁyutta Nikāya (1,819 suttas, ~79,800 lines), Aṅguttara Nikāya (1,408 suttas, ~78,200 lines). Combined ≈ 245,000 lines — roughly **17× everything scanned in the pass above**. A full sequential read-every-line scan at that scale isn't practical in one sitting; when this is picked up, consider Rule 11 of the `candidate-tagging` skill (sample first, then decide scan strategy) and likely a sampling or targeted approach (e.g. well-known/oft-cited suttas first) rather than line-by-line reading of all four texts.
- **Tibetan Kangyur sūtras** — roughly 229 individual `bo-toh<N>.md` files beyond the Udānavarga and the handful already covered via rail-backfill or the earlier 3-file live test (Toh 143, 149, 150). Each file is a separate sūtra of varying length; this also hasn't had a real scan pass.

Existing rails already drawn from a few of these files (see `2-RAILS/Verses/` — e.g. mn19-thought, sn1-1, an2-32-gratitude) don't count as a scan of the source text itself; they're one-off selections made without a bulk pre-tagging pass.

**Why this matters:** the Pali/Tibetan candidate pools are strong for the verse collections but still shallow on the prose Nikāyas and the bulk of the Kangyur relative to how thoroughly the Chinese canon has been covered. `verse-selection` can keep drawing on what's here in the meantime — this file is a reminder to eventually close the gap, not a blocker.

## When picking this back up

1. Re-read `4-SYSTEM/Skills/candidate-tagging/SKILL.md` in full.
2. Check `log.md`'s running balance and `theme-checklist.md`'s open gaps first, so the scan is looking for something.
3. Given the scale, parallel sub-agents per source file (or per chunk of a large file) are more practical than one sequential pass — see this session's approach for the verse collections as a template (each sub-agent reads its assigned range, returns candidates in the standard format, one person compiles into the pool file to avoid write conflicts).
4. Update this file's "Done" / "Not yet done" lists when a chunk completes.
