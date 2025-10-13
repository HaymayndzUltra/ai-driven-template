# Generate Cursor Rules

## Command: /Generate Cursor Rules

This command triggers the creation of comprehensive Cursor rules for the current project. When executed, the AI should:

### 1. **Discovery Phase**
- Scan the `.cursor/rules/` directory structure
- Identify existing master-rules, common-rules, and project-rules
- Analyze the project's technology stack and architecture
- Read key documentation files (README.md, package.json, requirements.txt, etc.)

### 2. **Analysis Phase**
- Determine what type of project this is (frontend, backend, fullstack, etc.)
- Identify the main technologies and frameworks used
- Check for missing project-specific rules
- Understand the existing rule hierarchy and patterns

### 3. **Generation Phase**
Create project-specific rules following this structure:

#### For Frontend Projects:
- **File**: `{project-path}/.cursor/rules/project-rules/{framework}-app-structure.mdc`
- **Content**: Framework-specific patterns, component structure, state management, styling guidelines, testing strategies

#### For Backend Projects:
- **File**: `{project-path}/.cursor/rules/project-rules/{framework}-backend-architecture.mdc`
- **Content**: API patterns, database models, authentication flows, service layer patterns, testing approaches

#### For Fullstack Projects:
- Create separate rules for frontend and backend components
- Include integration patterns and shared conventions

### 4. **Rule Format Requirements**
Each generated rule must include:

```yaml
---
description: "TAGS: [tag1,tag2] | TRIGGERS: keyword1,keyword2 | SCOPE: scope | DESCRIPTION: One-sentence summary"
alwaysApply: false
---
```

### 5. **Content Guidelines**
- **Structure**: Clear sections with headers
- **Examples**: Code examples for common patterns
- **Conventions**: Project-specific coding standards
- **Best Practices**: Framework-specific recommendations
- **Testing**: Testing strategies and patterns
- **Deployment**: Environment and deployment considerations

### 6. **Quality Checklist**
Before finalizing, ensure each rule:
- [ ] Has proper YAML frontmatter with TAGS, TRIGGERS, SCOPE, DESCRIPTION
- [ ] Includes practical code examples
- [ ] Covers the most common development scenarios
- [ ] Follows the existing rule naming conventions
- [ ] Is placed in the correct directory structure
- [ ] References relevant files using `[filename.ext](mdc:filename.ext)` format

### 7. **Output Format**
After generation, provide:
- Summary of rules created
- File locations
- Brief description of what each rule covers
- Instructions for how to use/activate the rules

---

## AGENTS.md Generation (Agent Behavior Contract)

Create or update a top-level `AGENTS.md` that defines how AI coding agents (including GPT-5-Codex) should operate within this repository.

### 1. File Location
- **Path**: `{project-root}/AGENTS.md`

### 2. Required Sections
- **Project Overview**: goals, scope, and primary tech stack
- **Coding Style**: language-specific formatting, naming conventions, preferred/avoided patterns
- **Build & Test Commands**: exact commands to run before/after edits (build, lint, typecheck, unit/e2e)
- **PR & Commit Guidelines**: branch naming, commit style, PR checklist, review expectations
- **Security & Compliance**: secret handling, dependency scanning, policy constraints
- **Performance & Accessibility** (if applicable): budgets, thresholds, tools
- **Repository Conventions**: directory structure, module boundaries, file naming
- **Change Management**: when to propose vs. auto-apply edits, approval gates

### 3. Suggested Template
```markdown
# AGENTS.md

## Project Overview
- Purpose: <one-liner>
- Scope: <frontend/backend/fullstack>
- Tech Stack: <frameworks, languages, runtime>

## Coding Style
- Formatting: <tool/config> (e.g., Prettier, Black)
- Naming: <conventions>
- Patterns: prefer <X>, avoid <Y>

## Build & Test
- Build: <command>
- Lint/Typecheck: <commands>
- Unit/E2E: <commands>
- CI Required Checks: <list>

## PR & Commits
- Branch: <pattern>
- Commits: <style>
- PR Checklist: <bullets>

## Security & Compliance
- Secrets: <policy>
- Dependency Scans: <tools>
- Policies: <lint/security rules>

## Performance & Accessibility (if applicable)
- Budgets/Thresholds: <values>
- Tools: <Lighthouse, axe, etc.>

## Repository Conventions
- Structure: <dirs>
- Boundaries: <rules>
- File Naming: <conventions>

## Change Management
- When to open PR vs auto-apply edits
- Required approvals and gates

## Agent Governance (Codex)
- Load order: `.cursor/rules/**/*.mdc` → `AGENTS.md` → `README.md`
- Rule application:
  - Honor `alwaysApply: true`
  - Use `globs` to scope file-specific rules (e.g., *.ts,*.tsx)
  - Use `description` for targeted fetching
- Precedence: project rules > AGENTS.md > common/master (unless master overrides)
- Execution gates: run build/lint/typecheck/tests before/after edits per this file
- Re-evaluate: re-absorb on session start and on any major context shift
```

### 4. Quality Checklist (AGENTS.md)
- [ ] Contains all sections above, customized to this repo
- [ ] Commands are copy-paste runnable
- [ ] Conventions are precise and enforceable
- [ ] PR and security checklists are actionable
- [ ] Agent Governance section included for Codex

---

## Codex Absorption & Enforcement

Ensure GPT-5-Codex absorbs and follows the same governance as Cursor by loading both the Cursor Rules and the `AGENTS.md`.

### 1. Absorption Order & Sources
- Load `.cursor/rules/` (master-rules, common-rules, project-rules)
- Load `AGENTS.md` from repo root
- Read `README.md` at the project scope as the architectural source of truth

