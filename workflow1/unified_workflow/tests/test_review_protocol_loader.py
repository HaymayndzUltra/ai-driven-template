"""Tests for the review protocol loader utilities."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
module_path = project_root / "unified_workflow" / "automation" / "review_protocol_loader.py"
spec = importlib.util.spec_from_file_location(
    "unified_workflow.automation.review_protocol_loader", module_path
)
module = importlib.util.module_from_spec(spec)
assert spec and spec.loader  # for mypy type checking
module.__package__ = "unified_workflow.automation"
sys.modules[spec.name] = module
spec.loader.exec_module(module)

ReviewProtocolLoader = module.ReviewProtocolLoader


class ReviewProtocolLoaderTests(unittest.TestCase):
    """Validate review protocol discovery and parsing."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[2]
        cls.loader = ReviewProtocolLoader(cls.repo_root)

    def test_available_protocols_lists_expected_entries(self) -> None:
        """Loader should return a non-empty list of protocol slugs."""
        protocols = self.loader.available_protocols()
        self.assertTrue(protocols, "Expected to discover review protocols")
        self.assertIn("code-review", protocols)

    def test_load_returns_structured_protocol(self) -> None:
        """Loaded protocol includes parsed checklist and metadata."""
        protocol = self.loader.load("code-review")
        self.assertEqual(protocol.slug, "code-review")
        self.assertTrue(protocol.path.exists())
        self.assertTrue(protocol.title)
        self.assertTrue(protocol.checklist, "Checklist should not be empty")
        self.assertIn("checklist", protocol.to_dict())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
