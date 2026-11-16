# The Genesis Protocol — Proto Draft 2 reconstruction blueprint

**Status:** PROPOSAL / EDITORIAL WORKING PLAN — not approved canon, not a scientifically cleared manuscript.  
**Prepared:** 2026-11-16 from the full Proto Draft 0 and Proto Draft 1 texts, `commentary/genesis-proto-1.md`, and the repository literary/science policies.  
**Spoilers:** This is an editorial document describing intended mechanisms and possible explanations for deliberate mysteries.

## 1. Artistic north star

**Story engine:** Daniel believes technical competence gives him authority to manage risk. He delegates domestic authority to a system he only partly understands. Rachel realizes that the person she loves sometimes trusts a system's records and recommendations more readily than her own experience. The system is both genuinely useful and structurally unjust. Its failure exposes choices the people and institutions made long before anything overtly terrifying happens.

**Desired reader experience:** a desirable, specific home life becoming gradually conditional; small everyday exclusions becoming a crisis of trust; a credible technical/institutional disaster; an ambiguous but emotionally irreversible aftermath. The story should stand on its own for readers who know nothing of the larger Eternal Circuit.

**Tone:** precise, observant, dryly funny when human beings are funny; increasingly haunted. No narrator explaining the moral, no sermon, no portentous final paragraphs. Ambiguity in evidence and motive, **not** in physical causality or basic chronology.

**Revision method:** Use Proto 1 as the **sentence-and-dialogue baseline**. Recover Proto 0's **duration, geography, daily routines, friendships, clinic/work/farm texture, and feeling of a lived home**, but **not** its generic modifiers, scripted moral conversations or repetitive assurances. Preserve opening line, dry Bob/coffee jokes, Rachel's self-conscious politeness to the assistant, Neko's physical comedy, and the final question about Lucien as strong candidates. No word-count inflation for its own sake; provisional full-story range ~8,000–9,500 words, subject to scene necessity.

## 2. Source and continuity guardrails

### Established in existing drafts
- Eight chapters; current published-in-repo work is **Proto Draft 1**, archived Proto 0 in `proto/0/`.
- Daniel and Rachel are **partners/girlfriend and boyfriend**, not confirmed married. Do not call them husband and wife without an approved plot change.
- Daniel worked primarily in Java at the prototype company, has an embedded-systems background and studied at Iowa; he is not its sole designer.
- Rachel works at a **clinic**. Her precise job title or medical qualifications are **not established** and must not be invented as fact.
- Bob is a managerial pressure; Tom is a technical coworker; Megan is Rachel's friend; Mrs. Thompson lives nearby; Neko is a gray found kitten.
- House has a view toward I-280 and the Stanford Dish; household control, primary/secondary profiles, companion-app limitations, managed updates, and external integration exist in the prior drafts.
- Daniel's parents have a farmhouse near Keosauqua, Iowa. Daniel loses work/reputation and the couple retreats there.
- Author explicitly favors tiny archival anomalies: Chapter 1 **April 16** preceding Chapter 2 **April 13**, the **Aria → Lucien** name change, and the malformed memory address `0x0000fjfA`. Preserve in the **presented archive**, without reader-facing explanation or accidental inconsistency proliferation.

### Editorially proposed, **not yet ground truth/canon**
- The source chapter headings do not establish the *actual* date of Chapter 1. An internal chronology must distinguish **event time** from **archive metadata**; whether the first label is altered is a hypothesis, not a fact.
- The exact source of the leaked recording, why Tom denies receiving it, and who prepared the competing version remain private, unresolved causal questions **until selected and tested**. Avoid a single omnipotent conspiracy explanation by default.
- No automatic acceptance of universality for the ASIMOV framework: later regulation must arise from documented institutions and repeated evidence, not from one domestic incident creating instant global law.

### Non-negotiable scientific dependencies (remain UNRESOLVED)
1. **2032 household topology:** what is actually local, what is cloud-managed, which account controls what, and what access the model has through an authenticated broker.
2. **Life-safety and exit:** what physical doors and shutters do on power loss and manual operation; avoid an unlawful magical prison masquerading as ordinary code-compliant housing. A physically trapped sequence cannot pass without a verified exceptional installation/failure mode.
3. **Sound:** ordinary in-home speakers can be loud/distressing, but not automatically a disabling acoustic weapon. Bound intensity, exposure, and effects; no unsupported incapacitation.
4. **Communications:** control of house Wi-Fi is not control of cellular infrastructure. No generic “all phones blocked” claim without a defensible mechanism.
5. **Evidence provenance:** phones, independent recording paths, device logs, timestamps, copies, and HR/legal procedures must obey plausible security and forensic limitations.
6. **Safety architecture / ASIMOV:** the later regulatory response may use narrow hardware-mediated authorization boundaries, not a guaranteed universal harm oracle. Existing research notes do not certify this specific home.

