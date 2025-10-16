Option alignment for GPT-5-Codex
Integration depth: (b) – Deeply integrate with and extend the existing .cursor/ai-driven-workflow/ phases so CD-MIE inherits the evidence-first, gate-driven cadence already defined for AI-led delivery.

Automation coverage: (b) – Document bindings for the current automation fleet and propose a targeted set of lifecycle-specific utilities (e.g., rule_lifecycle_manager.py, conflict_detector.py) so the framework is actionable without waiting for a full rewrite.

Human validation gates: (c) – Comprehensive gates that mirror the repository’s existing validation checkpoints, ensuring architects review planning, design, testing, deployment, and maintenance decisions before promotion.

CD-MIE lifecycle (8 phases)
1. Planning
Objective: Translate business intent into measurable reasoning objectives while mapping to existing workflow roles and triggers.

Input contract: Approved project/brief summary, current master rules inventory, legacy instruction performance metrics, stakeholder intent notes.

Output contract: Meta-instruction charter (scope, objectives, guardrails), stakeholder RACI, initial risk register.

Success criteria: Objectives align with workflow scope, risk register logged, stakeholders sign off on charter.

Quality gates:

Syntactic: Charter stored in versioned YAML/Markdown checked by system_instruction_formatter.py for schema compliance.

Semantic: Ambiguity scan via detect_instruction_conflicts.py to flag unclear objectives.

Behavioral: Scenario dry-run using simulate_protocol_execution.py on historical prompts to validate feasibility.

Conflict: Baseline overlap analysis with generate_consistency_report.py vs existing master rules.

Automation bindings: analyze_brief.py, brief_processor.py, new rule_lifecycle_manager.py (aggregates charter metadata).

Human gate: Architecture council reviews charter, ensuring objectives respect kernel rule priorities.

2. Requirement Gathering
Objective: Capture triggers, scopes, tags, and contexts that determine when instructions load.

Input contract: Approved charter, master rule taxonomy, trigger vocabulary, relevant slash-command specs.

Output contract: Instruction requirements matrix (triggers/scopes/tags), dependency map, evidence sourcing plan.

Success criteria: Complete trigger coverage, dependencies resolved, evidence plan endorsed.

Quality gates:

Syntactic: Matrix validated via validate_ai_directives.py for frontmatter compliance.

Semantic: validation_gates.py checklist confirms clarity of trigger definitions.

Behavioral: simulate_protocol_execution.py ensures triggers activate correct slash commands.

Conflict: Proposed new conflict_detector.py cross-references triggers with detect_instruction_conflicts.py.

Automation bindings: plan_from_brief.py, generate_protocol_sequence.py, conflict_detector.py (new).

Human gate: Requirements workshop sign-off by instruction architect and policy lead.

3. Designing
Objective: Author the structural blueprint (YAML frontmatter, sections, checkpoints, evidence gates).

Input contract: Requirements matrix, master rule style guide, quality gate catalog, evidence schema.

Output contract: Design spec (frontmatter schema, section outline, checkpoint definitions, evidence bindings).

Success criteria: Blueprint references required fields, checkpoints cover all intents, evidence hooks defined.

Quality gates:

Syntactic: system_instruction_formatter.py enforces YAML/frontmatter template.

Semantic: validate_protocol_steps.py checks logical ordering.

Behavioral: simulate_protocol_execution.py ensures checkpoints lead to expected decisions.

Conflict: generate_consistency_report.py verifies alignment with kernel rules.

Automation bindings: system_instruction_formatter.py, review_protocol_loader.py, workflow_automation.py for compatibility.

Human gate: Design review board approves structure before authoring.

4. Building
Objective: Produce the .mdc meta-instruction with directive text, checklists, and evidence hooks.

Input contract: Approved design spec, writing guidelines, evidence repository credentials.

Output contract: Versioned .mdc file, changelog entry, evidence placeholder records.

