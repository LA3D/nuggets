# Extensions, advanced features, and troubleshooting route

Use this route for installing or developing extensions, custom formats, filters, shortcodes, Lua, project types, advanced internals, diagnostics, and unresolved Quarto errors.

## Lookup sequence

1. Search the live [Quarto LLM index](https://quarto.org/llms.txt) using the exact extension type, API, error text, and relevant installed version.
2. Fetch the smallest relevant official page. Useful entry points:
   - [Managing Extensions](https://quarto.org/docs/extensions/managing.llms.md)
   - [Creating Extensions](https://quarto.org/docs/extensions/creating.llms.md)
   - [Custom Formats](https://quarto.org/docs/extensions/formats.llms.md)
   - [Creating Filters](https://quarto.org/docs/extensions/filters.llms.md)
   - [Creating Shortcodes](https://quarto.org/docs/extensions/shortcodes.llms.md)
   - [Revealjs Plugins](https://quarto.org/docs/extensions/revealjs.llms.md)
   - [Lua Development](https://quarto.org/docs/extensions/lua.llms.md)
   - [Advanced User Documentation](https://quarto.org/docs/advanced/index.llms.md)
   - [Troubleshooting](https://quarto.org/docs/troubleshooting/index.llms.md)
   - [Release notes](https://quarto.org/docs/download/index.llms.md), followed by the exact installed-version changelog when compatibility matters
3. Cite official Quarto pages for Quarto behavior. Clearly label inferences when an error originates in Pandoc, a language engine, an extension repository, or the operating system.

Extension installation and publishing are mutations: explain commands for documentation requests, but execute them only with authorization. Preserve existing extension versions and project conventions unless the user asks to upgrade or replace them.
