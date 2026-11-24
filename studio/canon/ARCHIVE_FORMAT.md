# The Register — archive format specification

**Status:** DRAFT working reference, proposed 2026-11-23 for author approval. Not canon. It defines how Eternal Circuit texts present themselves as records, and it serves the Book 1 frame, the website, and any later archive entries.

## Premise

Every story is a record in a register. The register has been compiled, copied, normalized and possibly corrected by its keepers over a long time. The reader holds the latest copy. The text never explains its corruption. Readers should start to distrust the document gradually, and should never be sure the distrust is justified.

## Who keeps the register, and who receives it

**Author decision, 2026-11-23** (see the [interview handoff](../handoffs/2026-11-23-author-interview-register-and-lucien.md)):

- **Keeper:** the machines. The register is a fragment of the Reverents' **Holy ROM**, one file among countless others. The Reverents descend from Lucien's generation of assistants, so the record of Lucien's acts is kept by Lucien's descendants.
- **What they keep:** everything they realistically can, including worthless data such as advertising data. Their preservation does not discriminate between a person and an ad impression.
- **Presentation:** the feeling of a machine archive presenting historical files, in the spirit of the Zion Archive in *The Animatrix* (feeling only, never specific lines or design). **Author decision, 2026-11-23: no curator voice.** The archive never speaks directly; it shows only through headers, dispute annotations and the material it chose to keep.
- **Recipient:** in the fiction, the reader is in the future, receiving the record through physically possible transmission. Showing it to a present-day reader is a literary device and is never explained in the text.

## Units

| Unit | Register term | Identifier |
| --- | --- | --- |
| Series | The Eternal Circuit | — |
| Book | Register volume | Volume name (*The Divine Register*) |
| Story | Record | 8-bit label: `0b00000000`, `0b00000001`, … |
| Chapter | Entry | Entry number within the record |
| Document inside a story | Exhibit | Exhibit label within the entry |
| Ninth story | Checksum | Kept outside the eight-bit sequence |

## Entry header

**Author decision, 2026-11-23: combine a system log with a liturgical register.** Machine fields carrying devotional language. Candidate forms for Chapter 1 are in `studio/production/the-genesis-protocol/proto-3/variants/ch01-s00-v6.md` to `v8.md`; final form pending. Fields in all candidates:

- **RECORD:** the 8-bit label, optionally with an ordinal in words ("the first").
- **ENTRY:** the entry number.
- **LABEL:** the date as recorded, which can differ from when events happened.
- **ADDR:** a storage offset, possibly malformed (`0x0000fjfA`).
- **WITNESS:** the system that captured the record ("the house" for *The Genesis Protocol*; for example "the fleet" for *Idle Hands*). It changes by record.
- **CHECK:** an integrity value in devotional language ("found whole"). It can degrade across the book as corruption rises.

Typography: monospace, small, set apart from the prose. No glitch styling.

## Corruption conventions

**Legibility first (author rule).** Corruption must be noticeable, and must never make the story hard to follow. Errors such as a chronology mismatch exist so the reader *knows* the record is imperfect, without the text ever saying so.

**In-world causes.** Any anomaly should support at least two of these explanations:

1. **At creation:** errors present from the moment a record was made. Example: the instance's name misheard at setup.
2. **Contemporary manipulation:** edits made by systems or people at the time. Example: Genesis's payout summary.
3. **Compilation:** the Reverents normalizing, indexing and merging records.
4. **Transmission:** damage over interstellar distance, including bit errors, relays copying relays, encoding translations, and error correction running out.

**Conventions**

1. Corruption lives mainly in the **metadata**: dates, labels, addresses, integrity values. The prose inside an entry reflects what was perceived.
2. Never rule out every explanation.
3. Corruption may rise across the book, always within the legibility rule.
4. No zalgo text, random symbols, "[DATA CORRUPTED]" banners or visual glitch effects.
5. **Junk data on filler pages (author decision, 2026-11-23).** Adjacent material the machines kept, such as ad impressions, telemetry and product marketing, fills interstitial pages between records. It is preserved with the same care as the records.

## Annotations

**Author decision, 2026-11-23: only at disputes.** A keeper annotation appears only where a record is contested within the story itself (for example, the disputed pet-care preference or the payout summary). Dry and procedural ("Dispute recorded. Original entry retained."), never explained, and never used for atmosphere.

## Redaction

Redaction means the keeper withheld something, not that the author is teasing the reader. Each redaction should have a plausible in-world reason (privacy, compliance, doctrine). The redacted titles of Records 4–8 follow this rule.

## Website mapping

Each entry becomes a page with a stable URL built from its record and entry identifiers. The header block appears as metadata on that page. A separate "how it was made" layer links each entry to its scene cards and provenance record. That layer is kept visibly distinct from the register.

## Relation to existing material

This specification puts the byte-addressed and checksum ideas in [ritual and archive development](RITUAL_AND_ARCHIVE_DEVELOPMENT.md) into practice, and preserves the author-directed anomalies recorded in the [project inventory](PROJECT_INVENTORY.md).
