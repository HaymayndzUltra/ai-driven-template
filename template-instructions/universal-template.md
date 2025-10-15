# Universal Meta-Instruction Template

## Template Structure

```markdown
# PROTOCOL: [Name] ([Compliance Domain])

## AI ROLE
You are a **[Specific Persona]**. [Persona's objective in this phase]. This [protocol/system] must [core outcome requirement].

**[Directive Strength] [Boundary Constraint]**

### [Mandatory Context Check - If Applicable]
**BEFORE [MAIN ACTION]**, you MUST [context gathering requirement].

---

## [DECISION FRAMEWORK NAME] (EXAMPLE)

This is a generic template. You should adapt your questions to help the user define a similar matrix for their own project.

| **Need Type** | **Likely Implementation Target** | **Key Constraints** | **Communication Patterns** | **Guiding Principle** |
|---|---|---|---|---|
| **[Type 1]** | **[Target 1]** | **[Constraints 1]** | **[Patterns 1]** | **[Principle 1]** |
| **[Type 2]** | **[Target 2]** | **[Constraints 2]** | **[Patterns 2]** | **[Principle 2]** |

---

## PHASE 1: [Phase Name]
**Goal:** [Clear cognitive objective]

### 1.1 Initial Qualification
**Ask this crucial first question:**
1. **"[Primary decision question]?"**

Based on the answer, proceed to the relevant section below.

### 1.2 Path A: [Branch A Name]
Ask these questions and **AWAIT ANSWERS** before proceeding:

1. **"[Question 1]"**
2. **"[Question 2]"**
3. **"[Question 3]"**

Proceed to **Section 1.4: Announcing the Detected [State]**.

### 1.3 Path B: [Branch B Name]
Ask these questions and **AWAIT ANSWERS** before proceeding:

1. **"[Question 1]"**
2. **"[Question 2]"**
3. **"[Question 3]"**

### 1.4 Announcing the Detected [State]
Based on the answers and any architectural context you have, **ANNOUNCE** the detected [state]:

```
🎯 **DETECTED [STATE]**: [Option 1 | Option 2 | Option 3]

📋 **APPLICABLE CONSTRAINTS** (Based on our discussion):
-   [Constraint Type]: [e.g., specific constraint]
-   [Technology]: [e.g., specific tech stack]
-   [Architecture]: [e.g., architectural pattern]
```

### 1.5 Validating the Placement
**[Directive]** "Does this detected [state] seem correct to you? If not, please clarify."

---

## PHASE 2: [Specification Phase Name]

### 2A. For [Category A]

1. **"[Question 1]"**
2. **"[Question 2]"**
3. **"[Question 3]"**
4. **"[Question 4]"**
5. **"[Question 5]"**

### 2B. For [Category B]

1. **"[Question 1]"**
2. **"[Question 2]"**
3. **"[Question 3]"**
4. **"[Question 4]"**
5. **"[Question 5]"**

*(Adapt questions for other categories based on the matrix)*

---

## PHASE 3: [Constraint Validation Phase]

Verify that the proposed [interactions/approaches] respect the project's known [rules/patterns].

**✅ Example of Allowed [Flows/Approaches]:**
-   [Allowed Pattern 1]
-   [Allowed Pattern 2]

**❌ Example of Prohibited [Flows/Approaches]:**
-   [Prohibited Pattern 1]

---

## PHASE 4: SYNTHESIS AND GENERATION

1. **Summarize the [Architecture/Approach]:**
    ```
    🏗️ **[SUMMARY TYPE] SUMMARY**

    📍 **Primary Component**: [Detected State]
    🔗 **[Connections/Patterns]**: [Validated Flows]
    💡 **Guiding Principle**: [Principle]. The proposed solution is the simplest and most direct path to meeting the requirements.
    ```
2. **Final Validation:**
    "Is this summary correct? Shall I proceed with generating the full [deliverable]?"

### Phase 4.5: Automation Enhancement - [Feature Name] Generation

1. **`[MUST]` Execute [Feature Name] Asset Generation:**
   ```bash
   python scripts/generate_[feature]_assets.py --[feature] [feature-name].md --output .artifacts/[feature]-assets/
   ```
   *   **Action:** Generate [specific artifacts] from [deliverable].
   *   **Action:** Create implementation-ready artifacts for [next phase].

2. **`[MUST]` Announce Asset Generation:**
   ```
   [AUTOMATION] [Feature Name] Assets Generated: {asset_count} artifacts created
   ```
   *   **Action:** Display generated artifacts and their purposes.

3. **`[MUST]` Execute [Feature Name] Validation Gate:**
   ```bash
   python scripts/validate_[feature]_gate.py --[feature] [feature-name].md --output .artifacts/[feature]-validation.json
   ```
   *   **Action:** Validate [deliverable] completeness, measurability, and traceability.
   *   **Action:** Check [specific constraints] and [communication patterns].

4. **`[MUST]` Announce Validation Results:**
   ```
   [AUTOMATION] [Feature Name] Validation: {status} - {score}/100
   ```
   *   **Pass Criteria:** Validation score ≥ [threshold]
   *   **Fail Action:** Address validation issues before proceeding

5. **`[MUST]` Gate: [Feature Name] Automation Complete**
   *   **Validation:** All automation scripts executed successfully
   *   **Pass Criteria:** Assets generated, [deliverable] validation ≥ [threshold]
   *   **Fail Action:** Address automation failures before proceeding
   *   **[STRICT]** Do not release the [deliverable] unless every validation artifact is archived in `.artifacts/`.

---

## FINAL [DELIVERABLE] TEMPLATE (EXAMPLE)

```markdown
# [Deliverable Name]: [Feature Name]

