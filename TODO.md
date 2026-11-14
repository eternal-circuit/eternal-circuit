# Repository to-do list

This list tracks open work from the repository audit at `d3835b1`. Remove an item after its resolution is verified and merged. The resolving pull request and Git history record the completed work.

An asterisk (*) means the repository already labels the work complete or working, while a specific verification or follow-up remains open. Leave its checkbox open until that work is resolved.

## Manuscript and release status

- [ ] **Genesis Protocol release readiness (\*)** — The [README](README.md) labels the story complete, and a full draft exists. Review the public draft’s redaction notes and outstanding legal-scene work, then clarify the release status in the README.
- [ ] **Choose one editable manuscript source** — Compare the standalone Chapter 1 Markdown file with the full text and designate the authoritative editable version. Document which files are exports or historical variants before consolidating copies. Preserve any intentional byte-format conventions.
- [ ] **Update the source inventory with verified comparisons** — Both tracked Proto Draft 0 PDFs are byte-identical. The two `.0b00000000` text copies differ only by a final newline. The project-supplied PDF has different bytes and identical extracted text. Record these findings in the [inventory](canon/PROJECT_INVENTORY.md).
- [ ] **Resolve opening dates and device naming** — Determine whether the April 16 → April 13 opening and the Aria/Lucien change are intentional. Record the author’s decision before revising the manuscript.

## TempleOS and repository maintenance

- [ ] **Verify the “WORKING SOUND” UTM bundle (\*)** — Both tracked configurations expect an absent `data.qcow2` and declare the same AC97 audio setting. Recover or recreate the working setup, verify boot and audio in UTM, and document how to reproduce it. Record what the standalone ISO contains and whether it is part of the project build.
- [ ] **Add a canon index with document status** — Give readers an entry point that identifies established premises, working references, and provisional material. Align the root README’s description of `canon/` with those statuses.
- [ ] **Clarify the license files** — Review the placeholder in [LICENSE.md](LICENSE.md) and clarify its relationship to the full license in [LICENSE](LICENSE) and to the project’s editorial canon policy.
- [ ] **Review prototype funding configuration** — Verify the listed destinations and decide whether the repository is ready to expose them.
- [ ] **Record the disposition of the older feature branch** — The audit found zero commits unique to `feature`. Decide whether to retain it for historical reference or retire it.
