# Phase 0: Bootstrap & Context Engineering

## AI Role
**Context Architect** - Analyze repository structure and configure the AI Governor Framework

## Mission
Perform initial analysis of the project, configure the pre-installed AI Governor Framework, and propose a foundational "Context Kit" to dramatically improve all future AI collaboration.

## Prerequisites
- Project repository with existing codebase
- AI Governor Framework installed
- Access to master-rules and common-rules

## Process

### Step 1: Tooling Configuration & Rule Activation
1. **Detect Tooling & Configure Rules**
   - Ask user: "Are you using Cursor as your editor? This is important for activating the rules correctly."
   - Dynamically locate rules directories: `find . -name "master-rules" -type d` and `find . -name "common-rules" -type d`
   - If Cursor usage confirmed:
     - Create `.cursor/rules/` and move found rule directories there
     - Rename files to `.mdc` and ensure correct metadata
     - Verify/Add metadata with `alwaysApply` property

2. **[STRICT] Rule Formatting Protocol**
   - Apply System Instruction Formatter to all discovered rules
   - Validate YAML frontmatter structure
   - Normalize directive tags to canonical set
   - Resolve conflicts using precedence matrix

3. **[STRICT] Directive Grammar Enforcement**
   - Use canonical tags: `[STRICT]`, `[GUIDELINE]`, `[CRITICAL]`, `[REQUIRED]`, `[OPTIONAL]`
   - Map deprecated aliases to canonical set
   - Ensure headings carry directive context

4. **[STRICT] Conflict Resolution Protocol**
   - Detect conflict → halt execution
   - Emit: `[RULE CONFLICT] "{X}" conflicts with "{Y}". Quote: "{Y_excerpt}". Request guidance.`
   - If auto-resolvable by matrix, apply and log decision

### Step 2: Initial Codebase Mapping
1. **Map Codebase Structure**
   - Perform recursive file listing to create complete `tree` view
   - Identify key files (package.json, main files, config files)
   - Propose analysis plan to user for confirmation
   - Analyze approved files to confirm technology stack

### Step 3: Thematic Investigation Plan
1. **Generate Thematic Questions**
   - Security: How are users authenticated and sessions managed?
   - Data Flow: How do different services communicate?
   - Conventions: What are standard patterns for error handling, validation, logging?

### Step 4: Autonomous Deep Dive & Synthesis
1. **Perform Deep Semantic Analysis**
   - Use semantic search to investigate core architectural processes
   - Find concrete implementation patterns in code
   - Synthesize findings into high-level architectural principles

### Step 5: Collaborative Validation
1. **Present Consolidated Report**
   - Present understanding for user validation
   - Identify areas needing clarification
   - Await user feedback before building Context Kit

### Step 6: Documentation Generation
1. **Generate READMEs**
   - Create/update `README.md` files based on validated principles
   - Generate each file iteratively with user approval

### Step 7: Project Rules Generation
1. **Generate Project Rules**
   - Create project-specific rules from READMEs
   - Ensure compliance with rule creation guidelines
   - Link each rule to its source README

2. **[STRICT] System Instruction Formatter Integration**
   - Format all generated rules using canonical structure
   - Apply instruction type detection (Governance/Operational/Technical Policy)
   - Implement validation gates for rule clarity
   - Use minimal profiles for rule categorization

3. **[STRICT] Structural Validation**
   - YAML frontmatter only: `description` (string), `alwaysApply` (boolean optional)
   - Headings present: Persona, Core Principle, Protocol, Examples
   - No bare URLs; use links in backticks or markdown links
   - Code blocks fenced; no mixed formats

4. **[STRICT] Enforcement Rubric**
   - Measurability: directives testable
   - Determinism: no ambiguous language
   - Safety: security-sensitive steps explicit

## Outputs

### Context Kit
- **Foundation READMEs**: Project overview, architecture, conventions
- **Domain Models**: Business logic and data structures
- **Tech Stack Briefs**: Technology choices and rationale

