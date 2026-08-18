---
name: quarto-docs
description: Use for current Quarto documentation about configuration, authoring, computation, projects, output formats, Reveal.js presentations, websites, blogs, publishing, extensions, CLI commands, and troubleshooting. Do not use for generic Markdown questions or unrelated slide tools.
---

# Quarto Docs

Provide current, cited Quarto guidance while preserving the user's chosen format and the conventions of any existing project.

## Official lookup first

**First substantive action for a Quarto documentation request:** search [Quarto's live LLM index](https://quarto.org/llms.txt) with a concise topic-specific query, select the smallest relevant `.llms.md` page, and actually open or fetch that page. Never answer from a search snippet or the index entry alone. If the retrieval tool cannot open the indexed `.llms.md` URL, fetch its corresponding canonical `quarto.org` HTML page and disclose that fallback. Use only `quarto.org` documentation for normative claims and cite the exact fetched page. If the official pages do not establish behavior, or appear newer than the installed Quarto version, say so explicitly.

For a narrow factual question, fetch the exact official page and answer without reading a route reference.

## Choose zero or one primary route

Read only the first matching reference when specialized routing is useful:

- Reveal.js or presentation authoring, options, presenting, themes, notes, or PDF behavior: [presentations.md](references/presentations.md)
- Websites, blogs, navigation, listings, or GitHub Pages and other publishing: [websites-publishing.md](references/websites-publishing.md)
- Document authoring, citations, cross-references, figures, tables, code cells, or computation: [authoring-computation.md](references/authoring-computation.md)
- Project structure, `_quarto.yml`, profiles, execution management, or CLI commands: [projects-cli-configuration.md](references/projects-cli-configuration.md)
- Extensions, custom formats, Lua, advanced features, or troubleshooting: [extensions-advanced-troubleshooting.md](references/extensions-advanced-troubleshooting.md)

Do not load every reference. Search the live index again when the exact topic is not covered by a curated entry point.

## Project-aware behavior

- For specific syntax, options, errors, or publishing behavior, establish the official documentation first.
- For implementation or compatibility work, then inspect the relevant local files and run `quarto --version` when available. Compare the installed version with the fetched documentation or release notes.
- Documentation-only questions do not authorize rendering, previewing, publishing, installing extensions, or editing files.
- Before changing a project, preserve its existing format, engine, directory layout, configuration style, and publishing workflow unless the user requests a migration.
- Prefer focused checks over rendering an entire site. Publishing and extension installation are external mutations and require explicit user authorization.
