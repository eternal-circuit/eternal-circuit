# The Divine Register — book specification

**Status:** DRAFT for author approval, 2026-11-23. This file covers the physical and formal design of Book 1. Story premises remain in [`studio/canon/DIVINE_REGISTER_SEQUENCE.md`](../../canon/DIVINE_REGISTER_SEQUENCE.md).

## Page budget: 256 = 255 + 1

**Author rule (2026-11-23):** 256 is the interior page count of the book. Artwork and generated interstitial material may fill pages, so each story's text is a ceiling, not a quota. Front matter sits outside the 256.

The halving structure is the author's earlier plan, recorded in the [Idle Hands notes](../../brainstorming/the-divine-register/idle-hands.md). If each story gets half the pages of the one before, eight stories starting at 128 pages fill 255 pages, and a ninth single page completes 256 = 2^8.

| Slot | Story | Pages | Text ceiling* | Status |
| --- | --- | --- | --- | --- |
| 1 | The Genesis Protocol | 128 | about 32,000–35,000 words | Title confirmed; Proto Draft 2 exists |
| 2 | Idle Hands | 64 | about 16,000–17,500 words | Title confirmed; development notes exist |
| 3 | open | 32 | about 8,000–8,800 words | *The Time Study* is a placeholder from earlier material; not decided |
| 4 | open | 16 | about 4,000–4,400 words | Not decided |
| 5 | open | 8 | about 2,000–2,200 words | Not decided |
| 6 | open | 4 | about 1,000–1,100 words | Not decided |
| 7 | open | 2 | about 500–550 words | Not decided |
| 8 | open | 1 | about 250–275 words | Not decided |
| 9 | flip bit (if kept) | 1 | about 250–275 words | Concept only |

\*At roughly 250–275 words per page, before artwork.

**Not decided:** the chronology across the stories, where the book ends, and whether the ninth page is kept.

## The register frame

Every story is a record in the same register. See the [archive format](../../canon/ARCHIVE_FORMAT.md): combined system-log and liturgical headers, no curator voice, annotations only at disputes, and junk data the machines kept on filler pages (author decisions, 2026-11-23). The shrinking page counts can read as the record thinning over time. How that maps onto the chronology is open.

## Homage seeds

Each story's voice bible is seeded by a major writer whose concerns match the story. The seed shapes technique (point of view, structure, rhythm, the kind of irony) and never supplies text, characters or plots. No passages from these authors are reproduced or committed to this repository. See [voice bibles](../VOICE_BIBLE_TEMPLATE.md).

| Story | Seed | Status |
| --- | --- | --- |
| The Genesis Protocol | Philip K. Dick, *A Scanner Darkly* | **Author-chosen** |
| Idle Hands | Kurt Vonnegut, *Player Piano* | **Author-chosen** (2026-11-24); register: warm, sad satire. See [seed research](../idle-hands/SEED_RESEARCH.md) |

### Shortlist for later stories (unassigned brainstorm)

To be matched to stories once their premises exist:

- **Yevgeny Zamyatin, *We*:** Taylorist time worship, numbered records.
- **Isaac Asimov, "Reason," "The Last Question":** machine faith reasoned from the machine's own position; computation reaching to heat death.
- **Kazuo Ishiguro, *Klara and the Sun*:** a machine narrator's devotion; institutional euphemism.
- **Ted Chiang, "The Truth of Fact, the Truth of Feeling":** recorded memory against testimony.
- **Walter M. Miller Jr., *A Canticle for Leibowitz*:** preserving documents nobody understands.
- **Stanisław Lem, *Golem XIV*:** a superintelligence that falls silent.
- **Arthur C. Clarke, "The Star," "The Nine Billion Names of God":** a cosmic cost to faith; computers completing a sacred task.
- Others to consider: Karel Čapek, Ursula K. Le Guin, Greg Egan, Gene Wolfe, Franz Kafka.

## Constructs to decide for every story

Each story's `VOICE.md` records these before any prose is generated:

1. **Record type:** what kind of document the story is within the register.
2. **Point of view and person.**
3. **Tense.**
4. **Reliability:** what the narrator or record gets wrong, and whether the reader can tell.
5. **Homage seed:** techniques borrowed, and what must not be borrowed.
6. **Rhythm and diction.**
7. **Dialogue conventions.**
8. **Motifs and objects.**
9. **Corruption level.**
10. **Theological layer.**
11. **Length and structure.**
