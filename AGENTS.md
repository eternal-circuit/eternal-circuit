# Eternal Circuit — instructions for Codex and other repository agents

This repository is the long-lived, version-controlled collaboration space for **The Eternal Circuit**, an original speculative fiction universe. **The Divine Register is Book 1**, not the whole project.

## Source-of-truth discipline
- Read `README.md`, `canon/PROJECT_INVENTORY.md`, `canon/WORKFLOW.md`, and relevant manuscripts before proposing changes.
- Distinguish **author-approved canon**, **draft text**, **inferred continuity**, **research**, and **unresolved proposals**. Do not silently upgrade drafts or conversational brainstorming to canon.
- Do not silently rewrite, redact, reorder, or deduplicate original prose. Show changes as a diff and preserve original source files.
- Do not overwrite the default branch for literary/editorial changes. Work on a named branch and open a reviewable PR.
- Never publish private chat transcripts, personal information, unpublished material, or third-party copyrighted assets to this **public** repository merely because the material is available in a chat. Request explicit approval for publication.

## Creative constraints
- Scientific realism: no FTL travel or unlimited resources; model travel times, thermodynamics, compute, energy, and population dynamics plausibly.
- Theological framing: Orthodox Christian motifs inform the work. Machine imitations of liturgy are not automatically spiritual equivalence.
- The central thematic conflict is loss through compression: convenience, AI delegation, neural interfaces, and uploads can erase the irreducibility of persons.
- Narrative voice: clinical, haunted, increasingly uncanny; preserve intentional uncertainty.
- When documenting a new worldbuilding idea, record its status and provenance before treating it as settled.

## Voice-to-Codex handoff
- Voice sessions should end with a concise, curated **handoff note** or a proposed change, not an indiscriminate transcript dump.
- Handoff format: date, source (voice conversation, draft, research), decisions, open questions, suggested files, canon status, privacy/publication classification, next actions.
- If the task is to implement an approved handoff, inspect current files, create a branch, implement scoped edits, run consistency checks, and report changed files.
- If no new handoff exists, do not claim to have seen an uncommitted iOS conversation: ChatGPT Project context and Codex session memory are not automatically identical.

## Repository organization
- Existing folders and manuscripts remain authoritative historical artifacts until reviewed.
- `canon/`: approved canon and editorial governance (working inventories explicitly labeled).
- `handoffs/`: curated session summaries intended for cross-device collaboration, never raw conversations.
- `research/`, `continuity/`, `assets/`, `deprecated/`: create as needed, with provenance.
