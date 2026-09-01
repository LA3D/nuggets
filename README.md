# AI Success Factors: Engineering Trust in Deployments
Blog and weekly slides for LA3D Projects including [Trusted AI](https://github.com/nd-crane), [CI-Compass](https://ci-compass.org/), and related projects.

## Content structure

- `posts/` contains the existing blog.
- `projects/` contains current research-project hubs and dated updates.
- `slides/` is the historical Nuggets slide archive; its paths remain stable so published links continue to work.
- `templates/nugget-reveal/` contains the canonical research-update deck template.
- `themes/marp/` contains shared themes for fast Marp update decks.

Create an AI4C2 update with:

```bash
python .agents/skills/nuggets-deck/scripts/new_deck.py ai4c2 YYYY-MM-DD --title "AI4C2 Research Update"
```

New project updates inherit shared Reveal.js settings and are drafts by default. Rendering or publishing the public site is a separate step.

## Mixed Quarto and Marp builds

The source filename selects the slide engine within a dated update directory:

- `index.qmd` is rendered by Quarto/Reveal.js.
- `index.marp.md` is rendered by Marp into the same directory under `docs/`.

Run the complete local site build with:

```bash
quarto render
```

Quarto renders the website and Reveal.js decks first. Its post-render script then finds every `index.marp.md` source and renders it with Marp's vertically scrolling `bare` template. Both kinds of presentation are therefore served from the existing GitHub Pages `docs/` tree.

Marp CLI must be installed and available on `PATH`. To rebuild only the Marp decks, run:

```bash
python3 scripts/render_marp.py
```

### Agentic learning annotations

Marp decks can opt into reusable, non-visual learning annotations by adding this front-matter field:

```yaml
publish_agentic_notes: true
```

Every slide in an opted-in deck must contain a Marp speaker-note comment with the following fields:

```markdown
<!--
AGENTIC LEARNING NOTES

Slide ID — stable-lowercase-id
Learning objective — ...
Core claim — ...
Explain — ...
Misconception — ...
Check — ...
Source routes — ...
Transition — ...
-->
```

The shared publisher in `scripts/learning_annotations.py` validates the notes and embeds one ordered W3C Web Annotation `AnnotationPage` in `script#agentic-learning-annotations`. Annotation targets use the deck's canonical URL plus its numbered slide fragment. The public vocabulary is published at `https://la3d.github.io/nuggets/ns/agentic-learning/`, and its reusable JSON-LD context is published at `https://la3d.github.io/nuggets/ns/agentic-learning/context.jsonld`.

Run the generic contract tests with:

```bash
python3 -m unittest discover -s tests -v
```

After reviewing the generated site, commit both the sources and `docs/`, then push `main`. GitHub Pages continues to publish from `main` → `docs/`.
