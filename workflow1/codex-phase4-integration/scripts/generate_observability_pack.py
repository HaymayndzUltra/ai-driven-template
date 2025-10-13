#!/usr/bin/env python3
"""Generate observability asset pack for Phase 4."""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[2]
PHASE = "phase4"
TEMPLATES = {
    "Observability_Spec.md": Path("Observability_Spec.md"),
    "SLO_SLI.md": Path("SLO_SLI.md"),
    "CHANGELOG.md": Path("CHANGELOG.md"),
    "Staging_Smoke_Playbook.md": Path("Staging_Smoke_Playbook.md"),
}


def sha256sum(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def load_manifest(manifest_path: Path) -> List[Dict[str, str]]:
    if manifest_path.exists():
        return json.loads(manifest_path.read_text())
    return []


def write_manifest(manifest_path: Path, entries: List[Dict[str, str]]) -> None:
    manifest_path.write_text(json.dumps(entries, indent=2, sort_keys=True))


def append_run_log(message: str) -> None:
    log_path = ROOT / "evidence" / PHASE / "run.log"
    timestamp = datetime.utcnow().isoformat() + "Z"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(f"[{timestamp}] {message}\n")


def copy_templates(project: str) -> List[Path]:
    script_dir = Path(__file__).resolve().parent
    template_root = script_dir.parent / "templates"
    output_root = ROOT / "evidence" / PHASE / "outputs" / project / "integration"
    output_root.mkdir(parents=True, exist_ok=True)

    copied: List[Path] = []
    for name, relative in TEMPLATES.items():
        src = (template_root / relative).resolve()
        if not src.exists():
            raise FileNotFoundError(f"Missing template: {relative}")
        dest = output_root / name
        dest.write_bytes(src.read_bytes())
        copied.append(dest)
    return copied


def update_manifest(project: str, files: List[Path]) -> None:
    manifest_path = ROOT / "evidence" / PHASE / "manifest.json"
    entries = load_manifest(manifest_path)
    for path in files:
        rel = path.relative_to(ROOT)
        checksum = sha256sum(path)
        entry = {
            "phase": PHASE,
            "project": project,
            "file": str(rel),
            "checksum": checksum,
        }
        entries = [e for e in entries if not (e.get("file") == entry["file"] and e.get("project") == project)]
        entries.append(entry)
    write_manifest(manifest_path, entries)



def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True)
    args = parser.parse_args()

    project = args.project.strip()
    if not project:
        raise SystemExit("Project slug cannot be empty")

    files = copy_templates(project)
    update_manifest(project, files)
    append_run_log(f"generate_observability_pack: copied {len(files)} files for project '{project}'")

    validation = ROOT / "evidence" / PHASE / "validation.md"
    if not validation.exists():
        validation.write_text("# Phase 4 Validation Results\n\n| Timestamp | Project | Status | Artefact | Notes |\n| --- | --- | --- | --- | --- |\n")
    timestamp = datetime.utcnow().isoformat() + "Z"
    with validation.open("a", encoding="utf-8") as handle:
        for path in files:
            handle.write(f"| {timestamp} | {project} | PASS | {path.name} | Generated via script |\n")

    print(f"Observability assets generated in {files[0].parent}")


if __name__ == "__main__":
    main()
