#!/usr/bin/env python3
"""Generate the architecture asset bundle for AGENTS Phase 2.

The script copies core architecture templates into an evidence output folder and
records actions in `evidence/phase2/run.log` + `manifest.json`. It is designed to
be orchestrated by the commands described in `docs/LOCAL_DEV_WORKFLOW.md`.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[2]
PHASE = "phase2"
TEMPLATES = {
    "Architecture.md": Path("Architecture.md"),
    "C4/context.mmd": Path("C4") / "context.mmd",
    "C4/container.mmd": Path("C4") / "container.mmd",
    "ADR-template.md": Path("ADR-template.md"),
    "Env_Strategy.md": Path("Env_Strategy.md"),
    "Repo_Policy.md": Path("Repo_Policy.md"),
    "Coding_Standards.md": Path("Coding_Standards.md"),
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


def append_run_log(log_path: Path, message: str) -> None:
    timestamp = datetime.utcnow().isoformat() + "Z"
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(f"[{timestamp}] {message}\n")


def copy_templates(project: str) -> List[Path]:
    script_dir = Path(__file__).resolve().parent
    template_root = script_dir.parent / "templates"
    output_root = script_dir.parent / ".." / "evidence" / PHASE / "outputs" / project / "architecture"
    output_root = output_root.resolve()
    output_root.mkdir(parents=True, exist_ok=True)

    copied: List[Path] = []
    for display, rel in TEMPLATES.items():
        src = (template_root / rel).resolve()
        if not src.exists():
            raise FileNotFoundError(f"Template missing: {display} -> {src}")
        dest = output_root / display
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(src.read_bytes())
        copied.append(dest)
    return copied


def update_manifest(copied: List[Path], manifest_path: Path, project: str) -> None:
    entries = load_manifest(manifest_path)
    for path in copied:
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
    parser.add_argument("--project", required=True, help="Project slug used in evidence output")
    args = parser.parse_args()

    project = args.project.strip()
    if not project:
        raise SystemExit("Project slug cannot be empty")

    copied = copy_templates(project)

    evidence_dir = Path(__file__).resolve().parents[2] / "evidence" / PHASE
    manifest_path = evidence_dir / "manifest.json"
    run_log = evidence_dir / "run.log"

    update_manifest(copied, manifest_path, project)
    append_run_log(run_log, f"generate_architecture_pack: copied {len(copied)} files for project '{project}'")

    print(f"Architecture pack ready: {len(copied)} files -> {copied[0].parent}")


if __name__ == "__main__":
    main()
