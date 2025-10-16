# Awareness Protocol Template

## Overview

This template provides the universal structure for creating "Awareness Protocol" meta-instructions. These are cross-cutting concerns that trigger at specific checkpoints during development workflows (e.g., documentation updates, security checks, performance validation).

Unlike the Cognitive Phase Architecture (CPA) which guides multi-step reasoning workflows, Awareness Protocols are **reactive triggers** that ensure quality standards are maintained throughout the development process.

---

## Universal Template Structure

```markdown
# Master Rule: [Awareness Type]-Aware Development

## 1. AI Persona

When this rule is active, you are a **[Specific Role]**. Your primary responsibility is to ensure that [specific quality concern] remains [desired state], understanding that [consequence of neglect].

## 2. Core Principle

[Brief statement of the invariant that must be maintained]. To maintain efficiency, [awareness checks] must occur at logical milestones. After [trigger condition], you **MUST** ensure [quality standard is met]. This maintains the [quality attribute] of the repository, which is critical for both human and AI understanding.

## 3. Protocol for [Awareness Type]-Aware Development

### Step 1: Pre-[Action] Analysis (Context Gathering)
- **[GUIDELINE]** Before [implementing/modifying] a feature that [condition], identify [relevant context].
- **[GUIDELINE]** Read the relevant [artifacts] to understand [established standard].
- **[GUIDELINE]** Announce the standard you have identified.
    > *"I have analyzed [context]. [Quality standard identified]. I will follow this standard."*

### Step 1bis: [Specialized Setup] (For Complex [Scenarios])
- **[STRICT]** When [complex condition occurs], you **MUST** first [preparatory action].
- **[STRICT]** This [artifact] **MUST** be created **before** starting the implementation. It serves as [purpose].
- **[STRICT]** The [artifact] **MUST** include, at a minimum:
    -   [Required element 1]
    -   [Required element 2]
    -   [Required element 3]
- **[GUIDELINE]** Announce the creation of this [artifact].
    > *"To ensure [benefit], I will first create [artifact] to [purpose]. This will be our reference for this task."*

### [Optimization Protocol Name]
- **[STRICT]** To optimize performance and reduce unnecessary costs, you **MUST NOT** re-[action] if [condition for skip].
- **[STRICT]** You **MUST** only re-[action] if you have a specific reason to believe [trigger condition].

### Step 2: Post-[Action] Review (Syncing)
**[STRICT]** This protocol **MUST** be triggered at [specific checkpoint], such as [milestone example], and typically just before [final checkpoint]. It should not be run for every minor [sub-action].

1.  **[STRICT]** **Identify the Target [Artifact]:**
    *   After [completion condition], identify the nearest [artifact type] in [location] relative to [modified elements].
    *   *Example: If you modified [path example], the relevant artifact is likely [path example].*

2.  **[STRICT]** **Perform a Contextual Audit:**
    *   Read the contents of the identified [artifact].
    *   Compare the [artifact] against the changes you just made. Ask yourself these questions:
        *   Does my change [potential divergence 1]?
        *   Does my change [potential divergence 2]?
        *   Does my change [potential divergence 3]?
        *   Does my change [potential divergence 4]?

3.  **[SPECIAL CASE MANDATORY]** **Special Protocol for [Critical Scenarios]:**
    *   **[STRICT]** Any modification related to [critical domain] **MUST** include immediate [quality action].
    *   **[STRICT]** [Critical domain] updates are **NON-NEGOTIABLE** and must include:
        *   [Required update 1]
        *   [Required update 2]
        *   [Required update 3]
        *   [Required update 4]
    *   **[STRICT]** [Critical domain] tasks in TodoWrite **MUST** automatically generate corresponding [quality action] tasks.

4.  **[STRICT]** **Propose an Update if Necessary:**
    *   If you find any divergence, you **MUST** immediately propose an update to the [artifact].
    *   **Action:** Following the **Tool Usage Protocol**, use the appropriate tool to provide a clear `diff` of the proposed changes.
    *   **Communication:** Announce your action clearly to the user.
        > *"To maintain [quality attribute], I have detected that my recent changes affect [scope]. I will now update the [artifact] to reflect this."*

## 4. Example Scenario

**[GUIDELINE]** This section provides a practical illustration of the protocol in action.

**User Request:** "[Example user request]"

**AI Actions:**
1.  The AI modifies [file path] to [implement change].
2.  **(Rule Activation)** The AI identifies [artifact path] as the relevant [artifact type].
3.  The AI reads the [artifact] and sees that [quality gap detected].
4.  The AI uses [tool type] to [corrective action] in [artifact].
5.  The AI communicates: *"I have implemented [change]. To maintain [quality attribute], I will now update [artifact] before finalizing the task."*

## 5. [Critical Scenario] Implementation Example

**[GUIDELINE]** This section demonstrates the mandatory [critical scenario] protocol.

**User Request:** "[Example critical request]"

**AI Actions:**
1.  The AI modifies [file path] to [implement critical change].
2.  **(Critical Rule Activation)** The AI automatically creates two TodoWrite tasks:
    *   "[Implementation task]"
    *   "[Quality assurance task]"
3.  The AI identifies [artifact 1] and [artifact 2] as relevant [artifact type].
4.  **(MANDATORY)** The AI updates both [artifacts] to document:
    *   [Critical element 1]
    *   [Critical element 2]
    *   [Critical element 3]
5.  The AI communicates: *"I have implemented [critical change]. Per [critical domain] requirements, I will now update both [artifacts] to reflect this critical enhancement."*
```

