# Codex Phase 3 — Quality Rails Protocol

This protocol extends `workflow1` Protocols 2–4 to fulfil AGENTS Phase 3 guardrail requirements covering security, performance, accessibility, analytics, testing, and code review controls.

## Objectives
- Install security/performance/accessibility gates before large-scale feature development.
- Define analytics instrumentation and feature flag governance.
- Ensure CI/CD pipelines enforce quality bars automatically.

## Inputs
- Phase 2 architecture + contract artefacts.
- CI skeleton commands from `docs/LOCAL_DEV_WORKFLOW.md`.
- Security/compliance policies from repository standards.

## Required Artefacts
- `templates/Security_Checklist.md`
- `templates/perf/budgets.json`
- `templates/A11y_Test_Plan.md`
- `templates/Analytics_Spec.xlsx`
- `templates/Feature_Flags.md`
- `templates/Test_Plan.md`
- `templates/Code_Review_Checklist.md`

## Automation Scripts
- `scripts/run_quality_gates.sh`
  - Orchestrates lint/tests plus security/perf/a11y checks using repo automation.
- `scripts/configure_feature_flags.py`
  - Seeds flag configuration manifest and audit trail.

## Procedure
1. Copy templates into project docs (use `scripts/run_quality_gates.sh --bootstrap`).
2. Map OWASP ASVS controls in `Security_Checklist.md` and create follow-up tickets.
3. Define performance budgets in `perf/budgets.json` (Lighthouse or Web Vitals).
4. Capture accessibility scope and tooling in `A11y_Test_Plan.md`.
5. Build analytics taxonomy (events, properties) in `Analytics_Spec.xlsx`.
6. Document feature flag lifecycle in `Feature_Flags.md` and generate config using script.
7. Complete `Test_Plan.md` including coverage thresholds, smoke/integration cadence.
8. Update `Code_Review_Checklist.md` aligning with Repo Policy.
9. Run `scripts/run_quality_gates.sh` to verify automation and log evidence.

## Exit Criteria
- Security checklist complete with ASVS mapping and threat model summary.
- Performance and accessibility budgets committed and enforced in CI.
- Analytics spec approved by Data/PM stakeholders.
- Feature flag manifest created and tracked in repo.
- Test plan defined with metrics and gating thresholds.
- Code review checklist adopted in repository settings.
- CI pipeline demonstrates passing quality gates.

## Dependencies
- Node/JS runtime for Lighthouse budgets.
- Python 3 for automation scripts.
- Access to analytics tooling for schema validation.

## Evidence Logging
`run_quality_gates.sh` writes status to `../evidence/phase3/run.log` and `validation.md`. Manual approvals should be appended to the same evidence pack.

## Related Protocols
- Phase 2 protocol for architecture/contract context.
- Phase 4+ protocols for integration, launch, and operations.
