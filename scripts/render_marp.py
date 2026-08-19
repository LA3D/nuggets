#!/usr/bin/env python3
"""Render repository Marp decks into Quarto's GitHub Pages output tree."""

from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "docs")
THEME = ROOT / "themes" / "marp" / "ai4c2.css"
SOURCE_NAME = "index.marp.md"


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

    sources = sorted(
        path
        for path in ROOT.glob(f"projects/**/{SOURCE_NAME}")
        if OUTPUT_ROOT not in path.parents
    )
    for source in sources:
        output = render(source)
        print(f"Rendered {source.relative_to(ROOT)} -> {output.relative_to(ROOT)}")

    if not sources:
        print(f"No {SOURCE_NAME} sources found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
