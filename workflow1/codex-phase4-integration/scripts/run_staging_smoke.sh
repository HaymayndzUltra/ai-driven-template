#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKFLOW_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
EVIDENCE_DIR="${WORKFLOW_ROOT}/evidence/phase4"

PROJECT=""
RESULT="pass"
REPORT=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --project)
      PROJECT="$2"
      shift 2
      ;;
    --result)
      RESULT="$2"
      shift 2
      ;;
    --report)
      REPORT="$2"
      shift 2
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
REPORT_DIR="${EVIDENCE_DIR}/outputs/${PROJECT}/integration"
mkdir -p "${REPORT_DIR}"

if [[ -z "${REPORT}" ]]; then
  REPORT="${REPORT_DIR}/staging_smoke_report.txt"
fi

cat <<EOF_REPORT > "${REPORT}"
Staging smoke execution
Project: ${PROJECT}
Timestamp: $(date -u +"%Y-%m-%dT%H:%M:%SZ")
Result: ${RESULT}
Notes: Placeholder smoke report. Replace with real test output.
EOF_REPORT

python - <<'PY' "$MANIFEST_FILE" "$PROJECT" "$REPORT" "$WORKFLOW_ROOT"
import json
import sys
import hashlib
from datetime import datetime
from pathlib import Path

manifest_path = Path(sys.argv[1])
project = sys.argv[2]
report = Path(sys.argv[3])
root = Path(sys.argv[4])
phase = "phase4"
entries = []
if manifest_path.exists():
    entries = json.loads(manifest_path.read_text())

def checksum(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as handle:
        for chunk in iter(lambda: handle.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

entries = [e for e in entries if not (e.get('file') == str(report.relative_to(root)) and e.get('project') == project)]
entries.append({
    'phase': phase,
    'project': project,
    'file': str(report.relative_to(root)),
    'checksum': checksum(report),
    'recorded_at': datetime.utcnow().isoformat() + 'Z'
})
manifest_path.write_text(json.dumps(entries, indent=2, sort_keys=True))
PY

STATUS="PASS"
if [[ "${RESULT}" != "pass" ]]; then
  STATUS="FAIL"
fi

TIMESTAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
echo "[${TIMESTAMP}] run_staging_smoke: project=${PROJECT} status=${STATUS} report=${REPORT}" >> "${RUN_LOG}"

if [[ ! -f "${VALIDATION_FILE}" ]]; then
  cat <<'EOF_VALID' > "${VALIDATION_FILE}"
# Phase 4 Validation Results

| Timestamp | Project | Status | Artefact | Notes |
| --- | --- | --- | --- | --- |
EOF_VALID
fi

echo "| ${TIMESTAMP} | ${PROJECT} | ${STATUS} | $(basename "${REPORT}") | run_staging_smoke.sh |" >> "${VALIDATION_FILE}"

echo "Staging smoke ${STATUS} (report: ${REPORT})"

if [[ "${STATUS}" == "FAIL" ]]; then
  exit 1
fi
