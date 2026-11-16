# Repository to-do list

This list tracks open work from the repository audit at `d3835b1`. Remove an item after its resolution is verified and merged. The resolving pull request and Git history record the completed work.

An asterisk (*) means the repository already labels the work complete or working, while a specific verification or follow-up remains open. Leave its checkbox open until that work is resolved.

## Manuscript and release status

- [ ] **Genesis Protocol literary and science review** — Proto Draft 2 is published as the author-selected main manuscript, but the holistic literary pass and technical/causal review remain open. Historical editorial notes are preserved in the archived drafts.
- [x] **Resolve opening dates and device naming** — Author confirmed the April 16 → April 13 discrepancy and Aria/Lucien shift should remain as understated archival corruption in Proto Draft 2.

## TempleOS and repository maintenance

- [ ] **Verify the “WORKING SOUND” UTM bundle (\*)** — Both tracked configurations expect an absent `data.qcow2` and declare the same AC97 audio setting. Recover or recreate the working setup, verify boot and audio in UTM, and document how to reproduce it. Record what the standalone ISO contains and whether it is part of the project build.
- [x] **Add a canon index with document status** — [Universe references](canon/README.md) distinguish editorial policies, working records, and research; the root README links to it.
- [x] **Clarify the license files** — The full [LICENSE](../LICENSE) remains at the root; the earlier [license-policy proposal](legacy/license-framework-draft.md) is preserved and marked historical, not operative.
- [ ] **Review prototype funding configuration** — Verify the listed destinations and decide whether the repository is ready to expose them.
- [ ] **Record the disposition of the older feature branch** — The audit found zero commits unique to `feature`. Decide whether to retain it for historical reference or retire it.
