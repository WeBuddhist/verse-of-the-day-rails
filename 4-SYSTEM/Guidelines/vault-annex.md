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
| 2 | Sutta Nipāta | Pali (KN) | `pi-sutta-nipata.md` | **imported** (73 suttas, CC0; en-sujato paired) |
| 3 | Udāna | Pali (KN) | `pi-udana.md` | **imported** (80 suttas, CC0; en-sujato paired) |
| 4 | Itivuttaka | Pali (KN) | `pi-itivuttaka.md` | **imported** (112 suttas, CC0; en-sujato paired) |
| — | ~~Theragāthā / Therīgāthā~~ | Pali (KN) | — | **excluded** — verses of the elder monks/nuns, *not* buddhavacana |
| 5 | Dīgha Nikāya | Pali | `pi-digha-nikaya.md` | **imported** (34 suttas, CC0; en-sujato paired) |
| 6 | Majjhima Nikāya | Pali | `pi-majjhima-nikaya.md` | **imported** (152 suttas, CC0; en-sujato paired) |
| 7 | Saṁyutta Nikāya | Pali | `pi-samyutta-nikaya.md` | **imported** (1,819 suttas, CC0; en-sujato paired) |
| 8 | Aṅguttara Nikāya | Pali | `pi-anguttara-nikaya.md` | **imported** (1,408 suttas, CC0; en-sujato paired) |
| 9 | Dīrgha Āgama (長阿含經, T1) | Chinese | `zh-digha-agama.md` | **imported** (30 sūtras; CBETA CC BY-NC-SA, non-commercial; source-only, no translation) |
| 10 | Madhyama Āgama (中阿含經, T26) | Chinese | `zh-madhyama-agama.md` | **imported** (222 sūtras; CBETA CC BY-NC-SA) |
| 11 | Saṁyukta Āgama (雜阿含經, T99) | Chinese | `zh-samyukta-agama.md` | **imported** (1,355 sūtras; CBETA CC BY-NC-SA) |
| 12 | Ekottarika Āgama (增壹阿含經, T125) | Chinese | `zh-ekottarika-agama.md` | **imported** (472 sūtras; CBETA CC BY-NC-SA) |
| 13 | Udānavarga (Toh 326) | Tibetan | `bo-udanavarga.md` | **imported** (PD; 89 Degé folio-blocks; mdo verse collection, Dhammapada parallel) |
| 14 | Further Kangyur mdo sūtras (by Tohoku no.) | Tibetan | `bo-toh<N>.md` | on demand — PD Degé root (OpenPecha/P000001); **mdo / Mahāyāna sūtras only, no tantra/Vinaya** (§ Kangyur scope). 84000 English = verbatim reference (§7). |

Āgama note: imported **source-only** (Literary Chinese, no paired translation exists under a clean license). Modern-language renderings are produced in-vault under review (§4). Use is **non-commercial / ShareAlike** per CBETA's license (§7) — keep separate from the CC0 Pali in any output licensing.

