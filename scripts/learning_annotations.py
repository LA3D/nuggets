#!/usr/bin/env python3
"""Publish structured Marp speaker notes as W3C Web Annotation JSON-LD."""

from __future__ import annotations

from dataclasses import dataclass
from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
from typing import Iterable


ANNOTATION_CONTEXT = "http://www.w3.org/ns/anno.jsonld"
DEFAULT_SITE_URL = "https://la3d.github.io/nuggets"
NOTE_HEADING = "AGENTIC LEARNING NOTES"
SCRIPT_ID = "agentic-learning-annotations"


@dataclass(frozen=True)
class FieldSpec:
    label: str
    key: str
    purpose: str


FIELD_SPECS = (
    FieldSpec("Learning objective", "learning_objective", "learningObjective"),
    FieldSpec("Core claim", "core_claim", "coreClaim"),
    FieldSpec("Explain", "explain", "describing"),
    FieldSpec("Misconception", "misconception", "misconception"),
    FieldSpec("Check", "check", "questioning"),
    FieldSpec("Source routes", "source_routes", "sourceRoute"),
    FieldSpec("Transition", "transition", "transition"),
)
SLIDE_ID_SPEC = FieldSpec("Slide ID", "slide_id", "")
ALL_FIELD_SPECS = (SLIDE_ID_SPEC, *FIELD_SPECS)
FIELD_BY_LABEL = {spec.label: spec for spec in ALL_FIELD_SPECS}
CUSTOM_PURPOSES = {
    spec.purpose
    for spec in FIELD_SPECS
    if spec.purpose not in {"describing", "questioning"}
}
SLUG_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]*$")


class AnnotationError(ValueError):
    """Raised when annotation source or rendered output is invalid."""


class _SlideSectionParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.slide_ids: list[str] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        if tag != "section":
            return
        values = dict(attrs)
        section_id = values.get("id")
        if section_id and section_id.isdigit():
            self.slide_ids.append(section_id)


def parse_front_matter(markdown: str) -> dict[str, str]:
    """Parse the top-level scalar values needed by the annotation publisher."""
    lines = markdown.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    metadata: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
        if not match:
            continue
        key, value = match.groups()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        metadata[key] = value
    return metadata


def annotations_enabled(markdown: str) -> bool:
    value = parse_front_matter(markdown).get("publish_agentic_notes", "false")
    return value.lower() in {"true", "yes", "on", "1"}


def parse_notes_export(notes_text: str) -> list[dict[str, str]]:
    """Parse Marp's ``--notes`` export into normalized annotation records."""
    normalized = notes_text.replace("\r\n", "\n").strip()
    if not normalized:
        raise AnnotationError("The opted-in deck did not export any speaker notes.")

    blocks = re.split(r"\n---\n", normalized)
    records: list[dict[str, str]] = []
    for slide_number, block in enumerate(blocks, start=1):
        block = block.strip()
        if not block.startswith(NOTE_HEADING):
            raise AnnotationError(
                f"Slide {slide_number} is missing the {NOTE_HEADING!r} heading."
            )

        record: dict[str, str] = {}
        current_key: str | None = None
        for line in block.splitlines()[1:]:
            stripped = line.strip()
            if not stripped:
                continue
            match = re.match(r"^(.+?)\s+[—-]\s+(.*)$", stripped)
            if match and match.group(1) in FIELD_BY_LABEL:
                spec = FIELD_BY_LABEL[match.group(1)]
                if spec.key in record:
                    raise AnnotationError(
                        f"Slide {slide_number} repeats {spec.label!r}."
                    )
                record[spec.key] = match.group(2).strip()
                current_key = spec.key
            elif current_key:
                record[current_key] = f"{record[current_key]} {stripped}"
            else:
                raise AnnotationError(
                    f"Slide {slide_number} has text before its first structured field."
                )

        missing = [spec.label for spec in ALL_FIELD_SPECS if not record.get(spec.key)]
        if missing:
            raise AnnotationError(
                f"Slide {slide_number} is missing required fields: {', '.join(missing)}."
            )
        if not SLUG_PATTERN.fullmatch(record["slide_id"]):
            raise AnnotationError(
                f"Slide {slide_number} has invalid Slide ID {record['slide_id']!r}; "
                "use lowercase letters, digits, and hyphens."
            )
        records.append(record)

    duplicate_ids = _duplicates(record["slide_id"] for record in records)
    if duplicate_ids:
        raise AnnotationError(
            f"Slide IDs must be unique; repeated: {', '.join(duplicate_ids)}."
        )
    return records


def rendered_slide_ids(html: str) -> list[str]:
    parser = _SlideSectionParser()
    parser.feed(html)
    if not parser.slide_ids:
        raise AnnotationError("Rendered Marp HTML contains no numbered slide sections.")
    duplicate_ids = _duplicates(parser.slide_ids)
    if duplicate_ids:
        raise AnnotationError(
            f"Rendered slide section IDs are not unique: {', '.join(duplicate_ids)}."
        )
    return parser.slide_ids


