#!/usr/bin/env python3
"""Record SLO status for Phase 6 operations."""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
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


def update_validation(project: str, status: str, notes: str) -> None:
    validation = ROOT / "evidence" / PHASE / "validation.md"
    if not validation.exists():
        validation.write_text("# Phase 6 Validation Results\n\n| Timestamp | Project | Status | Notes |\n| --- | --- | --- | --- |\n")
    timestamp = datetime.utcnow().isoformat() + "Z"
    with validation.open("a", encoding="utf-8") as handle:
        handle.write(f"| {timestamp} | {project} | {status} | {notes} |\n")


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
    parser.add_argument("--availability", type=float, default=99.9)
    parser.add_argument("--latency", type=float, default=280.0, help="p95 latency in ms")
    parser.add_argument("--error-rate", type=float, default=0.8)
    args = parser.parse_args()

    project = args.project.strip()
    if not project:
        raise SystemExit("Project slug cannot be empty")

    payload = {
        "project": project,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "metrics": {
            "availability_percent": args.availability,
            "p95_latency_ms": args.latency,
            "error_rate_percent": args.error_rate,
        },
        "status": "PASS" if (args.availability >= 99.5 and args.latency <= 300 and args.error_rate <= 1.0) else "FAIL",
    }

    output_dir = ROOT / "evidence" / PHASE / "outputs" / project / "operations"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "slo_status.json"
    existing: List[Dict[str, object]] = []
    if output_file.exists():
        try:
            existing = json.loads(output_file.read_text())
        except json.JSONDecodeError:
            existing = []
    existing.append(payload)
    output_file.write_text(json.dumps(existing, indent=2, sort_keys=True))

    update_manifest_entries(project, [output_file])
    append_run_log(f"monitor_slo: recorded status {payload['status']} for project '{project}'")
    update_validation(project, payload["status"], f"availability={args.availability}, latency={args.latency}, error_rate={args.error_rate}")

    print(f"SLO status recorded: {payload['status']} -> {output_file}")

    if payload["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
