#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKFLOW_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
PHASE_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
EVIDENCE_DIR="${WORKFLOW_ROOT}/evidence/phase3"
TEMPLATE_DIR="${PHASE_DIR}/templates"
QUALITY_GATE_SCRIPT="${WORKFLOW_ROOT}/../quality_gate_simple.sh"
PHASE="phase3"

PROJECT=""
BOOTSTRAP=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --project)
      PROJECT="$2"
      shift 2
      ;;
    --bootstrap)
      BOOTSTRAP=1
      shift
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 1
      ;;
  esac
done

if [[ -z "${PROJECT}" ]]; then
  echo "--project <slug> is required" >&2
  exit 1
fi

mkdir -p "${EVIDENCE_DIR}"
RUN_LOG="${EVIDENCE_DIR}/run.log"
VALIDATION_FILE="${EVIDENCE_DIR}/validation.md"
MANIFEST_FILE="${EVIDENCE_DIR}/manifest.json"

log() {
  local message="$1"
  local timestamp
  timestamp="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  echo "[${timestamp}] ${message}" | tee -a "${RUN_LOG}"
}

update_manifest() {
  local target_dir="$1"
  python - "$MANIFEST_FILE" "$PROJECT" "$target_dir" "$WORKFLOW_ROOT" <<'PY'
import json
import sys
from datetime import datetime
from pathlib import Path
import hashlib

manifest_path = Path(sys.argv[1])
project = sys.argv[2]
target_dir = Path(sys.argv[3])
root = Path(sys.argv[4])
phase = "phase3"
files = []
if target_dir.exists():
    for path in target_dir.rglob('*'):
        if path.is_file():
            files.append(path)
entries = []
if manifest_path.exists():
    entries = json.loads(manifest_path.read_text())

def checksum(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda: handle.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

entries = [e for e in entries if not (e.get('project') == project and e.get('phase') == phase and e.get('file', '').startswith(str((target_dir).relative_to(root))))]
for file in files:
    rel = file.relative_to(root)
    entries.append({
        'phase': phase,
        'project': project,
        'file': str(rel),
        'checksum': checksum(file),
        'recorded_at': datetime.utcnow().isoformat() + 'Z'
    })
manifest_path.write_text(json.dumps(entries, indent=2, sort_keys=True))
PY
}

if [[ ${BOOTSTRAP} -eq 1 ]]; then
  DEST="${EVIDENCE_DIR}/outputs/${PROJECT}/quality-rails"
  mkdir -p "${DEST}"
  cp "${TEMPLATE_DIR}/Security_Checklist.md" "${DEST}/Security_Checklist.md"
  cp "${TEMPLATE_DIR}/A11y_Test_Plan.md" "${DEST}/A11y_Test_Plan.md"
  cp "${TEMPLATE_DIR}/Feature_Flags.md" "${DEST}/Feature_Flags.md"
  cp "${TEMPLATE_DIR}/Test_Plan.md" "${DEST}/Test_Plan.md"
  cp "${TEMPLATE_DIR}/Code_Review_Checklist.md" "${DEST}/Code_Review_Checklist.md"
  mkdir -p "${DEST}/perf"
  cp "${TEMPLATE_DIR}/perf/budgets.json" "${DEST}/perf/budgets.json"
  cp "${TEMPLATE_DIR}/Analytics_Spec.xlsx" "${DEST}/Analytics_Spec.xlsx"
  log "Bootstrapped quality rail templates for project '${PROJECT}'"
  update_manifest "${DEST}"
fi

log "Running quality gate automation for project '${PROJECT}'"
if [[ -x "${QUALITY_GATE_SCRIPT}" ]]; then
  if "${QUALITY_GATE_SCRIPT}"; then
    STATUS="PASS"
  else
    STATUS="FAIL"
  fi
else
  log "quality_gate_simple.sh not executable or missing"
  STATUS="FAIL"
fi

mkdir -p "${EVIDENCE_DIR}"
if [[ ! -f "${VALIDATION_FILE}" ]]; then
  cat <<'EOF_VALID' > "${VALIDATION_FILE}"
# Phase 3 Validation Results

| Timestamp | Project | Status | Notes |
| --- | --- | --- | --- |
EOF_VALID
fi

echo "| $(date -u +"%Y-%m-%dT%H:%M:%SZ") | ${PROJECT} | ${STATUS} | run_quality_gates.sh |" >> "${VALIDATION_FILE}"

log "Quality gate status: ${STATUS}"

if [[ "${STATUS}" == "FAIL" ]]; then
  exit 1
fi
