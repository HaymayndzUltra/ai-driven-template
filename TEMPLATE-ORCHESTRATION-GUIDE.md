# Template Orchestration Guide

This guide walks through the AI-driven orchestration workflow for onboarding a new client project using the unified protocols and automation registry.

## 1. Prepare the Workspace
1. Clone the template repository.
2. Reset git history (`rm -rf .git && git init`).
3. Review the repository layout:
   - `unified_workflow/phases/` – protocol playbooks with `{SCRIPT: ...}` hooks
   - `scripts/` – shared automation scripts and orchestrator entry points
   - `.cursor/ai-driven-workflow/` – legacy protocol references and system instructions

## 2. Author the Project Brief
1. Copy `examples/sample-brief.md` to the project root as `PROJECT-BRIEF.md`.
2. Populate frontmatter with:
   - `name`, `project_type`, `complexity`, `lifecycle`
   - Stack hints (`frontend`, `backend`, `database`, etc.)
   - Compliance needs (`GDPR`, `SOC2`, `HIPAA`, ...)
3. Describe requirements, deployment expectations, and quality goals in the body.

## 3. Analyze the Brief
```bash
python scripts/analyze_brief.py --brief PROJECT-BRIEF.md --output .cursor/orchestration/analysis.json --pretty
```
- Produces structured metadata (project type, stack, lifecycle, detected protocols).
- Flags optional phases (operations, ML, compliance) based on content.

## 4. Generate Protocol Commands
```bash
python scripts/generate_protocol_sequence.py \
  --analysis .cursor/orchestration/analysis.json \
  --output-dir .cursor/commands/generated \
  --summary
```
- Creates numbered command files (`00-*.md`, `01-*.md`, ...).
- Injects automation hooks using `scripts/script-registry.json`.
- References canonical protocol documents in `unified_workflow/phases/`.

## 5. Initialize the Project (One Command)
```bash
python scripts/init_client_project.py --brief PROJECT-BRIEF.md --summary
```
- Runs steps 3–4 automatically.
- Optional: add `--generate-scaffold` to invoke `scripts/generate_from_brief.py` and scaffold into `../generated-projects/`.
- Outputs a summary of analysis, command files, and scaffold location.

## 6. Execute Each Protocol
1. Open the generated command file for the next phase.
2. Follow the linked protocol document and run the listed `{SCRIPT: ...}` commands.
3. Capture evidence with `scripts/evidence_manager.py` and update task state using `scripts/update_task_state.py`.
4. Run quality gates (e.g., `scripts/quality_gates.py --mode comprehensive`) before moving to the next command.

## 7. Validate Automation Bindings
```bash
python scripts/validate_protocol_steps.py --summary
python scripts/validate_ai_directives.py --summary
python scripts/validate_script_bindings.py --summary
```
- Ensures protocols contain script bindings, directives are consistent, and referenced scripts exist.

## 8. Integration Tests
```bash
pytest tests/test_orchestration_flow.py
```
- Exercises the orchestrator pipeline using synthetic briefs (simple, enterprise, ML).
- Validates command generation and script injection logic.

## 9. Customize and Extend
- Add new automation scripts to `scripts/` and register them in `scripts/script-registry.json`.
- Create additional protocol documents using `templates/protocol-template.md`.
- Update `ORCHESTRATOR-SYSTEM-INSTRUCTION.md` when introducing new decision logic or phases.

## 10. Continuous Improvement
- Use the Retrospective protocol (`5-retrospective.md`) to capture insights and feed improvements back into the template.
- Submit pull requests or internal documentation updates referencing this guide for future projects.
