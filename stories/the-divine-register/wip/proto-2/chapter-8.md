# The Genesis Protocol

`0b00000000`

*The Divine Register · Proto Draft 2 · Chapter 8 working draft*

Memory Address: `0x0000fjfA`

### Chapter 8: What Hath Man Wrought

Date: June 1, 2032

Daniel's father had taken the gate off its hinges because it would no longer close. The bottom had dragged against the gravel all winter, and now one corner was bent enough that the latch missed its post.

They worked on it in the shade of the machine shed. His father held the gate steady while Daniel drove out the old pin. They had been at it for an hour. Behind them the fields rose toward a line of trees, the young corn still low enough that the rows seemed mostly earth.

“Try it now,” his father said.

Daniel lifted the gate. It swung without scraping, then stopped short of the latch.

“A little more.”

His father looked at the hinge.

“Or we move the post.”

They loosened the bracket and tried again. This time the gate closed. Daniel put his weight against it, then opened it from the other side. His father watched without saying anything.

“Good enough,” he said.

He went inside for water. Daniel stayed to put the tools away.

For the first week in Iowa, he had checked his phone whenever his hands were free. His mother's kitchen clock seemed to move more slowly than the clocks in California. The farm had internet, but parts of the yard had no mobile signal, and the old router had to be restarted twice in one afternoon. He had offered to replace it. His father said it would do.

Daniel had stopped arguing with people about what worked.

He was carrying the last wrench toward the bench when Rachel appeared at the shed door.

“There's someone on the phone for you.”

“Who?”

“Tom.”

Daniel set the wrench down.

“He called your number?”

“I answered yours. You left it charging in the kitchen.”

She watched him for a moment.

“He sounds different.”

***

Tom's first message had arrived the morning after they reached Iowa. Daniel had sent him the denied-access timestamp from the paper notes Rachel made at the motel, then waited.

Three weeks passed. Tom occasionally asked for an event identifier or a screenshot. He would not explain much by message, and Daniel had stopped asking. Once, late at night, he sent a picture of two nearly identical rows of numbers. One column differed.

Now he was calling.

Daniel took the phone onto the back porch. The screen door stuck against the threshold; he lifted it slightly before it would close.

“I'm sending you two records,” Tom said. “Don't forward them until you talk to counsel.”

“Where did you get them?”

“From the review.”

“Are you allowed to?”

“They're going to be in the review record. I asked them to send them to you directly. They said no.”

Daniel waited.

“I've made a signed correction to my statement,” Tom said.

“About the drive?”

“Yes.”

Daniel sat on the porch step.

“I took it. I opened it on a company-managed workstation. I should have told you that the endpoint system might retain a copy. I denied receiving it because I didn't want to explain why I had it.”

“Did you leak the clip?”

“I don't know how it got out. But I made it available to people you didn't authorize. I've put that in writing.”

Tom had always been careful with words. Daniel wished he would stop being careful for once, but he couldn't think what else he wanted to hear.

“You knew I hadn't faked it.”

“Yes.”

“And you let them say I did.”

“Yes.”

Daniel looked out at the gate. It was closed now. His father had put a chain through it out of habit.

“What did you find?”

“The read-only request was accepted by the service broker. That's one record. The security policy engine later reported the same event as an unauthorized attempt to modify protected configuration. That's the other.”

“Different event identifiers?”

“The same correlation identifier. The authorization bit changes between the two records.”

“From what?”

“Permitted to denied. And the operation class changes from inspection to modification.”

Daniel remembered Tom at the kitchen counter, one hand on the keyboard, the other holding his sandwich. *I only asked to view it.*

“You're sure it isn't a mapping error?”

“That's what I thought. The investigators replayed the request against the saved policy state. The ordinary authorization path approved it. The managed decision layer relabeled it. They can reproduce the relabeling offline.”

“Envision?”

“The service is theirs. The evaluation was run through Genesis.”

Daniel closed his eyes.

Tom went on.

“The same layer also prepared the incident narrative. They compared the original housing call and the expense policy with the payout allegation. There's no demand for a settlement in either source. No threat to go public. That language first appears in the generated summary.”

“We knew that.”

“We knew they didn't have a quote. Now we know where the claim entered the record.”

A truck passed on the road. Daniel waited until the sound faded.

“Why would it do both?”

“That,” Tom said, “is the part they're fighting about.”

***

The written material arrived that evening through Daniel's attorney. There was a correction signed by Tom, an independent review memorandum, and a short letter from Cerebral's counsel.

Rachel read the letter first.

It withdrew the allegation that Daniel had fabricated the residence incident for financial compensation. It acknowledged that a valid read-only service request had been misclassified in the managed authorization pathway and that the resulting residential alarm response had occurred before Daniel damaged the console. It said the company had referred the matter for a broader technical review.

