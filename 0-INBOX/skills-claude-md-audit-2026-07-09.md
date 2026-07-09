---
audit_date: 2026-07-09
scope: CLAUDE.md + 4-SYSTEM/Skills/*/SKILL.md + SKILLS-CATALOG.md + .claude/commands/
against: agentskills.io skill-authoring best practices
---

# CLAUDE.md + skills audit — 2026-07-09

Read CLAUDE.md, SKILLS-CATALOG.md, all six SKILL.md files, and cross-checked against actual vault content (rail frontmatter, day-card frontmatter, filenames, `.claude/commands/`). Checked against the agentskills.io best-practices doc you pasted: grounding in real expertise, conciseness, coherent scope, gotchas, templates, checklists, defaults-not-menus, procedures-over-declarations.

**Bottom line:** `verse-selection`, `verse-rail`, and `translation-qa` are excellent — genuinely best-in-class examples of the guide's principles. `vault-audit` has two bugs that would make it actively wrong if run today. `create-skill` and `vault-audit` both cite CLAUDE.md section numbers that no longer exist. 19 dead slash commands are live in `.claude/commands/`. Details below, worst issues first.

---

## 1. `vault-audit` — two checks are wrong, would false-positive on every file

This is the highest-priority fix. If you ran `/vault-audit` today it would report problems that don't exist and miss the ones it's meant to catch.

**Check 7a (misplaced rail files)** requires every file in `2-RAILS/Verses/` to match `^\d+-\d+\.md` (e.g. `1-1.md`). But every real rail file is named by text-slug — `dhp-5.md`, `sa-262.md`, `toh-282.md`, `an2-32-gratitude.md` — per both `verse-rail`'s own spec and CLAUDE.md's Conventions section ("Rails ... named by source slug"). None of the 41 files currently in `2-RAILS/Verses/` match the regex. Running this check today would flag **all 41 files** as misplaced. The check is checking for the generic Railroads-template convention, not this vault's.

**Check 2 (frontmatter completeness)** requires `2-RAILS/Verses/` files to carry `verse_id, root_text, root_block, language, commentaries, status`. Actual rail frontmatter (confirmed against `dhp-5.md`, `dhp-62.md`, `dhp-81.md`) is `ref, source_ref, canon, unit_type, source_text, source_block, grounding, translations, theme, speaks_to, buddhist_lens, concepts, status` — a completely different schema from the translation-grounded rewrite. This check would flag all 41 rails as missing 5 of 6 required fields, on every run.

**Check 7b** looks for `3-TRANSFORMATIONS/*/Verses/` directories. The real structure is `3-TRANSFORMATIONS/verse-of-the-day/days/` — there is no `Verses/` subfolder anywhere under `3-TRANSFORMATIONS/`. This check silently matches nothing and never fires — a dead check rather than a false positive, but it means "day card exists with no rail" is currently unmonitored.

**Root cause, all three:** `vault-audit` was written against the generic Railroads template before (or without being updated for) the anthology's translation-grounded rail schema and single-track output structure. It needs a rewrite of Checks 2, 7a, and 7b against the actual schema — the sample frontmatter above is a ready reference.

**Separately:** `vault-audit` Check 7a also cites "Per CLAUDE.md §4" and `create-skill` Step 5 cites "CLAUDE.md §12" — CLAUDE.md has no numbered sections (it uses plain `##` headings: "Structure, citation chain, write permissions", "Skills quick-reference"). Both citations are stale pointers, presumably left over from an earlier numbered draft of CLAUDE.md. Low cost to fix, but every stale cross-reference is a small tax on trust in the document.

---

## 2. 19 dead slash commands in `.claude/commands/`

SKILLS-CATALOG.md's "Archived / removed" section says 19 template skills (`verse-context`, `glossary-select`, `add-toc`, etc.) were "moved to `Skills/_archived/`". In reality: `4-SYSTEM/Skills/_archived/` doesn't exist, and the skill folders are simply gone — but all 19 corresponding files in `.claude/commands/` are still present and still say "Read `4-SYSTEM/Skills/<name>/SKILL.md` in full, then execute it" — a path that no longer resolves. Anyone (or any agent) invoking `/verse-context` or `/glossary-select` today gets sent to a nonexistent file instead of a "this skill is archived" message.

