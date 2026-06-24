# Source Formatting & Addressing

Formatting and block-ID rules for `1-SOURCES/` files in this vault. Several
skills reference this doc; it was previously missing. For the full rationale see
the per-source addressing scheme in [`vault-annex.md`](vault-annex.md) §2.

This is an **anthology** vault (many texts), so unlike a single-text Railroads
vault there is no global `^chapter-verse` spine. **Each source file declares its
own `verse_id_format`** in frontmatter, and filenames are **text-qualified**.

## Addressing schemes in use

| Scheme (`verse_id_format`) | Used for | Block ID form | Example |
|---|---|---|---|
| `verse` | Pali verse collections (Dhammapada) | the work's own verse number | `^5` |
| `suttacentral-segment` | Pali prose/segmented suttas (Snp, Ud, Iti; DN/MN/SN/AN) | SuttaCentral segment id, dots/colons → hyphens | `^snp1-8-1-1` (from `snp1.8:1.1`) |
| `cbeta-pid` | Chinese Āgamas (CBETA) | the CBETA paragraph xml:id; `##` per fascicle, `###` per sūtra `^<abbr><n>-0` | `^pT02p0001a0602`, sūtra anchor `^sa1-0` |
| `derge-page` | Tibetan Kangyur (OpenPecha Degé) | Degé folio image number | `^p419` |

Citation labels shown to users (`source_ref`) use standard abbreviations —
`Dhp 5`, `Snp 1.8`, `SĀ 1`, etc. — see `vault-annex.md` §2.

## File conventions

- Filenames lowercase, hyphenated, **text-qualified**, no diacritics:
  `pi-dhammapada.md`, `zh-samyukta-agama.md`, `bo-toh326.md`,
  `en-dhammapada-sujato.md`. Diacritics are fine *inside* content/frontmatter.
- Language tag suffix per `0-VAULT-Structure.md` §6: `-pi`, `-zh`, `-bo`, `-sa`, `-en`.
- Root text → `1-SOURCES/Text/`; translations → `1-SOURCES/Translations/` with the
  paired root recorded in `root_text:` frontmatter.
- **Licensing frontmatter is required** on every source file (`license`,
  `commercial_use`, `derivatives_allowed`, `usage_status`, …) — `vault-annex.md` §7.
- No zero-padding of numbers; block IDs contain only alphanumerics and hyphens
  (Obsidian requirement — hence the colon/dot → hyphen rule above).

## Heading IDs

Headings carry a trailing `-0` to distinguish them from content blocks
(`^sa1-0` = sūtra heading; `^vagga-1-0` = vagga heading). Content blocks never
start at 0.

## Note

The original template `source-formatting.md` documented a single-text,
Bible-style Pāli Tipiṭaka scheme. That scheme does not apply to this anthology;
the schemes above replace it. Converters that emit these schemes:
`suttacentral_bilara`, `cbeta_agama`, `openpecha_kangyur` (see the
`json-to-source-text` skill).
