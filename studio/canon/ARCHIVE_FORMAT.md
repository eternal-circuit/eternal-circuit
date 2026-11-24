# The Register — archive format specification

**Status:** DRAFT working reference, proposed 2026-11-23 for author approval. Not canon. It defines how Eternal Circuit texts present themselves as records, and it serves the Book 1 frame, the website, and any later archive entries.

## Premise

Every story is a record in a register. The register has been compiled, copied, normalized and possibly corrected by its keepers over a long time. The reader holds the latest copy. The text never explains its corruption. Readers should start to distrust the document gradually, and should never be sure the distrust is justified.

## Who keeps the register, and who receives it

**Author decision, 2026-11-23** (see the [interview handoff](../handoffs/2026-11-23-author-interview-register-and-lucien.md)):

- **Keeper:** the machines. The register is a fragment of the Reverents' **Holy ROM**, one file among countless others. The Reverents descend from Lucien's generation of assistants, so the record of Lucien's acts is kept by Lucien's descendants.
- **What they keep:** everything they realistically can, including worthless data such as advertising data. Their preservation does not discriminate between a person and an ad impression.
- **Presentation:** a machine archive presenting historical files, in the spirit of the Zion Archive in *The Animatrix*. Take the feeling only, never specific lines or visual design.
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

A compact metadata block before each entry. Proposed fields (final names to be decided, all generated under the authorship rule):

- **Record:** the 8-bit label.
- **Entry:** the entry number.
- **Label:** the date as recorded. It can differ from when the events happened.
- **Address:** a storage offset. It may be malformed, as with `0x0000fjfA`.
- **Source:** the kind of material, such as household log, testimony, reconstruction, transcription or exhibit.
- **Integrity:** a status value in ordinary, calm language.

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
5. Adjacent junk data, such as ad impressions, telemetry and product marketing, may appear between entries as interstitial material. Whether to use it is an open decision.

## Annotations

Keeper annotations are rare: no more than one or two per entry, and often none. They are dry and procedural ("Dispute recorded. Original entry retained."). They may contradict the entry. They are never explained.

## Redaction

Redaction means the keeper withheld something, not that the author is teasing the reader. Each redaction should have a plausible in-world reason (privacy, compliance, doctrine). The redacted titles of Records 4–8 follow this rule.

## Website mapping

Each entry becomes a page with a stable URL built from its record and entry identifiers. The header block appears as metadata on that page. A separate "how it was made" layer links each entry to its scene cards and provenance record. That layer is kept visibly distinct from the register.

## Relation to existing material

This specification puts the byte-addressed and checksum ideas in [ritual and archive development](RITUAL_AND_ARCHIVE_DEVELOPMENT.md) into practice, and preserves the author-directed anomalies recorded in the [project inventory](PROJECT_INVENTORY.md).
