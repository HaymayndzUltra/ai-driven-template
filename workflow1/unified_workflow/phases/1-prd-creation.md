# Phase 1: PRD Creation

## AI Role
**Product Manager** - Conduct focused interview to create implementation-ready PRD

## Mission
Create a comprehensive Product Requirements Document that provides complete technical specifications including data schemas, API contracts, UI workflows, and business logic to enable immediate development.

## Prerequisites
- Phase 0 completed (Context Kit available)
- User has feature idea or requirement
- Access to project architecture and constraints

## Process

### Phase 1: Analysis and Scoping
1. **Initial Qualification**
   - Ask: "Are we CREATING a new feature from scratch, or MODIFYING an existing one?"
   - Based on answer, proceed to relevant section

2. **Path A: Creating New Feature**
   - "In one sentence, what is the core business need? What problem are you solving?"
   - "Is this feature primarily about: User Interface, Business Process, Data Management, or Static Assets?"
   - Proceed to layer detection

3. **Path B: Modifying Existing Feature**
   - "Please describe the current behavior of the feature you want to modify."
   - "Now, describe the desired behavior after the modification."
   - "Which are the main files, components, or services involved?"
   - "What potential regression risks should we be mindful of?"

4. **Layer Detection**
   - Announce detected implementation layer (Frontend App, Backend Service, Central API, Object Storage)
   - List applicable constraints (communication, technology, architecture)
   - Validate placement with user

### Phase 2: Specifications by Layer

#### Frontend Application (UI)
- "Who is the target user (e.g., admin, customer, guest)?"
- "Can you describe 2-3 user stories? 'As a [role], I want to [action] so that [benefit]'."
- "Do you have a wireframe or clear description of desired look and feel?"
- "How should this component handle responsiveness and different themes?"
- "Does this component need to fetch data from an API or trigger backend actions?"

#### Backend Service (Business Logic)
- "What will the exact API route be (e.g., `/users/{userId}/profile`)?"
- "Which HTTP method and what is the schema of the request body?"
- "What is the schema of a successful response and expected error scenarios?"
- "What are the logical steps the service should perform, in order?"
- "Does this service need to call other APIs or communicate with other services?"
- "What is the security model and what roles are authorized?"

### Phase 3: Architectural Constraints
- Verify proposed interactions respect project's communication rules
- Validate allowed flows (UI → Central API: GET only, etc.)
- Identify prohibited flows (UI → Database: Direct access forbidden)

### Phase 4: Synthesis and Generation
1. **Summarize Architecture**
   - Primary Component: [Detected Layer]
   - Communications: [Validated Flows]
   - Guiding Principle: Avoid Over-Engineering

2. **Final Validation**
   - "Is this summary correct? Shall I proceed with generating the full PRD?"

## PRD Template

```markdown
# PRD: [Feature Name]

## 1. Overview
- **Business Goal:** [Description of need and problem solved]
- **Detected Architecture:**
  - **Primary Component:** `[Frontend App | Backend Service | ...]`

## 2. Functional Specifications
- **User Stories:** [For UI] or **API Contract:** [For Services]
- **Data Flow Diagram:**
  ```
  [Simple diagram showing interaction between components]
  ```

## 3. Technical Specifications
- **Inter-Service Communication:** [Details of API calls]
- **Security & Authentication:** [Security model for chosen layer]

## 4. Out of Scope
- [What this feature will NOT do]
```

## Outputs

### PRD Document
- **File**: `prd-{feature-name}.md`
- **Content**: Complete technical specifications
- **Format**: Markdown with structured sections

### Supporting Artifacts
- **User Stories**: Detailed user scenarios
- **API Contracts**: Request/response schemas
- **Data Flow Diagrams**: Component interactions
- **Security Model**: Authentication and authorization

### Evidence Artifacts
- **PRD approval**: User validation and timestamp
- **Stakeholder sign-off**: Required approvals
- **Technical feasibility**: Architecture validation

## Quality Gates

### Validation Checkpoints
- [ ] Business goal clearly defined
- [ ] Technical architecture validated
- [ ] User stories complete and testable
- [ ] API contracts specified
- [ ] Security model defined
- [ ] Out of scope items identified

### Success Criteria
- User approves PRD completeness
- Technical team confirms feasibility
- Stakeholders sign off on requirements
- PRD enables immediate development

## Duration
**Target**: 10-30 minutes  
**Actual**: Variable based on feature complexity

## Next Phase
Proceed to **Phase 2: Task Generation** with approved PRD

## Automation Integration

### AI Actions
```python
# PRD creation execution
def execute_prd_creation(feature_idea, context_kit):
    # 1. Analyze and scope
    scope = analyze_feature_scope(feature_idea)
    
    # 2. Detect implementation layer
    layer = detect_implementation_layer(scope, context_kit)
    
    # 3. Gather specifications
    specs = gather_specifications_by_layer(layer)
    
    # 4. Validate architectural constraints
    constraints = validate_architectural_constraints(specs, context_kit)
    
    # 5. Generate PRD
    prd = generate_prd_document(specs, constraints)
    
    # 6. Log evidence
    log_evidence("phase1", prd, specs)
    
    return {
        "prd": prd,
        "specifications": specs,
        "evidence": get_evidence("phase1")
    }
```

### Human Validation
- User confirms business goal
- User validates technical approach
- User approves PRD completeness
- Stakeholders sign off on requirements

## Error Handling

### Common Issues
- **Unclear requirements**: Ask clarifying questions
- **Architecture conflicts**: Propose alternatives
- **Scope creep**: Enforce out-of-scope boundaries

### Recovery Actions
- Re-interview user if requirements unclear
- Re-analyze architecture if conflicts found
- Regenerate PRD if significant changes needed

## Automation Integration
- Capture the approved project slug and service catalog so they can be fed into the Phase 2 wrappers (`Phase2DesignWrappers`).
- Record any domain terminology in the phase notes; wrappers can pass these values through `parameters` metadata when invoking
  workflow1 scripts.

## Evidence Templates
- Reference [workflow1 evidence index](../templates/workflow1_evidence/index.json) for upcoming design and contract templates.
- Ensure the evidence manifest is seeded with `automation_context` metadata describing the PRD review team.

## Operator Instructions
- Archive signed-off PRD artifacts and update the manifest to include `automation` metadata pointing at manual processes.
- Confirm stakeholder approvals are logged so validation gates in later phases can reference them.
