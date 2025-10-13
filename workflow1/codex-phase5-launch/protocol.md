# Codex Phase 5 — Launch Readiness Protocol

Extends `workflow1` Protocol 4–5 to satisfy AGENTS Phase 5 hardening requirements.

## Objectives
- Finalise deployment, rollback, DR, and observability plans for production.
- Ensure documentation, SEO (if public), and compliance sign-offs complete.
- Record rehearsal evidence and go-live readiness.

## Inputs
- Phase 4 integration assets (observability, SLO/SLI, CHANGELOG, smoke logs).
- Feature backlog and release notes draft.
- On-call rotation and incident management process.

## Required Artefacts
- `templates/Deployment_Runbook.md`
- `templates/Rollback_Plan.md`
- `templates/Prod_Observability.md`
- `templates/Backup_Policy.md`
- `templates/DR_Plan.md`
- `templates/GoLive_Checklist.md`
- `templates/Release_Notes.md`
- `templates/SEO_Checklist.md`

## Automation Scripts
- `scripts/rehearse_rollback.sh`
  - Simulates rollback procedure, captures evidence, updates manifest.
- `scripts/verify_dr_restore.sh`
  - Logs backup/restore validation output for audit trails.

## Procedure
1. Copy templates into project documentation using automation scripts.
2. Populate deployment and rollback details, including on-call contacts.
3. Run `scripts/rehearse_rollback.sh --project <slug>` to capture rehearsal evidence.
4. Execute DR test per `verify_dr_restore.sh --project <slug>`.
5. Finalise `GoLive_Checklist.md` and ensure all items have status + owners.
6. Update `Release_Notes.md` with version details, features, and known issues.
7. Complete `SEO_Checklist.md` if product is public-facing.
8. Record approvals in evidence pack and confirm readiness with stakeholders.

## Exit Criteria
- Deployment runbook and rollback plan approved and rehearsed.
- Backup and DR strategy validated with timestamped evidence.
- Production observability plan signed off (dashboards, alerts, runbooks).
- Go-Live checklist 100% complete with approvals.
- Release notes published and distributed to stakeholders.
- SEO checklist complete or explicitly not applicable.

## Dependencies
- Access to staging/prod-like environment for rehearsal.
- On-call tooling (PagerDuty, Opsgenie) configured.
- Compliance/legal approvals captured.

## Evidence Logging
Scripts append to `../evidence/phase5/run.log`, update `manifest.json`, and add PASS/FAIL entries to `validation.md`. Manual sign-offs must be logged as well.

## Related Protocols
- Phase 4 integration for upstream readiness.
- Phase 6 operations for post-launch activities.
