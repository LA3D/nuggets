#!/usr/bin/env python3
"""Create a new Nuggets deck from the canonical repository template."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def repository_root() -> Path:
    return Path(__file__).resolve().parents[4]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("slug", help="lowercase kebab-case directory name")
    args = parser.parse_args()

    if not SLUG.fullmatch(args.slug):
        parser.error("slug must be lowercase kebab-case (for example: agentic-context)")

    root = repository_root()
    source = root / "templates" / "nugget-reveal" / "index.qmd"
    destination = root / "slides" / args.slug

    if destination.exists():
        parser.error(f"refusing to overwrite existing path: {destination}")
    if not source.is_file():
        parser.error(f"template not found: {source}")

    destination.mkdir(parents=False)
    shutil.copy2(source, destination / "index.qmd")
    print(destination / "index.qmd")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
