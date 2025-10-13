#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKFLOW_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
EVIDENCE_DIR="${WORKFLOW_ROOT}/evidence/phase5"

PROJECT=""
RESULT="pass"
NOTES=""

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
    --notes)
      NOTES="$2"
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
OUTPUT_DIR="${EVIDENCE_DIR}/outputs/${PROJECT}/launch"
mkdir -p "${OUTPUT_DIR}"

REPORT="${OUTPUT_DIR}/rollback_rehearsal.txt"
TIMESTAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
cat <<EOF_REPORT > "${REPORT}"
Rollback rehearsal report
Project: ${PROJECT}
Timestamp: ${TIMESTAMP}
Result: ${RESULT}
Notes: ${NOTES}
Steps executed: refer to Rollback_Plan.md
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
phase = "phase5"
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

echo "[${TIMESTAMP}] rehearse_rollback: project=${PROJECT} status=${STATUS} report=${REPORT}" >> "${RUN_LOG}"

if [[ ! -f "${VALIDATION_FILE}" ]]; then
  cat <<'EOF_VALID' > "${VALIDATION_FILE}"
# Phase 5 Validation Results

| Timestamp | Project | Status | Artefact | Notes |
| --- | --- | --- | --- | --- |
EOF_VALID
fi

echo "| ${TIMESTAMP} | ${PROJECT} | ${STATUS} | $(basename "${REPORT}") | rehearse_rollback.sh ${NOTES} |" >> "${VALIDATION_FILE}"

echo "Rollback rehearsal ${STATUS} (report: ${REPORT})"

if [[ "${STATUS}" == "FAIL" ]]; then
  exit 1
fi
