#!/usr/bin/env python3
"""Schedule retrospectives and update evidence for Phase 6."""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[2]
PHASE = "phase6"


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
    log_path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.utcnow().isoformat() + "Z"
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(f"[{timestamp}] {message}\n")


def update_validation(project: str, count: int) -> None:
    validation = ROOT / "evidence" / PHASE / "validation.md"
    if not validation.exists():
        validation.write_text("# Phase 6 Validation Results\n\n| Timestamp | Project | Status | Notes |\n| --- | --- | --- | --- |\n")
    timestamp = datetime.utcnow().isoformat() + "Z"
    with validation.open("a", encoding="utf-8") as handle:
        handle.write(f"| {timestamp} | {project} | PASS | Scheduled {count} retros |\n")


def update_manifest_entries(project: str, files: List[Path]) -> None:
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
    parser.add_argument("--start", help="Start date ISO format", default=datetime.utcnow().date().isoformat())
    parser.add_argument("--cadence", type=int, default=14, help="Cadence in days")
    parser.add_argument("--count", type=int, default=4, help="Number of retros to schedule")
    args = parser.parse_args()

    project = args.project.strip()
    if not project:
        raise SystemExit("Project slug cannot be empty")

    start_date = datetime.fromisoformat(args.start)
    cadence = timedelta(days=args.cadence)
    entries = []
    for index in range(args.count):
        when = start_date + cadence * index
        entries.append({
            "project": project,
            "retro_number": index + 1,
            "scheduled_for": when.isoformat(),
            "facilitator": "TBD",
            "status": "Scheduled",
        })

    output_dir = ROOT / "evidence" / PHASE / "outputs" / project / "operations"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "retro_schedule.json"
    output_file.write_text(json.dumps(entries, indent=2, sort_keys=True))

    update_manifest_entries(project, [output_file])
    append_run_log(f"schedule_retros: scheduled {len(entries)} retros for project '{project}'")
    update_validation(project, len(entries))

    print(f"Retro schedule generated -> {output_file}")


if __name__ == "__main__":
    main()
