# Next Session Plan

## Priority Files
1. .cursor/ai-driven-workflow/review-protocols/utils/_review-router.md
2. .cursor/ai-driven-workflow/review-protocols/utils/context-analyzer.md
3. .cursor/ai-driven-workflow/review-protocols/utils/enhanced-static-template.md

## Continuity Guidance
- Trace how severity vocabularies (`[STRICT]`, `[CRITICAL]`, glyph classifications) from the design system and accessibility reviews must be routable by the utility layer, ensuring the audit router can interpret UI-focused findings without losing priority semantics.【F:.cursor/ai-driven-workflow/review-protocols/design-system.md†L21-L129】【F:.cursor/ai-driven-workflow/review-protocols/ui-accessibility.md†L112-L171】
- Align pre-production and security audit outputs with the router’s dependency scanning or escalation hooks so release-blocking vulnerabilities surface in utility orchestration logic.【F:.cursor/ai-driven-workflow/review-protocols/pre-production.md†L54-L61】【F:.cursor/ai-driven-workflow/review-protocols/security-check.md†L37-L44】
- Maintain context on Layer 2/7 interplay when inspecting utilities to confirm metadata propagation for security and readiness checkpoints remains intact across automated routing.【F:.cursor/ai-driven-workflow/review-protocols/pre-production.md†L6-L53】

## Evidence Requirements
- Capture how each utility structures routing metadata, context ingestion, or template rendering, citing line anchors that show how severity levels, layer identifiers, or telemetry hooks are encoded.
- Document integration points between utility outputs and the specialized protocols analyzed in this session, emphasizing how security and UI audits feed into routing decisions.

## Session Goals
- Produce full five-section analyses for the prioritized utilities, emphasizing how they operationalize severity tagging and context chaining for audit outputs.
- Extend the insight log with observations about routing intelligence and update the dependency map to include telemetry handoffs between utilities and protocol-specific reviews.
