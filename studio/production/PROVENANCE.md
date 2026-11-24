# Provenance record format

**Status:** DRAFT, proposed 2026-11-23.

Each scene has one record at `studio/production/<story>/<draft>/log/<scene-id>.md`. Append new entries; never rewrite earlier ones. The records let a reader trace every surviving sentence back to the model and instructions that produced it.

```markdown
---
scene: ch01-s01
card_revision: <commit hash of the card used>
---

## Round 1 — 2026-11-24

- **Model:** claude-fable-5-2
- **Instructions:** prompts/ch01-s01-r1.md (or inline below)
- **Inputs:** card, BRIEF.md, voice references, canon files (with commit hashes)
- **Variants:** v1, v2, v3
- **Decision:** rejected all
- **Notes to model:** "The opening joke lands too early. Begin in the middle of the plates argument. End before Daniel answers."

## Round 2 — 2026-11-24

- **Model:** claude-fable-5-2
- **Variants:** v4, v5, v6
- **Decision:** v5, paragraphs 1–6, joined with v6, paragraphs 4–end at a sentence boundary
- **Arrangement:** deleted v5 paragraph 3
- **Result:** variants/ch01-s01-final.md
```

Record every rejected round as well. The rejections show where the authorship is.
