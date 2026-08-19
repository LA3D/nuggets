#!/usr/bin/env python3
"""Create a dated project-update deck from the canonical template."""

from __future__ import annotations

import argparse
from datetime import date
import re
from pathlib import Path


SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def repository_root() -> Path:
    return Path(__file__).resolve().parents[4]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", help="project slug (for example: ai4c2)")
    parser.add_argument("date", help="meeting date in YYYY-MM-DD format")
    parser.add_argument("--title", help="deck title (defaults to '<Project> Research Update')")
    args = parser.parse_args()

    if not SLUG.fullmatch(args.project):
        parser.error("project must be lowercase kebab-case (for example: ai4c2)")
    try:
        date.fromisoformat(args.date)
    except ValueError:
        parser.error("date must be a valid date in YYYY-MM-DD format")

    root = repository_root()
    source = root / "templates" / "nugget-reveal" / "index.qmd"
    updates = root / "projects" / args.project / "updates"
    destination = updates / args.date

    if destination.exists():
        parser.error(f"refusing to overwrite existing path: {destination}")
    if not source.is_file():
        parser.error(f"template not found: {source}")
    if not (updates / "_metadata.yml").is_file():
        parser.error(f"project update metadata not found: {updates / '_metadata.yml'}")

    destination.mkdir(parents=False)
    project_label = args.project.replace("-", " ").upper()
    title = args.title or f"{project_label} Research Update"
    content = source.read_text(encoding="utf-8")
    content = content.replace("{{TITLE}}", title)
    content = content.replace("{{DATE}}", args.date)
    content = content.replace("{{PROJECT_LABEL}}", project_label)
    output = destination / "index.qmd"
    output.write_text(content, encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