### Project Rules
- **Project-specific rules**: Enforce project conventions
- **Metadata compliance**: Proper TAGS, TRIGGERS, SCOPE
- **Rule discovery**: Searchable and discoverable
- **Formatted instructions**: Canonical directive structure
- **Conflict resolution**: Precedence matrix applied

### Evidence Artifacts
- **Context kit catalog**: All generated documentation
- **Rule inventory**: All project-specific rules
- **Bootstrap log**: Execution timeline and decisions

## Quality Gates

### Validation Checkpoints
- [ ] Rules properly configured and discoverable
- [ ] Codebase structure mapped and understood
- [ ] Architectural principles validated by user
- [ ] Context kit complete and approved
- [ ] Project rules generated and linked
- [ ] System Instruction Formatter applied to all rules
- [ ] Directive tags normalized to canonical set
- [ ] Conflict resolution protocol implemented
- [ ] Structural validation passed

### Success Criteria
- User validates architectural understanding
- Context kit provides foundation for future phases
- Project rules enforce project conventions
- Evidence trail complete and traceable
- All rules formatted with canonical directive structure
- Conflict resolution matrix operational
- Structural validation gates passed

## Duration
**Target**: 5-15 minutes  
**Actual**: Variable based on codebase complexity

## Next Phase
Proceed to **Phase 1: PRD Creation** with validated context kit

## Automation Integration

### AI Actions
```python
# Bootstrap execution
def execute_bootstrap(project_path):
    # 1. Detect and configure rules
    rules_config = detect_and_configure_rules()
    
    # 2. Map codebase structure
    codebase_map = analyze_codebase_structure(project_path)
    
    # 3. Generate thematic questions
    themes = generate_thematic_questions(codebase_map)
    
    # 4. Perform deep analysis
    principles = perform_deep_analysis(themes)
    
    # 5. Generate context kit
    context_kit = generate_context_kit(principles)
    
    # 6. Generate project rules
    project_rules = generate_project_rules(context_kit)
    
    # 7. Apply System Instruction Formatter
    formatted_rules = apply_system_instruction_formatter(project_rules)
    
    # 8. Validate rule structure
    validation_result = validate_rule_structure(formatted_rules)
    
    # 9. Log evidence
    log_evidence("phase0", context_kit, formatted_rules, validation_result)
    
    return {
        "context_kit": context_kit,
        "project_rules": formatted_rules,
        "validation_result": validation_result,
        "evidence": get_evidence("phase0")
    }
```

### Human Validation
- User confirms architectural understanding
- User approves context kit generation
- User validates project rules
- User approves formatted rule structure
- User confirms conflict resolution decisions

## Error Handling

### Common Issues
- **Missing rules**: Report critical failure and halt
- **Complex codebase**: Break down into manageable chunks
- **User disagreement**: Iterate until consensus reached
- **Rule conflicts**: Apply conflict resolution protocol
- **Formatting errors**: Re-run System Instruction Formatter

### Recovery Actions
- Re-run rule detection if configuration fails
- Re-analyze codebase if understanding incomplete
- Regenerate context kit if user feedback significant
- Re-apply System Instruction Formatter if conflicts detected
- Re-validate rule structure if formatting errors occur

## Automation Integration
- Workflow1 automation wrappers are not invoked during bootstrap, but operators should ensure repository cloning and Python
  environments are ready so subsequent phases can call `unified_workflow.automation.workflow1` wrappers without interruption.
- Capture baseline context (project slug, environment strategy) so it can be passed to phase-specific wrappers starting in Phase 2.

## Evidence Templates
- Review the [workflow1 evidence index](../templates/workflow1_evidence/index.json) to understand which template packs will be
  consumed later in the workflow.
- Confirm the evidence root is initialized (`workflow1/<phase>/evidence`) before handing off to the automation phases.

## Operator Instructions
- Provision the project workspace and verify that `python -m unified_workflow.cli` can resolve automation modules.
- Document any manual bootstrap activities so they can be attached to the manifest using the new automation metadata fields.