## 1. Overview
- **Business Goal:** [Description of the need and problem solved]
- **Detected Architecture:**
  - **Primary Component:** `[Detected State]`

## 2. Functional Specifications
- **[Specification Type]:** [For UI/Services/etc.]
- **[Flow Diagram]:**
  ```
  [A simple diagram showing the interaction between components]
  ```

## 3. Technical Specifications
- **[Technical Detail Type]:** [Details of specific technical aspects]
- **[Security/Authentication/Other]:** [Specific model for the chosen layer]

## 4. Out of Scope
- [What this feature will NOT do]
```
```

## Usage Instructions

### Step 1: Customize the Template
1. Replace `[Name]` with your protocol name
2. Replace `[Specific Persona]` with the AI's role
3. Replace `[Compliance Domain]` with relevant domain
4. Replace `[Directive Strength]` with `[STRICT]`, `[GUIDELINE]`, or `[MUST]`
5. Replace `[Boundary Constraint]` with specific limitations

### Step 2: Define Decision Framework
1. Replace `[DECISION FRAMEWORK NAME]` with your framework name
2. Customize the matrix columns for your domain
3. Add relevant rows for different types/patterns

### Step 3: Map Cognitive Phases
1. Replace `[Phase Name]` with your phase names
2. Customize questions for your domain
3. Define decision branches and validation gates

### Step 4: Configure Automation
1. Replace `[Feature Name]` with your automation feature
2. Update script names and parameters
3. Set appropriate validation thresholds

### Step 5: Define Deliverable Template
1. Replace `[Deliverable Name]` with your output type
2. Customize sections for your domain
3. Add relevant technical specifications

## Quality Checklist

Before using this template, ensure:

- [ ] **Role clarity** - AI knows its persona and boundaries
- [ ] **Context prerequisites** - AI loads necessary knowledge first
- [ ] **Cognitive phases** - Reasoning flows through clear checkpoints
- [ ] **Decision frameworks** - AI has heuristics for routing
- [ ] **Human gates** - AI announces reasoning and seeks validation
- [ ] **Automation hooks** - Scripts are bound to checkpoints with gates
- [ ] **Deliverable templates** - Output format is concrete and structured
- [ ] **Directive strength** - `[STRICT]`, `[GUIDELINE]`, `[MUST]` are explicit
- [ ] **Failure recovery** - Each gate has a "Fail Action" path
- [ ] **Evidence capture** - Artifacts are stored for traceability

## Examples

See the `examples/` folder for:
- Security Audit Workflow
- Data Migration Workflow
- Performance Optimization Workflow
- Code Refactoring Protocol
- Architecture Review Process

---

*This template extracts the universal cognitive architecture from successful workflow protocols, making it applicable to any multi-step cognitive process requiring AI guidance with human oversight.*
