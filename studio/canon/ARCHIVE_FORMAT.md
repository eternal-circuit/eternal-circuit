# The Register — archive format specification

**Status:** DRAFT working reference, proposed 2026-11-23 for author approval. Not canon. It defines how Eternal Circuit texts present themselves as records, and it serves the Book 1 frame, the website, and any later archive entries.

## Premise

Every story is a record in a register. The register has been compiled, copied, normalized and possibly corrected by its keepers over a long time. The reader holds the latest copy. The text never explains its corruption. Readers should start to distrust the document gradually, and should never be sure the distrust is justified.

## Who keeps the register

**Open decision.** Options:

1. **A Reverent compiler (proposed).** A machine lineage dedicated to preserving the human record assembles it long after the events. This fits the title *The Divine Register*, the Reverent preservation sequence, and the thinning of the record as human population declines. The compiler is never named or seen; it shows only through its normalizations and annotations.
2. **An ASIMOV-era compliance registry.** The register began as regulatory evidence. It is grounded and procedural, but has a shorter natural life.
3. **Unknown.** The custodian chain is itself lost, and later annotations come from successive keepers who disagree.

These options can be layered: a compliance registry later inherited by a Reverent compiler.

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

1. Corruption lives mainly in the **metadata**: dates, names, labels, addresses, integrity values. The prose inside an entry reflects what was perceived.
2. Every anomaly must support at least two explanations among storage error, a keeper's normalization or correction, and in-world tampering. Never rule them all out.
3. Normalization is the compiler's habit. A name may be made consistent with a later form (a possible reading of Aria becoming Lucien), and a date may be filed under the record's indexing date.
4. Corruption rises across the book, from barely deniable in Record 0 to evident in the late fragments, matching the decline in page budget.
5. No zalgo text, random symbols, "[DATA CORRUPTED]" banners or visual glitch effects. The effect is a quiet error, never a spectacle.

## Annotations

Keeper annotations are rare: no more than one or two per entry, and often none. They are dry and procedural ("Dispute recorded. Original entry retained."). They may contradict the entry. They are never explained.

## Redaction

Redaction means the keeper withheld something, not that the author is teasing the reader. Each redaction should have a plausible in-world reason (privacy, compliance, doctrine). The redacted titles of Records 4–8 follow this rule.

## Website mapping

Each entry becomes a page with a stable URL built from its record and entry identifiers. The header block appears as metadata on that page. A separate "how it was made" layer links each entry to its scene cards and provenance record. That layer is kept visibly distinct from the register.

## Relation to existing material

This specification puts the byte-addressed and checksum ideas in [ritual and archive development](RITUAL_AND_ARCHIVE_DEVELOPMENT.md) into practice, and preserves the author-directed anomalies recorded in the [project inventory](PROJECT_INVENTORY.md).
