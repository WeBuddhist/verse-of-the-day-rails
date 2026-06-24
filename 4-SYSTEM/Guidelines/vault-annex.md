# Vault Annex — verse-of-the-day conventions

The methodology guidelines (`0-VAULT-Structure.md`, `../../1-SOURCES/About Sources.md`, `../../2-RAILS/About Rails.md`, `../../3-TRANSFORMATIONS/About Transformations.md`) are **text-agnostic** — they apply to any Railroads vault built on any classical text. This annex records the conventions specific to *this* vault: **WeBuddhist Verse of the Day**.

When the Guidelines and this annex disagree on a vault-specific detail, this annex wins.

---

## 0. How this vault differs from a standard Railroads vault

A standard Railroads vault serves **one classical text** and produces versions of it (translations, adaptations, study plans). **This vault is different.** It is a **curated anthology**: its output is a stream of short daily verses — *verse of the day* — drawn from the **words of the Buddha (buddhavacana)** across three canonical collections:

- the **Pali Canon** (Tipiṭaka, esp. the Sutta Piṭaka and the verse texts of the Khuddaka Nikāya);
- the **Chinese Āgamas** (the Chinese parallels to the Nikāyas, in the Taishō canon);
- the **Tibetan Kangyur** (the "translated word" — sūtra sections).

So `1-SOURCES/Text/` holds **many source texts, not one**: one file per canonical work (or per logical unit), each keeping its own native numbering. The "transformation" is a **Plan** (`verse-of-the-day`) that selects individual verses, localizes them into the app's languages, and arranges them on a calendar. There is no single root-text spine; the addressing scheme (§2) is therefore **per-source**.

The rails still apply: a verse is only published once its meaning is grounded against the source (and, where available, commentary), and every localized rendering cites its rail. The point of the system here is **authenticity and traceability of daily verses** — never an un-sourced or "fake Buddha quote."

---

## 1. The text(s)

This vault serves **WeBuddhist Verse of the Day** — a curated daily-verse anthology of the Buddha's words across the Pali, Chinese, and Tibetan canons, localized for the WeBuddhist app.

Source-text files in `1-SOURCES/Text/` are added per canonical work as they are imported. Current and planned sources:

| Order | Work | Canon | Filename | Status |
| ----- | ---- | ----- | -------- | ------ |
| 1 | Dhammapada | Pali (KN) | `pi-dhammapada.md` | **imported** (423 verses, CC0; en-sujato translation paired) |
| 2 | Sutta Nipāta | Pali (KN) | `pi-sutta-nipata.md` | planned |
| 3 | Udāna | Pali (KN) | `pi-udana.md` | planned |
| 4 | Itivuttaka | Pali (KN) | `pi-itivuttaka.md` | planned |
| 5 | Theragāthā / Therīgāthā | Pali (KN) | `pi-theragatha.md` / `pi-therigatha.md` | planned |
| 6 | Dīgha / Majjhima / Saṁyutta / Aṅguttara Nikāya | Pali | `pi-<nikaya>.md` | planned (prose; verse-bearing suttas) |
| 7 | Saṁyukta / Madhyama / Dīrgha / Ekottarika Āgama | Chinese | `zh-<agama>.md` | planned |
| 8 | Kangyur sūtra sections | Tibetan | `bo-<work>.md` | planned (pending license — see §7) |

The priority for verse-of-the-day is the **verse collections** (KN: Dhammapada, Sutta Nipāta, Udāna, Itivuttaka, Thera/Therīgāthā) — they are short verses by nature and the ideal daily-verse material.

---

## 2. Addressing scheme

Because this is a multi-source anthology, **each source file declares its own `verse_id_format`**. There is no global spine. Two schemes are used:

**(a) Verse collections — `verse_id_format: verse`.** Block ID = the work's own continuous verse number, no zero-padding. Example: Dhammapada verse 1 → `^1`, verse 423 → `^423`. Vagga (chapter) headings are organizational only and use a `^vagga-N-0` heading anchor.

**(b) Prose / segmented suttas — `verse_id_format: suttacentral-segment`.** Block ID = the SuttaCentral segment ID with colons and dots replaced by hyphens (Obsidian block IDs allow only alphanumerics and hyphens). Example: `mn1:1.2` → `^mn1-1-2`. The `uid` (e.g. `mn1`) is recorded in frontmatter so the original SuttaCentral reference is always recoverable.

**Cross-canon references** in rails and plan files use the form `[[1-SOURCES/Text/<file>#^<block-id>]]`. Always record the canonical citation (e.g. "Dhammapada 1", "MN 1:1.2", "SĀ 262", "Toh 113") in the `source_ref` frontmatter field of the rail/plan file.

---

## 3. Registered commentary IDs

Verse-of-the-day is primarily a **source + translation** anthology; commentary is consulted to ground meaning but is optional per verse. Commentaries are registered here as they are added.

| `registered_id` | Title | Tier | Language | File |
| --------------- | ----- | ---- | -------- | ---- |
| _(none registered yet)_ | | | | |

When a commentary is needed to disambiguate a verse (e.g. Dhammapada-aṭṭhakathā for a Dhammapada verse), register it here before citing it in any rail.

---

## 4. Language tracks

