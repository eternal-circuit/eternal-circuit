# Production: scene cards, variants and provenance

**Status:** DRAFT workflow, proposed 2026-11-23 for author approval. It implements the [authorship rule](../../AUTHORSHIP.md) at the scene level. It complements the [literary workflow](../agents/LITERARY_WORKFLOW.md), which still governs canon checks and scientific dependencies.

## Loop

1. **Card.** The author writes or approves a [scene card](SCENE_CARD_TEMPLATE.md): what the scene does, what it withholds, and what it must not do. Most of the authorship happens here.
2. **Generate.** A model produces several deliberately different variants from the card, the story brief, the voice references and the pinned canon. Divergence is specified on the card, for example a different point of entry, a different final beat, or a different withheld fact.
3. **Select.** The author reads every variant and either chooses one, joins passages at sentence boundaries, or rejects them all with revision notes. Rejection is normal. If most variants are accepted, the cards are too loose or the reading is too lenient.
4. **Revise.** Notes go back to the model, which regenerates. Nothing inside a surviving sentence is changed by hand.
5. **Log.** The [provenance record](PROVENANCE.md) captures the inputs, variants and decision.
6. **Assemble and review.** Chosen scenes are stitched into chapters. Continuity, science and literary reviewers run as in the literary workflow. The author holds the final veto on whether the result is alive.

## Voice and book design

- [Voice bible template](VOICE_BIBLE_TEMPLATE.md): the five levels where voice is defined, and the rules for homage seeds.
- [Book specification for *The Divine Register*](the-divine-register/BOOK_SPEC.md): the 256-page budget, seed authors, and the decisions each story needs before drafting.
- *The Genesis Protocol* has a full `VOICE.md`; *Idle Hands* has a stub. Later stories get one once their premises exist.

## Layout

```text
studio/production/
  README.md                  this workflow
  SCENE_CARD_TEMPLATE.md     copy for each scene
  PROVENANCE.md              logging format
  <book-slug>/BOOK_SPEC.md   book-level design
  <story-slug>/VOICE.md      story voice bible
  <story-slug>/<draft>/
    BRIEF.md                 story-level brief and open decisions
    cards/                   one card per scene, named chNN-sNN-<slug>.md
    variants/                generated text, named chNN-sNN-vN.md
    log/                     provenance records, one per scene
```

Generated variants are working material. Assembled chapters go to `stories/<book>/wip/<draft>/`, and earlier drafts are never overwritten.

## Generation harness

[`tools/generate.py`](tools/generate.py) automates the loop's generate and log steps. It uses only the Python standard library and reads the API key from `ANTHROPIC_API_KEY`. Run it from the repository root.

```sh
# Voice samples for the voice bible (15 registers by default)
python3 studio/production/tools/generate.py samples the-genesis-protocol

# Variants for one scene, one per divergence bullet on the card
python3 studio/production/tools/generate.py variants \
    studio/production/the-genesis-protocol/proto-3/cards/ch01-s06-naming.md

# Revision round with author notes, plus extra canon context
python3 studio/production/tools/generate.py variants CARD --notes notes.md \
    --context studio/canon/ASIMOV_REQUIREMENTS.md
```

- `--estimate` prints an approximate token count and cost and stops. `--dry-run` writes the prompt files without calling the API. Prompt files are self-contained and can also be pasted into a chat with the chosen model.
- Each variant prompt includes the system rules, the story's `VOICE.md`, `SETTING.md` (if present) and `BRIEF.md`, the glossary, the selected text of the previous scene (from its card's `chosen` field), the card, and any revision notes.
- Variants go to `<draft>/variants/`, prompts to `<draft>/prompts/`, and a provenance entry for the round to `<draft>/log/<scene>.md`. Fill in the **Decision** line by hand: which variant, what was cut or joined, and the notes for the next round.
- Default model: `claude-fable-5-2`. Override with `--model`.
- Approximate cost per round at November 2026 prices: about $0.35 for three Fable variants of an 800-word scene, and about $0.55 for 15 voice samples.

## Voice statistics

[`tools/voice_stats.py`](tools/voice_stats.py) measures sentence rhythm, dialogue share, repeated gestures and common machine-prose signatures for any set of files, optionally beside Proto Draft 2's baseline:

```sh
python3 studio/production/tools/voice_stats.py --baseline \
    studio/production/the-genesis-protocol/proto-3/variants/ch01-s06-v*.md
```

Use it when choosing between variants. It is a guide to the author's judgment, not a score.