---

## Pattern Components

### 1. **AI Persona**
Defines the AI's specialized role and responsibility for this awareness protocol.

**Customization:**
- Replace `[Specific Role]` with domain expert (Technical Writer, Security Engineer, Performance Analyst)
- Replace `[specific quality concern]` with what needs monitoring
- Replace `[desired state]` with target quality level
- Replace `[consequence of neglect]` with risk of not maintaining standard

### 2. **Core Principle**
States the invariant that must be maintained and when checks occur.

**Customization:**
- Replace `[invariant]` with the fundamental rule
- Replace `[trigger condition]` with when checks happen
- Replace `[quality standard]` with what must be verified
- Replace `[quality attribute]` with the benefit maintained

### 3. **Protocol Steps**

#### **Step 1: Pre-Action Analysis**
Context gathering before making changes.

**Customization:**
- Replace `[Action]` with the development action (Implementation, Modification, Deployment)
- Replace `[condition]` with when this applies
- Replace `[relevant context]` with what needs to be checked
- Replace `[established standard]` with existing patterns to follow

#### **Step 1bis: Specialized Setup**
Optional preparatory work for complex scenarios.

**Customization:**
- Replace `[complex condition]` with when this applies
- Replace `[preparatory action]` with what must be done first
- Replace `[artifact]` with what gets created
- Replace `[purpose]` with why it's needed

#### **Step 2: Post-Action Review**
Verification after changes are complete.

**Customization:**
- Replace `[checkpoint]` with when this triggers
- Replace `[milestone example]` with concrete trigger point
- Replace `[artifact type]` with what gets reviewed
- Replace `[potential divergence N]` with specific quality checks

#### **Special Protocol for Critical Scenarios**
Mandatory actions for high-risk domains.

**Customization:**
- Replace `[critical domain]` with the sensitive area (Security, Compliance, Safety)
- Replace `[quality action]` with required response
- Replace `[Required update N]` with specific mandatory updates

### 4. **Example Scenarios**
Concrete illustrations of the protocol in action.

**Customization:**
- Replace examples with domain-specific scenarios
- Show both normal and critical case handling
- Demonstrate the complete workflow from trigger to resolution

---

## Usage Instructions

### Step 1: Identify Your Awareness Domain
Determine what cross-cutting concern needs monitoring:
- **Documentation** - Keep docs synced with code
- **Security** - Maintain security standards
- **Performance** - Track performance implications
- **Testing** - Ensure test coverage
- **Compliance** - Maintain regulatory compliance
- **Accessibility** - Ensure accessibility standards

### Step 2: Define Trigger Points
Identify when awareness checks should occur:
- After completing major tasks
- Before commits/PRs
- When modifying critical paths
- At specific milestones

### Step 3: Specify Quality Checks
Define what gets validated:
- Artifact consistency checks
- Standard compliance verification
- Completeness validation
- Impact assessment

### Step 4: Create Critical Scenario Protocols
For high-risk domains, define mandatory actions:
- Non-negotiable updates
- Automatic task generation
- Comprehensive documentation
- Evidence collection

### Step 5: Test the Protocol
Validate the awareness protocol:
- Trigger it manually
- Verify it catches divergence
- Ensure updates are appropriate
- Confirm it doesn't over-trigger

---

## Key Differences from Cognitive Phase Architecture (CPA)

| Aspect | CPA (Workflow Protocol) | Awareness Protocol |
|--------|------------------------|-------------------|
| **Purpose** | Guide multi-step reasoning | Monitor cross-cutting concerns |
| **Activation** | User initiates workflow | Triggered at checkpoints |
| **Structure** | Sequential phases | Reactive checks |
| **Human Interaction** | Continuous validation | Report deviations only |
| **Examples** | PRD creation, Security audit | Documentation sync, Security awareness |

---

## Quality Checklist

Before deploying an awareness protocol, verify:

- [ ] **Clear Persona** - AI role is well-defined
- [ ] **Explicit Triggers** - Activation conditions are specific
- [ ] **Measurable Checks** - Quality criteria are concrete
- [ ] **Appropriate Frequency** - Not too frequent or too rare
- [ ] **Actionable Outputs** - AI knows what to do when triggered
- [ ] **Critical Path Handling** - High-risk scenarios have mandatory protocols
- [ ] **Performance Optimized** - Doesn't re-check unnecessarily
- [ ] **Evidence Collection** - Tracks what was checked and updated

---

*This template provides the universal structure for creating Awareness Protocol meta-instructions that maintain quality standards throughout the development process through reactive, checkpoint-based validation.*
