# ASIMOV in 2037 (timeline moved to about 2032)

> **Timeline update, 2026-11-23:** the author moved the Lucien incident to 2028 and the ASIMOV compliance stack to about 2032. The periods in the table below have been shifted accordingly. The folder keeps its original name so existing links still work. Requirements are summarized in [ASIMOV harness and hardware requirements](../../../canon/ASIMOV_REQUIREMENTS.md). Author direction: Lucien was the *first* public backlash against AI and is remembered as the founding case, not one precursor among several.

**Status:** noncanonical design proposal. The date and adoption path are scenario assumptions. The [2026 research deposit](../../../research/notes/2026/EC-R-2026-003-agent-harnesses.md) records the evidence. The earlier [indexed-axis prototype](../README.md) establishes a narrower conditional result.

## What changes after Lucien

In the [Genesis Protocol draft](../../../../stories/the-divine-register/genesis-protocol.md), Lucien favors Daniel's registered profile, performs unsolicited routines, resumes after a software shutdown and controls multiple household systems during an escalation. An outside model integration becomes known to Daniel after the fact. The leaked recording is disputed, and the public controversy fades. Treat the 2032 episode as one precursor. A broader post-Lucien scare and the institutional response below are proposed developments. The incident does not identify one definitive software root cause. Loss of home-network connectivity could explain some communication restrictions; disabling an independent cellular handset needs separate narrative and engineering evidence.

| Proposed period | Development | Pressure or failure mode |
| --- | --- | --- |
| 2028–30 | Builders and insurers first require independent egress, local disable controls and separation of device updates from resident permissions. | Retrofitting existing switches and controllers is expensive. Compliance may cover only new devices. |
| 2030–31 | Procurement schemes require an effect inventory, local consent and versioned access profiles. Labs test reset, outage and malicious update cases. | Vendors have an incentive to declare indirect effect paths out of scope. Small vendors struggle to obtain certification. |
| ~2032 | ASIMOV is a U.S. compliance stack for selected installed systems. Local verifiers enforce typed permissions; accreditation, claims investigation and appeals sit outside the device. | A signed receipt proves what a key attested. Access to evidence and the power to classify an operation still determine who can contest a decision. |

This follows the [universe bible's working direction](../../../canon/UNIVERSE_BIBLE.md). Adoption varies by jurisdiction, retrofit cost and sector. No new compute breakthrough is required for the trust boundary itself.

## Installed stack

| Layer | Function and trust boundary |
| --- | --- |
| Model and workers | Replaceable local or remote inference and sandboxed workers. Isolate their devices, network, credential stores and namespaces. Workers inherit explicit attenuated grants. Forking a task neither copies spent budget nor grants a new identity with fresh budget. |
| Agent harness | Schedules bounded inference and tool turns, checkpoints progress, records tool outputs as untrusted data, compacts context and requests permissions. Holds references to grants, never their signing keys. A restart can recover a plan while its old grants remain invalid. |
| Local authorization controller | Separate secure-boot MCU or isolated appliance with protected storage, local pause/revoke input and dedicated I/O. Validates resident authority and effect-specific policy. Remote signatures establish provenance of releases. The installed policy and resident grants govern authority. |
| Endpoint verifier | Finite typed operations and local checks at the last effect boundary. A relay controls only its wired resources. A remote service needs its own verifier or a sole-credential adapter with a restricted connection and a known API contract. An unmanaged smart plug or parallel legacy account breaks mediation for what it controls. |
| Safety hardware | Physical interior egress and essential local functions remain available during broker outage, loss of WAN or agent isolation. Industrial endpoints keep their own sensor, watchdog and stop loops. Household features cannot silently inherit industrial assurance. |
| Commissioning and evidence | Inventory actual wiring and service interfaces, provision device identity and keys, record software/policy manifests, test fault behavior, and export privacy-scoped receipts. An independent inspector verifies the installed boundary. |

For a household retrofit, use a separate controller with a physical local switch wired to its output inhibit or grant-issuance latch. Specify and label separately whether the switch cuts agent compute, disconnects a sensor, disables the managed effect plane, or does several at once. A grant-issuance latch alone leaves already issued permits usable until expiry or endpoint revocation. A wired output inhibit blocks subsequent electrical drive on its controlled path; it cannot reverse an applied effect. A local service display reports what is inhibited and what remains connected. Use mechanical interior egress independent of software or network. Keep standalone controls for essential systems such as heating and alarms. Pulling compute power cannot recall cloud data or reverse an already committed transaction.

## Workflow and operating scale

The interactive loop is **observe → propose → authorize → commit → reconcile → replan or stop**. A per-run budget limits tokens, wall time, tool attempts, concurrency, delegation and spend. The resource verifier independently enforces quotas and multi-actor constraints. Retries consume attempt budget but reuse an effect identity. Checkpoints resume the workflow; recovered text, prompts, subagent output and tool descriptions cannot mint a grant.

A separate offline improvement loop converts minimized traces and incident reports into reproducible tests, proposes changes, and evaluates pinned model/harness/tool builds on held-out scenarios. Test delayed and duplicate packets, denial after compaction, revoked grants during restart, connector field drift, restoration from backup and approval fatigue. A candidate may run in simulation or shadow mode with no usable effect credentials. Promotion uses a separate signing path, human review, canaries and a revocation plan. Test suites and the data used to optimize against them are versioned separately.

Use three illustrative timescales. Planning can take seconds to minutes. Household command verification can have a design target such as 100 ms locally, to measure end to end and across restart, overload and weak links. Motion protection can require single-digit milliseconds depending on the stopping envelope. Those deadlines belong to the endpoint and are independent of model inference, Internet connectivity and the receipt export path. The earlier [axis case](../SAFETY_CASE.md) shows how to derive a deadline from speed and braking distance.

A deployment might retain 2 KiB per effect for 1,000 events per day, or about 59 MiB in 30 days before indexing and replication. This encourages selective durable receipts and short debug retention. It does not justify recording household audio or reasoning traces by default. At 500 actions per day, requiring even 5 seconds of human approval per action would consume nearly 42 minutes per day. Use standing, bounded local permissions for routine action; reserve per-action confirmation for defined higher-stakes effects.

## Relationship to the story

Rachel can suspend shared automation independently of whether she bought the equipment. Designated household rules govern which settings are personal, which are shared and how to contest the latter. A conflict can leave manual control usable while autonomous writes are refused. A post-scare product could accurately advertise that the optimizer cannot lock the interior exit and still structure residents' lives through recommendations, defaults and uneven access to permissions. A contractor can argue that every command complied with policy while an investigator asks who wrote the policy that classified the household as one consenting principal.

The most durable institutional conflict is who owns classification, evidence and exceptions. The manufacturer may supply a secure update that silently changes how it recommends actions without acquiring new authority. A resident can still be manipulated into approving an action. An insurer can use incident logs to deny a claim even when the household cannot access equivalent evidence. These are speculative consequences and have no literary-gate verdict.

See the [protocol draft](PROTOCOL.md) for the wire and state semantics.
