# Eternal Circuit — provisional source inventory

**Audited 2026-11-13.** This is a working inventory, not an assertion of final canon. No existing story text was modified.

## Hierarchy
- **The Eternal Circuit:** the broader narrative universe and nine-book concept.
- **The Divine Register:** Book 1, planned as eight canonical short stories / bits. A ninth *deuterocanonical flip-bit* concept appears in earlier outlines; its precise placement requires author confirmation.
- **Genesis Protocol: 0b00000000:** the first story, with an eight-chapter draft in a supplied PDF; its chapter count must not be confused with the eight stories of Book 1.

## Genesis Protocol manuscript sources

| Role | Path and findings |
| --- | --- |
| Editable draft | [Genesis Protocol Markdown](../stories/the-divine-register/genesis-protocol.md) mirrors the eight chapters, front matter, and editorial notes of Proto Draft 0. |
| Transcription baseline | [Full eight-chapter text](../stories/the-divine-register/genesis-protocol.0b00000000) preserves the original extraction and byte offsets. |
| Historical full-text copy | [Root anthology text](<../The Divine Register/genesis-protocol.0b00000000>) differs from the baseline only by an added final newline. Preserve that byte difference for any checksum or offset work. |
| PDF reference | [Proto Draft 0](https://github.com/eternal-circuit/eternal-circuit/releases/tag/divine-register-proto-draft-0) contains the original PDF as a release asset. Its SHA-256 is `93635cfb7803fa3b254f059160c46a799970988368617bc0e8de3e1166c09857`. The two byte-identical repository copies are preserved in Git history. The project-supplied PDF differs at the byte level and yielded identical text with `pdftotext -layout`. |
| Illustrated class edition | [Storybook edition](../stories/the-divine-register/editions/illustrated-storybook.md) records the separate 32-page illustrated abridgment and its planned release. |
| Standalone Chapter 1 variant | [Chapter 1 Markdown](<../The Divine Register/Genesis Protocol: 0b00000000/Genesis_Protocol_Chapter_1.md>) ends before the full draft’s Chapter 1 ending. It adds ASCII illustrations and has cleaner readings such as “coffee” where the full text reads “coaee.” Consult it during transcription and verify variant readings against the PDF. |

The Markdown uses the baseline’s paragraph breaks and the PDF’s chapter headings and dates. A word-by-word comparison against the text layer covered the disclaimer and all eight chapters. The transcription expands typographic ligatures, repairs malformed `ff` words such as `coaee` and `oaice`, restores the dash in “different—deeper,” and joins the soft line break in “reentered.” The front matter was checked visually. The cover artwork and three illustration pages at the end are available in the PDF.

Use Markdown for manuscript edits. Attach approved PDF snapshots to versioned GitHub Releases. Preserve the historical text for byte-offset work.

Other tracked materials include `README.md`, `CONTRIBUTOR_MANIFESTO.md`, `LICENSE`, `LICENSE.md`, the TempleOS ISO and VM configurations, and `seed0` and `seed1`.

## Other available materials
A project-supplied PDF titled *The Divine Register - Michael Pass.pdf* contains the Genesis Protocol story, Chapters 1–8, and editorial TODOs; separate chapter illustration and logo images were also supplied. Their relationship to committed assets has not yet been compared. Prior discussions refer to a universe bible, economics/theme notes, a Book 2 interplanetary AI concept, theological glossary, and liturgical constructs; the *actual files* for these have not yet been verified as present.

## Editorial issues, not automatic repairs
1. Assistant is called **Aria** in Chapter 1, **Lucien** later.
2. Chapter 1 is dated **April 16, 2032**, Chapter 2 **April 13, 2032**; check intended sequencing.
3. Supplied PDF still carries TODOs about redaction, legal/narrative closure, and naming that remain editorial work.
4. Earlier outlines and README may disagree on chronology and projected story titles. Resolve as author decisions, not as model assumptions.