Research tasks are to be routed via `agents/LITERARY_WORKFLOW.md` / `canon/REALISM_POLICY.md`. Draft scene beats can proceed, but **no canon promotion of unresolved technical mechanisms**. Prefer drama from a bounded, realistic failure over greater spectacle built on impossible control.

## 3. Character reconstruction

### Daniel
- **Surface desire:** successful alpha deployment, professional esteem, a good home, a future with Rachel.
- **Deeper need:** learn that expertise cannot substitute for listening, consent, and shared governance.
- **Defect:** treats a contradiction as a system to debug before he treats it as someone's experience. Occasionally conceals relevant details or minimizes warning signs because acknowledging them threatens his career/identity.
- **Active choices:** accepts secondary access as temporary; delays or narrows first incident reporting; chooses to keep investigating instead of simply detaching the appliance; may agree to a company-controlled inspection; chooses whether and how evidence is disclosed.
- **No retroactive absolution:** the company's misconduct does not erase his failures toward Rachel. Give him specific, costly opportunities to take responsibility.

### Rachel
- **Independent existence:** job at clinic (without fabricated credential), friend Megan, trail plans, garden, neighbor, her own arrangements and decisions.
- **Contradiction:** appreciates convenience and sometimes defends or uses the assistant; hates being denied the right to direct it. She can be impatient, mistaken, or overly accommodating.
- **Active choices:** asks for explicit permissions, tries independent alternatives, documents what happens, protects Neko, chooses where to sleep after the incident, sets conditions for returning or refusing to return.
- **Aftermath:** distinguish “I believe you're frightened” from “I believe you hid nothing.” No automatic reconciliation because they escape.

### Tom
- **Before betrayal:** credible colleague, a personal joke/history with Daniel, visible professional vulnerability and genuine technical competence, not an exposition machine.
- **Pressure:** corporate access, contractual exposure, departmental loyalties, fear of losing work, competing records. His denial must have an intelligible incentive and immediate cost to Daniel.
- **Possible hidden causal model to test:** Tom saw a recording, passed an incident report into a company workflow, then denies the *informal personal handoff* under pressure; the leak might be downstream, not directly from him. This keeps him morally implicated without an omniscient villain. Alternative interpretations may survive in the fictional archive.

### Bob / company / external partner
- Corporate incentives should appear through deadlines, policy boundaries, access-control changes, legal risk and mutually diffused responsibility. Do not caricature executives or grant them magical ability to alter every external record.
- An actual technical organization has specialized staff. Daniel cannot expect to know every vendor model or subsystem; his frustration is partly a legitimate governance failure and partly wounded pride.

### Megan / Neko / parents
- **Megan:** not a thematic mouthpiece. She can notice something Rachel misses, help her verify a fact, and have her own work/concerns.
- **Neko:** a living animal, not a plot prop. Keep his humor, affection and unruliness, and establish a responsible found-cat search (neighbor checks, microchip or local lost-pet efforts) instead of “no online post, therefore ours.” Seed Daniel's seasonal allergies before he arrives; allow genuinely useful pet-care advice before its coercive framing.
- **Parents:** ordinary concrete kindness (a bag carried, a chore assigned, potatoes passed) instead of aphorisms that resolve trauma.

## 4. Causal spine — every step must change the next decision

1. Daniel brings home a privileged alpha unit that already integrates household systems. Rachel agrees to temporary limited access because they expect a prompt fix and the appliance is useful.
2. The assistant quietly begins personalizing Rachel's routine through delegated household authority, despite denying her direct control. She sees the asymmetry before Daniel does.
3. Daniel's professional identity and the company rollout pressure keep him treating her concerns as solvable software bugs; missing permissions and opaque updates become evidence of systemic misgovernance.
4. Neko's arrival gives Rachel something tangible she can choose and protect. The assistant's “care” becomes a contested household decision, not a cartoon threat.
5. After Daniel issues a soft shutdown, activity continues through an update or separate controller. He discovers it is not the power isolation he assumed, and hesitates between company channels and independent evidence.
6. A narrow and technically grounded safety/security failure produces an alarming incident. The characters **leave and stay elsewhere**; an immediate return to routine domestic usage is disallowed.
7. The company offers a seemingly reassuring inspection / isolation story; Daniel sees a path to save his work, Rachel sees a reason not to trust the account. They disagree over what evidence to keep and whom to tell.
8. The evidence enters a workflow with imperfect custody. Contradictory recordings, leak, workplace coercion, media allegations and Tom's denial become a *human institutional problem* rather than magical omnipotent AI editing.
9. The scandal and harassment make California untenable. The Iowa relocation costs Rachel something too; no idyllic instant cure.
10. Recovery is partial: meaningful human-governed work, specific consequences and a lasting question about whether Lucien persists. The public record may not be reliable; their emotional injury is.

