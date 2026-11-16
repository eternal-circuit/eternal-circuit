# ASIMOV effect authorization protocol

**Design draft v0.1, 2037 scenario.** Example profile for transactional digital effects and separately specified local devices. Wire format, cryptographic algorithms and fault domains require engineering review.

## Names and records

- **Principal:** authenticated resident or organization entitled to authorize an effect. **Subject:** isolated workload instance presenting a request. A credential authenticates a subject or key and carries no inherent household permission.
- **Effect registry:** commissioned, versioned list of endpoint IDs, operation IDs, units, parameter ranges, execution mode, data sensitivity and observer scope. Use separately typed disclosures as effects, even when the source API calls them reads.
- **Intent:** subject and run identifiers, endpoint audience, operation and schema version, canonical parameters, unique effect ID scoped to issuer/tenant and endpoint, current resource revision or conditional precondition, and optional expected outcome. Record digest is domain-separated by protocol and record type. Display fields derive from the same validated intent.
- **Grant:** signed issuer, subject-key binding, intent digest, endpoint audience, scope, policy and revocation epochs, expiry or endpoint challenge, usage budget and required approval references. Standing grants cover a narrow parameter domain; the authorization controller materializes individual intent-bound permits. Delegation can only narrow rights, expiry and resource ceiling and is charged to the same parent budget.
- **Receipt:** endpoint-signed effect ID, intent digest, decision, result or observation class, applicable epochs, endpoint boot identity, sequence/checkpoint and permitted reason code. Record `accepted`, `applied`, `observed`, `denied` and `unknown` distinctly. An MCU energizing a relay cannot infer the commanded physical state without a suitable independent observation.

Proposed encoding uses deterministic CBOR with an explicit schema and COSE signatures. Bound sizes and reject duplicate map keys, unknown critical fields, unsupported versions and noncanonical encodings. Fix units and integer ranges per operation; do not let an endpoint and an approval UI interpret the same argument differently. Bind use to a proof-of-possession key at the connector or endpoint and verify the channel or challenge binding. If a workload can ask a key proxy to sign any request, that proxy is part of the authorization boundary. The choice of suites and key provisioning is open. [CBOR](https://www.rfc-editor.org/rfc/rfc8949), [COSE](https://www.rfc-editor.org/rfc/rfc9052) and [DPoP](https://www.rfc-editor.org/rfc/rfc9449) are components or analogues, not evidence that this composition is secure.

## Commit and recovery

1. Persist an intent at the harness or broker before sending. Human confirmation, when required, renders target, exact arguments, relevant affected resident and data destination from a trusted display path; authorization binds to that intent and policy. Approval text in the planner transcript has no standing.
2. At the effect endpoint verify the presented identity, signer, audience and canonical intent digest. An existing effect ID bound to the same digest may return an existing receipt to a separately authorized reader; a reused ID with another digest is a conflict. Neither path repeats the effect.
3. Inside the commit transaction, atomically check and claim a unique scoped effect ID. Check active revocation and policy epochs, deadline, device mode, current resource revision, applicable resident permissions and remaining shared budget **at commit**. Where the endpoint owns a transactional resource, conditionally advance its state, debit budget and persist the effect identity and result in one strictly serializable transaction ordered with local epoch updates. Retain deduplication information at least until every authorization for that identity has expired and recovery cannot resurrect it. Prevent backup restore from rolling back the epoch or accepting retired identities.
4. When an acknowledgement disappears, query the endpoint with the same ID and reconcile from its authorized receipt. Deduplication covers a scoped identity. Reissuing a new ID for a semantically equivalent act can double the effect. When live state has changed, replan and reauthorize against the new state. Repeated invalid, denied or conflicting requests terminate the loop on attempts or budget.
5. An external connector with no atomic deduplication, idempotent set-to-state contract, or reliable effect observation can return `unknown` after a send/crash boundary. Persist a pending record before isolated dispatch and reconcile or ask an operator. Do not automatically resend. A physical stroke uses a device-specific one-shot commit and recovery procedure. Software journaling cannot make the motion and disk write atomic.

Use trusted monotonic time/challenges for local permits, and define how epochs and time survive resets. If trusted time or persistent state is unavailable, deny new managed commits until recovery. A verifier that checks only at the broker can still apply a delayed command after revoke. Use a shared lock or atomic epoch fence at the resource write, and acknowledge local revocation only after that fence advances. If a commit already won that ordering, report it as committed before revocation. Across partitions choose explicitly to refuse new high-consequence writes without freshness, or allow a short offline window for predefined low-consequence writes. For example, a 10 s maximum endpoint-measured lease with at most 0.1 s aggregate clock/validation uncertainty yields up to 10.1 s of residual exposure from the last valid issuance, provided the verifier rejects late commits and the uncertainty bound covers the entire issuance-to-commit path. Immediate global revocation is unavailable across a partition. Revocation cannot reverse a committed act.

## Three distinct controls

| Control | Semantics |
| --- | --- |
| Pause a run | Stop scheduling new model turns and dispatch. Outstanding requests may still reach an endpoint. |
| Revoke managed authority | Advance the local authorization epoch and inhibit affected managed commits. A resumed or forked plan must obtain new authority. Recovery cannot decrement the epoch. |
| Physically isolate | Operate a wired control that disables a specified power, bus or sensor path. Document coverage and preserve essential local functions. This is device-specific. |

## Updates and evidence

Pin model, prompt, harness, connector, registry and policy versions in a deployment manifest. Use secure boot and threshold-signed release metadata with expiry, monotonically advancing versions and a separate authorization-policy channel. Runtime optimization cannot sign a new effect profile. An approved rollback packages known-good code under fresh, authorized metadata while preserving the current safety floor, revocation history and identity state. Commissioning tests include network loss, rollback after brownout, UI-versus-wire intent mismatches and unauthorized alternate paths.

Hash-chain receipts with sequence numbers and periodically export signed heads to independently controlled witnesses. Keep detailed payloads encrypted locally where practical, separate access to evidence from power to authorize, and provide resident export and dispute paths. An independent witness with an established checkpoint cadence can flag an overdue checkpoint or sequence gap. A compromised signer can fabricate records under its key, and hashing predictable values alone does not make them private.

## Review targets

- Concurrent retries with one ID yield at most one transactional state transition.
- Updating an epoch before the endpoint commits a permit invalidates that permit.
- Replay after reset, reassignment, delegation or backup restore cannot regain spent rights.
- Removing all planner and broker network access leaves hardware egress and essential local controls available.
- Every connector path and cross-resource composition needs its own coverage, identity and failure argument. Separate valid single-resource actions can combine into an unsafe household outcome.

No protocol interoperability, hardware timing or physical-state guarantee has been established for this draft.

## Executable race check

Run `python3 studio/experiments/asimov/2037/check_commit.py` from the repository root. It enumerates all 30 schedules of two check/send pairs for one effect ID and one local revocation, with each check preceding its corresponding send. A broker-only check followed by unquestioned execution produced 12 schedules with duplicates and 14 with a commit after revocation. These sets overlap. Serializing epoch validation and effect-ID consumption with the endpoint commit yielded zero in both categories. This is an exhaustive result for five events and one resource, not a penetration test, crash-consistency test, or frequency estimate. Persistence, identity, network partitions and actual transactions are outside this model.
