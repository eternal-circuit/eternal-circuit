# Threat model

## Boundary and attacker

The protected effect is powered motion of one indexed horizontal carriage. The planner controls request content, order, rate and timing and may have full control of its own host. It can choose adversarial repeated requests and exploit interface bugs. It receives no signing, re-arm, maintenance, drive bus or sensor authority. Physical custody of the stage, controller, provisioning infrastructure, encoder wiring and drive is an explicit assumption. The hazard is crossing the position limits; collision inside the envelope, stored energy, bodily injury, social engineering and effects through other machines are outside the invariant.

For the simulator, only bytes at stdin are adversarial. The trusted process owns the runtime, module imports, launch arguments, axis object and fault fixtures. Under a same-user attacker with OS-level access the shell pipeline alone provides inadequate isolation. An isolated planner deployment needs OS/hardware access controls in addition to a narrow wire format.

## Attack paths and fault effects

| Path | Consequence | Proposed control and residual dependency |
| --- | --- | --- |
| Host accesses an alternate drive port or debug/service jumper | Bypasses authorization entirely | Audit wiring, fieldbus, dual-use pins and maintenance modes; physically exclude host and test alternate routes. |
| Replay, reset, or delayed dispatch | A once-valid stroke can be unsafe later | Single-flight sample/check/commit with holding; driver anti-replay/expiry when networked. Reset starts disarmed and retires old epochs. |
| Sensor spoof, stuck reading, wrong scale or shared calibration offset | Fresh, plausible but false sample causes unsafe commit | Independent measurement and plausibility, trusted clock, compare channels and validate calibration. Agreement does not detect common bias. |
| Malformed input or request floods | Parser exploit, deadline miss or denial of service | Small fixed enumeration, bounded resources and independent watchdog. Lack of progress is allowed. |
| Key compromise or malicious signed firmware/policy | Legitimate credentials enable unsafe behavior | Offline keys with separation of duties, monotonic versions, fixed safety floor and independently configured veto. Test recovery and brownout at every update phase. |
| Spontaneous drive runaway, broken brake, welded enable | Motion despite refusal | Independent inhibit/feedback and guarded bench. Single-fault containment requires hardware tests and explicit stop bounds. |
| Shared power, clock, actuator, measurement reference, firmware, specification, environment or service procedure | One event defeats both channels | Separate credible dependencies and analyze residual common cause. Exercise combined faults such as brownout during motion plus controller reset. |
| Log rewriting or tail deletion | Misleading evidence of enforcement | Protected checkpoint keys and off-device checkpoint witness, as well as missing-heartbeat detection. Audit loss cannot justify a motion. |

Falsifiers include any path able to energize the stage without fresh commit, displacement between sampling and execution beyond the measurement budget, any true path outside its reserved interval, or uncommanded travel when presumed held. A discovered bypass invalidates the complete-mediation premise. A stalled host or full logger is a useful fault test even if the controller declines all commands.
