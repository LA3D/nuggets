from __future__ import annotations

from html.parser import HTMLParser
import json
from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from learning_annotations import (  # noqa: E402
    ANNOTATION_CONTEXT,
    AnnotationError,
    CUSTOM_PURPOSES,
    SCRIPT_ID,
    build_annotation_page,
    canonical_deck_url,
    inject_annotation_page,
    parse_notes_export,
    publish_vocabulary,
    rendered_slide_ids,
)


def note(slide_id: str, extra: str = "") -> str:
    return f"""AGENTIC LEARNING NOTES

Slide ID — {slide_id}
Learning objective — Learn {slide_id}.
Core claim — Claim {slide_id}.
Explain — Explain {slide_id}.{extra}
Misconception — Not that.
Check — Why?
Source routes — Follow the source.
Transition — Continue.
"""


class _ScriptParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_script = False
        self.scripts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "script" and dict(attrs).get("id") == SCRIPT_ID:
            self.in_script = True
            self.scripts.append("")

    def handle_data(self, data: str) -> None:
        if self.in_script:
            self.scripts[-1] += data

    def handle_endtag(self, tag: str) -> None:
        if tag == "script" and self.in_script:
            self.in_script = False


class LearningAnnotationTests(unittest.TestCase):
    def test_builds_valid_ordered_web_annotations(self) -> None:
        records = parse_notes_export(f"{note('one')}\n---\n{note('two')}")
        canonical = canonical_deck_url(
            "https://example.test/nuggets", Path("projects/example/update")
        )
        page = build_annotation_page(
            records, ["1", "2"], canonical, "https://example.test/nuggets"
        )

        self.assertEqual(page["type"], "AnnotationPage")
        self.assertEqual(page["@context"][0], ANNOTATION_CONTEXT)
        self.assertEqual(len(page["items"]), 2)
        self.assertEqual(page["items"][1]["target"], f"{canonical}#2")
        self.assertEqual(
            page["items"][0]["id"], f"{canonical}#annotation-one"
        )
        purposes = {body["purpose"] for body in page["items"][0]["body"]}
        self.assertIn("describing", purposes)
        self.assertIn("questioning", purposes)
        for term in CUSTOM_PURPOSES:
            self.assertIn(
                f"https://example.test/nuggets/ns/agentic-learning/#{term}", purposes
            )

    def test_injection_is_discoverable_valid_json_and_script_safe(self) -> None:
        records = parse_notes_export(note("safe", " </script><p>unsafe</p>"))
        page = build_annotation_page(
            records,
            ["1"],
            "https://example.test/deck/",
            "https://example.test",
        )
        output = inject_annotation_page(
            '<html><head></head><body><section id="1"></section></body></html>',
            page,
        )

        self.assertEqual(output.count('name="agentic-learning"'), 1)
        self.assertEqual(output.count(f'id="{SCRIPT_ID}"'), 1)
        self.assertNotIn("</script><p>unsafe</p>", output)
        parser = _ScriptParser()
        parser.feed(output)
        self.assertEqual(len(parser.scripts), 1)
        parsed = json.loads(parser.scripts[0])
        self.assertEqual(parsed["items"][0]["target"], "https://example.test/deck/#1")

    def test_rejects_missing_fields_duplicates_and_count_mismatch(self) -> None:
        with self.assertRaisesRegex(AnnotationError, "missing required fields"):
            parse_notes_export(
                "AGENTIC LEARNING NOTES\n\nSlide ID — incomplete"
            )
        with self.assertRaisesRegex(AnnotationError, "must be unique"):
            parse_notes_export(f"{note('same')}\n---\n{note('same')}")
        records = parse_notes_export(note("one"))
        with self.assertRaisesRegex(AnnotationError, "does not match"):
            build_annotation_page(records, ["1", "2"], "https://example.test/deck/")

    def test_finds_rendered_slide_fragments(self) -> None:
        html = '<section id="1"></section><div><section id="2"></section></div>'
        self.assertEqual(rendered_slide_ids(html), ["1", "2"])

    def test_publishes_dereferenceable_vocabulary_resources(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            destination = publish_vocabulary(ROOT, Path(temporary))
            context_path = destination / "context.jsonld"
            index_path = destination / "index.html"
            self.assertTrue(context_path.is_file())
            self.assertTrue(index_path.is_file())
            context = json.loads(context_path.read_text(encoding="utf-8"))["@context"]
            html = index_path.read_text(encoding="utf-8")
            for term in CUSTOM_PURPOSES:
                self.assertIn(term, context)
                self.assertIn(f'id="{term}"', html)


if __name__ == "__main__":
    unittest.main()