### 2. Application Principles
- **Rules precedence**: project-specific rules > AGENTS.md > common/master rules (unless a master rule explicitly overrides)
- **Execute build/lint/test commands** from `AGENTS.md` and relevant rules before/after edits
- **Conform to coding standards** and PR guidelines defined across rules and `AGENTS.md`
- **Respect security, performance, and accessibility gates** specified

### 3. Activation Triggers
- On session start or context shift, re-absorb `.cursor/rules/`, `AGENTS.md`, and `README.md`
- Before code changes, verify the applicable rules and `AGENTS.md` requirements

### 4. Verification
- [ ] Codex followed rule-specific checklists
- [ ] CI checks from `AGENTS.md` pass locally before PR
- [ ] Generated code matches style and architectural conventions
- [ ] All `.mdc` rules properly loaded and applied based on globs/alwaysApply

---

**Usage**: Type `/Generate Cursor Rules` in any `.cursor/commands/` file to trigger this process.

**Triggers**: "generate", "cursor rules", "create rules", "rule generation", "AGENTS.md", "codex absorption"

5. Content Guidelines
Structure: Clear sections with headers
Examples: Code examples for common patterns
Conventions: Project-specific coding standards
Best Practices: Framework-specific recommendations
Testing: Testing strategies and patterns
Deployment: Environment and deployment considerations
6. Quality Checklist
Before finalizing, ensure each rule:
[ ] Has proper YAML frontmatter with TAGS, TRIGGERS, SCOPE, DESCRIPTION
[ ] Includes practical code examples
[ ] Covers the most common development scenarios
[ ] Follows the existing rule naming conventions
[ ] Is placed in the correct directory structure
[ ] References relevant files using [filename.ext](mdc:filename.ext) format
7. Output Format
After generation, provide:
Summary of rules created
File locations
Brief description of what each rule covers
Instructions for how to use/activate the rules
AGENTS.md Generation (Agent Behavior Contract)
Create or update a top-level AGENTS.md that defines how AI coding agents (including GPT-5-Codex) should operate within this repository.
1. File Location
Path: {project-root}/AGENTS.md
2. Required Sections
Project Overview: goals, scope, and primary tech stack
Coding Style: language-specific formatting, naming conventions, preferred/avoided patterns
Build & Test Commands: exact commands to run before/after edits (build, lint, typecheck, unit/e2e)
PR & Commit Guidelines: branch naming, commit style, PR checklist, review expectations
Security & Compliance: secret handling, dependency scanning, policy constraints
Performance & Accessibility (if applicable): budgets, thresholds, tools
Repository Conventions: directory structure, module boundaries, file naming
Change Management: when to propose vs. auto-apply edits, approval gates
3. Suggested Template

# AGENTS.md

## Project Overview
- Purpose: <one-liner>
- Scope: <frontend/backend/fullstack>
- Tech Stack: <frameworks, languages, runtime>

## Coding Style
- Formatting: <tool/config> (e.g., Prettier, Black)
- Naming: <conventions>
- Patterns: prefer <X>, avoid <Y>

## Build & Test
- Build: <command>
- Lint/Typecheck: <commands>
- Unit/E2E: <commands>
- CI Required Checks: <list>

## PR & Commits
- Branch: <pattern>
- Commits: <style>
- PR Checklist: <bullets>

## Security & Compliance
- Secrets: <policy>
- Dependency Scans: <tools>
- Policies: <lint/security rules>

## Performance & Accessibility (if applicable)
- Budgets/Thresholds: <values>
- Tools: <Lighthouse, axe, etc.>

## Repository Conventions
- Structure: <dirs>
- Boundaries: <rules>
- File Naming: <conventions>

## Change Management
- When to open PR vs auto-apply edits
- Required approvals and gates

## Agent Governance (Codex)
- Load order: `.cursor/rules/**/*.mdc` → `AGENTS.md` → `README.md`
- Rule application:
  - Honor `alwaysApply: true`
  - Use `globs` to scope file-specific rules (e.g., *.ts,*.tsx)
  - Use `description` for targeted fetching
- Precedence: project rules > AGENTS.md > common/master (unless master overrides)
- Execution gates: run build/lint/typecheck/tests before/after edits per this file
- Re-evaluate: re-absorb on session start and on any major context shift

. Quality Checklist (AGENTS.md)
[ ] Contains all sections above, customized to this repo
[ ] Commands are copy-paste runnable
[ ] Conventions are precise and enforceable
[ ] PR and security checklists are actionable
[ ] Agent Governance section included for Codex
Codex Absorption & Enforcement
Ensure GPT-5-Codex absorbs and follows the same governance as Cursor by loading both the Cursor Rules and the AGENTS.md.
1. Absorption Order & Sources
Load .cursor/rules/ (master-rules, common-rules, project-rules)
Load AGENTS.md from repo root
Read README.md at the project scope as the architectural source of truth
2. Application Principles
Rules precedence: project-specific rules > AGENTS.md > common/master rules (unless a master rule explicitly overrides)
Execute build/lint/test commands from AGENTS.md and relevant rules before/after edits
Conform to coding standards and PR guidelines defined across rules and AGENTS.md
Respect security, performance, and accessibility gates specified
3. Activation Triggers
On session start or context shift, re-absorb .cursor/rules/, AGENTS.md, and README.md
Before code changes, verify the applicable rules and AGENTS.md requirements
4. Verification
[ ] Codex followed rule-specific checklists
[ ] CI checks from AGENTS.md pass locally before PR
[ ] Generated code matches style and architectural conventions
[ ] All .mdc rules properly loaded and applied based on globs/alwaysApply
Usage: Type /Generate Cursor Rules in any .cursor/commands/ file to trigger this process.
Triggers: "generate", "cursor rules", "create rules", "rule generation", "AGENTS.md", "codex absorption"
```