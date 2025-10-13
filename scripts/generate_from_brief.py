#!/usr/bin/env python3
"""
Brief-driven project orchestration that generates separate frontend and backend projects
with curated Cursor rules per domain.

Usage:
  python scripts/generate_from_brief.py \
    --brief docs/briefs/project1/brief.md \
    --output-root ../_generated \
    --force --yes
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path
from typing import Dict, List
import sys
import shlex

from project_generator.core.brief_parser import BriefParser


FRONTEND_RULES = {
    "nextjs": ["nextjs.mdc", "nextjs-formatting.mdc", "nextjs-rsc-and-client.mdc", "typescript.mdc"],
    "angular": ["angular.mdc", "typescript.mdc"],
    "nuxt": ["vue.mdc", "typescript.mdc"],
    "expo": ["expo.mdc", "react-native.mdc", "typescript.mdc"],
}

BACKEND_RULES = {
    "fastapi": ["fastapi.mdc", "python.mdc", "rest-api.mdc", "open-api.mdc"],
    "django": ["django.mdc", "python.mdc", "rest-api.mdc", "open-api.mdc"],
    "nestjs": ["nodejs.mdc", "typescript.mdc", "rest-api.mdc", "open-api.mdc"],
    "go": ["golang.mdc", "nethttp.mdc", "rest-api.mdc", "open-api.mdc"],
}

DB_ADDONS = {
    "mongodb": ["mongodb.mdc"],
    "firebase": ["firebase.mdc"],
}

COMPLIANCE_RULES = {
    "hipaa": "industry-compliance-hipaa.mdc",
    "gdpr": "industry-compliance-gdpr.mdc",
    "sox": "industry-compliance-sox.mdc",
    "pci": "industry-compliance-pci.mdc",
}


def write_rules_manifest(manifest_path: Path, names: List[str]) -> None:
    # Deduplicate while preserving order
    seen = set()
    ordered: List[str] = []
    for n in names:
        if n not in seen:
            seen.add(n)
            ordered.append(n)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(ordered, indent=2), encoding="utf-8")


def build_fe_manifest(frontend: str, compliance: List[str]) -> List[str]:
    rules = list(FRONTEND_RULES.get(frontend, []))
    # Domain rules (focused)
    rules += [
        "accessibility.mdc",
        "nextjs-a11y.mdc" if frontend == "nextjs" else None,
    ]
    return [r for r in rules if r]


def build_be_manifest(backend: str, database: str, compliance: List[str]) -> List[str]:
    rules = list(BACKEND_RULES.get(backend, []))
    rules += DB_ADDONS.get(database, [])
    # Domain rules common to backends (focused)
    rules += [
        "performance.mdc",
        "observability.mdc",
    ]
    return rules


def run_argv(argv: list[str], cwd: Path | None = None) -> int:
    try:
        out = subprocess.run(argv, cwd=str(cwd) if cwd else None, check=False, text=True)
        return out.returncode
    except Exception as e:
        print(f"[ERROR] command failed: {argv}: {e}")
        return 1


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate separate FE/BE projects from brief.md with curated rules")
    p.add_argument("--brief", required=True, help="Path to brief.md")
    p.add_argument("--output-root", default="../_generated", help="Root directory for generated projects")
    p.add_argument("--force", action="store_true", help="Overwrite existing project directories")
    p.add_argument("--yes", action="store_true", help="Run non-interactively")
    p.add_argument("--workers", type=int, default=8)
    return p.parse_args()


def main() -> None:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    output_root = Path(args.output_root)
    if not output_root.is_absolute():
        output_root = (repo_root / output_root).resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    spec = BriefParser(args.brief).parse()

    # Use the same Python interpreter that launched this script
    python_bin = shlex.quote(os.environ.get("PYTHON", sys.executable or "python3"))

    # FE project (if any)
    fe_name = f"{spec.name}-frontend" if spec.frontend != "none" else None
    be_name = f"{spec.name}-backend" if spec.backend != "none" else None

    # Determine compliance fallback if not provided
    comp_list = list(spec.compliance)
    if not comp_list:
        if spec.industry == "ecommerce":
            comp_list = ["pci", "gdpr"]
        elif spec.industry == "finance":
            comp_list = ["sox", "pci"]
        elif spec.industry == "healthcare":
            comp_list = ["hipaa"]
        else:
            comp_list = ["gdpr"]

    if fe_name:
        fe_dir = output_root / fe_name
        if fe_dir.exists() and args.force:
            import shutil
            shutil.rmtree(fe_dir)
        manifest = build_fe_manifest(spec.frontend, comp_list)
        # Write manifest OUTSIDE the target project directory to avoid being deleted by generator --force
        fe_manifest_path = output_root / "_rules_manifests" / f"{fe_name}.json"
        write_rules_manifest(fe_manifest_path, manifest)
        cmd = (
            f"{python_bin} scripts/generate_client_project.py"
            f" --name {fe_name}"
            f" --industry {spec.industry}"
            f" --project-type web"
            f" --frontend {spec.frontend}"
            f" --backend none"
            f" --database none"
            f" --auth {spec.auth}"
            f" --deploy {spec.deploy}"
            f" --output-dir {str(output_root)}"
            f" --workers {args.workers}"
            f" --include-cursor-assets"
            f" --minimal-cursor"
            f" --rules-manifest {str(fe_manifest_path)}"
            f" {'--features ' + ','.join(spec.features) if spec.features else ''}"
            f" --skip-system-checks"
            f" --yes"
            f" {'--force' if args.force else ''}"
        ).strip()
        print(f"\n[FE] {cmd}")
        code = run_argv(shlex.split(cmd), cwd=repo_root)
        if code != 0:
            raise SystemExit(code)

    # BE project (if any)
    if be_name:
        be_dir = output_root / be_name
        if be_dir.exists() and args.force:
            import shutil
            shutil.rmtree(be_dir)
        manifest = build_be_manifest(spec.backend, spec.database, comp_list)
        # Write manifest OUTSIDE the target project directory to avoid being deleted by generator --force
        be_manifest_path = output_root / "_rules_manifests" / f"{be_name}.json"
        write_rules_manifest(be_manifest_path, manifest)
        cmd = (
            f"{python_bin} scripts/generate_client_project.py"
            f" --name {be_name}"
            f" --industry {spec.industry}"
            f" --project-type api"
            f" --frontend none"
            f" --backend {spec.backend}"
            f" --database {spec.database}"
            f" --auth {spec.auth}"
            f" --deploy {spec.deploy}"
            f" --output-dir {str(output_root)}"
            f" --workers {args.workers}"
            f" --include-cursor-assets"
            f" --minimal-cursor"
            f" --rules-manifest {str(be_manifest_path)}"
            f" {'--features ' + ','.join(spec.features) if spec.features else ''}"
            f" {'--compliance ' + ','.join(comp_list) if comp_list else ''}"
            f" --skip-system-checks"
            f" --yes"
            f" {'--force' if args.force else ''}"
        ).strip()
        print(f"\n[BE] {cmd}")
        code = run_argv(shlex.split(cmd), cwd=repo_root)
        if code != 0:
            raise SystemExit(code)

    print("\n✅ Generation complete.")


if __name__ == "__main__":
    main()

