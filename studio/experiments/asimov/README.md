# ASIMOV reference prototype

The fictional [ASIMOV Stack](../../canon/UNIVERSE_BIBLE.md#institutions-and-lineages) takes its name from Isaac Asimov. Its in-world expansion is **Autonomous Systems Integration, Mediation, and Operational Verification**.

Noncanonical engineering research for one guarded horizontal indexing stage. The hypothesis is that an independent authorization controller can enforce a precisely specified motion restriction at a completely mediated interface, given bounded sensing and plant behavior.

| Document | Contents |
| --- | --- |
| [Architecture](ARCHITECTURE.md) | Authority, trust roots, interfaces, hardware options and bench design |
| [Threat model](THREAT_MODEL.md) | Adversary, bypasses, shared dependencies and falsification |
| [Safety case](SAFETY_CASE.md) | State model, invariant, proof and timing budget |
| [Results](RESULTS.md) | Commands, test outcomes and counterexamples |
| [Research deposit](../../research/notes/2026/EC-R-2026-002-asimov-indexed-axis.md) | Durable method, findings and original-source ledger |

Run from the repository root with Python 3.10 or newer. No third-party packages required.

```sh
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=studio/experiments
python3 -m asimov.simulation.planner | python3 -m asimov.simulation.run
python3 -m asimov.simulation.run --demo
python3 -m asimov.formal.check
python3 -m unittest discover -s studio/experiments/asimov/tests -v
```

The simulation consumes request bytes over stdin and owns its in-memory plant. It runs no planner-supplied code. The pipeline illustrates an interface boundary. Deployment isolation, cryptography, measured timing and physical validation belong to the proposed bench prototype.

For the proposed post-Lucien deployment and its effect authorization protocol, see [ASIMOV in 2037](2037/README.md).