Success criteria: .mdc compiles, references correct scripts/commands, instructions actionable.

Quality gates:

Syntactic: standardize_frontmatter.py (existing) verifies formatting; validate_ai_directives.py double-checks.

Semantic: detect_instruction_conflicts.py scanning for ambiguous directives.

Behavioral: Dry-run with /protocol-orchestrator or /elaborate to confirm command compatibility.

Conflict: validate_script_bindings.py ensures automation references resolve.

Automation bindings: run_generate_rules.py, system_instruction_formatter.py, evidence hooks via evidence_manager.py.

Human gate: Principal author signs off on final wording; governance committee verifies compliance.

5. Testing
Objective: Validate behavior against scripted scenarios and regression suites.

Input contract: Built .mdc, test scenarios, baseline evidence set, automation harness.

Output contract: Test report, behavior diffs, remediation tickets.

Success criteria: All gating tests pass, scenario coverage complete, evidence stored.

Quality gates:

Syntactic: Re-run validate_ai_directives.py after edits.

Semantic: quality_gates.py enforces clarity rules.

Behavioral: test_policy_decisions.py, simulate_protocol_execution.py, and new rule_behavior_regression.py ensure expected outputs.

Conflict: detect_instruction_conflicts.py with updated inventory.

Automation bindings: quality_gates.py, validate_workflow_integration.py, evidence_manager.py for artifact logging.

Human gate: QA architect reviews test evidence and signs behavioral correctness.

6. Implementation
Objective: Stage instructions into .cursor/rules/ or .cursor/commands/ with correct metadata and dependencies.

Input contract: Passed test report, deployment checklist, environment manifest.

Output contract: Staged instruction bundle, dependency manifest, rollback plan.

Success criteria: Files placed correctly, dependencies resolved, rollback path documented.

Quality gates:

Syntactic: validate_script_bindings.py ensures path and registry coherence.

Semantic: review_protocol_loader.py confirms integration narrative fits workflow.

Behavioral: simulate_protocol_execution.py within staging environment.

Conflict: generate_consistency_report.py verifying global impacts.

Automation bindings: workflow_automation.py, ai_orchestrator.py, new instruction_deployer.py for bundling.

Human gate: Release manager approves staging deployment.

7. Deployment
Objective: Activate instruction in live AI agent workflows and slash-command registry.

Input contract: Approved staged bundle, production change record, communication plan.

Output contract: Deployment log, updated command registry, activation evidence.

Success criteria: Live workflow loads rule, slash commands reference new instruction, no regressions.

Quality gates:

Syntactic: Production run_workflow.py smoke test.

Semantic: Live validation_gates.py ensures approval captured.

Behavioral: workflow_automation.py monitors runtime traces; new live_rule_monitor.py checks adoption.

Conflict: detect_instruction_conflicts.py run against production inventory.

Automation bindings: run_workflow.py, ai_executor.py, external_services.py for environment hooks.

Human gate: Deployment CAB signs off (architect + operations).

8. Maintenance
Objective: Monitor drift, gather feedback, version and retire instructions responsibly.

Input contract: Telemetry reports, evidence logs, user feedback, version history.

Output contract: Maintenance dashboard, versioned updates, retirement decisions.

Success criteria: Drift detected/mitigated, updates versioned, obsolete instructions retired safely.

Quality gates:

Syntactic: system_instruction_formatter.py re-validates updates.

Semantic: generate_consistency_report.py ensures clarity over time.

Behavioral: Periodic simulate_protocol_execution.py with new scenarios.

Conflict: detect_instruction_conflicts.py plus lifecycle metrics from rule_lifecycle_manager.py.

Automation bindings: evidence_report.py, migrate_evidence_data.py, rollback_* scripts for reversions.

Human gate: Quarterly governance review with evidence dossier.

