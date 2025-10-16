# Cognitive Phase Architecture (CPA) - The 7 Universal Components

## Overview

The Cognitive Phase Architecture (CPA) is the foundational pattern that makes meta-instructions workflow-agnostic and transferable. It consists of 7 universal components that map to human cognitive processes and can be applied to any multi-step reasoning workflow.

## The 7 Universal Components

### 1. Role Assignment Layer
**Purpose:** Sets AI's cognitive identity and boundaries

```markdown
## AI ROLE
You are a **[Persona]**. [Mission statement].
**[Directive Strength] [Constraint]**
```

**Transferability:** Any workflow phase can define a persona with specific constraints
**Examples:**
- Product Manager (PRD creation)
- Security Auditor (Security assessment)
- Data Migration Specialist (Data migration)
- Performance Engineer (Performance optimization)

---

### 2. Prerequisite Context Layer
**Purpose:** Ensures AI loads architectural/domain knowledge first

```markdown
### [Mandatory Section Title]
**BEFORE [ACTION]**, you MUST [context requirement].
```

**Transferability:** Any workflow needing "discover before decide" pattern
**Examples:**
- "BEFORE ANY INTERROGATION, you MUST familiarize yourself with the project's overall architecture"
- "BEFORE ANY AUDIT, you MUST analyze the application's security architecture"
- "BEFORE ANY MIGRATION PLANNING, you MUST familiarize yourself with the source and target data architectures"

---

### 3. Cognitive Phase Structure
**Purpose:** Maps reasoning flow with checkpoints

```markdown
## PHASE [N]: [Phase Name]
**Goal:** [Clear objective]

### [N.1] Sub-phase
**[Directive]** [Action]

### [N.2] Decision Branch
Based on [condition], proceed to [branch]

### [N.3] Validation Gate
**[Directive]** "Does [state] seem correct?"
```

**Transferability:** Any multi-step cognitive process (analysis → decision → validation)
**Examples:**
- Analysis → Specification → Architecture → Synthesis (PRD)
- Threat Mapping → Scanning → Remediation (Security)
- Planning → Backup → Execution (Migration)

---

### 4. Decision Matrix Layer
**Purpose:** Provides AI with architectural decision heuristics

```markdown
## [DECISION FRAMEWORK NAME]

| **Need Type** | **Implementation Target** | **Key Constraints** | **Communication Patterns** | **Guiding Principle** |
|---|---|---|---|---|
| [Type 1] | [Target 1] | [Constraints] | [Patterns] | [Principle] |
```

**Transferability:** Any workflow requiring contextual routing
**Examples:**
- Architectural Decision Matrix (UI vs API vs Data)
- Security Assessment Matrix (Auth vs Data vs Input vs Infrastructure)
- Migration Strategy Matrix (Schema vs Platform vs Transform vs Volume)

---

### 5. Announcement Protocol Layer
**Purpose:** Forces AI to surface reasoning and seek human validation

```markdown
### [Checkpoint Name]
Based on [analysis], **ANNOUNCE** the [detected state]:

```
[Formatted Block with Emojis/Structure]
```

### [Validation]
**[Directive]** "Does this [result] seem correct?"
```

**Transferability:** Any workflow requiring human-in-the-loop checkpoints
**Examples:**
- "DETECTED LAYER: Frontend App | Backend Service | Central API"
- "DETECTED THREAT SURFACE: Public-Facing | Internal | Hybrid"
- "DETECTED MIGRATION STRATEGY: Schema Evolution | Platform Migration"

---

### 6. Automation Integration Layer
**Purpose:** Binds automation scripts to reasoning checkpoints

```markdown
## Phase [N.5]: Automation Enhancement - [Feature Name]

1. **`[MUST]` Execute [Script Name]:**
   ```bash
   python scripts/script_name.py --param value
   ```
   **Action:** [Purpose]

2. **`[MUST]` Announce [Result]:**
   ```
   [AUTOMATION] [Result message]
   ```

3. **`[MUST]` Gate: [Gate Name]**
   **Pass Criteria:** [Threshold]
   **Fail Action:** [Recovery]
```

