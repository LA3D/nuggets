# Websites, blogs, and publishing route

Use this route for website/blog structure, navigation, search, listings, output directories, drafts, and publishing destinations or CI.

## Lookup sequence

1. Search the live [Quarto LLM index](https://quarto.org/llms.txt) for the exact site or publishing topic.
2. Fetch the narrowest relevant official page. Useful entry points:
   - [Creating a Blog](https://quarto.org/docs/websites/website-blog.llms.md)
   - [Website Navigation](https://quarto.org/docs/websites/website-navigation.llms.md)
   - [Document Listings](https://quarto.org/docs/websites/website-listings.llms.md)
   - [Website Search](https://quarto.org/docs/websites/website-search.llms.md)
   - [Website Options](https://quarto.org/docs/reference/projects/websites.llms.md)
   - [Publishing Basics](https://quarto.org/docs/publishing/index.llms.md)
   - [GitHub Pages](https://quarto.org/docs/publishing/github-pages.llms.md)
   - [Publishing with CI](https://quarto.org/docs/publishing/ci.llms.md)
   - [CLI publish](https://quarto.org/docs/cli/publish.llms.md)
3. Cite the exact page. Distinguish documented alternatives such as checked-in `docs/`, a `gh-pages` branch, and GitHub Actions rather than assuming one.

Search terms: `website`, `blog`, `navbar`, `listing`, `output-dir`, `docs`, `gh-pages`, `GitHub Actions`, `freeze`, `publish`.

For “How does this site publish?” fetch the publishing page first, then inspect `_quarto.yml`, `_publish.yml`, `.github/workflows/`, `.nojekyll`, `.gitignore`, and repository branches as relevant. Do not publish, render, push, or change GitHub settings for a documentation-only request.