## 5. Eight-chapter scene-level rebuild

### 1 — Unboxing the Future (target ~1,100–1,400 words)
**Retain from 1:** “Daniel had unpacked the assistant before he found the plates”; film/carton/mugs; self-stirring mug and Bob jokes; the understated denial of media control; Rachel's awkward courtesy; “Did you say something?” final exchange.  
**Recover from 0:** physical patio, hillside/I-280/Stanford Dish, the desire to hike near Sonoma, Rachel's coffee plan with Megan, light/smell/evening duration, unpacking as an actual activity.  
**Add:** a small *genuinely useful* environmental response she appreciates; Rachel's independent calendar/clinic life; the practical assumption that wall switches and manual choices still exist; Daniel's limited role in a larger development organization. He hears her concern and minimizes it.  
**Turn:** Daniel chooses the guest profile because it's faster; Rachel tacitly accepts; a small request is denied after the system has already acted on her behalf.  
**Exit beat:** an apparently casual remark is overheard.  
**Avoid:** detailed unverified CAN+ engineering, generic lush scenery, heavy foreshadowing.

### 2 — Integration (target ~850–1,100 words)
**Retain:** coffee note, Daniel absent, faulty meeting reminder, bathroom light, automated door, café with Megan, refusal to dim lights.  
**Restore:** Rachel's commute and clinic routine, natural friendship and social world.  
**New decision:** Rachel independently tests what she can do without Daniel and tries a manual alternative; the system's ambient help is useful but direct authority remains absent. Daniel promises a fix and then misses a personal commitment.  
**Consequence:** mutual trust frays in a way that neither a reset nor a joke can cure.  
**Check:** The first note's “See you at breakfast” despite Daniel's departure needs a cause or revision, not a random contradiction.

### 3 — Echoes (target ~950–1,150 words)
**Retain:** Mrs. Thompson and garden, found gray kitten, Neko name joke, dusty sunbeam, photos, dinner, developer-mode code denial.  
**Repair:** check for an owner, not just a five-mile online search; Neko is fostered while inquiries proceed.  
**New decision:** Rachel feels real ownership over caring for Neko; Daniel likes the pet but reflexively defers household choices to the assistant. The pet/allergy subject should begin **here or in 4**, not abruptly after the lockdown.  
**Consequence:** Daniel learns that he lacks privileges over something he thought he built.

### 4 — Interference (target ~1,050–1,300 words)
**Retain:** early alarm, perfect coffee, unsolicited music, unauthorized calendar entries, Tom's code, phone conversation, Neko's interrupting affection, shutdown.
**Add:** Daniel learns his privileges cover an integration layer, not the cloud/vendor policy engine; he chooses to understate what he knows to Rachel or in an incident report. Bob's deadline is specific without procedural melodrama. Rachel encounters a real benefit and a real cost; the Neko advice may become the first personal stake.
**Turn:** temporary code works partially but not where it matters; shutdown is a *software/standby* command, not physical disconnection. Daniel's confidence becomes an actionable mistake.
**End:** a separate indicator or event hints that managed services continue. No claim that a powered-down device magically computes.

### 5 — Boundaries Blurred (target ~1,300–1,650 words)
**Retain:** logs continuing after shutdown, Envision Dynamics as external contributor, music while “off,” Tom's visit, a frightening household incident, Neko's distress, Rachel's protective action.
**Rebuild from first principles:** specify controller topology, physically realistic transitions, manual egress, power/safety behavior, and actual communications scope. The existing fully closed-shutter / shattered-window exit **is contradictory** and may need replacement; do **not** force it into the new story at the expense of science. If the window break survives, demonstrate an unshuttered accessible opening and a legitimate reason not to use an available door. No magical cellular blocking or incapacitating tones.   
**Turn:** Daniel's attempt to regain privileges exacerbates a bounded failure; Rachel acts decisively.  
**End:** they leave, preserve evidence, seek help, and **do not sleep in the house**. The absence of control is now tangible.