**Kangyur scope boundary (what we take, what we don't).** From the Tibetan Kangyur we include the **sūtra section (mdo)** — the Buddha's discourses, including **Mahāyāna sūtras**. We **exclude**: the **Tantra section (rgyud)** — because WeBuddhist serves *all* Buddhists and tantra is tradition-specific and often restricted/empowerment-gated; the **Vinaya ('dul ba)** — monastic rules, not verse-of-the-day material; and any scholastic/abhidharma-type material. The flagship import is the **Udānavarga (Toh 326)**, a mdo-section verse collection of the Buddha's utterances (the Tibetan parallel to the Dhammapada). Tibetan root is Public Domain; we make our **own** modern translations from it, optionally consulting 84000's English as a verbatim reference (§7).

**Pali coverage now in the vault:** the four main Nikāyas (DN, MN, SN, AN) plus the four buddhavacana verse collections of the Khuddaka Nikāya (Dhammapada, Sutta Nipāta, Udāna, Itivuttaka) — the core of the Sutta Piṭaka, all CC0 with paired Sujato English. **Not imported:** the Vinaya Piṭaka (monastic rules) and Abhidhamma Piṭaka (scholastic analysis) — neither is verse-of-the-day material; and the mixed-authorship KN texts (Jātaka, Apadāna, Buddhavaṁsa, Theragāthā/Therīgāthā, etc.), which are not direct words of the Buddha.

The priority for verse-of-the-day is the **buddhavacana verse collections** of the Khuddaka Nikāya: Dhammapada, Sutta Nipāta, Udāna, Itivuttaka — all now imported. **Theragāthā / Therīgāthā are deliberately excluded**: they are verses attributed to named elder monks and nuns, not words of the Buddha. Only the Buddha's words belong in this vault.

---

## 2. Addressing scheme

Because this is a multi-source anthology, **each source file declares its own `verse_id_format`**. There is no global spine. Two schemes are used:

**(a) Verse collections — `verse_id_format: verse`.** Block ID = the work's own continuous verse number, no zero-padding. Example: Dhammapada verse 1 → `^1`, verse 423 → `^423`. Vagga (chapter) headings are organizational only and use a `^vagga-N-0` heading anchor.

**(b) Prose / segmented suttas — `verse_id_format: suttacentral-segment`.** Block ID = the SuttaCentral segment ID with colons and dots replaced by hyphens (Obsidian block IDs allow only alphanumerics and hyphens). Example: `mn1:1.2` → `^mn1-1-2`. The `uid` (e.g. `mn1`) is recorded in frontmatter so the original SuttaCentral reference is always recoverable.

**Cross-canon references** in rails and plan files use the form `[[1-SOURCES/Text/<file>#^<block-id>]]`. Always record the canonical citation in the `source_ref` frontmatter field of the rail/plan file.

### Citation labels (shown with every verse of the day)

Each verse of the day displays its source using the standard scholarly abbreviation below. This is the `source_ref` the app shows under the verse (e.g. **Dhp 16**).

| Source | Label | Number format | Example | Links to |
| ------ | ----- | ------------- | ------- | -------- |
| Dhammapada | `Dhp` | verse | **Dhp 16** | `pi-dhammapada.md#^16` |
| Sutta Nipāta | `Snp` | vagga.sutta (+ verse) | **Snp 1.8** | `pi-sutta-nipata.md#^snp1-8-...` |
| Udāna | `Ud` | vagga.sutta | **Ud 1.10** | `pi-udana.md#^ud1-10-...` |
| Itivuttaka | `Iti` | sutta | **Iti 26** | `pi-itivuttaka.md#^iti26-...` |
| Dīgha Nikāya | `DN` | sutta | **DN 16** | `pi-digha-nikaya.md#^dn16-...` |
| Majjhima Nikāya | `MN` | sutta | **MN 10** | `pi-majjhima-nikaya.md#^mn10-...` |
| Saṁyutta Nikāya | `SN` | saṁyutta.sutta | **SN 56.11** | `pi-samyutta-nikaya.md#^sn56-11-...` |
| Aṅguttara Nikāya | `AN` | nipāta.sutta | **AN 3.65** | `pi-anguttara-nikaya.md#^an3-65-...` |
| Dīrgha Āgama | `DĀ` | sūtra | **DĀ 2** | `zh-digha-agama.md#^da2-0` |
| Madhyama Āgama | `MĀ` | sūtra | **MĀ 1** | `zh-madhyama-agama.md#^ma1-0` |
| Saṁyukta Āgama | `SĀ` | sūtra | **SĀ 262** | `zh-samyukta-agama.md#^sa262-0` |
| Ekottarika Āgama | `EĀ` | sūtra | **EĀ 1** | `zh-ekottarika-agama.md#^ea1-0` |

Rules: Pali sources use Roman abbreviations (`Dhp`, `MN`…); Chinese Āgamas use the diacritic `Ā` form (`SĀ`, `MĀ`…) to distinguish them from the Pali parallels. A verse-of-the-day day file records both the human label in `source_ref` and the exact block link in `source_link`, so the displayed "Dhp 16" always resolves to its grounded source.

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
| **CBETA** (Chinese Āgama / canon source text) | CC BY-NC-SA 3.0 TW | non-commercial only | yes — derivatives must be ShareAlike | **usable (non-commercial)** | WeBuddhist is a non-profit using CBETA as an internal source to produce modern translations (not republishing CBETA's text). Conditions: (1) use stays genuinely non-commercial — a free, non-monetised app; (2) attribute CBETA + Taishō base text; (3) modern translations derived from it inherit CC BY-NC-SA (**ShareAlike** — they can't later go under a commercial/more-restrictive license); (4) don't redistribute CBETA's source text unchanged as a product. CBETA's non-commercial grant covers the Taishō base text for this use. *Not legal advice — confirm the app's non-commercial status.* |
| **SuttaCentral lzh** (Literary Chinese Āgama fragments) | CC0 (SC) | yes | yes | partial-only | Clean license but **incomplete** — only fragments of SA/MA/EA are segmented, and there is **no paired translation**. Not a viable full Āgama source on its own. |
| **Degé Kangyur — Tibetan root** (Esukhia → OpenPecha/P000001, via BDRC) | Public Domain | yes | yes | **cleared** | Mechanical reproduction of a public-domain woodblock edition. No restrictions. The source to import for Tibetan. OpenPecha is WeBuddhist's own stack; BDRC is a partner. |
| **84000** (Kangyur → English) | CC BY-NC-ND | non-commercial only | **no derivatives** | **reference-pairing only** | Two permitted uses: (a) store the **whole** translation verbatim as a paired reference layer — with attribution **and** its footnotes, non-commercial (ND allows verbatim redistribution; it forbids altering/excerpting); (b) consult it as a reference when writing our own translation (84000 explicitly permits this, acknowledgement appreciated). **NOT permitted for verse of the day:** publishing a single-verse **excerpt** of their translation, or adapting their English into our modern wording — both violate ND. So 84000 = grounding reference; the shipped verse must be **our own** modern rendering from the PD Tibetan, citing 84000. |
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
