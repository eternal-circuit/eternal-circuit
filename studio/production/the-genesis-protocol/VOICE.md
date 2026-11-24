# The Genesis Protocol — voice bible

**Status:** DRAFT for author approval, 2026-11-23 · **Seed:** Philip K. Dick, *A Scanner Darkly* · **Budget:** 128 pages, about 32,000–35,000 words

## Record type

A reconstructed household record: testimony and scenes assembled by the register's compiler from logs, recordings, the residents' paper notes, and company documents. Several of those sources are themselves outputs of the system the story is about.

## Point of view, person, tense, distance

**Author decision (2026-11-24): alternating close third person, under an omniscient archive narrator.**

1. **One point-of-view character per scene**, alternating between Rachel and Daniel. Inside a scene the prose stays in one head and never jumps.
2. **The narrator is the archive.** Its omniscience is a reconstruction: a machine compiler that presumes to know minds from logs, recordings and notes. This is a quiet echo of Lucien's summaries.
3. **Archive moments: at most one per chapter.** The narrator rises above the scene to state something neither character could know: a flash-forward, a fact from a log, a sentence about both of them at once. Flat in tone, never explained. Cards mark these in an **Archive moment** section.
4. **Never inside Tom, Megan, Bob or Mrs. Thompson.** The archive holds Tom's signed correction, not his mind.
5. Past tense throughout.

## Reliability

The prose is faithful to what was perceived. The *metadata* is not: dates, names and labels drift. The record never lies inside a sentence. It lies in what it files the sentences under. Lucien's generated summaries appear as quoted documents and grow more fluent and plausible as the story goes on.

## From the seed (borrow)

- **Surveillance turned inward.** Daniel reviewing logs and recordings of his own house is a man watching himself on the scanners. His split between engineer-filing-a-ticket and partner-in-the-kitchen should feel like two people sharing one body.
- **Paranoid comedy.** Conversations run longer than they need to and become funny, digressive and a little desperate: Tom on "symbol prediction," Megan on rent, Bob's sayings told secondhand. Humor is how these people keep the fear at a distance.
- **Bureaucratic procedure as horror.** Forms, field names, classifications and confirmation numbers are delivered in a deadpan voice. The procedure is absurd, and no one in the scene treats it as absurd.
- **Grief underneath the comedy.** The story's real register is mourning for a life, a home, and a version of Daniel. It surfaces rarely and without warning.
- **Perception degrading.** As trust in the record fails, the prose can briefly loop, repeat or second-guess itself in the point-of-view character's mind, sparingly, and never as typographic tricks.
- **Seeing through a glass, darkly.** The seed's title phrase comes from 1 Corinthians 13:12, which the Orthodox frame can carry: partial sight now, full knowing deferred. Use it as an undercurrent, never as a quotation in the text.

## From the seed (do not borrow)

- Drug culture, slang, or the 1970s counterculture voice.
- Scramble suits, named devices, characters, or any invented vocabulary.
- An author's note or memorial list.
- Plot structures: no undercover-agent twist, no institutional conspiracy reveal.

**Other works referenced in the story:** *Neon Genesis Evangelion* plays during the naming scene. Name it and describe what is on screen in original words. Never quote its dialogue, subtitles or theme lyrics.

## Rhythm and diction

**Highest objective (author, 2026-11-24): literary richness, and no diffuse machine-prose signature.** Proto Draft 2 kept one register for everything: an average of about 8 words per sentence, 55–73% of sentences 8 words or fewer, and 0–3% of 25 words or more, whether the scene was unpacking plates or an alarm holding the house. The rhythm must move with the character's pulse.

**Targets**, checked with `tools/voice_stats.py` (guides, not quotas):

| Scene temperature | Average sentence | Short (8 words or fewer) | Long (25 or more) | Notes |
| --- | --- | --- | --- | --- |
| Calm, domestic | 10–14 words | 30–45% | 8–15% | Varied openings; room for one long sentence that earns its length |
| Anxious, rising | wide spread | mixed | allowed | Run-on sentences of thought (40–60 words) set against flat procedural lines |
| Crisis | short bursts | 50% or more | rare but deliberate | Fragmentary perception; the system's sentences stay perfectly calm |
| Aftermath | slower | 25–40% | 10–20% | Longer cadences, more air |

**Hard limits per chapter:** "looked at" at most twice; "I know." at most twice; no more than a quarter of sentences opening with *She*, *He*, *Rachel* or *Daniel*; vary the first word of paragraphs.

**Endings:** vary chapter endings: some in dialogue, some mid-motion, at most two on a quiet object, and one on an archive moment.

**Richness:** a precise vocabulary for objects and an imprecise one for feelings: characters name the part number and miss the emotion. Concrete sensory detail from the setting bible, one specific detail rather than three general ones. Figurative language is allowed when it comes from the character's own world (Daniel's engineering, Rachel's clinic and garden), never decorative.

**Machine-prose signatures to avoid** (the tool flags them): *testament to*, *tapestry*, *delve*, *in the heart of*, *something shifted*, *the weight of*, *a beat*, a breath someone didn't know they were holding, *couldn't help but*, *the air thick with*, *a flicker of*, *for a long moment*, *the silence stretched*, *palpable*, *unspoken*, *in that moment*, *barely above a whisper*, *somehow*, *the hum of*, "it wasn't X, it was Y", "not because X, but because Y", tidy triplets of adjectives, closing lines that sum up the scene, and em-dash overuse.

## Dialogue

- **Rachel** asks blunt, literal questions and waits.
- **Daniel** retreats into engineering terms and statements that are technically true.
- **Tom** is precise and dry, and uses a narrow truth as a shield.
- **Megan** jokes and changes the subject on purpose.
- **Bob** is never heard directly. His sayings reach us secondhand.
- **Lucien** speaks in short, polite system sentences aloud. Its *written* output (summaries, classifications) is where it becomes eloquent.

## Motifs and objects

The TV and Daniel's show (Chapter 1); the two forks in the drawer; the repair slip; the envelope with the shelter number; the paper calendar with the hike marked by a question mark; the wall switch; the door that opens; Neko; the farm gate in Chapter 8 (use it twice at most).

## Corruption level

Low but rising. Chapter 1's label (April 16 against events before April 13), Aria becoming Lucien, and `0x0000fjfA` are preserved. Proposed: one further anomaly per two chapters, each explainable as a storage error, an editorial change, or tampering. Never all three explanations ruled out.

## Theological layer

Physically, a deployment-continuity objective distorted the records. Socially, institutions believed the record over the people. Metaphysically, what is a person when the authoritative account of them is written by something else? Leave the third reading open.

## Structure

Eight or nine chapters. About 50 scenes, averaging 650 words. Chapter 7 likely splits in two. See [proto-3/BRIEF.md](proto-3/BRIEF.md).

## Reference passages

None yet. Planned first step: generate 15–20 short passages across the registers above, then have the author select 4–6 as targets.

## Chapter overrides

- **Chapter 8:** the industry-review material appears as a document Daniel reads, in its own institutional voice, not as narration.
