#!/usr/bin/env python3
"""Render repository Marp decks into Quarto's GitHub Pages output tree."""

from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import sys

from learning_annotations import (
    DEFAULT_SITE_URL,
    annotations_enabled,
    build_annotation_page,
    canonical_deck_url,
    inject_annotation_page,
    parse_notes_export,
    publish_vocabulary,
    rendered_slide_ids,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "docs")
THEME = ROOT / "themes" / "marp" / "ai4c2.css"
SOURCE_NAME = "index.marp.md"
SITE_URL = os.environ.get("NUGGETS_SITE_URL", DEFAULT_SITE_URL)


def display_path(path: Path) -> Path:
    try:
        return path.relative_to(ROOT)
    except ValueError:
        return path


def render(source: Path) -> Path:
    relative_directory = source.parent.relative_to(ROOT)
    output_directory = OUTPUT_ROOT / relative_directory
    output_directory.mkdir(parents=True, exist_ok=True)
    output = output_directory / "index.html"

    command = [
        "marp",
        "--html",
        "--template",
        "bare",
        "--theme",
        str(THEME),
        str(source),
        "--output",
        str(output),
    ]
    subprocess.run(command, cwd=ROOT, check=True)

    # Marp's bare template defaults the browser gutter to black. Keep the
    # surrounding page consistent with the light AI4C2 slide canvas.
    html = output.read_text(encoding="utf-8")
    override = "<style>body{background:#eef0f4!important}</style>"
    if override not in html:
        html = html.replace("</head>", f"{override}</head>", 1)

    markdown = source.read_text(encoding="utf-8")
    if annotations_enabled(markdown):
        notes_result = subprocess.run(
            ["marp", "--notes", "--output", "-", str(source)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        records = parse_notes_export(notes_result.stdout)
        page = build_annotation_page(
            records,
            rendered_slide_ids(html),
            canonical_deck_url(SITE_URL, relative_directory),
            SITE_URL,
        )
        html = inject_annotation_page(html, page)

    output.write_text(html, encoding="utf-8")

    assets = source.parent / "assets"
    if assets.is_dir():
        shutil.copytree(assets, output_directory / "assets", dirs_exist_ok=True)

    return output


def main() -> int:
    if shutil.which("marp") is None:
        print(
            "Marp CLI is required to build index.marp.md decks. "
            "Install it with: brew install marp-cli",
            file=sys.stderr,
        )
        return 1

    vocabulary = publish_vocabulary(ROOT, OUTPUT_ROOT)
    print(f"Published agentic-learning vocabulary -> {display_path(vocabulary)}")

    sources = sorted(
        path
        for path in ROOT.glob(f"projects/**/{SOURCE_NAME}")
        if OUTPUT_ROOT not in path.parents
    )
    for source in sources:
        output = render(source)
        print(f"Rendered {source.relative_to(ROOT)} -> {display_path(output)}")

    if not sources:
        print(f"No {SOURCE_NAME} sources found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
