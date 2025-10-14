# 02. Task Generation & Delivery Plan

## Purpose
Use the protocol at `unified_workflow/phases/2-task-generation.md` to complete this phase. Follow the unified template and capture evidence for the orchestrator.

## Context Snapshot
- Project Type: enterprise-saas
- Complexity: enterprise
- Lifecycle: production
- Stack: backend: Python, FastAPI, Celery, Redis, database: PostgreSQL, MongoDB, frontend: React, TypeScript, Next.js, TailwindCSS, infrastructure: AWS, Terraform, Docker, Kubernetes
- Compliance Signals: GDPR, HIPAA, ISO27001, SOC2

## Automation Hooks
- ✅ `scripts/enrich_tasks.py` (Task Enrichment)
- ✅ `scripts/lifecycle_tasks.py` (Lifecycle Mapping)

## Execution Guidance
1. Review the linked protocol document and confirm prerequisites.
2. Execute the automation hooks above (or their equivalents) to accelerate the phase.
3. Record artifacts with `scripts/evidence_manager.py` and update task state as needed.
4. Run the phase quality gate before handing off to the next protocol.

## Evidence & Quality Gates
- Ensure quality gate scripts report success before advancing.
- Attach logs, reports, and approvals to the evidence manifest.
- Document deviations or skipped automation in the orchestrator report.