# The Divine Register — book specification

**Status:** DRAFT for author approval, 2026-11-23. This file covers the physical and formal design of Book 1. Story premises remain in [`studio/canon/DIVINE_REGISTER_SEQUENCE.md`](../../canon/DIVINE_REGISTER_SEQUENCE.md).

## Page budget: 256 = 255 + 1

Each story is half the length of the one before it. Eight halvings from 128 pages sum to 255. The ninth checksum, or flip bit, takes the final page, which makes 256 = 2^8. Human decline is visible in how much page space each story gets.

| Slot | ID | Story | Pages | Approx. words* | Form the length suggests |
| --- | --- | --- | --- | --- | --- |
| 1 | `0b00000000` | The Genesis Protocol | 128 | 32,000–35,000 | Novella in chapters |
| 2 | `0b00000001` | Idle Hands | 64 | 16,000–17,500 | Novelette |
| 3 | `0b00000010` | The Time Study | 32 | 8,000–8,800 | Long short story |
| 4 | `0b00000011` | [redacted] | 16 | 4,000–4,400 | Short story |
| 5 | `0b00000100` | [redacted] | 8 | 2,000–2,200 | Short short |
| 6 | `0b00000101` | [redacted] | 4 | 1,000–1,100 | Flash fiction or a document cluster |
| 7 | `0b00000110` | [redacted] | 2 | 500–550 | A single document |
| 8 | `0b00000111` | [redacted] | 1 | 250–275 | A fragment |
| 9 | checksum | flip bit | 1 | 250–275 | A single page, set apart |
| | | **Total** | **256** | **about 63,000–70,000** | |

\*Assumes a trade paperback at roughly 250–275 words per page. Final pagination depends on typesetting.

**Open decisions**
- Do the front matter, dedication and register headers count toward the 256 pages, or sit outside them? Proposed: outside, so the body is exactly 256.
- Is the halving exact to the page, or a target within ±10%? Proposed: exact to the page in the final typeset edition, approximate while drafting.

## The register frame

Every story is a record in the same register. See the draft [archive format](../../canon/ARCHIVE_FORMAT.md). As the stories shrink, the records thin from full testimony to documents to fragments. The form should make the halving feel inevitable rather than arbitrary.

## Homage seeds

Each story's voice bible is seeded by a major writer whose concerns match the story. The seed shapes technique (point of view, structure, rhythm, the kind of irony) and never supplies text, characters or plots. No passages from these authors are reproduced or committed to this repository. See [voice bibles](../VOICE_BIBLE_TEMPLATE.md).

| Slot | Story | Proposed seed | Why it fits | Alternate |
| --- | --- | --- | --- | --- |
| 1 | The Genesis Protocol | **Philip K. Dick**, *A Scanner Darkly* | Surveillance turned on the self; a man reviewing recordings of his own home; paranoid comedy and grief | — (author-chosen) |
| 2 | Idle Hands | **Kurt Vonnegut**, *Player Piano* | Automation and the end of meaningful work; a craftsman's recorded motions replacing him, matching the apprentice whose repair is learned by the fleet | Karel Čapek, *R.U.R.* |
| 3 | The Time Study | **Yevgeny Zamyatin**, *We* | Taylorist time worship and a society run by a schedule; a narrative made of numbered records | Franz Kafka |
| 4 | [machine ritual divergence] | **Isaac Asimov**, "Reason" (*I, Robot*) | A robot reasons its way to faith from its own station; dialogue-driven logic puzzles; a framing interview | Asimov, "The Last Question" |
| 5 | [synthetic intimacy / reproduction] | **Kazuo Ishiguro**, *Klara and the Sun* / *Never Let Me Go* | A machine narrator who worships the sun; institutional euphemism; devastation through understatement | Ursula K. Le Guin |
| 6 | [failed upload] | **Ted Chiang**, "The Truth of Fact, the Truth of Feeling" / "The Lifecycle of Software Objects" | Recorded memory against family testimony; digital minds that need care | Greg Egan, *Permutation City* |
| 7 | [Reverent cathedral] | **Walter M. Miller Jr.**, *A Canticle for Leibowitz* | Monks preserving technical documents they don't understand; comedy and devotion across centuries | Gene Wolfe |
| 8 | [ascetic refuses to compute] | **Stanisław Lem**, *Golem XIV* | A superintelligence that lectures and then falls silent, framed by human editors' prefaces | Asimov, "The Last Question" |
| 9 | flip bit | **Arthur C. Clarke**, "The Star" / "The Nine Billion Names of God" | A cosmic event that costs a faith something; computers finishing a sacred task; a plain final-line turn | Asimov, "The Last Question" |

The book moves from literary paranoia (Dick) through social satire (Vonnegut, Zamyatin) to robot logic (Asimov), quiet machine interiority (Ishiguro, Chiang), devotion (Miller), silence (Lem), and cosmic finality (Clarke).

## Constructs to decide for every story

Each story's `VOICE.md` records these before any prose is generated:

1. **Record type:** what kind of document the story is within the register (testimony, log, diary, transcript, lecture, fragment).
2. **Point of view and person:** whose perception, first or third person, and how close.
3. **Tense.**
4. **Reliability:** what the narrator or record gets wrong, and whether the reader can tell.
5. **Homage seed:** techniques borrowed, and what must not be borrowed.
6. **Rhythm and diction:** sentence-length habits, vocabulary, what to avoid.
7. **Dialogue conventions.**
8. **Motifs and objects** that carry meaning.
9. **Corruption level:** how visibly this record is damaged or edited. Proposed: rising slowly across the book.
10. **Theological layer:** what the three-layer reading (physical, social, metaphysical) leaves open in this story.
11. **Length and structure:** page budget, chapter count and scene count.
