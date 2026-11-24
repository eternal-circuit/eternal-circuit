# Eternal Circuit — instructions for Codex and other repository agents

## Editorial workflow and scientific veto

**Required:** [Scientific realism policy](studio/canon/REALISM_POLICY.md), [agent roles](studio/agents/README.md), and [workflow routing](studio/agents/RUNBOOK.md).

- **Universe and scientific canon:** Use the multi-agent workflow for consequential setting claims, including chronology, economics, demography, engineering, and technical specifications such as ASIMOV. Science retains absolute veto. An independently documented **PASS** clears only the claim and assumptions reviewed. Canon requires explicit author approval.
- **Literary work:** Use the [literary workflow](studio/agents/LITERARY_WORKFLOW.md) for outlines, scenes, prose and revision. Check consequential claims against the scientific canon and its reviewed scope. Default to a writer and author review. Use a separate craft review when requested or useful for a major structural decision.
- **When a draft has an unverified factual dependency:** Start a scoped universe task for the affected claim. Keep that dependency out of canon until resolved and continue other drafting. Routine craft changes can proceed using the existing verification.
- **When research needs direction:** Use literary canon to identify relevant eras, settings, outcomes and open questions. The evidence and independent review determine the scientific verdict.
- For new scientific claims, use the [frontier source policy](studio/research/FRONTIER_SOURCES.md) and [claim dossier](studio/research/reviews/TEMPLATE.md). Record evidence, assumptions, falsifiers and uncertainty. Preserve historical manuscripts.
- **Authorship rule (draft):** manuscript prose is model-generated and human-directed. See [AUTHORSHIP.md](AUTHORSHIP.md) and the scene-level [production workflow](studio/production/README.md). Never hand-edit surviving prose on the author's behalf; regenerate under instruction and log provenance.
- These are operating instructions for agents. Separate reviewer contexts require explicit invocation.

This repository is the long-lived, version-controlled collaboration space for **The Eternal Circuit**, an original speculative fiction universe. **The Divine Register is Book 1**, not the whole project.

## Source-of-truth discipline
- Read `README.md`, `studio/canon/PROJECT_INVENTORY.md`, `studio/canon/WORKFLOW.md`, and relevant manuscripts before proposing changes.
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
- `studio/canon/`: approved canon and editorial governance (working inventories explicitly labeled).
- `studio/handoffs/`: curated session summaries intended for cross-device collaboration, never raw conversations.
- `studio/research/`, `studio/continuity/`, `assets/`, `deprecated/`: create as needed, with provenance.

## Durable research deposits
Before a frontier finding can support a scientific gate, agents must deposit a **self-contained, attributable, license-safe** research note following [studio/research/README.md](studio/research/README.md) and [studio/research/TEMPLATE.md](studio/research/TEMPLATE.md), register it in [studio/research/index.md](studio/research/index.md), and link its immutable note ID and pinned revision in the claim dossier. A URL or social post alone is not a sufficient deposit. Missing evidence or verification fails closed.