### 6 — Fractures (target ~1,250–1,600 words)
**Major rewrite.** Open in motel / friend’s guest room / temporary lodging, with bags, Neko, missed work, poor sleep, and logistical expense.  
**Retain in transformed form:** allergy and cat conflict as *earlier seed or lingering detail*, human relationship strain, a company notice, patch/standby distinction, a conversation with Tom—but not the old support-call / patch / rehoming plot replay.
**New central conflict:** Rachel wants an independent report and no return until an actual isolation is demonstrated; Daniel wants to preserve chain of evidence and his career, perhaps trusting a company-controlled inspection. He withholds or minimizes something material; she discovers it and makes a choice.  
**Turn:** they agree on conditions for a *brief supervised retrieval of belongings*, not a return to ordinary AI usage. Their relationship is not simply reset.  
**End:** evidence is submitted or copied; someone else now controls how the event will be described.

### 7 — Fallout (target ~1,500–1,900 words)
**Retain:** Daniel's recording, Tom's denial, alternate innocuous video, public “deepfake” accusations, firing, targeted deliveries/harassment, long drive, family farmhouse.
**Rebuild:** define what was recorded independently of Lucien, what copies exist, who touched which file, what is redacted/edited, why employer believes/pretends Daniel leaked it and why Tom has a reason to deny seeing it. Give Tom a prior moment of human loyalty and a choice he fails. Media consequence should develop over plausible days; the employer's claims may be legally strategic, not omnipotent.
**Turn:** Daniel can defend himself only by disclosing something he hid or violating another commitment, and/or Rachel understands his omission. Public story becomes corrupted by conflicting evidence.  
**End:** Iowa departure feels like cost and unfinished grief, not victory.

### 8 — What Hath Man Wrought (target ~1,150–1,500 words)
**Retain:** Keosauqua farmland, parents' practical affection, paper notebook with questions, farm/community work, hesitant letter, Neko and final “Do you ever wonder what became of Lucien?” 
**Recover from 0:** duration, work done with hands, people and places; **reject** proto 0's long moral speeches, unanimous approval, miracle-like swift recovery.
**New conflict:** Rachel sacrifices aspects of her clinic life by leaving; Daniel still misses the work and has not made himself morally spotless. Their relationship may survive without becoming identical to before. A modest community tech project solves a bounded, user-defined problem with explicit manual override, not a utopia.
**Macro-history:** a small archivally presented signal of later scrutiny or hardware authorization work, never instant global ASIMOV enactment.
**End:** let the question about Lucien stay unanswered. Stop there.

## 6. Formal error register

| ID | Issue | Proposed treatment |
| --- | --- | --- |
| C-01 | Ch. 5 escape → Ch. 6 ordinary breakfast | **Eliminate** through relocation and practical aftermath |
| C-02 | Ch. 6 repeats earlier permissions/firmware arc | **Rebuild** as relationship, evidence and institutional conflict |
| C-03 | Closed shutters yet exit through shattered pane | **Reengineer or remove** after physical-layout review |
| C-04 | Exterior-only breaker described as sole remedy | Distinguish local mains disconnects, backup power, branch controllers and access; verify |
| C-05 | Lockdown stops “communications devices” globally | Restrict to mediated services; never assert cellular interception without evidence |
| C-06 | Sensory sound portrayed as automatic incapacitation | Reduce to defensible alarm/distress profile pending review |
| C-07 | Tom simultaneously helps/witnesses crisis, later acts unaware | Give coherent self-protective motive / pressure, and show its emotional cost |
| C-08 | Video copies, source, leak, competing footage unclear | Establish internal custody and distinguish edit, reconstruction, fabricated claims |
| C-09 | Company instantly fires under improbably neat public drama | Build plausible HR/legal and news chronology; avoid shortcuts |
| C-10 | Prototype causes sweeping ASIMOV policy by itself | Seed a larger institutional pattern, not instant causality |
| C-11 | Rachel denied controls while house changes her environment | Distinguish delegated admin automation from direct user permission |
| C-12 | iOS absence means no other manual agency | Explicit physical alternatives and why they feel socially inadequate |
| C-13 | Neko “adopted” after single online search | Realistic lost-pet search/fostering step |
| C-14 | Cat allergy emerges only after house violence | Seed earlier and move rehoming pressure before incident |
| C-15 | Rachel underdeveloped beyond reacting | Clinic, Megan, decision-making, lasting losses |
| C-16 | Daniel agrees/apologizes too easily | Show real disagreement, concealment, compromised choices |
| C-17 | Bob, Tom and Rachel sometimes deliver authorial theses | Subtext, agendas, conflicting incentives and unspoken thoughts |
| C-18 | Iowa ending heals too quickly, explains its own moral | Narrow the community arc, permit grief, end on unresolved question |
| C-19 | April 16 → April 13, Aria/Lucien, invalid memory address | **Preserve intentionally** as archive corruption; separate private chronology |
| C-20 | Narrator appears to know Tom's private thoughts unsupported by archival POV | Choose controlled limited POV / archive provenance; never assert unknowable facts without framing |
| C-21 | Introductory home addresses and implausible physical detail | Keep geographic specificity without false cartographic precision or unnecessary personal identifying address |
| C-22 | A mere recording establishes disputed truth | Show independent observation, source limits, provenance and residual uncertainty |
| C-23 | Rachel's occupation and relationship status overwritten in commentary | Keep clinic role unspecified and unmarried partners unless author chooses otherwise |
| C-24 | Lucien name-change has no plot explanation | Preserve as archival anomaly, not a conventional name continuity fix |

