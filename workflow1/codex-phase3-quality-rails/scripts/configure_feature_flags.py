#!/usr/bin/env python3
"""Manage feature flag manifests for AGENTS Phase 3."""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict

ROOT = Path(__file__).resolve().parents[2]
PHASE = "phase3"


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


def parse_flag(raw: str) -> Dict[str, str]:
    parts = [p.strip() for p in raw.split(":")]
    if len(parts) < 3:
        raise ValueError("Flag definitions must use key:type:owner format")
    key, flag_type, owner, *rest = parts
    description = rest[0] if rest else ""
    return {
        "key": key,
        "type": flag_type,
        "owner": owner,
        "description": description,
    }


def update_flag_manifest(project: str, flags: List[Dict[str, str]]) -> Path:
    dest = ROOT / "evidence" / PHASE / "outputs" / project / "quality-rails" / "feature_flags.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    data = {"project": project, "updated_at": datetime.utcnow().isoformat() + "Z", "flags": []}
    if dest.exists():
        try:
            data = json.loads(dest.read_text())
        except json.JSONDecodeError:
            pass
    existing = {flag["key"]: flag for flag in data.get("flags", [])}
    for flag in flags:
        existing[flag["key"]] = {**existing.get(flag["key"], {}), **flag}
        existing[flag["key"]]["updated_at"] = datetime.utcnow().isoformat() + "Z"
    data["flags"] = sorted(existing.values(), key=lambda x: x["key"])
    dest.write_text(json.dumps(data, indent=2, sort_keys=True))
    return dest


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
    parser.add_argument("--flag", action="append", default=[], help="Flag definition key:type:owner[:description]")
    args = parser.parse_args()

    project = args.project.strip()
    if not project:
        raise SystemExit("Project slug cannot be empty")

    flags = [parse_flag(raw) for raw in args.flag]
    dest = update_flag_manifest(project, flags)
    update_manifest_entries(project, [dest])
    append_run_log(f"configure_feature_flags: updated manifest with {len(flags)} new flags for project '{project}'")
    print(f"Feature flag manifest updated: {dest}")


if __name__ == "__main__":
    main()
