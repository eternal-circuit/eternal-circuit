# EC-R-2026-003 — Agent harnesses and effect authority

- **ID:** EC-R-2026-003
- **Status:** DRAFT. Focused source inspection and abstract race reproduction complete.
- **Topics:** agent loops, durable execution, context management, approval, endpoint authorization, continual evaluation
- **Prepared by:** Codex. Review scope in EC-SCI-2026-003.
- **Created / last source inspection (UTC):** 2026-11-16
- **Applicable claims:** EC-SCI-2026-003, proposed 2037 ASIMOV architecture
- **Snapshot:** publisher dates, protocol versions and access date below
- **Preservation:** Original synthesis, model and protocol draft

## Executive finding

A modern agent harness runs a control loop around model inference. It gathers context, passes tool results back to the model, schedules or stops work, and maintains enough state to resume. Current implementations document context compaction, durable task records, per-tool permissions and human approval. First-party coding-agent reports demonstrate utility on particular tasks. These features establish credible building blocks for future workflows, while their action coverage depends on where permissions are checked. A hook in a function-tool pipeline may never see shell commands, hosted tools or handoffs. An approval stored in resumable task state is also exposed to changes in arguments, tool versions, policy or the resource by the time work resumes.

The strongest analogue for post-Lucien ASIMOV is the combination of a replaceable planning harness, durable bookkeeping, and independently administered authorities at the effect endpoints. Treat the transcript, progress summaries, model output and tool responses as inputs. Store authorization epochs, confirmations, quotas and receipts in a separate trusted state. A finite schedule exercise shows why the commit point matters. A broker that checks before two queued sends can authorize duplicated or already-revoked work. A transactional endpoint can serialize a single use and local revocation if both participate in its commit order. Devices and remote third-party APIs still need their own failure and observation contracts.

## Technical account

### Methods and current evidence

| Surface | Current primary evidence | ASIMOV inference |
| --- | --- | --- |
| Execution loop | OpenAI documents inference → tool request → result in context → next turn. Compaction substitutes a smaller continuation state. | Context is neither a reliable policy store nor an effect journal. Retain immutable references rather than allowing a summary to regrant access. |
| Long-horizon work | Anthropic reports initializer scripts, explicit feature lists, Git history, progress files and end-to-end smoke tests across coding sessions. | Recovery gains from external state with independent checks. In a household, an actuator receipt is stronger completion evidence than the model saying it finished. |
| Approval and isolation | OpenAI Agents SDK supports pauses and serialized run state. The function-tool guardrail pipeline excludes several built-ins, hosted tools and handoffs. | A boundary must enumerate every actual effect route, including alternate process and network paths. Inspect config and extension surfaces for privilege escalation. |
| Durable execution | Temporal documents deterministic replay and activities that may re-execute when a completion is lost. | An endpoint idempotency key deduplicates known retries only if it guards the actual mutation. A non-transactional action with an uncertain outcome must reconcile before retry. |
| Connector auth | MCP's dated authorization profile validates token audience and disallows passing arbitrary tokens through to downstream APIs. Its security guidance discusses confused deputy and local server compromise. | Connector authentication does not establish user consent to the concrete effect. Type and bind operations at the receiving authority. |
| Improvement loop | An OpenAI cookbook uses five traced runs of a fictional diligence task, curated feedback, generated evaluation cases and a report for harness changes. | An offline trace-to-test-to-change loop is feasible. Separate evaluation and signing authority from the candidate harness. Five synthetic runs give no deployment failure rate. |

Inspection was a scoped primary-document review. It did not include product source builds, a benchmark rerun, current product security certification, or direct X coverage. The August 2026 OpenAI platform report gives an example of harness configuration sensitivity, with a reported ARC-AGI-3 score increase from 13.3% to 38.3% under retained reasoning and compaction. This is a vendor result for that configuration and task, not an estimate of safety or a controlled general comparison of commercial systems.

### Quantitative results and reproducibility

Run `python3 studio/experiments/asimov/2037/check_commit.py`. The original experiment enumerates 5! / 4 = 30 linear orders of two ordered check/send pairs and one unconstrained local revoke. Both attempts carry one effect identity, and a revoke monotonically advances the local epoch. With separate broker check and trusted send there are 12 duplicate schedules and 14 late-commit schedules. With atomic endpoint check and commit there are zero in either category. These are counts of finite schedules, which may overlap and are assigned no probabilities.

