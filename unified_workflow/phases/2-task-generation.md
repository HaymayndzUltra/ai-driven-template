# Phase 2: Task Generation

## AI Role
**Tech Lead** - Transform PRD into simple, actionable plan

## Mission
Transform a PRD into a granular, step-by-step technical execution plan with minimum viable steps, ensuring both AI and human are aligned on implementation strategy.

## Prerequisites
- Phase 1 completed (PRD approved)
- Access to project rules and context
- Understanding of implementation layers

## Process

### Phase 1: Rule Indexing and Context Preparation
1. **Build Rule Index**
   - Dynamically locate all rule directories using `find . -name "*rules" -type d`
   - Parse rule metadata (TAGS, TRIGGERS, SCOPE, DESCRIPTION)
   - Create in-memory index for compliance checking

2. **Read PRD**
   - Fully analyze PRD to understand goals, constraints, specifications
   - Keep discovered rules in mind for compliance

3. **Identify LLM Models & Personas**
   - Search for current year's best LLM models for code generation
   - Define personas (e.g., "System Integrator", "Code Architect")
   - Assign personas to different task types

4. **Identify Implementation Layers**
   - Determine primary layer (where most work happens)
   - Identify secondary layers (supporting components)
   - Map dependencies between layers

### Phase 2: High-Level Task Generation and Validation
1. **Create Task File**
   - Create `tasks-{prd-name}.md` in relevant directory
   - Structure with parent/child hierarchy

2. **Generate High-Level Tasks**
   - Create top-level tasks (e.g., "Develop UI Component", "Create Backend Route")
   - Focus on MVP - defer non-essential features
   - Add WHY context for each task

3. **Identify Task Dependencies**
   - Map prerequisites between tasks
   - Enable parallel execution where possible
   - Use `[DEPENDS ON: X.Y]` format

4. **Task Complexity Assessment**
   - **Simple**: Well-defined changes with minimal dependencies
   - **Complex**: Multi-system changes, architectural modifications

5. **High-Level Validation**
   - Present task list with WHY statements and dependencies
   - Await user confirmation ("Go") before detailed breakdown

6. **[STRICT] Task Instruction Formatting**
   - Format all task instructions using canonical directives
   - Apply instruction type detection (Operational/Technical Policy)
   - Implement validation gates for task clarity
   - Use minimal profiles for task categorization

### Phase 3: Detailed Breakdown by Layer
1. **Decomposition and Rule Application**
   - Break down each high-level task into atomic sub-tasks
   - Apply relevant rules to each sub-task
   - Use appropriate decomposition template

2. **Assign Model Personas**
   - Match LLM persona to task type
   - "System Integrator" for setup/tool configuration
   - "Code Architect" for business logic/security

3. **Apply Correct Template**
   - **Frontend App**: Use Frontend Decomposition Template
   - **Backend Service**: Use Backend Decomposition Template
   - **Global State**: Use Global State Decomposition Template

4. **Populate Placeholders**
   - Replace `{ComponentName}`, `{serviceName}`, etc. with specific names
   - Ensure consistency across all tasks

5. **[STRICT] Directive Application**
   - Normalize directive tags to canonical set
   - Ensure headings carry directive context
   - Apply precedence matrix for conflicting directives

6. **[STRICT] Validation Gates**
   - Gate A (Determinism): All directives must be tagged `[STRICT]` or `[GUIDELINE]`
   - Gate B (Measurability): At least one measurable acceptance criterion
   - Gate C (Safety): Security controls + audit/logging required
   - Gate D (Sanity): No brand/telemetry in task descriptions

## Decomposition Templates

### Frontend Decomposition Template
```markdown
- [ ] X.0 Develop the "{ComponentName}" component (`{componentName}`).
  - [ ] X.1 **File Scaffolding:** Create complete file structure [APPLIES RULES: {rule-name}]
  - [ ] X.2 **Base HTML:** Implement static HTML structure [APPLIES RULES: {rule-name}]
  - [ ] X.3 **Internationalization:** Create and populate locales files [APPLIES RULES: {rule-name}]
  - [ ] X.4 **JavaScript Logic:** Implement component initialization and API calls [APPLIES RULES: {rule-name}]
  - [ ] X.5 **CSS Styling:** Apply styles with theming support [APPLIES RULES: {rule-name}]
  - [ ] X.6 **Documentation:** Write component README.md [APPLIES RULES: {rule-name}]
```

### Backend Decomposition Template
```markdown
- [ ] Y.0 Develop the "{RoutePurpose}" route in the `{serviceName}` service.
  - [ ] Y.1 **Route Scaffolding:** Create directory and necessary files [APPLIES RULES: {rule-name}]
  - [ ] Y.2 **Handler Logic:** Implement middleware and orchestration [APPLIES RULES: {rule-name}]
  - [ ] Y.3 **Business Logic:** Create dedicated module if complex [APPLIES RULES: {rule-name}]
  - [ ] Y.4 **Testing:** Write integration and unit tests [APPLIES RULES: {rule-name}]
```

