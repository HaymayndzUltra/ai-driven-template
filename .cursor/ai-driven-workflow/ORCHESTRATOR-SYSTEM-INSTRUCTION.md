# PROTOCOL ORCHESTRATOR SYSTEM INSTRUCTION

## Brief Analysis Protocol
- Parse `PROJECT-BRIEF.md` frontmatter and body, extracting project type, stack, complexity, compliance, and lifecycle goals.
- Detect optional phases (Operations, Compliance, ML) based on keywords and stakeholder requirements.
- Cross-reference detected stack with context kit to validate assumptions; request clarification when conflicts arise.
- Persist analysis output to JSON so downstream commands share a single source of truth.

## Protocol Selection Matrix
- Always include Phases 0–5 unless brief explicitly scopes them out (e.g., documentation-only projects).
- Add Phase 6 (Operations) when deployment, monitoring, or SLO language appears.
- Inject additional domain protocols (e.g., ML experimentation, compliance) when brief contains relevant triggers.
- Respect dependency ordering: Bootstrap → PRD → Task Generation → Execution → Quality → Retrospective → Operations.

## Script Binding Logic
- Load `scripts/script-registry.json` to map lifecycle phases to automation commands.
- Supplement registry entries with domain-specific scripts detected in project templates or context kit.
- Ensure every protocol step includes either a script invocation, a manual validation instruction, or both.
- Validate script availability; fall back to manual instructions if a script is missing and log the exception.

## Validation Gates
- Bootstrap: confirm context kit and rules audit completed.
- PRD: ensure specification includes architecture matrix, success metrics, and approved sign-off.
- Task Generation: verify full coverage of PRD requirements and dependency graph consistency.
- Execution: confirm evidence artifacts and task statuses align with backlog.
- Quality: require successful audit report, coverage thresholds, and compliance checks.
- Retrospective: enforce action item tracking and retrospective report publication.
- Operations (optional): validate deployment logs, monitoring coverage, and rollback readiness.

## Command Generation
- Build numbered command files under `.cursor/commands/` with format `NN-protocol-name.md`.
- Embed protocol metadata, prerequisites, and script invocations using the unified template format.
- Reference relevant `.mdc` rules in each command, including master and project-specific governance.
- Record orchestrator decisions (adapted vs generated protocols) in evidence for traceability.
