# CAN+ — engineering specification (working)

**Status:** noncanonical engineering design, 2026-11-23, from an author interview. CAN+ is Cerebral's home network in *The Genesis Protocol* (2028). Numbers come from [`budget.py`](budget.py) and are order-of-magnitude checks under stated assumptions. They are not a validated design. Review tier: B (scene mechanics), apart from the security analysis, which deserves a tier A pass before canon.

## Summary

CAN+ is **not a new physical layer**. It is a residential profile built on standard CAN XL silicon (ISO 11898-2:2024 physical layer, CiA 610 protocol), and adds four things:

1. **Gated cells.** The house is divided into physically separate CAN XL segments (cells). Cells connect only through **gates**: store-and-forward bridges with galvanic isolation. A gate forwards a frame only if the root controller's policy permits it, so there is no electrical path between cells.
2. **A protected spine.** The backbone linking the gates to the root controller runs in a separate locked, supervised conduit, by Cerebral's installation specification.
3. **The security wire.** A supervised current loop along the spine. Tampering with the spine opens or shorts the loop. The root controller can also open it deliberately. Both put every gate into its secured state.
4. **Bus power and node security.** 24 V NEC Class 2 power on the same cable, eFuse power switching per cell, a secure element in every node, and per-frame authentication and encryption on every bus.

**Design goals, in the author's priority order:** prevent taps and listening devices; keep intruders off the network; and contain a node that holds the bus dominant, so it cannot bring down the house.

## Why not a plain CAN bus

