# Dev-Workflow Template

Source of truth template for AI-driven development workflow.

## Quick Start

1. **Clone the template and reset git history**
   ```bash
   git clone <template-repo-url> my-new-project
   cd my-new-project
   rm -rf .git && git init
   ```

2. **Provide a project brief**
   - Copy `examples/sample-brief.md` to `PROJECT-BRIEF.md` and adjust details.
   - Include stack, complexity, lifecycle, and compliance signals in the frontmatter.

3. **Run the protocol orchestrator**
   ```bash
   python scripts/init_client_project.py \
     --brief PROJECT-BRIEF.md \
     --summary
   ```
   - Analysis JSON is written to `.cursor/orchestration/analysis.json`
   - Protocol command files are generated in `.cursor/commands/generated/`
   - Optionally add `--generate-scaffold` to trigger `scripts/generate_from_brief.py`

4. **Execute commands phase by phase**
   - Each command links to the canonical protocol in `unified_workflow/phases/`
   - Automation hooks are injected from `scripts/script-registry.json`
   - Record evidence with `scripts/evidence_manager.py`

## What's Included

- ✅ 7-phase ai-driven-workflow protocols
- ✅ 8 master rules + 10 common rules
- ✅ 20+ automation scripts
- ✅ Validation and testing tools
- ✅ CI/CD integration templates
- ✅ Comprehensive documentation

## Unified Protocols

- **Protocol 00**: Client Discovery (job post → project brief)
- **Protocol 0**: Bootstrap & Context Engineering
- **Protocol 1**: Implementation-Ready PRD
- **Protocol 2**: Task Generation & Delivery Plan
- **Protocol 3**: Execution & Evidence Capture
- **Protocol 4**: Quality Audit & Release Readiness
- **Protocol 5**: Retrospective & Continuous Improvement
- **Protocol 6** *(dynamic)*: Operations, Deployment & Observability (added when the brief requires production operations)

## Orchestration & Validation Tools

- **Brief analysis**: `python scripts/analyze_brief.py --brief PROJECT-BRIEF.md --pretty`
- **Command generation**: `python scripts/generate_protocol_sequence.py --analysis .cursor/orchestration/analysis.json --summary`
- **Project initialization**: `python scripts/init_client_project.py --brief PROJECT-BRIEF.md --summary`
- **Protocol validation**:
  ```bash
  python scripts/validate_protocol_steps.py --summary
  python scripts/validate_ai_directives.py --summary
  python scripts/validate_script_bindings.py --summary
  ```
- **Integration tests**: `pytest tests/test_orchestration_flow.py`

## Customization

1. Add project-specific rules to `.cursor/rules/project-rules/`
2. Customize automation scripts in `scripts/`
3. Update CI/CD workflows in `.github/workflows/`

## Documentation

- `.cursor/ai-driven-workflow/README.md` – Legacy protocol reference
- `.cursor/ai-driven-workflow/ORCHESTRATOR-SYSTEM-INSTRUCTION.md` – System instruction used by the protocol orchestrator
- `unified_workflow/phases/` – Updated protocol playbooks aligned with automation hooks
- `TEMPLATE-ORCHESTRATION-GUIDE.md` – End-to-end orchestration workflow
- `MIGRATION-GUIDE.md` – Notes for teams upgrading from previous versions
- `CLAUDE.md` – AI boot sequence with orchestration trigger
