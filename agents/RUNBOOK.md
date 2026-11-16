# Orchestrator runbook

## Input
Receive a bounded question, target story/file, publication classification, desired deliverable and whether the author is requesting **research**, **proposal**, **draft**, or **canon promotion**. Never infer authorization to publish private/unreleased material from access to a conversation.

## Phase A — ingest
Read root `AGENTS.md`, `README.md`, `canon/PROJECT_INVENTORY.md`, `canon/WORKFLOW.md`, `canon/REALISM_POLICY.md`, applicable manuscripts and source notes. Extract the *minimum testable scientific claims* on which the narrative depends. Assign claim IDs and identify relevant era and environment.

## Phase B — research, in parallel where feasible
1. **Frontier scout:** track current publications, GitHub repositories, technical talks, labs, engineering demonstrations, and relevant X posts. Output leads with dates, firsthand attribution and links.
2. **Evidence verifier:** locate original papers, methods, datasets, code, demonstrations, corrections and reproduction; distinguish announcement vs measured result.
3. **Quantitative modeler:** produce dimensional analysis, credible ranges, prior/base rates, uncertainty bounds, limiting bottlenecks and alternative scenarios.
4. **Canon keeper:** in parallel check timeline and existing story implications; findings do not substitute for physics clearance.

## Phase C — primary gate
Give independent science adversary the claim, source packet and model, with instructions to **try to falsify it**, quantify failure modes, test hidden assumptions and check selection bias. It must explicitly choose PASS / CONDITIONAL PASS / BLOCK / UNRESOLVED with justification. A reviewer may request more research. All but PASS halt the canon pipeline. No appeals based on author enthusiasm, elegance or theme.

## Phase D — secondary gate
Only after PASS: literary adversary challenges causality, stakes, narrative necessity, exposition, character agency and whether implausible coincidence masquerades as science. It may request changes or flag story issues. If revisions affect physical premises return to Phase B/C.

## Phase E — human approval
Prepare decision memo: evidence dossier, two adversarial reviews, known limitations, alternate options, proposed diff, and clear question for the author. Only explicit author approval moves a proposal to canon.

## Phase F — commit
Use a named Git branch and reviewable PR. Never directly change default branch. Keep original prose intact until diff approval. Add commentary explaining pivotal choices, and keep obsolete or blocked variants as **noncanonical research notes**, never quietly merge them as fictional truth.

## Stop conditions
STOP if sources unavailable, probability claim unjustified, science verdict not PASS, no author approval, privacy uncertain, branch/check status unknown, or unexpected contradiction. Report the blocker and a tractable next experiment/research task.

## Suggested machine-readable review summary
```yaml
claim_id: EC-SCI-0001
target: "stories/..."
reviewed_commit: "<sha>"
science_verdict: UNRESOLVED
literary_verdict: NOT_STARTED
author_approval: PENDING
canon_status: PROPOSED
source_reviewed_at: YYYY-MM-DD
evidence_dossier: research/reviews/...
```
Do not imply this YAML is an automated enforcement system. Real branch protection / CI remains a separate future implementation.

## Mandatory durable research deposit
Between Phases B and C, the scout/verifier/modeler must propose self-contained research notes under `research/notes/YYYY/`, using `research/TEMPLATE.md`, and update `research/index.md` in the same branch/PR. A verifier independently checks the note. The science adversary references the local note ID and commit/revision as well as primary sources. Link-only dossiers do not qualify. See `research/README.md`.
