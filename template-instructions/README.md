# Template Instructions: Universal Meta-Instruction Pattern

## Overview

This folder contains the extracted meta-instruction pattern that makes any workflow protocol **workflow-agnostic and transferable**. The pattern is based on **Cognitive Phase Architecture (CPA)** and can be applied to any multi-step cognitive process requiring AI guidance with human oversight.

## Core Pattern: Cognitive Phase Architecture (CPA)

The universal structure follows this formula:

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

## Files in this Folder

- `universal-template.md` - The complete universal template structure (Workflow Protocol)
- `awareness-protocol-template.md` - Template for cross-cutting concern protocols (Awareness Protocol)
- `retrospective-protocol-template.md` - Template for post-completion analysis workflows (Retrospective Protocol)
- `cognitive-phase-architecture.md` - Detailed explanation of the 7 universal components
- `quality-checklist.md` - Checklist for creating transferable meta-instructions

## Quick Start

### For Workflow Protocols (Multi-step Reasoning):
1. **Read** `universal-template.md` to understand the structure
2. **Study** `cognitive-phase-architecture.md` to understand the components
3. **Apply** the pattern to your specific workflow (PRD, Security Audit, etc.)

### For Awareness Protocols (Cross-cutting Concerns):
1. **Read** `awareness-protocol-template.md` to understand the structure
2. **Identify** your cross-cutting concern (Documentation, Security, Performance, etc.)
3. **Apply** the pattern to create checkpoint-based validation

### For Retrospective Protocols (Post-completion Analysis):
1. **Read** `retrospective-protocol-template.md` to understand the structure
2. **Identify** your retrospective domain (Implementation, Security, Performance, etc.)
3. **Apply** the pattern to create evidence-based learning workflows

### General:
- **Use** `quality-checklist.md` to validate your meta-instruction

## Key Benefits

- **Workflow-Agnostic**: Works for PRD, Security Audit, Data Migration, etc.
- **Human-in-the-Loop**: Built-in validation checkpoints
- **Automation-Ready**: Scripts bind to reasoning checkpoints
- **Evidence-Based**: Captures artifacts for traceability
- **Structured Output**: Concrete deliverable templates

## Usage

To create a new workflow protocol:

1. **Define the Role** - What persona does AI embody?
2. **Map the Cognitive Phases** - What is the reasoning flow?
3. **Create Decision Matrices** - What are the routing heuristics?
4. **Identify Human Gates** - Where does AI need validation?
5. **Bind Automation** - Which scripts serve which checkpoints?
6. **Define the Template** - What is the deliverable format?

## Pattern Types

### Workflow Protocols (CPA - Cognitive Phase Architecture)
Multi-step reasoning workflows with sequential phases:
- PRD Creation
- Security Audit
- Data Migration
- Code Refactoring
- Architecture Review

### Awareness Protocols (Cross-cutting Concerns)
Checkpoint-based validation that triggers reactively:
- Documentation-Aware Development
- Security-Aware Development
- Performance-Aware Development
- Testing-Aware Development
- Compliance-Aware Development

### Retrospective Protocols (Post-completion Analysis)
Evidence-based learning workflows that extract improvements:
- Implementation Retrospective
- Security Retrospective
- Performance Retrospective
- Deployment Retrospective
- Quality Retrospective
- Process Retrospective

---

*This pattern extracts the universal cognitive architecture from the PRD protocol, making it applicable to any workflow requiring structured AI guidance with human oversight.*