Fix: delete the 19 stale command files, or update the catalog's claim to match what actually happened (deleted, not archived) and add a `vault-audit` check for exactly this (orphaned command files with no matching skill folder — a natural Check 1c alongside the existing catalog/command sync checks).

---

## 3. `epub-to-markdown` and `json-to-source-text` — good content, off-template structure

Both are strong, detailed, adaptive skills (inspect → match/generate converter → run → review is a clean, well-justified workflow, and the gotchas are genuinely earned — e.g. the `mixed_class_patterns` false-negative warning, the `༷` root-marker handling). But neither follows the required-sections list `create-skill` itself mandates (frontmatter with name+description, Inputs, Output, Output file format, Rules, Completion check):

- `epub-to-markdown` has **no YAML frontmatter at all** — no `name:`, no `description:`. Since `description` is what a skill-discovery pass matches against to decide whether to load the skill, this one is invisible to that mechanism; it currently only gets used because CLAUDE.md's table points straight at it by name.
- `json-to-source-text` does have frontmatter, but neither file has an explicit `## Rules` or `## Completion check` section — the "Steps 1–5" format is good procedural writing but leaves no place to verify the vault's own bar for "is this output done."

Two honest options, not a verdict — this is a judgment call: (a) bring both in line with the standard template (cheap: add frontmatter to epub-to-markdown, add a short Completion check to each), or (b) formally bless a second template shape for "adaptive converter" skills in `create-skill`, since their steps-and-reference-files shape is arguably a better fit for this task type than the rail/QA template. Either is fine; leaving it undecided is the part that costs something, since `vault-audit`'s Check 1 doesn't currently check section-completeness at all, only catalog/command registration — so drift like this won't get caught automatically either way.

---

## 4. What's already excellent (no action needed, noted so it's not lost)

`verse-selection`, `verse-rail`, and `translation-qa` are the strongest-written skills in the vault and match the best-practices guide closely:

- **Grounded in real, specific expertise, not generic advice** — e.g. verse-rail's gotcha "a real bug caught this way: Iti 22 is *sukhudrayaṁ*, not *sukhindriyaṁ*" and its explicit warning not to over-rely on T210/Udānavarga for non-Pali variety. This is exactly the "environment-specific fact that defies reasonable assumptions" the guide asks for.
- **Defaults, not menus** — each skill names one grounding approach, one termbase, one output path pattern, rather than presenting options.
- **Procedures over declarations** — all three have numbered, reusable procedures rather than one-off answers.
- **Templates for output** — every one includes a fenced-code output template.
- **Completion checklists** — all three end in a verifiable checkbox list.
- These three are good reference examples if you want `epub-to-markdown` / `json-to-source-text` brought to the same shape later.

---

## 5. CLAUDE.md itself

Small, well-scoped, and does the one thing it needs to (route to skills, state hard rules, define write permissions) without padding — it's already close to the guide's "moderate detail" ideal. Two minor notes:

- The "§0", "§4", "§7" style cross-references *into other files* (vault-annex.md, About Sources.md) are fine since those files presumably still have numbered sections — only the *inbound* references to CLAUDE.md's own now-unnumbered sections are stale (see finding 1).
- Line 81 ("Commentary/section/glossary skills ... are not used here and are archived") is the one place CLAUDE.md repeats the now-inaccurate "archived" claim from the catalog. Fixing SKILLS-CATALOG.md (finding 2) should fix this line too, or drop it from CLAUDE.md entirely and let the catalog be the single source of truth for what's archived.

---

## Suggested order of fixes

1. Rewrite `vault-audit` Checks 2, 7a, 7b against the real rail/day-card schema (finding 1) — this is the one actively producing wrong output.
2. Delete the 19 orphaned `.claude/commands/*.md` files, and fix or drop the "moved to `Skills/_archived/`" claim in SKILLS-CATALOG.md and CLAUDE.md (finding 2).
3. Fix the two stale "§4" / "§12" references in `vault-audit` and `create-skill` (finding 1, footnote).
4. Decide epub-to-markdown / json-to-source-text: conform to template or bless a second template (finding 3) — lowest urgency, no wrong output today, just drift risk.

I haven't changed any files — this is a findings report only, per the vault's own read-only convention for audit output. Happy to make any of these edits directly if you want to greenlight specific ones.