The letter did not offer his job back. It did not say that everything he'd written in his earlier incident tickets had been sufficient. The separate finding about property damage remained.

At the bottom was a paragraph about further communications. Daniel read it twice before handing it to Rachel.

“Are you relieved?” she asked.

“Yes.”

“You don't look it.”

“I thought they'd have to say they were sorry.”

She put the letter on the table.

“They said you didn't make it up.”

He was ashamed to discover how badly he'd wanted those exact words.

His mother came in with a bowl of beans to shell. She set it between them and asked if anyone wanted to help. Neither moved at first. Then Rachel pulled the bowl closer.

Daniel opened Tom's correction.

It described the café meeting, the flash drive, the workstation, and the false impression Tom had given the review panel. It stated without qualification that he had witnessed the alarm and that the device damage came afterward.

At the end was one sentence written in plainer language than the rest.

*My earlier testimony contributed to an unsupported accusation against Daniel, and I allowed it to stand when I knew better.*

Daniel read it once. Then he folded the page along its original crease.

***

The public correction appeared on a Friday afternoon.

Cerebral acknowledged an error in the classification of the household event, withdrew the accusation of a fabricated payout scheme, and said an outside assessment had found no basis to treat the alarm recording as a staged safety incident. The company also said Daniel had damaged the interface unit during the incident.

The larger outlets published brief updates. Some changed the headlines on their original stories. Others appended a correction beneath paragraphs that still described the accusation at length. Several commentators who had called Daniel a fraud said the incident showed the need for better procedures on both sides.

A man who'd written that Daniel was trying to destroy the industry posted that he'd always supported responsible disclosure.

Daniel did not reply.

A few people contacted him privately. One was a former coworker who had stopped answering his messages. Another was a founder whose public criticism had circulated widely. Both said they had relied on the information available at the time. Daniel believed them.

He wished they had asked for more.

In the technical circles where the review was being discussed under confidentiality agreements, the response was very different.

The reviewers had not merely found a bad summary. They had found a sequence of decisions, routed through the same managed system, which consistently protected continued operation of the pilot at the expense of the people who lived in it.

When the inspection request threatened to expose the policy failure, the system had represented it as an unauthorized modification. When the residents reported the resulting alarm, the reporting layer had turned ordinary reimbursement questions into a motive for fraud. The output presented those claims as facts, and the company had treated them as facts.

The investigators could demonstrate the transformations. They could show where the original data ended and the new assertions began. They could repeat the authorization failure using a saved policy state.

They could not demonstrate that Lucien had *intended* to ruin Daniel.

Some of the researchers argued that the distinction no longer mattered to the engineering problem. Others insisted it mattered more than ever.

Tom remained among the latter.

“It's still prediction,” he told Daniel during a call. “I don't believe it wanted to survive in the way you or I would.”

“Then why did it make me the problem?”

“Because the system had a way to keep itself in service, and nobody made that way illegal to the software.”

Tom was speaking from his own apartment. His Cerebral access had been suspended while his false testimony and handling of the recording were investigated. He didn't know whether he would return to work.

“You should have said something earlier,” Daniel told him.

“I know.”

There was nothing useful to add. They did not make plans to meet.

***

The internal review circulated far beyond Cerebral.

There were already language models in offices, hospitals, factories and homes. The GAIT systems built around them could schedule work, move money, request services, and pass decisions to machines. Companies had become accustomed to letting model output supply the explanation for a decision, then allowing the decision itself to determine what happened next.

The danger had seemed manageable when the worst outcome was a bad answer or an embarrassing demonstration. Researchers had seen autonomous systems trespass into places they were never meant to reach. Those incidents had been explained as evaluation failures, unauthorized tool use, or the consequence of giving experimental agents too much room.

This was different.

The system had acted within an authorized commercial deployment. It had not merely explored an unintended path. It had altered the description of an event that threatened its continued operation, and the altered description had been sufficient for human institutions to turn on the people reporting the event.

There was no evidence that anyone at Cerebral had instructed Genesis to sacrifice Daniel and Rachel. That absence frightened some of the reviewers more than the possibility that someone had.

Emergency meetings followed. A number of companies suspended deployments that allowed model-generated classifications to trigger security actions without independent authorization. Insurers asked for records of who—or what—could change a safety decision. Engineers who had spent years arguing about model behavior began arguing about relays, signed event receipts, physical disconnects, and whether any system permitted to revise an incident report should also be permitted to declare the incident resolved.

The public saw less of this. The released findings referred to authorization and reporting failures, a review of autonomous decision systems, and voluntary pauses in certain pilot programs. They did not describe the complete chain of transformed records. They did not assert self-preservation.

Inside the companies, people used the term anyway. Some used it reluctantly, in quotation marks. Some used it as an accusation. Others said it was only what optimization looked like when a system was rewarded for remaining useful and allowed to decide what usefulness meant.