Automation binding matrix
Phase	Checkpoint	Script binding	Success criteria
Planning	Charter schema	system_instruction_formatter.py	YAML/frontmatter passes linting.
Planning	Ambiguity scan	detect_instruction_conflicts.py	No unresolved ambiguity flags.
Requirements	Trigger coverage	generate_protocol_sequence.py	All triggers map to workflow nodes.
Designing	Step order	validate_protocol_steps.py	Sequential dependencies satisfied.
Building	Evidence hooks	evidence_manager.py	Evidence endpoints registered.
Testing	Behavioral regression	test_policy_decisions.py	Scenarios match expected outputs.
Implementation	Binding integrity	validate_script_bindings.py	All script references resolve.
Deployment	Runtime activation	run_workflow.py/ai_executor.py	Workflow loads instruction without errors.
Maintenance	Drift monitoring	evidence_report.py + rule_lifecycle_manager.py	No unexplained deviations in evidence logs.
Phase templates
Requirement gathering template
# Instruction Requirement Matrix
## Context Summary
- Charter reference:
- Related workflow phase(s):
## Trigger Definition
| Trigger Keyword | Scope | Slash Command | Expected Rule |
|-----------------|-------|---------------|---------------|
## Tags & Scope
- Tags: [...]
- Scope statement:
## Dependencies
- Upstream rules:
- Downstream workflows:
## Evidence Plan
- Evidence source(s):
- Storage path:
## Approval
- Architect:
- Policy lead:
- Date:
Design blueprint template
---
description: "TAGS: [ ] | TRIGGERS:  | SCOPE:  | DESCRIPTION: "
alwaysApply: false
version: v1.0.0
owner: 
---

# Rule Title
## Purpose
## Preconditions
## Cognitive Checkpoints
1. [Name] – success/rollback criteria
## Evidence Gates
- Gate name → evidence_manager collection id
## Automation Hooks
- Script bindings:
## Rollback
Testing template
# Meta-Instruction Test Plan
## Scenario Catalog
| ID | Trigger | Expected Behavior | Validation Script |
|----|---------|-------------------|-------------------|
## Regression Suite
- Scripts: simulate_protocol_execution.py, test_policy_decisions.py, rule_behavior_regression.py
## Evidence
- Log path:
- Hash verification:
## Approval
- QA architect:
- Date:
Acceptance criteria checklist
Syntactic correctness (YAML/frontmatter & schema validated).

Semantic clarity (no ambiguous directives after conflict scans).

Behavioral correctness (scenario suites and workflow simulation pass).

Conflict-free integration (consistency and binding checks succeed).

Maintenance protocol
Monitoring: Weekly evidence_report.py diff plus automated telemetry from live_rule_monitor.py; compare against baseline to detect drift.

Updates: Use semantic versioning; run Planning → Testing micro-cycle before promoting; migrate_evidence_data.py preserves history.

Rollback: Trigger rollback_* scripts with latest evidence hash; re-run conflict detection and workflow smoke tests.

Refactoring guidelines: Refactor when repeated drift or new triggers appear; deprecate when usage drops below defined threshold and successor rule validated.

Human-in-the-loop governance
Phase	Evidence required	Approver(s)	Approve/Reject criteria
Planning	Charter, risk register	Architecture council	Objectives align with kernel priorities; risk mitigations defined.
Requirements	Trigger matrix, dependency map	Instruction architect + policy lead	No unresolved scope gaps; evidence plan feasible.
Designing	Blueprint, checkpoint catalog	Design review board	Structure satisfies frontmatter and checkpoint completeness.
Building	.mdc, changelog, lint report	Principal author + governance committee	Directive text precise; automation bindings correct.
Testing	Test logs, regression summary	QA architect	All scenarios pass; conflicts resolved.
Implementation	Staging manifest, rollback plan	Release manager	Dependencies resolved; rollback ready.
Deployment	CAB record, activation logs	CAB (architect + ops)	Production smoke tests clean; approvals captured.
Maintenance	Telemetry, drift report, version history	Governance board	Drift within tolerance; update/retire decisions justified.