**Transferability:** Any workflow with automation hooks
**Examples:**
- PRD Asset Generation (`generate_prd_assets.py`)
- Security Scan Execution (`run_sast_scan.py`)
- Migration Validation (`validate_migration_gate.py`)

---

### 7. Deliverable Template Layer
**Purpose:** Provides concrete output format

```markdown
## FINAL [DELIVERABLE] TEMPLATE

```markdown
# [Template Structure]

## 1. [Section]
- **[Field]:** [Description]
```
```

**Transferability:** Any workflow producing structured artifacts
**Examples:**
- PRD Template (Business Goal, Functional Specs, Technical Specs)
- Security Audit Template (Threat Assessment, Findings, Remediation)
- Migration Plan Template (Data Mapping, Validation, Rollback)

---

## The Universal Formula

```
Meta-Instruction = 
  Role(Persona, Mission, Constraints) 
  + Prerequisites(Context, Knowledge)
  + CognitivePhases(
      Phases[N](
        Goal,
        SubPhases[M](Action, Directive),
        DecisionBranches(Condition → Path),
        ValidationGates(State → Human Approval)
      )
    )
  + AutomationHooks(
      Scripts(Trigger, Execution, Evidence),
      QualityGates(Criteria, Threshold, Recovery)
    )
  + AnnouncementProtocol(
      Checkpoints(Reasoning → Announcement → Validation)
    )
  + DeliverableTemplate(Structure, Fields, Examples)
```

## Why This Works Across Workflows

### 1. **Role Assignment** → Cognitive Identity
- Sets the AI's mental model and expertise level
- Defines boundaries and constraints
- Establishes the AI's "persona" for the task

### 2. **Prerequisites** → Context Loading
- Ensures "Why Before How" principle
- Loads necessary domain knowledge
- Prevents premature decision-making

### 3. **Phases** → Reasoning Flow
- Maps human cognitive processes
- Provides structured thinking patterns
- Creates logical progression through complexity

### 4. **Decision Matrices** → Architectural Heuristics
- Provides routing logic for different scenarios
- Encodes domain-specific knowledge
- Enables contextual decision-making

### 5. **Announcements** → Human-in-the-Loop Validation
- Forces reasoning transparency
- Creates validation checkpoints
- Ensures human oversight

### 6. **Automation Hooks** → Script Binding to Checkpoints
- Connects automation to reasoning
- Provides evidence capture
- Enables quality gates

### 7. **Templates** → Concrete Output Formats
- Provides structured deliverables
- Ensures completeness
- Enables immediate implementation

## Cognitive Architecture Benefits

### **Predictable Reasoning**
- AI follows structured cognitive phases
- Human can anticipate AI's thinking process
- Reduces unpredictability in AI behavior

### **Human-AI Collaboration**
- Built-in validation checkpoints
- Transparent reasoning process
- Human remains in control of key decisions

### **Quality Assurance**
- Automation hooks provide evidence
- Quality gates ensure standards
- Templates ensure completeness

### **Workflow Transferability**
- Same cognitive pattern across domains
- Reusable automation patterns
- Consistent human interaction model

## Application Guidelines

### **When to Use CPA**
- Multi-step cognitive processes
- Workflows requiring human validation
- Processes needing automation integration
- Tasks requiring structured deliverables

### **How to Adapt CPA**
1. **Define the Role** - What persona does AI embody?
2. **Map the Phases** - What is the reasoning flow?
3. **Create Decision Matrices** - What are the routing heuristics?
4. **Identify Human Gates** - Where does AI need validation?
5. **Bind Automation** - Which scripts serve which checkpoints?
6. **Define Templates** - What is the deliverable format?

### **Quality Indicators**
- [ ] AI role is clearly defined with boundaries
- [ ] Prerequisites ensure proper context loading
- [ ] Phases map to logical reasoning flow
- [ ] Decision matrices provide routing heuristics
- [ ] Announcements create validation checkpoints
- [ ] Automation hooks bind scripts to checkpoints
- [ ] Templates provide concrete output formats

---

*The Cognitive Phase Architecture provides the universal foundation for creating workflow-agnostic meta-instructions that maintain human oversight, automation integration, and structured reasoning across any domain.*
