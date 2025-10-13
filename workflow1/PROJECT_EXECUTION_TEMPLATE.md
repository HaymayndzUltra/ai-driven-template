# Project Execution Template (Phases 0–6)

Use this template to plan and execute engagements with the extended workflow1 protocols.

## Phase 0 — Bootstrap
- [ ] Review engagement brief and success metrics.
- [ ] Populate context kit, stakeholder map, and communication plan.
- Evidence: `evidence/phase0` (legacy format).

## Phase 1 — PRD Creation
- [ ] Generate PRD aligned with business goals.
- [ ] Validate requirements and constraints with stakeholders.
- Evidence: `evidence/phase1` (legacy format).

## Phase 2 — Design & Planning
- [ ] Run planning automation (`make plan-from-brief`).
- [ ] Execute `codex-phase2-design/scripts/generate_architecture_pack.py`.
- [ ] Execute `codex-phase2-design/scripts/generate_contract_assets.py`.
- [ ] Confirm ADR approvals, OpenAPI lint, CI skeleton status.
- Evidence: `evidence/phase2` (`run.log`, `validation.md`, `manifest.json`).

## Phase 3 — Quality Rails
- [ ] Bootstrap templates via `run_quality_gates.sh --bootstrap`.
- [ ] Populate security, performance, accessibility, analytics, testing, and review artefacts.
- [ ] Configure feature flags with `configure_feature_flags.py`.
- [ ] Run `run_quality_gates.sh` and ensure CI gates are green.
- Evidence: `evidence/phase3`.

## Phase 4 — Integration
- [ ] Generate observability pack via `generate_observability_pack.py`.
- [ ] Update CHANGELOG and SLO/SLI definitions.
- [ ] Run staging smoke automation `run_staging_smoke.sh` after deployments.
- [ ] Confirm observability telemetry working.
- Evidence: `evidence/phase4`.

## Phase 5 — Launch
- [ ] Complete deployment, rollback, DR, and observability templates.
- [ ] Rehearse rollback (`rehearse_rollback.sh`) and verify DR restore (`verify_dr_restore.sh`).
- [ ] Finalise Go-Live checklist, release notes, SEO checklist.
- [ ] Collect sign-offs from Product, Engineering, SRE, Legal/Privacy.
- Evidence: `evidence/phase5`.

## Phase 6 — Operations
- [ ] Record SLO adherence with `monitor_slo.py`.
- [ ] Schedule retrospectives via `schedule_retros.py`.
- [ ] Maintain dependency and security update logs; complete retros/postmortems.
- [ ] Verify vulnerability SLAs and action closure cadence.
- Evidence: `evidence/phase6`.

## Governance & Reporting
- Update `INDEX.md` when new artefacts or automation scripts are introduced.
- Ensure each phase's validation log contains PASS/FAIL entries before progressing.
- Maintain manifest checksums for traceability and audit.
