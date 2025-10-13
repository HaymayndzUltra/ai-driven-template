#!/usr/bin/env python3
"""Generate contract-first assets for AGENTS Phase 2."""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[2]
PHASE = "phase2"


def sha256sum(path: Path) -> str:
    import hashlib

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


def ensure_template_copy(template_root: Path, relative: Path, destination: Path) -> Path:
    src = (template_root / relative).resolve()
    if not src.exists():
        raise FileNotFoundError(f"Missing template: {relative}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(src.read_bytes())
    return destination


def create_openapi_stub(dest: Path, service: str) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        return dest
    content = f"""openapi: 3.1.0
info:
  title: {service.title()} API
  version: 0.1.0
  description: Contract-first stub generated during Phase 2.
servers:
  - url: http://localhost:8000
    description: Local mock server
paths:
  /health:
    get:
      summary: Health probe
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    example: ok
"""
    dest.write_text(content)
    return dest


def update_manifest(records: List[Path], manifest_path: Path, project: str) -> None:
    entries = load_manifest(manifest_path)
    for path in records:
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
    parser.add_argument("--service", required=True, help="Service slug for OpenAPI stub")
    args = parser.parse_args()

    project = args.project.strip()
    service = args.service.strip()
    if not project or not service:
        raise SystemExit("Project and service slugs cannot be empty")

    script_dir = Path(__file__).resolve().parent
    template_root = script_dir.parent / "templates"
    evidence_root = ROOT / "evidence" / PHASE / "outputs" / project / "contracts"
    evidence_root.mkdir(parents=True, exist_ok=True)

    copied: List[Path] = []
    copied.append(ensure_template_copy(template_root, Path("Product_Backlog.csv"), evidence_root / "Product_Backlog.csv"))
    copied.append(ensure_template_copy(template_root, Path("Sprint0_Plan.md"), evidence_root / "Sprint0_Plan.md"))
    copied.append(ensure_template_copy(template_root, Path("OpenAPI/README.md"), evidence_root / "OpenAPI_README.md"))

    openapi_stub = evidence_root / "openapi" / f"{service}.yaml"
    copied.append(create_openapi_stub(openapi_stub, service))

    manifest_path = ROOT / "evidence" / PHASE / "manifest.json"
    run_log = ROOT / "evidence" / PHASE / "run.log"

    update_manifest(copied, manifest_path, project)
    append_run_log(run_log, f"generate_contract_assets: generated {len(copied)} artefacts for project '{project}' service '{service}'")

    print(f"Contract assets generated in {evidence_root}")


if __name__ == "__main__":
    main()
