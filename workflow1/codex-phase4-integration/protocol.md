# Codex Phase 4 — Integration Protocol

Extends `workflow1` Protocol 3–4 to deliver AGENTS Phase 4 outputs: staged integration, observability, and release readiness artefacts.

## Objectives
- Deliver features behind flags with reliable staging deployments.
- Document observability strategy and draft SLO/SLIs.
- Maintain changelog and smoke testing routines.

## Inputs
- Phase 2–3 artefacts (architecture, contracts, quality rails).
- Feature backlog and flag manifest.
- CI/CD pipelines.

## Required Artefacts
- `templates/Observability_Spec.md`
- `templates/SLO_SLI.md`
- `templates/CHANGELOG.md`
- `templates/Staging_Smoke_Playbook.md`

## Automation Scripts
- `scripts/run_staging_smoke.sh`
  - Executes smoke tests against staging and logs evidence.
- `scripts/generate_observability_pack.py`
  - Copies observability templates and injects metadata.

## Procedure
1. Ensure feature work is gated by flags per Phase 3 outputs.
2. Run `python scripts/generate_observability_pack.py --project <slug>` to prepare docs.
3. Execute staging deployments using repo CI/CD.
4. Run `scripts/run_staging_smoke.sh --project <slug>` after each deployment.
5. Update `CHANGELOG.md` entries for each feature toggle or release candidate.
6. Draft initial SLO/SLI targets referencing performance budgets.
7. Confirm telemetry pipelines (logs, metrics, traces) are operational.

## Exit Criteria
- Observability spec completed with log/metric/trace coverage.
- SLO/SLI definitions approved by engineering + product leads.
- Staging smoke playbook validated (green run recorded in evidence).
- CHANGELOG initialised and linked to backlog items.
- Staging stability metrics meet budgets (p75/p95 as defined).

## Dependencies
- Access to staging environment and credentials.
- Smoke testing framework (e.g., Playwright/Cypress/Postman).
- Observability stack (Grafana/Prometheus, Datadog, etc.).

## Evidence Logging
Scripts append to `../evidence/phase4/run.log`, populate `manifest.json`, and update `validation.md`. Manual approvals must be recorded as well.

## Related Protocols
- Phase 3 quality rails for gating.
- Phase 5 for launch readiness.