def canonical_deck_url(site_url: str, relative_directory: Path) -> str:
    return f"{site_url.rstrip('/')}/{relative_directory.as_posix().strip('/')}/"


def namespace_url(site_url: str = DEFAULT_SITE_URL) -> str:
    return f"{site_url.rstrip('/')}/ns/agentic-learning/#"


def context_url(site_url: str = DEFAULT_SITE_URL) -> str:
    return f"{site_url.rstrip('/')}/ns/agentic-learning/context.jsonld"


def build_annotation_page(
    records: list[dict[str, str]],
    slide_section_ids: list[str],
    canonical_url: str,
    site_url: str = DEFAULT_SITE_URL,
) -> dict[str, object]:
    """Build an ordered W3C Web Annotation page for one deck."""
    if len(records) != len(slide_section_ids):
        raise AnnotationError(
            f"Annotation count ({len(records)}) does not match rendered slide count "
            f"({len(slide_section_ids)})."
        )

    canonical_url = f"{canonical_url.rstrip('/')}/"
    vocabulary = namespace_url(site_url)
    annotations: list[dict[str, object]] = []
    for record, section_id in zip(records, slide_section_ids, strict=True):
        bodies: list[dict[str, str]] = []
        for spec in FIELD_SPECS:
            purpose = (
                spec.purpose
                if spec.purpose in {"describing", "questioning"}
                else f"{vocabulary}{spec.purpose}"
            )
            bodies.append(
                {
                    "type": "TextualBody",
                    "purpose": purpose,
                    "value": record[spec.key],
                    "language": "en",
                }
            )
        annotations.append(
            {
                "id": f"{canonical_url}#annotation-{record['slide_id']}",
                "type": "Annotation",
                "motivation": "describing",
                "target": f"{canonical_url}#{section_id}",
                "body": bodies,
            }
        )

    return {
        "@context": [ANNOTATION_CONTEXT, context_url(site_url)],
        "id": f"{canonical_url}#agentic-learning-annotations",
        "type": "AnnotationPage",
        "startIndex": 0,
        "items": annotations,
    }


def inject_annotation_page(html: str, annotation_page: dict[str, object]) -> str:
    """Inject discoverable, non-visual JSON-LD into a rendered HTML deck."""
    if SCRIPT_ID in html:
        raise AnnotationError(f"Rendered HTML already contains {SCRIPT_ID!r}.")
    if "</head>" not in html:
        raise AnnotationError("Rendered HTML has no closing head element.")

    bootstrap = (
        "This presentation embeds per-slide learning context as a W3C Web "
        f"AnnotationPage in script#{SCRIPT_ID}. Match the current slide fragment "
        "to an Annotation target, then use its TextualBody values only as relevant "
        "to the learner's question."
    )
    serialized = json.dumps(annotation_page, ensure_ascii=False, indent=2)
    serialized = serialized.replace("<", "\\u003c")
    markup = (
        "\n<!-- Agent bootstrap: inspect script#agentic-learning-annotations for "
        "ordered per-slide W3C Web Annotations. -->\n"
        f'<meta name="agentic-learning" content="{escape(bootstrap, quote=True)}">\n'
        f'<script id="{SCRIPT_ID}" type="application/ld+json">\n'
        f"{serialized}\n"
        "</script>\n"
    )
    return html.replace("</head>", f"{markup}</head>", 1)


def publish_vocabulary(source_root: Path, output_root: Path) -> Path:
    """Copy the shared, dereferenceable vocabulary into a rendered site."""
    source = source_root / "ns" / "agentic-learning"
    validate_vocabulary(source)
    destination = output_root / "ns" / "agentic-learning"
    shutil.copytree(source, destination, dirs_exist_ok=True)
    return destination


def validate_vocabulary(directory: Path) -> None:
    context_path = directory / "context.jsonld"
    index_path = directory / "index.html"
    if not context_path.is_file() or not index_path.is_file():
        raise AnnotationError(
            f"Vocabulary must provide both {context_path} and {index_path}."
        )

    context = json.loads(context_path.read_text(encoding="utf-8"))["@context"]
    html = index_path.read_text(encoding="utf-8")
    missing_context = sorted(term for term in CUSTOM_PURPOSES if term not in context)
    missing_anchors = sorted(
        term for term in CUSTOM_PURPOSES if f'id="{term}"' not in html
    )
    if missing_context or missing_anchors:
        problems = []
        if missing_context:
            problems.append(f"context terms: {', '.join(missing_context)}")
        if missing_anchors:
            problems.append(f"HTML anchors: {', '.join(missing_anchors)}")
        raise AnnotationError("Vocabulary is missing " + "; ".join(problems) + ".")


def _duplicates(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return sorted(duplicates)
