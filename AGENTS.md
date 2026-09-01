# Nuggets authoring guide

Nuggets is the LA3D research-meeting slide and blog archive. Quarto `.qmd` files are authored source; `docs/` is generated GitHub Pages output.

## Preserve the archive

- Do not move, rename, or rewrite historical posts or decks unless the user explicitly asks. Their paths are public URLs.
- Do not hand-edit generated files in `docs/` or `_freeze/`.
- Do not render the whole site for a deck edit. Render only the deck being changed.
- Do not commit, push, or publish unless the user explicitly asks.
- Preserve unrelated untracked work, especially `slides/graphrag_3_7_25/`.

## Work in the saved checkout

- The user authorizes one agent at a time to edit the saved checkout directly.
- For routine repository work, do not create or use Git worktrees, and do not leave isolated worktrees that require a later merge into the saved checkout.

## Build a new presentation

Use the `$nuggets-deck` skill and `templates/nugget-reveal/index.qmd`. New published decks belong at `slides/<descriptive-slug>/index.qmd`; use `.agents/skills/nuggets-deck/scripts/new_deck.py <slug>` to scaffold one without overwriting files.

Work interactively:

1. Establish the meeting purpose, audience, desired decision or discussion, and source set.
2. Propose a narrative and slide outline; get user approval before drafting a full deck.
3. Scaffold from the canonical template and preserve its CRC/LA3D branding.
4. Keep one main claim per slide. Prefer diagrams and legible evidence over dense prose.
5. Record source links and provenance close to claims and images. Never fabricate a citation.
6. Use Obsidian/vault notes or private collaboration material only when the user explicitly identifies and approves it for this deck. Do not copy private material into the public repository by default.
7. Add speaker notes for context that should not crowd the slide.
8. Render the single deck, inspect the HTML visually at presentation dimensions, fix overflow and broken assets, and iterate with the user.

For exact Quarto syntax or behavior, use `$quarto-docs` and official Quarto documentation. The repository uses Reveal.js, the local `reveal-header` extension, `slides/images/crc.scss`, and existing logos in `slides/images/`.

## Publishing boundary

Drafting and local rendering do not authorize publication. Before publishing, confirm the title, date, status, citations, permissions for every asset, and whether the deck should appear in the public slide listing. Publishing normally updates generated `docs/`; keep that as a separate, explicit step.
