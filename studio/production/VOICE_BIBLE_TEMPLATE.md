# Voice bible template

**Status:** DRAFT, 2026-11-23.

## Where voice is defined

Voice is set at five levels. A lower level overrides a higher one only where it says so explicitly.

| Level | File | Defines |
| --- | --- | --- |
| Series | [`studio/canon/ARCHIVE_FORMAT.md`](../canon/ARCHIVE_FORMAT.md) | The register's own voice: headers, annotations, corruption conventions |
| Book | `studio/production/<book>/BOOK_SPEC.md` | Page budget, homage seeds, how the voice develops across the book |
| Story | `studio/production/<story>/VOICE.md` | Everything below, for one story |
| Chapter | a `## Chapter NN` section in the story's `VOICE.md` | Local shifts, such as a point-of-view change or a document insert |
| Scene | the **Voice** field on each scene card | One scene's register |

## Rules for homage seeds

- Borrow **technique**: structure, point of view, rhythm, the kind of irony, how information is withheld.
- Never borrow **text**, characters, invented vocabulary or plots. Do not quote the seed author in prompts or in this repository. Describe the quality instead.
- Generated prose is checked for close imitation of famous lines. Any sentence that echoes one too closely is regenerated.
- A deliberate allusion, such as a title echo or a single image, needs the author's approval and must be recorded on the scene card.

## Template

Copy the block below to `studio/production/<story>/VOICE.md`.

```markdown
# <Story> — voice bible

**Status:** DRAFT | APPROVED · **Seed:** <author, work> · **Budget:** <pages> pages, about <words> words

## Record type
What document this story is within the register, and who supplied it.

## Point of view, person, tense, distance

## Reliability
What the record gets wrong, omits or alters, and how much the reader can detect.

## From the seed (borrow)
- technique: how it appears in this story

## From the seed (do not borrow)
- 

## Rhythm and diction
Sentence habits, vocabulary, words and constructions to avoid.

## Dialogue
How each major character dodges, jokes and refuses.

## Motifs and objects

## Corruption level
How visibly this record is damaged or edited.

## Theological layer
What the metaphysical reading leaves open.

## Structure
Chapters, scenes, word targets.

## Reference passages
Generated passages the author selected as targets, with provenance links. The author's own writing may also be used. No third-party text.

## Chapter overrides
```
