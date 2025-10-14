# Migration Guide: Unified Workflow Orchestrator

This guide helps teams upgrading from earlier versions of the template integrate the new protocol orchestrator, script registry, and updated protocol playbooks.

## 1. Automation Module Relocation
- All orchestrator scripts moved from `unified_workflow/automation/` to the shared `scripts/` package.
- Update imports to use `from scripts.<module> import ...` instead of `unified_workflow.automation`.
- The `scripts/__init__.py` file now re-exports common utilities (orchestrator, evidence manager, quality gates, etc.).

## 2. Dependency Management
- Core dependencies are consolidated in the root `requirements.txt`.
- Legacy `unified_workflow/requirements.txt` now references the root file (`-r ../requirements.txt`).
- Update your environment installation scripts to use `pip install -r requirements.txt`.

## 3. Protocol Alignment
- Protocol markdown files in `unified_workflow/phases/` now follow the unified template with explicit `{SCRIPT: ...}` hooks.
- Ensure any custom protocols adopt the same structure so validators can detect automation bindings.
- Generated command files live under `.cursor/commands/generated/` and link back to the updated protocol documents.

## 4. Orchestrator Workflow
- New scripts provide the orchestration pipeline:
  1. `scripts/analyze_brief.py` parses `PROJECT-BRIEF.md` and outputs analysis JSON.
  2. `scripts/generate_protocol_sequence.py` reads the analysis and produces numbered command files.
  3. `scripts/init_client_project.py` stitches the steps together and optionally scaffolds a project from the brief.
- The orchestrator relies on `scripts/script-registry.json` to map automation scripts to protocol phases. Extend this file when introducing new scripts.

## 5. Validation Enhancements
- `scripts/validate_protocol_steps.py` now checks for `{SCRIPT: ...}` bindings in unified protocols.
- `scripts/validate_ai_directives.py` validates the new `ORCHESTRATOR-SYSTEM-INSTRUCTION.md`.
- `scripts/validate_script_bindings.py` (new) verifies that registry entries and markdown script references resolve to actual executables.

## 6. Testing Updates
- A new integration test (`tests/test_orchestration_flow.py`) exercises the orchestrator pipeline using synthetic briefs.
- Add `pytest` to your CI pipeline to ensure orchestrator regressions are caught early.

## 7. Documentation Refresh
- Review `README.md`, `TEMPLATE-ORCHESTRATION-GUIDE.md`, and `ORCHESTRATOR-SYSTEM-INSTRUCTION.md` for the latest workflow instructions.
- Update any internal runbooks to reference the new command locations and orchestration commands.

## 8. Optional Cleanup
- If you forked the template previously, remove stale copies of automation modules under `unified_workflow/automation/` after confirming your project imports the shared `scripts` package.

For additional support, consult `TEMPLATE-ORCHESTRATION-GUIDE.md` or the example workflow demonstrated in `examples/sample-brief.md`.
