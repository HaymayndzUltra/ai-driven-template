# Next Session Plan

## Priority Files
1. .cursor/ai-driven-workflow/review-protocols/design-system.md
2. .cursor/ai-driven-workflow/review-protocols/pre-production.md

## Continuity Guidance
- Map how the design-system checklist inherits the structural guarantees established by the architecture review so UI components respect module boundaries and communication contracts.【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L10-L26】
- Align pre-production validation with the quick review’s remediation outputs to ensure critical fixes are verified before deployment sign-off.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L42-L48】
- Trace severity tags and layered validation terminology to maintain linguistic cohesion for the audit router when expanding into UI and release reviews.【F:.cursor/ai-driven-workflow/review-protocols/code-review.md†L10-L40】【F:.cursor/ai-driven-workflow/review-protocols/architecture-review.md†L10-L55】

## Evidence Requirements
- Capture explicit quality gates, tooling integrations, and artifact expectations unique to design system and pre-production contexts, citing line anchors in each protocol.
- Document dependencies on shared review utilities (e.g., `_review-router.md`, context analyzers) once referenced, noting how routing metadata propagates.

## Session Goals
- Produce comprehensive five-section analyses with ASCII diagrams for both protocols, emphasizing integration points with previously mapped architecture and code reviews.
- Extend the insight log with UI/release governance patterns and update the dependency map to reflect any new telemetry or approval loops introduced by these protocols.
