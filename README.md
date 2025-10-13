# Dev-Workflow Template

Source of truth template for AI-driven development workflow.

## Quick Start

1. Clone this template:
   ```bash
   git clone <template-repo-url> my-new-project
   cd my-new-project
   ```

2. Initialize your project:
   ```bash
   rm -rf .git
   git init
   ```

3. Start with Protocol 00 (Client Discovery):
   - Paste your job post or project requirements
   - AI will generate project brief

4. Continue with Protocol 0 (Bootstrap):
   - AI will analyze codebase and setup context

## What's Included

- ✅ 7-phase ai-driven-workflow protocols
- ✅ 8 master rules + 10 common rules
- ✅ 20+ automation scripts
- ✅ Validation and testing tools
- ✅ CI/CD integration templates
- ✅ Comprehensive documentation

## Protocols

- **Protocol 00**: Client Discovery (job post → project brief)
- **Protocol 0**: Bootstrap (codebase analysis, context setup)
- **Protocol 1**: PRD Creation (requirements → implementation plan)
- **Protocol 2**: Task Generation (PRD → execution tasks)
- **Protocol 3**: Task Processing (execute tasks, capture evidence)
- **Protocol 4**: Quality Audit (run tests, validate quality)
- **Protocol 5**: Retrospective (review, improve)

## Validation Tools

Run validation at any time:
```bash
# Validate protocol consistency
python3 scripts/validate_protocol_steps.py
python3 scripts/validate_ai_directives.py
python3 scripts/generate_consistency_report.py

# Run integration tests
bash scripts/test_workflow_integration.sh
```

## Customization

1. Add project-specific rules to `.cursor/rules/project-rules/`
2. Customize automation scripts in `scripts/`
3. Update CI/CD workflows in `.github/workflows/`

## Documentation

- `.cursor/ai-driven-workflow/README.md` - Full protocol guide
- `.cursor/ai-driven-workflow/INTEGRATION-GUIDE.md` - Automation integration
- `.cursor/ai-driven-workflow/VALIDATION-GUIDE.md` - Validation system
- `CLAUDE.md` - AI boot sequence
