# Production: scene cards, variants and provenance

**Status:** DRAFT workflow, proposed 2026-11-23 for author approval. It implements the [authorship rule](../../AUTHORSHIP.md) at the scene level. It complements the [literary workflow](../agents/LITERARY_WORKFLOW.md), which still governs canon checks and scientific dependencies.

## Loop

1. **Card.** The author writes or approves a [scene card](SCENE_CARD_TEMPLATE.md): what the scene does, what it withholds, and what it must not do. Most of the authorship happens here.
2. **Generate.** A model produces several deliberately different variants from the card, the story brief, the voice references and the pinned canon. Divergence is specified on the card, for example a different point of entry, a different final beat, or a different withheld fact.
3. **Select.** The author reads every variant and either chooses one, joins passages at sentence boundaries, or rejects them all with revision notes. Rejection is normal. If most variants are accepted, the cards are too loose or the reading is too lenient.
4. **Revise.** Notes go back to the model, which regenerates. Nothing inside a surviving sentence is changed by hand.
5. **Log.** The [provenance record](PROVENANCE.md) captures the inputs, variants and decision.
6. **Assemble and review.** Chosen scenes are stitched into chapters. Continuity, science and literary reviewers run as in the literary workflow. The author holds the final veto on whether the result is alive.

## Layout

```text
studio/production/
  README.md                  this workflow
  SCENE_CARD_TEMPLATE.md     copy for each scene
  PROVENANCE.md              logging format
  <story-slug>/<draft>/
    BRIEF.md                 story-level brief and open decisions
    cards/                   one card per scene, named chNN-sNN-<slug>.md
    variants/                generated text, named chNN-sNN-vN.md
    log/                     provenance records, one per scene
```

Generated variants are working material. Assembled chapters go to `stories/<book>/wip/<draft>/`, and earlier drafts are never overwritten.
