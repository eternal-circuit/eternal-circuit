# iPhone Voice ↔ GitHub ↔ Desktop Codex workflow

Status: **proposed operating workflow**. GitHub is the durable interchange; ChatGPT Project memory and Codex memory do not automatically synchronize.

## Capture during a voice conversation
Speak naturally about worldbuilding, plot, continuity, technical realism, or theology. At a safe stopping point, ask: **"Create an Eternal Circuit handoff from this conversation and prepare it in GitHub."** Do not require screen interaction while driving.

## Prepare a reviewable handoff
Make a short structured document in `handoffs/YYYY-MM-DD-topic.md`. Include:
- Session summary (only project-relevant content)
- Decisions explicitly made vs possibilities merely discussed
- Canon status: proposed / approved / unresolved
- Sources or links, uncertainties, and technical claims needing verification
- Proposed repository edits, the next Codex task, and its route in the [agent runbook](../agents/RUNBOOK.md)
- Publication classification: public-safe / private / needs review

Use a branch and PR for changes to a public repo. Do not commit raw personal audio/transcripts. Ask for review before making public any content that might be private or unpublished.

## Work on Mac
1. Open the ChatGPT desktop app and select Codex, or use Codex in a local checkout of `eternal-circuit/eternal-circuit`.
2. Pull/fetch the latest approved changes; if a handoff is in a PR, check out its branch or read the PR.
3. Tell Codex: **"Read AGENTS.md and the latest handoff, then implement the approved tasks on a branch. Preserve canon and open a PR."**
4. Review and merge; do not treat generated text as author-approved without review.

## Return to iPhone
Ask the assistant to review the latest commits or PR. It should read GitHub first and give an oral recap. New ideas become a new curated handoff; never assume a Mac-only Codex chat is automatically in the iOS conversation history.

## Optional faster path
Use ChatGPT **Work** voice on iPhone, when available, for longer cross-device tasks; Work chats can sync across devices. Codex Cloud tasks can also be accessed across devices after their environment is set up. Neither replaces a durable versioned story archive.

## Guardrails
- Public repository: assume all merged text is public.
- Unverified continuity is not canon.
- Keep conversations safe for hands-free use; review approvals and diffs only when parked.
