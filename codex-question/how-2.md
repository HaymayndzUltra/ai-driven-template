CD-MIE Lifecycle Overview
The Contract-Driven Meta-Instruction Engineering (CD-MIE) lifecycle extends the existing five-phase AI-driven workflow so that meta-instructions follow the same evidence-backed, phase-gated rigor already used for broader project orchestration. It enforces the master rule structure for .mdc files, ensuring every instruction carries compliant frontmatter and directive formatting. Each phase incorporates syntactic, semantic, behavioral, and conflict-resolution gates to keep instructions precise and production safe.

Phase Playbook
1. Planning – Define Instruction Outcomes
Objective: Clarify the cognitive behaviors the instruction must guarantee while mapping them to existing workflow phases for continuity.

Input Contract: Approved problem statement or change request, relevant master rules, and current workflow dependencies.

Output Contract: Draft objective brief summarizing expected AI behaviors, affected scopes, and dependency touchpoints.

Success Criteria: Objectives map cleanly to workflow responsibilities with no unresolved dependencies; stakeholders agree on scope.

Automation Bindings: system_instruction_formatter.py to structure objectives, proposed instruction_objective_mapper.py to catalogue triggers, and validation_gates.py to capture approval evidence.

Quality Gates: Semantic clarity review plus conflict scan against kernel directives using detect_instruction_conflicts.py.

Human Gate: Architecture lead validates objective alignment and signs off through validation_gates.py with captured rationale.

2. Requirement Gathering – Trigger/Scope Analysis
Objective: Enumerate triggers, tags, scopes, and contexts required to load and apply the instruction correctly.

Input Contract: Planning brief, repository of existing triggers/tags, and context taxonomy.

Output Contract: Requirements matrix covering triggers, scopes, contexts, conflict considerations, and success metrics.

Success Criteria: Every trigger maps to a scope and tag, and overlaps with existing rules are flagged.

Automation Bindings: analyze_brief.py (for structured metadata extraction), plan_from_brief.py, and proposed meta_context_catalog.py for context inventories.

Quality Gates: Syntactic validation of requirement fields, conflict detection, and semantic review for ambiguities.

Human Gate: Instruction architect confirms trigger coverage and records approval evidence.

3. Designing – Rule Architecture
Objective: Blueprint YAML frontmatter, cognitive checkpoints, and evidence gates so the rule is execution-ready.

Input Contract: Requirements matrix, master rule templates, governance guidelines.

Output Contract: Design specification including frontmatter schema, checkpoint flow, and evidence capture model.

Success Criteria: Frontmatter conforms to canonical format, checkpoints cover all success paths, and evidence gates align with workflow protocols.

Automation Bindings: system_instruction_formatter.py, generate_protocol_sequence.py for checkpoint alignment, and proposed rule_schema_linter.py for schema linting.

Quality Gates: Syntactic schema lint, semantic intent reconciliation, and conflict simulation.

Human Gate: Senior rule designer approves blueprint and checkpoint logic.

4. Building – Author Instruction
Objective: Produce the .mdc rule/command with validated frontmatter and directive body.

Input Contract: Approved design spec, templates, and style guides.

Output Contract: Draft .mdc or .md instruction plus change log.

Success Criteria: File passes linting, adheres to style guides, and links to evidence gates.

Automation Bindings: system_instruction_formatter.py, standardize_frontmatter.py, and proposed rule_editor_cli.py for authoring assistance.

Quality Gates: Frontmatter syntactic validation, semantic clarity review, and initial conflict scan.

Human Gate: Instruction author and peer reviewer co-sign the draft.

5. Testing – Behavioral Validation
Objective: Prove the instruction produces expected agent behavior across scenarios.

Input Contract: Draft instruction, scenario catalog, simulation harness.

Output Contract: Test report with scenario coverage, behavioral logs, and issue list.

Success Criteria: All planned scenarios pass, no regressions, and coverage meets threshold.

Automation Bindings: simulate_protocol_execution.py, validate_ai_directives.py, detect_instruction_conflicts.py, and proposed rule_behavior_bench.py for load testing.

Quality Gates: Full syntactic/semantic checks, behavioral assertions, and conflict detection rerun.

Human Gate: QA architect reviews evidence and issues final go/no-go.

6. Implementation – Repository Integration
Objective: Stage validated instruction into .cursor/rules/ or .cursor/commands/ with governance metadata.

Input Contract: Passed test report, deployment checklist, version metadata.

Output Contract: Merged instruction, update summary, and evidence bundle.

Success Criteria: Instruction stored in correct location, references added to registries, and audit entries created.

Automation Bindings: run_generate_rules.py, workflow_automation.py, validation_gates.py, and proposed rule_lifecycle_manager.py to handle versioning.

Quality Gates: Repository schema validation, dependency verification, and human approval capture.

Human Gate: Governance board reviews integration path via validation_gates.py checkpoint.

7. Deployment – Activation in Workflows
Objective: Activate instruction in live agent pipelines with monitoring hooks.

Input Contract: Implementation evidence, rollout plan, rollback playbook.

Output Contract: Deployment record, activation confirmation, and monitoring configuration.

Success Criteria: Instruction loads in the relevant workflow phase, automation bindings succeed, and fallback paths verified.

Automation Bindings: run_workflow.py, ai_executor.py, workflow_automation.py, and proposed rule_activation_monitor.py for real-time health.