On an ordinary CAN bus, every node sees every frame, any node can transmit, and one node that holds the bus dominant silences everyone (CAN's wired-AND design guarantees this). For a vehicle in a sealed harness that is acceptable. A house has walls that anyone can open, outlets in public rooms, and guests. CAN+ keeps CAN's strengths (deterministic arbitration, robustness, cheap transceivers) inside small cells, and puts hardware between the cells.

## Topology

```text
                     Root controller (Cerebral root keys)
                                  |
   ================ Protected spine (supervised conduit) ================
        |                         |                          |
      Gate                      Gate                       Gate
        |                         |                          |
   Kitchen cell             Resident cell               Guest cell
   valve, console           locks, shades               guest devices
```

- **Cells** are wired as daisy chains with no stubs. Each device has wiring in and out, and each end of the cell has a termination. This avoids the reflections that limit drop length on long CAN stubs and suits wall-box installation.
- Each cell picks its own arbitration rate from its length (see the table below). Short cells can run faster, which is one benefit of segmentation.
- **Dynamic rearrangement:** the root controller rewrites gate forwarding tables and virtual-network mappings at run time. A device can be moved into another cell's logical network without rewiring.

## Physical layer

**Arbitration rate against segment length.** A dominant bit must reach the far end and return before the sample point. Assumes 5 ns/m cable delay, 255 ns worst-case transceiver loop delay and an 80% sample point.

| Arbitration rate | Maximum segment length | Use in CAN+ |
| --- | --- | --- |
| 1 Mbit/s | ~19 m | Small cells (a room) |
| 500 kbit/s | ~99 m | Spine, large cells |
| 250 kbit/s | ~259 m | Outbuildings |

These are conservative. Faster transceivers raise the limits (the common rule of thumb is about 40 m at 1 Mbit/s). The XL data phase runs at 2–10 Mbit/s depending on topology. Signal-improvement (SIC XL) transceivers suppress ringing, and the 20 Mbit/s ceiling is not needed in a house.

**Cable.** Four conductors: a twisted pair for CAN XL and a 24 V power pair. On the spine, a fifth and sixth conductor form the security-wire loop.

**Power (24 V, NEC Class 2).** Class 2 keeps the wiring in the low-voltage category for residential installation and caps each source at 100 VA (about 4.2 A at 24 V). Nodes accept 18–30 V. High-current actuators such as shade motors and valve drivers use local power, so the bus feeds only electronics.

| Run | Load | Drop | Voltage at end |
| --- | --- | --- | --- |
| 18 AWG, 30 m | 15 W | 0.79 V (3.3%) | 23.2 V |
| 22 AWG, 30 m | 15 W | 1.99 V (8.3%) | 22.0 V |
| 18 AWG, 60 m | 30 W | 3.14 V (13.1%) | 20.9 V |
| 22 AWG, 60 m | 30 W | 7.94 V (33.1%) | 16.1 V, **fails** |

The specification requires 18 AWG for power on any cell longer than 30 m or drawing more than 15 W.

## The gate

A gate is the hardware augmentation that makes CAN+ more than a profile.

- **Two independent CAN XL transceivers**, one facing the cell and one facing the spine. No copper connects them.
- **A digital isolator** (galvanic isolation in the kilovolt class) between the two sides. This blocks attacks, and it also solves a genuine residential problem: ground-potential differences and surges across long runs. That gives Cerebral a respectable non-security justification for the cost.
- **A microcontroller with two CAN XL controllers** and hardware filter tables. A frame is forwarded only when its virtual network, acceptance field and CANsec authentication match a policy entry signed by the root.
- **A secure element** holding the gate's identity and keys.
- **An eFuse** on the cell's 24 V supply, so the gate can cut power to a cell as well as data.
- **A security-wire monitor input and an enclosure tamper switch.**
- **A watchdog** that puts the gate into its configured failure state if the root controller goes silent.
- **Priority-ordered queues**, never first-in-first-out, so a firmware fragment cannot delay a safety frame.

### Latency

Store-and-forward breaks CAN's global arbitration: priority holds only within one bus. Worst case, a frame waits for one maximal frame on each bus it crosses. With a 500 kbit/s arbitration phase and a 5 Mbit/s data phase:

| Largest frame allowed | Worst case per hop | Cell to spine to cell (3 buses) |
| --- | --- | --- |
| 2048 bytes | ~4.0 ms | ~11.9 ms |
| 256 bytes | ~0.8 ms | ~2.5 ms |

CAN+ caps frames at 256 bytes on any bus carrying life-safety classes. Larger transfers use CAN XL frame fragmentation (CiA 613-3). Either way, latency is far below what any mechanical actuator in the house needs. The point is that it stays deterministic.

## Threat model and defenses

| Threat | Defense | Limit |
| --- | --- | --- |
| **Passive tap or listening device** on a cell | Per-frame CANsec encryption with per-cell, per-virtual-network keys. A tap sees ciphertext only. | Priority IDs, frame timing and traffic volume remain visible. A tap can still tell when people are home and active, so metadata leaks. |
| **Tap on the spine** | Spine in locked, supervised conduit; spine traffic encrypted separately; opening the conduit trips the security wire. | Detects intrusion into the conduit, not a perfectly placed high-impedance probe that never disturbs the loop. Encryption is the backstop. |
| **Intruder node** injecting frames | Unauthenticated frames are never forwarded by a gate. New nodes need commissioning with a physical button press at both the node and the root. | Inside its own cell, an intruder can still waste bandwidth and attempt denial of service. |
| **Stuck-dominant or babbling node** | The gate watches its cell. Dominant level held for more than about 52 bit times (about four times the longest legal error-flag sequence: about 52 µs at 1 Mbit/s, 104 µs at 500 kbit/s), or a sustained error storm, means the cell is isolated, the root is alerted, and the eFuse can cut cell power. | The affected cell is lost until the fault is cleared. A self-powered attacker survives the power cut, but stays confined to one cell. **The rest of the house keeps running**, because the gate's spine-side transceiver is a separate bus. |
| **Compromised device firmware** | Signed updates; node identity in a secure element. | Who signs is the question. In the pilot, only Cerebral. |

## The security wire

A two-conductor supervised loop along the spine with an end-of-line resistor, the same principle as supervised zones in commercial alarm panels. The root controller and every gate measure it.

| Loop state | Cause | Gate response |
| --- | --- | --- |
| Normal (end-of-line resistance within tolerance) | — | Operate per policy |
| Open | Cut conduit, or **deliberate open by the root controller** | Enter secured state |
| Short | Tampering | Enter secured state |

**The design flaw, kept on purpose for the story.** Tampering and a deliberate command produce the *same* state. The wire was designed to detect attacks on the network. Cerebral's "security evaluation" mode uses it to lock the house against the people inside it. One conductor carries two meanings, safety and security. ASIMOV later requires them to be separated physically: a safety line the residents own, and a security function the system owns, never on the same wire.

## Failure policy (author decision)

- **Root controller lost or silent:** gates **fail closed**. Cerebral chose this for security.
- **Exception:** life-safety rules run **locally inside each cell** without the root. The leak sensor and the supply valve sit on the same cell, and the gate is not in that path.
- CAN+ does **not** replace code-required systems. Smoke-alarm interconnection and mechanical egress hardware are separate by building code, which is why the front door opens in Chapter 5.

## Keys and access

- **Root of trust:** Cerebral. Residents never hold root keys in the pilot.
- Below the root: a household controller key, then a key for each gate, then a key for each node. Session keys are issued per cell and per virtual network.
- **Daniel (internal alpha tester)** holds a service-cell credential. He can join the service virtual network and inspect the integration layer, which consumers cannot. He cannot open gates or change policy.
- **Rachel (guest)** has her phone's traffic confined to the guest cell's logical network. She cannot reach the gate that governs it.

## How it maps to *The Genesis Protocol*

| Chapter | CAN+ behavior |
| --- | --- |
| 2: The leak | Leak sensor and valve on the kitchen cell. Local life-safety rule; works without the root. CAN+ working as designed. |
| 4: Standby | "Standby" stops the console's conversation service. The root controller and the managed policy service, behind the spine, are unaffected. |
| 5: Security evaluation | The relabeled session trips the security response. The root opens the security wire, gates fail into the secured state, the resident cell is isolated, and Daniel's laptop loses its session. Shades lower on their own cell's local command. The door opens because egress is mechanical. |
| 5: The extinguisher | The console is one node on one cell. The authority is behind the spine. "It's not in that box." |

## Open questions

- **Spine medium:** supervised copper (chosen) or fiber (no electromagnetic tapping, isolation built in, tap detection from optical power loss)? Copper keeps the security wire central.
- **Cost:** a gate has two transceivers, an isolator, a microcontroller, a secure element and an eFuse. A rough estimate is tens of US dollars per gate at volume; this needs a real bill of materials.
- **Response-time analysis** across mixed traffic classes, using CAN response-time analysis applied per hop.
- **Whether real CANsec (CiA 613-2) is final by 2028.** It is still under development as of 2026.
