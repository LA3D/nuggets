# AI Success Factors: Engineering Trust in Deployments
Blog and weekly slides for LA3D Projects including [Trusted AI](https://github.com/nd-crane), [CI-Compass](https://ci-compass.org/), and related projects.

## Content structure

- `posts/` contains the existing blog.
- `projects/` contains current research-project hubs and dated updates.
- `slides/` is the historical Nuggets slide archive; its paths remain stable so published links continue to work.
- `templates/nugget-reveal/` contains the canonical research-update deck template.

Create an AI4C2 update with:

```bash
python .agents/skills/nuggets-deck/scripts/new_deck.py ai4c2 YYYY-MM-DD --title "AI4C2 Research Update"
```

New project updates inherit shared Reveal.js settings and are drafts by default. Rendering or publishing the public site is a separate step.