Quality Gates: Final semantic sanity check, behavioral smoke test, and conflict monitor.

Human Gate: Deployment manager provides final sign-off before activation.

8. Maintenance – Continuous Governance
Objective: Monitor instruction performance, manage updates, and handle retirement decisions.

Input Contract: Live telemetry, evidence logs, feedback backlog.

Output Contract: Maintenance review report, change proposals, and version tags.

Success Criteria: Drift detected and addressed, evidence stays current, and deprecation plans documented.

Automation Bindings: evidence_manager.py, evidence_report.py, quality_gates.py, validation_gates.py, and proposed rule_retrospective_analyzer.py for trend analysis.

Quality Gates: Periodic behavioral regression, conflict scans, and compliance reviews.

Human Gate: Quarterly governance council reviews telemetry and approves update/retire decisions.


| Phase          | Checkpoint            | Script Binding                                                                                    | Success Criteria                                                                 |
| -------------- | --------------------- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Planning       | Objective alignment   | `system_instruction_formatter.py`, `validation_gates.py`                                          | Objectives linked to workflow phases with recorded approval.:codex-file-citation |
| Requirements   | Trigger mapping       | `analyze_brief.py`, `plan_from_brief.py`                                                          | Every trigger/context pair catalogued without collisions.:codex-file-citation    |
| Designing      | Schema lint           | `generate_protocol_sequence.py`, `system_instruction_formatter.py`, `rule_schema_linter.py` (new) | Frontmatter passes structural checks.:codex-file-citation:codex-file-citation    |
| Building       | Authoring compliance  | `standardize_frontmatter.py`, `rule_editor_cli.py` (new)                                          | Draft compiled with conformant directives.:codex-file-citation                   |
| Testing        | Behavioral validation | `simulate_protocol_execution.py`, `validate_ai_directives.py`, `rule_behavior_bench.py` (new)     | Scenarios pass; conflict detector clean.:codex-file-citation                     |
| Implementation | Version control       | `workflow_automation.py`, `run_generate_rules.py`, `rule_lifecycle_manager.py` (new)              | Instruction registered and versioned correctly.:codex-file-citation              |
| Deployment     | Activation monitoring | `run_workflow.py`, `ai_executor.py`, `rule_activation_monitor.py` (new)                           | Instruction loads in target workflow phase.:codex-file-citation                  |
| Maintenance    | Drift watch           | `evidence_manager.py`, `quality_gates.py`, `rule_retrospective_analyzer.py` (new)                 | Telemetry shows no unmitigated drift; audits pass.:codex-file-citation           |



Phase Templates
Requirement Gathering Template
Instruction Objective ID

Triggers: [keyword] → expected context

Scopes: global/domain/project

Tags: [governance,workflow-phase]

Context Dependencies: linked phases, files, or services

Conflict Inventory: overlapping rules, resolution plan

Success Metrics: behavioral KPIs, evidence sources

Design Template
Frontmatter Draft (TAGS/TRIGGERS/SCOPE/DESCRIPTION, alwaysApply)

Cognitive Checkpoints: sequence, entry criteria, exit proof

Evidence Gates: artifact type, capture tool, responsible owner

Fallback Paths: error handling, recovery triggers

Integration Hooks: workflow phases, command bindings, automation scripts

Testing Template
Scenario Matrix: scenario ID, trigger inputs, expected behavior

Validation Steps: syntactic/semantic/behavioral/conflict checks with tooling

Observation Log: actual behavior, variances, artifacts

Approval Summary: QA lead decision, outstanding issues, mitigations

Acceptance Criteria Checklist
Syntactic correctness: YAML frontmatter validated and compliant.

Semantic clarity: directives unambiguous with scope, trigger, and dependency resolution documented.

Behavioral correctness: scenario suite passes and aligns with workflow expectations.

Conflict-free integration: collision scans pass and priority logic respected.

Maintenance Protocol
Monitoring: Automate periodic evidence capture and behavioral audits using evidence_manager.py, quality_gates.py, and custom telemetry to detect drift or gaps.

Update Procedure: Version through rule_lifecycle_manager.py, run targeted regression tests, and document approvals via validation_gates.py; maintain backward-compatible schemas per extensibility guidance.

Refactoring Guidelines: Refactor when objectives change or evidence shows recurring mitigations; deprecate when workflows evolve beyond scope; ensure rollback bundles exist for every release.

Human-in-the-Loop Governance
Mandatory architect approvals at planning, requirement, design, testing, implementation, deployment, and maintenance retrospectives, captured through validation_gates.py workflow states.

Evidence packets must include objective briefs, requirement matrices, design specs, test reports, deployment records, and maintenance telemetry.

Approve/reject criteria: fulfillment of phase success metrics, closure of open issues, and confirmation that acceptance checklist remains green.

Alignment Decisions
Integration depth: (b) Deep integration with and extension of the current .cursor/ai-driven-workflow/ phases to ensure consistent reasoning gates.

Automation script coverage: (b) Document bindings for existing scripts and propose targeted new utilities (e.g., lifecycle manager, behavior bench) to close gaps surfaced by CD-MIE.

Human validation gates: (c) Comprehensive gates spanning planning through maintenance, matching the multi-phase validation system already enforced by validation_gates.py