Source languages and the six app output (localization) languages. Note that `zh` and `bo` appear as **both** source and output languages — keep source files (`zh` = Chinese Āgama text; `bo` = Kangyur text) distinct from output streams (modern Chinese / modern Tibetan renderings).

| Tag | Language | Role |
| --- | -------- | ---- |
| `pi` | Pāli | source |
| `zh` | Chinese | source (Āgamas) **and** output (modern Mandarin) |
| `bo` | Tibetan | source (Kangyur) **and** output (modern Tibetan) |
| `sa` | Sanskrit | source (where extant; Devanāgarī) |
| `en` | English | output |
| `hi` | Hindi | output |
| `ne` | Nepali | output |
| `mn` | Mongolian (Cyrillic) | output |

The verse-of-the-day **Plan** (`3-TRANSFORMATIONS/Plans/verse-of-the-day/`) has one stream per output language: `en/`, `bo/`, `zh/`, `hi/`, `ne/`, `mn/`.

**Output language requirement — modern, plain language.** Every output stream must render verses in *contemporary, immediately understandable* language (modern Mandarin, modern colloquial Tibetan, contemporary Hindi/Nepali, modern Mongolian, plain English) — not classical or scholarly register. Where the only authoritative translation is classical (e.g. Literary Chinese, classical Tibetan), the meaning is sourced from it but the output is freshly rendered in modern language and flagged for native-reviewer sign-off.

---

## 5. Bilingual glossary pairs

Built as translation streams come online. Source→output pairs anticipated: `pi-en`, `pi-zh`, `pi-bo`, `pi-hi`, `pi-ne`, `pi-mn` (and `zh-*`, `bo-*` for Āgama/Kangyur sources).

| File | Source | Target | Status |
| ---- | ------ | ------ | ------ |
| _(none yet)_ | | | |

---

## 6. Active transformation tracks

| Track | Category | Status |
| ----- | -------- | ------ |
| `verse-of-the-day` | Plan | scaffolding |

---

## 7. Source licensing register

**Critical for this vault.** Verse-of-the-day ships in a commercial app, and modernizing a verse is a *derivative work*. Every source file therefore carries licensing frontmatter, and no source enters the pipeline until its license is recorded here and cleared for use.

### Required licensing frontmatter (add to every `1-SOURCES/` file)

```yaml
license: "CC0 | CC-BY-4.0 | CC-BY-NC-4.0 | CC-BY-NC-ND | public-domain | proprietary"
license_url: "https://..."
rights_holder: "e.g. Bhikkhu Sujato / SuttaCentral"
commercial_use: true | false
derivatives_allowed: true | false        # modernizing/translating requires this
attribution_required: true | false
attribution_text: "credit line to display, if required"
usage_status: "cleared | pending-permission | blocked"
```

### Register

| Source | License | Commercial | Derivatives | Status | Notes |
| ------ | ------- | ---------- | ----------- | ------ | ----- |
| **SuttaCentral — Bhikkhu Sujato** (Pali root + English) | CC0 / public domain | yes | yes | **cleared** | Best base. Modern English already. |
| **CBETA** (Chinese Āgama / canon source text, Taishō v.1–55) | Creative Commons (verify per text) | verify | yes | cleared-with-check | Source text only; English is sparse — render modern downstream. |
| **84000** (Tibetan Kangyur → English) | CC BY-NC-ND | no | no | **blocked** | Non-commercial + no-derivatives. Pursue a Khyentse Foundation content-use grant (KF runs 84000 and is a WeBuddhist partner) before importing. |
| **Access to Insight — Thanissaro** | CC BY-NC | no | yes | reference-only | Do not ship; reference for meaning only. |
| 19th-c. translations (Müller etc.) | public domain (age) | yes | yes | usable-but-archaic | Fails the modern-language requirement (§4). |

**Tibetan/Kangyur note:** the Kangyur *root text* (Tibetan) is ancient and not under copyright; the block is on modern *translations* like 84000's. Importing Tibetan source text from an openly-licensed edition is possible; the modern-language Tibetan output is then produced in-vault under review.

---

## 8. Source-language tags used in this vault

| Tag | Script / System | Use |
| --- | --------------- | --- |
| `-pi` | Pāli romanisation (diacritics) | Pali root texts |
| `-zh` | Chinese (Traditional unless noted) | Āgama / canon source |
| `-bo` | Unicode Tibetan | Kangyur source |
| `-sa` | Devanāgarī | Sanskrit source where extant |

Default for Pali sources is `-pi`. Roman/Wylie alternative scripts go in separate edition files.

---

## 9. Where to look next

- [`0-VAULT-Structure.md`](0-VAULT-Structure.md) — the architecture in full.
- [`../../1-SOURCES/About Sources.md`](../../1-SOURCES/About%20Sources.md) — source-file rules.
- [`../../3-TRANSFORMATIONS/About Transformations.md`](../../3-TRANSFORMATIONS/About%20Transformations.md) — Plan-track rules.
- [`Skills/json-to-source-text/SKILL.md`](Skills/json-to-source-text/SKILL.md) — source import; the `suttacentral_bilara` converter handles SuttaCentral CC0 data.
- [`import-runbook.md`](import-runbook.md) — how to bulk-import the Pali Canon from SuttaCentral.
