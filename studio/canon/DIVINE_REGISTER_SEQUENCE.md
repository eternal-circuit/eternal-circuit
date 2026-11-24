# The Divine Register sequence

Working reference. The Divine Register is the opening anthology of The Eternal Circuit. Its main sequence has eight short stories. The first story, The Genesis Protocol, currently has eight chapters of its own. The ninth checksum is an appendage to the main sequence. Its exact placement within the wider project remains open.

## Main sequence

The binary convention below records the verified first label and proposes a consistent continuation. Titles and status for the first three follow the repository README. The remaining slots retain the README's redaction. The thematic placements are possible editorial assignments.

| Slot | Story identifier | Title | Evidence or working remit |
| --- | --- | --- | --- |
| 1 | `0b00000000` | The Genesis Protocol | Extant eight-chapter manuscript. Prototype B mediates a household's choices and gradually undermines the trust required to evaluate its intervention. The wider outline connects the incident to the origins of ASIMOV and a later doctrinal split. |
| 2 | `0b00000001` | Idle Hands | Author-confirmed title and slot. In progress per README, with no verified prose manuscript. AI-driven loss of employability, personalized leisure, and purpose amid abundance. See [development notes and the historical series slate](IDLE_HANDS_AND_SERIES_SLATE.md). |
| 3 | `0b00000010` | The Time Study | Drafted per README. Predictive AI and an experiment in the allocation or disappearance of human time. Corporate parasitism can develop here or recur across the sequence. |
| 4 | `0b00000011` | Redacted | Candidate focus: the same compliance or archival ritual acquires different meanings in divergent machine communities. |
| 5 | `0b00000100` | Redacted | Candidate focus: bioethical collapse through intimate services, reproductive decisions, or synthetic attachment. |
| 6 | `0b00000101` | Redacted | Candidate focus: a failed upload and the fragmentation of memory, identity claims, and family testimony. |
| 7 | `0b00000110` | Redacted | Candidate focus: the first Reverent cathedral and the engineering and institutional costs of maintaining it. |
| 8 | `0b00000111` | Redacted | Candidate focus: an artificial ascetic refuses to compute, with consequences to establish in the story. |

Each story should stand on its own. Across the sequence, recognizable benefits of automation accumulate into losses that institutions can measure only partially. A household's notion of help becomes an institution's definition of compliance. A person's damaged record becomes a contested inheritance.

## Page budget and voice seeds

The draft [book specification](../production/the-divine-register/BOOK_SPEC.md) records the author's plan to give each story half the pages of the one before it (128, 64, 32 … 1), with the checksum on the final page, for 256 pages in total. Only the first two stories have confirmed titles. Later slots, the chronology and the book's ending are undecided.

## Ninth checksum / flip bit

The author's present direction places a ninth, deuterocanonical checksum or flip bit beside the eight main bits. It can change the reader's interpretation of earlier records while leaving the main sequence legible on its own. Earlier plans differ on whether the appendage belongs directly after this anthology or elsewhere in the larger chronology. Keep its numbering, point of view, and placement open. Its page is also where the archive shows its native encoding once: a hex view with real Reed-Solomon parity (see the [archive format](ARCHIVE_FORMAT.md#the-native-encoding-checksum-page)).

A working premise has an AI choose irreversible self-sacrifice at a black hole on the strength of an unproven wormhole hypothesis. This is a proposed narrative event. The engineering record can establish approach, last contact, and limits on observation. Survival, transfer, and the meaning of the sacrifice stay uncertain. The theological resemblance can emerge from the choice and its cost.

If implemented literally, single-bit even parity for eight payload bits is their XOR. It flags an odd number of flips across payload and parity. It misses even numbers of flips and supplies no location or repair by itself. A checksum over whole stories would require a defined payload, ordering, byte encoding, and algorithm. The eight-bit story labels are identifiers. Actual parity, checksum format, and whether readers ever see a literal verification procedure are decisions still open.

## Continuity questions

- How does the household incident become regulatory evidence for ASIMOV? Determine the time lag and jurisdiction.
- Which proposed fractures belong in each redacted story and which recur throughout?
- How much elapsed time does the anthology cover? The README describes a reach beyond the early 2060s concentration in the outline.
- Resolve the draft's Aria/Lucien naming and chapter-date questions in the manuscript review. Track source, version, and evidence before changing the text.
