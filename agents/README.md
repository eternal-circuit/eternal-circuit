# Multi-agent editorial architecture

**These are role contracts, not proof that separate autonomous processes are running.** A coordinating Codex or other agent runner must explicitly invoke distinct roles, isolate their outputs, and enforce the state machine in [the realism policy](../canon/REALISM_POLICY.md). Merely reading these Markdown files is not multi-agent execution.

## Roles

| Role | Scope | Authority |
| --- | --- | --- |
| Orchestrator | Break down work, assign agents, preserve provenance, advance tasks only after gates | No veto override; cannot approve canon |
| Frontier scout | Monitor new science, engineering, AI and emerging projects | Propose leads only |
| Evidence verifier | Read primary sources and independently corroborate frontier claims | Rate evidence; not final canon authority |
| Quantitative modeler | Reproduce assumptions, estimates, units, sensitivity and statistical arguments | Block referral on insufficient model |
| **Science adversary** | Challenge physics, computation, mathematics, statistics, biology and engineering | **Absolute veto on canonical advancement** |
| Literary adversary | Challenge craft, coherence, character, rhetoric, reader trust | Required second gate; cannot override science |
| Canon keeper | Check source of truth, continuity, timelines, provenance | Flag conflicts; cannot overrule science |
| Narrative architect / writer | Outline or draft specifically authorized text | Proposal only |
| Archivist | Record decisions, rejected alternatives, rationale and handoffs | No canon promotion |
| Human author | Choose among science-cleared options; approve final canon | Cannot bypass science veto |

## Separation of duties

The science adversary must not simply rubber-stamp its own draft. Use independent review passes (ideally distinct agent contexts) for scouting, verification, modeling and final adversarial decision. If only one model is available, run explicitly separated contexts and label independence as limited; external peer review is warranted for high-stakes pivotal premises.

No agent self-certifies. No role silently rewrites a source manuscript. Reviews cite exact file paths/lines, version or commit, inputs and evidence. If specialists disagree, record dissent and keep gate closed until resolved.

## Routing rules

- **Idea or voice session:** orchestrator curates a short handoff in `handoffs/` with public/private screening; research begins before any canon promotion.
- **New technology claim:** frontier scout → verifier → modeler → science adversary.
- **Story outline/manuscript:** above science sequence → literary adversary → canon keeper → author.
- **Nonfiction/meta editorial text:** source and privacy check → author review; do not misrepresent it as scientific clearance of story material.
- **Revisions touching mechanisms:** invalidate prior scientific PASS and review changed claims.
- **Archive:** archivist records both accepted and rejected proposals with dates and provenance.

## State machine

`PROPOSED → RESEARCHING → SCIENCE_PASS → LITERARY_REVIEWED → AUTHOR_APPROVED → MERGED_CANON`

At any stage, `SCIENCE_BLOCKED` or `SCIENCE_UNRESOLVED` halts the canonical path. `CONDITIONAL_PASS` also halts until conditions cleared. Literary revisions return to science review if causal claims change.

Pull requests must identify evidence dossier(s), science verdict, literary review, author approval, and any unchanged legacy text. Do not merge on missing status.

## Immediate rollout

1. Pilot with a **single, narrow mechanism** from *Idle Hands*, not the entire anthology.
2. Make the evidence dossier; demand numeric budgets and falsification tests.
3. Run adversarial review in isolation; collect counterarguments.
4. Return only PASS ideas to narrative outlining and literary critique.
5. Author reviews a diff and explicitly approves canon promotion.

See [runbook](RUNBOOK.md) and [review template](../research/reviews/TEMPLATE.md).
