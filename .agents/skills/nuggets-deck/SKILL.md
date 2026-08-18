---
name: nuggets-deck
description: Build or revise LA3D Nuggets research-meeting presentations in this repository using Quarto Reveal.js, the canonical CRC/LA3D template, approved source material, citations, speaker notes, focused rendering, and visual review. Use for deck planning, scaffolding, drafting, or presentation QA; do not use for PowerPoint or Google Slides.
---

# Nuggets Deck

Collaborate with the user to create an evidence-rich meeting presentation while preserving the public archive and established branding.

## Start with the story

Before drafting many slides, establish the audience, meeting purpose, desired outcome, time available, and approved source set. When the user has not settled the topic or phase name, leave those fields provisional rather than inventing them.

Propose a compact narrative and slide outline. Pause for approval at a meaningful editorial decision: the story, not every sentence. Then draft one main claim per slide, with evidence and a clear transition.

## Use the repository workflow

Read the root `AGENTS.md`, then [authoring-workflow.md](references/authoring-workflow.md). Scaffold new decks with:

```bash
python .agents/skills/nuggets-deck/scripts/new_deck.py <descriptive-slug>
```

The helper copies `templates/nugget-reveal/index.qmd` to `slides/<slug>/index.qmd` and refuses to overwrite an existing destination. Do not manually copy a historical deck as a template.

For exact Reveal.js syntax, rendering options, citations, extensions, or Quarto behavior, invoke `$quarto-docs` and consult the smallest relevant official page. Preserve the repository's Quarto format rather than converting to another slide system.

## Handle sources and assets carefully

- Use only sources the user supplied, approved, or asked you to research.
- Keep citations and image provenance close to the claim; never invent bibliographic details.
- Treat the Obsidian vault as private source material. Read only user-approved notes and do not publish private text or assets by default.
- Reuse the shared CRC/LA3D theme and logos. Do not redraw, recolor, or replace institutional branding.
- Write meaningful alt text or captions and keep projected text and diagrams legible.
- Put supporting detail, caveats, and transitions in Reveal.js speaker notes.

## Verify before handoff

Render only the deck being edited to a temporary output location when possible. Visually inspect the title, representative content, dense, image, and closing slides at 1600×900. Check overflow, contrast, broken links/assets, citation visibility, and speaker notes. Iterate on defects.

Drafting does not authorize updating `docs/`, publishing, committing, or pushing. Ask before those steps.
