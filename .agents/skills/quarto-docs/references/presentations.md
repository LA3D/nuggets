# Reveal.js and presentations route

Use this route for `revealjs`, slide structure, speaker notes/view, navigation, themes, fragments, incremental content, multiplexing, self-contained output, printing, and presentation-specific format options.

## Lookup sequence

1. Search the live [Quarto LLM index](https://quarto.org/llms.txt) for the exact feature plus `revealjs` or the requested presentation format.
2. Prefer the narrowest matching page and fetch it. Useful official entry points:
   - [Revealjs](https://quarto.org/docs/presentations/revealjs/index.llms.md)
   - [Presenting Slides](https://quarto.org/docs/presentations/revealjs/presenting.llms.md)
   - [Reveal Themes](https://quarto.org/docs/presentations/revealjs/themes.llms.md)
   - [Advanced Reveal](https://quarto.org/docs/presentations/revealjs/advanced.llms.md)
   - [Revealjs Options](https://quarto.org/docs/reference/formats/presentations/revealjs.llms.md)
   - [Presentations](https://quarto.org/docs/presentations/index.llms.md) for cross-format questions
3. Cite the fetched page that establishes the answer. Use the options reference for exact YAML keys; use the guide pages for authoring and behavior.

Search terms: `speaker notes`, `speaker view`, `slide-number`, `incremental`, `fragments`, `theme`, `self-contained`, `print pdf`, `multiplex`.

If implementation is requested, inspect the deck frontmatter and nearby project configuration after the lookup. Do not silently convert a Reveal.js deck to PowerPoint, Beamer, or another format.
