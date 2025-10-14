import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.analyze_brief import analyze_brief
from scripts.generate_protocol_sequence import (
    SCRIPT_REGISTRY_PATH,
    build_commands,
    load_registry,
)


@pytest.fixture(scope="module")
def registry() -> dict:
    return load_registry(SCRIPT_REGISTRY_PATH)


def write_brief(tmp_path: Path, frontmatter: str, body: str = "") -> Path:
    content = "---\n" + frontmatter.strip() + "\n---\n" + body
    brief_path = tmp_path / "PROJECT-BRIEF.md"
    brief_path.write_text(content, encoding="utf-8")
    return brief_path


def test_simple_web_app_flow(tmp_path: Path, registry: dict) -> None:
    brief = write_brief(
        tmp_path,
        """
name: Test Web App
project_type: web-app
frontend: react
backend: node
complexity: simple
        """,
        body="Build a marketing landing page with authentication and analytics.",
    )

    analysis = analyze_brief(brief)
    analysis_dict = json.loads(analysis.to_json())

    assert "6-operations" not in analysis.detected_protocols
    assert analysis.detected_protocols[:3] == ["0-bootstrap", "1-prd-creation", "2-task-generation"]

    commands_dir = tmp_path / "commands"
    artifacts = build_commands(analysis_dict, commands_dir, registry)
    assert len(artifacts) == len(analysis.detected_protocols)
    bootstrap_command = (commands_dir / artifacts[0].filename).read_text(encoding="utf-8")
    assert "scripts/normalize_project_rules.py" in bootstrap_command


def test_enterprise_operations_detection(tmp_path: Path, registry: dict) -> None:
    brief = write_brief(
        tmp_path,
        """
name: Enterprise Platform
project_type: platform
backend: python
complexity: complex
lifecycle: production
        """,
        body="""
We require 24/7 operations, deployment automation, monitoring, and incident response.
Ensure compliance with SOC2 and GDPR.
        """,
    )

    analysis = analyze_brief(brief)
    analysis_dict = json.loads(analysis.to_json())

    assert "6-operations" in analysis.detected_protocols
    assert "4-quality-audit" in analysis.detected_protocols
    assert "SOC2" in analysis.metadata["compliance"]

    commands_dir = tmp_path / "enterprise_commands"
    artifacts = build_commands(analysis_dict, commands_dir, registry)

    operations_command = None
    for artifact in artifacts:
        if artifact.slug == "6-operations":
            operations_command = (commands_dir / artifact.filename).read_text(encoding="utf-8")
            break
    assert operations_command is not None
    assert "deploy_backend.sh" in operations_command
    assert "collect_perf.py" in operations_command


def test_ml_brief_adds_experiments(tmp_path: Path, registry: dict) -> None:
    brief = write_brief(
        tmp_path,
        """
name: ML Forecasting Service
project_type: ml
backend: python
complexity: moderate
        """,
        body="""
The solution trains machine learning models and deploys inference endpoints.
Monitoring model drift and experiment tracking are required.
        """,
    )

    analysis = analyze_brief(brief)
    analysis_dict = json.loads(analysis.to_json())

    assert "ml-experiments" in analysis.detected_protocols

    commands_dir = tmp_path / "ml_commands"
    artifacts = build_commands(analysis_dict, commands_dir, registry)

    ml_command = None
    for artifact in artifacts:
        if artifact.slug == "ml-experiments":
            ml_command = (commands_dir / artifact.filename).read_text(encoding="utf-8")
            break
    assert ml_command is not None
    assert "run_workflow.py" in ml_command
