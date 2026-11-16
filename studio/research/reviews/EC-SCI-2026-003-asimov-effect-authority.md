# EC-SCI-2026-003 — Effect authority in the proposed 2037 ASIMOV stack

- **Status:** SCIENCE_UNRESOLVED for the integrated deployment.
- **Target:** Noncanonical 2037 scenario, [stack](../../asimov/2037/README.md) and [protocol](../../asimov/2037/PROTOCOL.md).
- **Reviewed design and evidence revision:** `7d054e19ec0d0cd7c37cdc91016aab3405db9766`. Follow-up text captures the reviewer's clarifications on fencing, permit issuance and checkpoint cadence.
- **Date:** 2026-11-16.
- **Reviewer:** Separate Scientific Adversary context with shared model family and workspace. No hardware test, implementation audit or full independent evidence-fidelity review.

## Mechanism and assumptions

One endpoint can bind mutation and budget debit to a unique scoped effect ID in a strictly ordered, durable transaction with no recovery rollback. A local epoch fence orders commits against revocation. Boot and firmware integrity provide a separate assurance argument from physical effect isolation. Across a network partition the endpoint cannot distinguish a cancellation it never received from a run that was never cancelled.

## Source and evidence ledger

| Evidence | Type | Limit |
| --- | --- | --- |
| [EC-R-2026-003](../notes/2026/EC-R-2026-003-agent-harnesses.md), pinned `7d054e19ec0d0cd7c37cdc91016aab3405db9766` | Primary source synthesis and original race model, DRAFT | Harness reports explain current practices. They do not establish complete effect coverage. |
| [EC-R-2026-002](../notes/2026/EC-R-2026-002-asimov-indexed-axis.md), pinned `15fcaa8c82aaf8d606740985f7c4aaaf093fd12e` | Primary hardware-source synthesis, DRAFT | Architecture building blocks and their limited evidence |
| [Race checker](../../asimov/2037/check_commit.py), pinned `7d054e19ec0d0cd7c37cdc91016aab3405db9766` | Exhaustive search of 30 schedules | One endpoint and effect ID. Cross-resource and persistence semantics are assumed. |

## Quantitative audit

The endpoint version of the abstract model yields zero duplicate or post-revocation commits in 30 schedules. The split broker check yields 12 duplicate and 14 post-revocation schedules. Neither count estimates probability. For remote expiry a 10.1 s illustrative cap assumes a 10 s issuance-to-commit lease plus at most 0.1 s aggregate elapsed-time error, validation at commit, and no acceptance without a valid clock or equivalent challenge.

## Verdicts and falsifiers

| Claim | Verdict | Basis and re-review trigger |
| --- | --- | --- |
| A transactional endpoint performs at most one mutation per scoped effect ID under atomic uniqueness, mutation, debit and durable recovery. | **PASS** | A second durable mutation for the same scoped ID would falsify the abstraction or show an integration failure. |
| An endpoint rejects new commits with a stale epoch once a local revoke advances the shared commit fence. | **PASS** | A mutation ordered after the fence update and using the previous epoch would falsify the claim. |
| A partitioned endpoint can honor immediate remote revoke while continuing to accept managed writes. | **BLOCK** | Its local observations can be identical in two runs that differ only in whether the remote party revoked. |
| The integrated 2037 domestic profile has complete installed mediation and independent local controls. | **UNRESOLVED** | Existing parts support a constrained demonstrator. Require effect and wiring inventory, install and restore fault tests, independent egress checks, and evidence of actual adoption to advance corresponding claims. |

## Literary gate and canon

Literary gate **NOT_STARTED**. No scientific clearance for the assembled deployment. No canon promotion or author approval requested.