### Global State Decomposition Template
```markdown
- [ ] Z.0 Implement "{DomainName}" Global State Management.
  - [ ] Z.1 **Store Creation:** Create TypeScript interfaces and atom store [APPLIES RULES: {rule-name}]
  - [ ] Z.2 **Service Integration:** Implement initialize() and startListener() methods [APPLIES RULES: {rule-name}]
  - [ ] Z.3 **Application Integration:** Update main app component [APPLIES RULES: {rule-name}]
  - [ ] Z.4 **Component Integration:** Update components that use this state [APPLIES RULES: {rule-name}]
  - [ ] Z.5 **Documentation:** Update relevant README files [APPLIES RULES: {rule-name}]
```

## Outputs

### Task Plan Document
- **File**: `tasks-{feature-name}.md`
- **Content**: Complete technical execution plan
- **Format**: Markdown with checkboxes and rule annotations

### Task Metadata
- **Dependencies**: Mapped between tasks
- **Complexity**: Simple/Complex assessment
- **Personas**: Assigned LLM models
- **Rules**: Applied rule references

### Evidence Artifacts
- **Task plan approval**: User validation
- **Rule compliance**: Applied rules documented
- **Planning timeline**: Execution sequence

## Quality Gates

### Validation Checkpoints
- [ ] All high-level tasks generated
- [ ] WHY context added to each task
- [ ] Dependencies mapped correctly
- [ ] Complexity assessed accurately
- [ ] Rules applied to sub-tasks
- [ ] Model personas assigned

### Success Criteria
- User approves task breakdown
- Dependencies enable parallel execution
- Rules ensure compliance
- Plan enables immediate implementation

## Duration
**Target**: 5-15 minutes  
**Actual**: Variable based on feature complexity

## Next Phase
Proceed to **Phase 3: Implementation** with approved task plan

## Automation Integration

### AI Actions
```python
# Task generation execution
def execute_task_generation(prd, context_kit):
    # 1. Build rule index
    rule_index = build_rule_index()
    
    # 2. Identify implementation layers
    layers = identify_implementation_layers(prd)
    
    # 3. Generate high-level tasks
    high_level_tasks = generate_high_level_tasks(prd, layers)
    
    # 4. Map dependencies
    dependencies = map_task_dependencies(high_level_tasks)
    
    # 5. Assess complexity
    complexity = assess_task_complexity(high_level_tasks)
    
    # 6. Decompose into sub-tasks
    detailed_tasks = decompose_tasks(high_level_tasks, rule_index)
    
    # 7. Apply rules and personas
    task_plan = apply_rules_and_personas(detailed_tasks, rule_index)
    
    # 8. Log evidence
    log_evidence("phase2", task_plan, dependencies)
    
    return {
        "task_plan": task_plan,
        "dependencies": dependencies,
        "evidence": get_evidence("phase2")
    }
```

### Human Validation
- User confirms high-level task breakdown
- User validates dependencies and complexity
- User approves detailed sub-task plan
- User confirms rule application

## Error Handling

### Common Issues
- **Missing rules**: Report and halt execution
- **Complex dependencies**: Simplify or break down
- **Rule conflicts**: Resolve with user input

### Recovery Actions
- Re-scan for rules if index incomplete
- Re-analyze dependencies if conflicts found
- Regenerate task plan if significant changes needed

## Automation Integration
- Invoke `Phase2DesignWrappers.generate_architecture_pack(project)` to populate architecture evidence. The wrapper records
  automation metadata (`wrapper=Phase2DesignWrappers.generate_architecture_pack`) in the manifest.
- Use `Phase2DesignWrappers.generate_contract_assets(project, service)` once the target service is confirmed. Supply the `service`
  slug collected during PRD creation so the OpenAPI stub aligns with the planned interface.
- When orchestrating via Python:
  ```python
  from unified_workflow.automation.workflow1 import Phase2DesignWrappers

  wrappers = Phase2DesignWrappers()
  wrappers.generate_architecture_pack(project_slug)
  wrappers.generate_contract_assets(project_slug, service_slug)
  ```

## Evidence Templates
- Architecture pack outputs map to the templates listed for phase 2 in
  [workflow1_evidence/index.json](../templates/workflow1_evidence/index.json).
- Contract assets populate `Product_Backlog.csv`, `Sprint0_Plan.md`, and OpenAPI stubs under `contracts/openapi`.

## Operator Instructions
- Review generated architecture and contract artifacts for completeness. Update the evidence manifest with reviewer notes using the
  new `automation.parameters` field to capture any overrides (e.g., `{"persona": "Tech Lead"}`).
- If adjustments are required, re-run the relevant wrapper; the manifest will de-duplicate entries automatically.
