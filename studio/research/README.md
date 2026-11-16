# Eternal Circuit research library

This directory is the **durable, repository-native knowledge base** for research agents and editors. Links are provenance, **not the knowledge itself**. Every accepted research note must remain useful if every external URL disappears.

## Layout

- `index.md` — browsable register of research notes and their claims.
- `notes/YYYY/EC-R-YYYY-NNN-slug.md` — standalone, self-contained research notes, one bounded topic per note.
- `reviews/` — claim-specific scientific gate dossiers, which **cite note IDs and pinned revisions**, not just URLs.
- `FRONTIER_SOURCES.md` — discovery, verification and source-quality rules.
- `TEMPLATE.md` — required format for new research notes.

## Required intake and deposit procedure

1. **Discover:** record the lead, date, source type and original URL; X is a lead source, never sole scientific proof.
2. **Retrieve and verify:** read the original artifact and methods, seek independent replication/criticism; if inaccessible mark `UNVERIFIED`, not `VERIFIED`.
3. **Synthesize locally:** write a substantive **original-language, non-verbatim** technical summary with the mechanism, measured results, sample sizes, conditions, uncertainty, limitations, quantitative parameters and what the result does **not** establish. Include enough context to reconstruct the relevant reasoning without opening the link. Explain equations in text and include units and assumptions.
4. **Archive provenance:** original URL, title, authors, publisher/venue, publication and access dates, DOI/arXiv identifier or commit SHA if available, and links to data/code/corrections. Where legally permitted, preserve an author's own notes, small factual tables, reproducible calculations and derived models in the repo; **do not copy full third-party papers, posts, paywalled text, figures or code without appropriate license and attribution**.
5. **Cross-reference:** assign immutable note ID, update `index.md`, link to related notes and scientific claim dossiers. Cite `EC-R-...` ID plus the repository commit SHA or tagged version for auditability.
6. **Review:** independent verifier checks accuracy, source interpretation, numerical consistency, provenance and copyright; status `DRAFT → VERIFIED` only after this review.
7. **Maintain:** corrections and new evidence append a dated revision note; never silently rewrite history or promote a research note directly to canon. Mark `SUPERSEDED` or `RETRACTED` with links and reason.

## Agent write contract

Each agent may **propose** new research notes on its own branch or PR. No agent should deposit raw scraped pages, social media timelines, unfiltered chat logs, credentials or sensitive private data. Only curated, attributed, license-safe notes. Include an index change in the same PR. A research deposit does not imply the science adversary has passed the corresponding story claim.

## Link-rot resilience

A URL going dead must not destroy the local explanation, parameters, uncertainty or counterarguments. For high-impact findings, additionally record permanent identifiers, the exact tested software/model version, environment, reproducibility recipe, and (where permitted) a hash of source artifacts. If the underlying primary source was not examined, state that prominently. Local summaries are a *working evidence record*, not a substitute for verifying contested results when possible.

## Minimal completion criteria

A note is not complete if it consists only of a headline, link, abstract, marketing claims, or a generic summary. It must answer: **What was actually demonstrated? Under which conditions? How strong is the evidence? What can we safely infer? What remains unknown? Why does it matter to the story?**
