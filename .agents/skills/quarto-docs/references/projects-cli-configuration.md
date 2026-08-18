# Projects, CLI, and configuration route

Use this route for `_quarto.yml`, project types, profiles, render targets, execution management, environment configuration, scripts, and Quarto CLI commands.

## Lookup sequence

Search the live [Quarto LLM index](https://quarto.org/llms.txt) with the command, option, configuration key, or error. Fetch the smallest official page, favoring:

- [Project Basics](https://quarto.org/docs/projects/quarto-projects.llms.md)
- [Project Options](https://quarto.org/docs/reference/projects/options.llms.md)
- [Project Profiles](https://quarto.org/docs/projects/profiles.llms.md)
- [Managing Execution](https://quarto.org/docs/projects/code-execution.llms.md)
- [Project Scripts](https://quarto.org/docs/projects/scripts.llms.md)
- [Project Environment Variables](https://quarto.org/docs/projects/environment.llms.md)
- [Command Line Reference](https://quarto.org/docs/cli/index.llms.md)
- Narrow command pages such as [render](https://quarto.org/docs/cli/render.llms.md), [create](https://quarto.org/docs/cli/create.llms.md), [publish](https://quarto.org/docs/cli/publish.llms.md), and [use](https://quarto.org/docs/cli/use.llms.md)

For exact flags, use the narrow CLI command page. For implementation or compatibility, inspect `_quarto.yml` and related profiles only after the official lookup, then check `quarto --version`. Do not execute render, preview, serve, publish, create, or extension commands for a documentation-only request.