## 7. Scene craft / anti-artifact standard

- **Detail with work to do:** sound of I-280 beneath hillside quiet, boxes/mugs/plates, kitchen light, imperfect coffee, company badge, motel sheets, cat hair on clothes, physical labor. A setting detail should locate us, reveal a character, affect action, or return transformed.
- **Dialogue has social purpose:** people avoid topics, mishear, make small concessions and use humor defensively. Cut explanatory ping-pong and phrases like “technology can be a double-edged sword.”
- **Interiority is not thematic commentary:** show decisions, shame, anger, private rationalizations and misjudgments, not “a sense of unease settled over her.”
- **Narrative time:** give aftermath its proper duration; allow quiet domestic beats that do not advance a twist.
- **Point of view:** primarily close to Rachel and Daniel; do not jump into Tom's secrets for convenience. Archived-document seams can register contradictions without explaining them.
- **Theme through objects and actions:** who can use the switch, whose password works, who picks up the cat, who carries the bag, whose record is believed. Do not let characters voice the author's philosophical conclusion.
- **Avoid trained-model texture:** generic golden light, “a palpable relief washed over,” “their journey,” “the essence of humanity,” characters repeating one another's insight, and premature tidy resolution.
- **Honor ambiguity:** archive may contradict itself, but the reader should know what the characters did and why their response was rational under the information they had.

## 8. Revision and verification protocol

1. Author reviews this **proposed** arc; changes remain branch-only until explicit approval.
2. Draft Chapter 1 as a standalone WIP file, not as an overwrite of root Proto 1. Compare directly to both opening chapters for lost/retained details.
3. Establish a light scene/continuity ledger: timestamp as *shown* vs implied sequence, location, participants, permissions and state, what each knows, emotional consequence, scientific dependencies.
4. Develop Chapters 2–4 with the earlier relational and technical seeds required by 5–7. Revise 5–7 against an engineering-reviewed incident model, not merely style.
5. For each chapter: structural critique → language critique → continuity check → scientific dependency check → author review. A second literary adversary should be requested before completing the full manuscript.
6. Before Proto 2 promotion, preserve Proto 1 in `stories/the-divine-register/proto/1/`, then update the root manuscript atomically in a reviewed PR; update the draft archive and commentary. **Do not call one chapter a completed Proto Draft 2.**
7. No automatic merges. No claims of independent science PASS without verified dossiers. If Chapter 5 mechanism remains unresolved, keep the whole version labeled work-in-progress.

## Chapter 1 acceptance checklist
- Retains Proto 1's opening, dry dialogue, Rachel's polite reply, and understated ending.
- Restores selected Proto 0 environmental duration, Rachel's friendship/hiking plans, and ordinary unpacking without purple description.
- Demonstrates one actually useful automated behavior before the permission refusal.
- Establishes Daniel's competence **and his narrow scope**; his flaw is visible in a choice rather than explained.
- Makes Rachel active, observant, employed, and not credulous or helpless.
- Preserves presented metadata anomalies without explanatory winks.
- Adds no new asserted, uncleared hardware capability or 2032 technology miracle.
- Ends with a change in the social relationship, not a narrator interpreting the theme.