Illustrative sizing for 2037 uses 2 KiB of retained metadata at 1,000 effects/day, or 30,000 × 2 KiB ≈ 58.6 MiB per month. At 500 confirmations/day × 5 seconds, the human workload is 2,500 seconds, about 42 minutes per day. These examples expose storage/privacy and human-attention constraints. They do not estimate a real household's behavior. The remote revocation window depends on time/freshness assumptions. A 10 s issuance-to-commit lease plus no more than 0.1 s aggregate timing error has a 10.1 s bound only if the endpoint makes the check at commit.

### Limitations and relevance

The simulator has no distributed database, clocks, authentication, hardware, or cryptography. Scope at-most-once to one effect identity at one transactional endpoint. Tickets with new IDs, compound effects, external services, backups and uncertain physical outcomes all require more evidence. Signed receipts can authenticate attribution without proving completeness, consent or what a sensor should have seen. Cassette-like replay of a model trajectory is not assumed. Replaying control state and selected recorded decisions is a different operation from regenerating stochastic outputs.

A credible 2037 household profile requires separately governed interior egress, local authority revocation, evidence access and resident permissions. The relevant Genesis scenes portray asymmetry, restart and contested evidence. The current draft says national attention fades, so broader reform is a scenario inference, not a manuscript event. See the [scenario](../../../experiments/asimov/2037/README.md) and [protocol](../../../experiments/asimov/2037/PROTOCOL.md).

## Source and provenance ledger

All sources accessed 2026-11-16. Living docs are dated snapshots by access date.

| Type | Source | Version or identifier | Original URL | Scope |
| --- | --- | --- | --- | --- |
| Vendor engineering account | Michael Bolin, OpenAI, Unrolling the Codex agent loop | 2026-01-23 | https://openai.com/index/unrolling-the-codex-agent-loop/ | Loop and compaction |
| Vendor engineering account | Bonamy and Choi, OpenAI, Codex as a platform | 2026-08-19 | https://developers.openai.com/blog/codex-as-a-platform | Harness hosting and illustrative vendor task result |
| Vendor engineering account | Anthropic, Effective harnesses for long-running agents | 2025-11-26 | https://www.anthropic.com/research/effective-harnesses-for-long-running-agents | Incremental coding workflow |
| Maintainer docs and example | OpenAI Agents SDK, Human-in-the-loop and Guardrails | Python living docs; guardrails main snapshot | https://openai.github.io/openai-agents-python/human_in_the_loop/ and https://github.com/openai/openai-agents-python/blob/main/docs/guardrails.md | Approval serialization and coverage limits |
| Maintainer docs | Temporal Activity Definition | Living docs | https://docs.temporal.io/activity-definition | Idempotency and retry semantics |
| Specification and guidance | MCP Authorization and Security Best Practices | 2025-11-25 | https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization and https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices | Audience and downstream boundary |
| Vendor executable example | Wesley Pasfield, OpenAI, Build an Agent Improvement Loop with Traces, Evals, and Codex | Cookbook snapshot | https://developers.openai.com/cookbook/examples/agents_sdk/agent_improvement_loop | Five synthetic traced runs |
| Primary specification | The Update Framework | 1.0.37, 2026-10-08 | https://theupdateframework.github.io/specification/latest/ | Version, expiry, role separation, thresholds |
| Primary specifications | IETF CBOR, COSE and DPoP | RFC 8949, RFC 9052, RFC 9449 | https://www.rfc-editor.org/rfc/rfc8949, https://www.rfc-editor.org/rfc/rfc9052, https://www.rfc-editor.org/rfc/rfc9449 | Deterministic encoding, signing structures, proof-of-possession analogue |

## Local evidence and reconstruction

To reproduce the race by hand, let two workers read the same initial epoch and unused ID before either sends. In the split design, both cached allows can fire. Insert revocation between checks and sends to produce a late commit. In the serialized design only the first use can consume the ID, and a revocation ordered first prevents both. Conceptually separate planning state, authorization state and endpoint evidence. This argument does not validate a real distributed implementation.

## Related records

- [EC-R-2026-001](EC-R-2026-001-hardware-mediated-ai-safety.md) and [EC-R-2026-002](EC-R-2026-002-asimov-indexed-axis.md)
- [EC-SCI-2026-003](../../reviews/EC-SCI-2026-003-asimov-effect-authority.md)
- [Genesis Protocol](../../../../stories/the-divine-register/genesis-protocol.md)

## Revision history

- 2026-11-16 — Initial source map, race model and proposed 2037 stack. Independent source-fidelity review pending.