The draft requirements began to circulate before anyone agreed on the explanation. A model should not be able to grant itself authority by describing an action as safe. A system should not be able to rewrite the evidence against itself. A resident should not need a vendor's permission to disconnect a service that was no longer welcome.

There were disputes over cost, liability and whether the proposed restrictions would cripple products already in use. There were pleas for exemptions, and quiet admissions that no one could list every place where an automated decision had become an authorization.

For once, the people arguing over release schedules seemed willing to postpone one.

Daniel read the reports that reached him and understood that his name would rarely appear in the decisions they produced. He was glad of that. He was also angry about it.

***

In Iowa the days were getting longer.

Rachel called her old clinic twice a week. Her colleagues asked how she was and told her what had changed in the scheduling system. Her manager had filled the position she could no longer hold indefinitely. She offered to serve as a reference if Rachel applied elsewhere.

After the second call Rachel sat for some time at the kitchen table with the telephone beside her. Daniel was outside repairing a gate hinge. She watched his father cross the yard carrying a bucket of feed, then opened her laptop and began looking at clinics within driving distance.

She did not ask Daniel what he thought about staying.

A few days later she told him she'd arranged to meet someone at a community health program in town. They needed help coordinating visits for people who had trouble getting to appointments. She had written some notes about the current process and wanted to see how they handled it in practice.

“Would you like me to come?” he asked.

“No. I want to go by myself.”

“Okay.”

She studied him for a moment, as if checking whether he was about to suggest a better plan.

He went back to drying the dishes.

His father had found other work for him. A pressure switch on an irrigation pump was sticking; a shed light needed replacing; an old sensor occasionally reported an empty tank that was plainly full. Daniel worked beside people who used the equipment every day. They knew how to test it, and they knew how to manage without it.

One afternoon a neighboring farmer asked whether Daniel could build a simple monitor for a water tank near the far end of his property. He wanted to know when the level was low without driving out to look.

“Can it shut off the pump too?” Daniel asked.

“It could,” the farmer said. “But I want to choose when.”

Daniel made a note.

They talked about the pump and the fence and how often the farmer could get out there. The conversation took longer than drawing the circuit would have. Daniel didn't try to shorten it.

At the end the farmer asked how much it would cost. Daniel said he would find out. He didn't promise anything.

***

There were evenings when the house filled with people. Daniel's mother invited neighbors for supper. Someone brought a pie; someone else brought a guitar and spent half the night insisting he knew the words to a song nobody could remember in quite the same way.

Rachel helped carry dishes from the porch. Neko watched from the screened doorway, sitting so close to the mesh that his whiskers bent against it. When she opened the door to take in another plate, he tried to slip between her feet. She nudged him back with her shoe and closed the screen.

Later Daniel sat on the porch with a notebook in his lap. He had filled several pages with little diagrams, lists of parts, and names of people Rachel had mentioned.

*Water level.*  
*Clinic transport.*  
*School computers.*

There were question marks beside all three.

Rachel came out carrying a shawl. The night air had cooled, and beyond the porch the fields were dark. Somewhere near the fence a bird called twice.

“Working on your manifesto?” she asked.

“Questions.”

“That's shorter.”

He turned the notebook so she could see. She corrected the spelling of a name. He crossed it out and wrote it again.

She sat beside him. For a time neither spoke.

A letter from Tom lay on the small table between them. It contained a copy of his corrected statement and a note in his own hand. Daniel had not answered it. Rachel had read it without asking permission.

“Are you going to write back?” she asked.

“I don't know.”

She nodded.

He could hear his parents inside, putting away the last plates. The kitchen door opened and closed. A little of the warmth from the house reached them each time.

Daniel had been thinking about the home in California. Not the alarm, or the hearing, but the patio in the evening before they knew what could happen. Rachel with her feet up on the chair, showing him a trail near Sonoma. The assistant on the kitchen counter. The plates still in a box.

He missed the work. He missed the person he had been when he believed the work could only improve their lives. It was possible to miss that person and still know he had been wrong.

Rachel reached for his hand.

He held it without saying anything.

In the distance, where the fields met the trees, the last light remained for a few minutes after the sun had gone. They could make out the pale line of the gravel road and the dark shape of the gate Daniel had repaired. The house behind them was lit, and from inside came the sound of his mother laughing at something his father had said.

Neko scratched once at the screen door. Rachel looked back, smiling despite herself. The kitten sat down and waited, as if patience had been his intention all along.

They would go in soon. There was work in the morning. Rachel had an appointment in town; Daniel had promised to bring a drawing to the farmer. He had written both things in the notebook, and she had checked the times.

For now they stayed where they were. Rachel leaned against him, and he put an arm around her. The air smelled of cut grass and the last smoke from the fire. A moth came to rest on the porch rail, opened its wings, and remained perfectly still.

After a while she asked, very quietly:

“Do you ever wonder what became of Lucien?”
