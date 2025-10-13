# Codex Phase 6 — Operations Protocol

Extends `workflow1` Protocol 5 to meet AGENTS Phase 6 operational requirements for post-launch excellence.

## Objectives
- Maintain SLO compliance and rapid incident response.
- Track dependency and security updates.
- Conduct retrospectives and postmortems with action tracking.

## Inputs
- Phase 5 launch artefacts (runbooks, DR plans, observability dashboards).
- On-call rotation schedule.
- Incident management tooling.

## Required Artefacts
- `templates/Postmortem_Template.md`
- `templates/Dependency_Update_Log.md`
- `templates/Security_Update_Log.md`
- `templates/Retro_Template.md`

## Automation Scripts
- `scripts/monitor_slo.py`
  - Reads observability outputs or mock metrics to log SLO status.
- `scripts/schedule_retros.py`
  - Generates retrospective calendar entries and updates evidence logs.

## Procedure
1. Run `monitor_slo.py --project <slug>` weekly to capture SLO adherence.
2. Update dependency and security logs after each maintenance window.
3. Use `schedule_retros.py --project <slug>` to create retro/postmortem placeholders.
4. Conduct retrospectives, populate action items, and track closure.
5. Record postmortems for incidents including root cause, remediation, and follow-up tasks.
6. Ensure vulnerability SLA compliance (no high/critical >14 days outstanding).

## Exit Criteria (Steady State)
- SLO metrics documented for 2–4 consecutive weeks with PASS results.
- Dependency and security logs updated within defined cadence.
- Retro actions closed on time; follow-up tasks linked to backlog.
- Postmortems completed for all incidents above severity threshold.

## Dependencies
- Access to observability metrics or exports.
- Issue tracker integration for follow-up tasks.
- Calendar system for scheduling retros.

## Evidence Logging
Scripts append to `../evidence/phase6/run.log`, update `manifest.json`, and maintain `validation.md` records. Manual updates must follow the same evidence structure.

## Related Protocols
- Phase 5 launch for runbooks.
- Earlier phases for backlog/task traceability.
