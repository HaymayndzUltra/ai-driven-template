# 🤖 AGENTS.md - Master Rules Interpretation Guide

## Purpose
This document explains how AI agents (including GPT-5-Codex) should interpret and apply the `.mdc` (Markdown with Cursor) format used in master rules and common rules.

## Understanding .mdc Format

### What is .mdc?
`.mdc` files are **Markdown with Cursor** files that contain:
1. **YAML Frontmatter** - Metadata and configuration
2. **Markdown Content** - Human-readable instructions
3. **Cursor-Specific Directives** - AI agent behavior instructions

### File Structure
```yaml
---
description: "TAGS: [tag1,tag2] | TRIGGERS: keyword1,keyword2 | SCOPE: scope | DESCRIPTION: One-sentence summary"
alwaysApply: true/false
---

# Rule Title

## Rule Content
Detailed instructions for AI agents...
```

## Frontmatter Interpretation

### Description Field Structure
The `description` field follows this **exact format**:
```
TAGS: [tag1,tag2,tag3] | TRIGGERS: keyword1,keyword2 | SCOPE: scope | DESCRIPTION: One-sentence summary
```

**Components**:
- **TAGS**: Categories for rule classification
- **TRIGGERS**: Keywords that activate this rule
- **SCOPE**: Where this rule applies (global, specific domain, etc.)
- **DESCRIPTION**: Brief summary of rule purpose

### alwaysApply Property
- **`true`**: Rule is **mandatory** and must be loaded in every session
- **`false`**: Rule is **optional** and loaded based on relevance

## Rule Loading Logic

### Priority System
When loading rules, AI agents must follow this priority order:

1. **Priority 1: Absolute Directives (Kernel)**
   - Rules with `alwaysApply: true`
   - Core system rules (e.g., collaboration guidelines)
   - **CRITICAL**: Must be loaded first

2. **Priority 2: Scope Matching**
   - Rules whose `SCOPE` matches current context
   - Perfect scope matches get highest relevance

3. **Priority 3: Keyword Matching**
   - Rules whose `TRIGGERS` contain keywords from user request
   - Partial matches are acceptable

4. **Priority 4: Concept Matching**
   - Rules whose `TAGS` align with task intent
   - Used as general guidance

### Loading Process
```
1. Scan .cursor/rules/ directory
2. Read YAML frontmatter of each .mdc file
3. Apply priority system to select relevant rules
4. Load selected rules into context
5. Announce loaded rules to user
```

## Rule Application Logic

### When Rules Apply
Rules are applied based on:

1. **Context Detection**
   - Current working directory
   - File types being worked on
   - Technology stack detected
   - User request keywords

2. **Trigger Matching**
   - Keywords in user request
   - File patterns
   - Command patterns
   - Context changes

3. **Scope Validation**
   - Global rules: Always applicable
   - Domain rules: Only in specific contexts
   - Project rules: Only in project scope

### Rule Execution
When a rule is triggered:

1. **Parse Instructions**: Extract actionable steps
2. **Validate Context**: Ensure rule applies to current situation
3. **Execute Steps**: Follow rule instructions precisely
4. **Collect Evidence**: Document compliance
5. **Report Results**: Provide feedback to user

## Master Rules Specific Logic

### Core Master Rules (alwaysApply: true)
These rules form the **kernel** and must always be loaded:

1. **Context Discovery Protocol** - System initialization
2. **AI Collaboration Guidelines** - Human-AI interaction
3. **Code Quality Checklist** - Development standards
4. **Code Modification Safety** - Change management
5. **Documentation Guidelines** - Documentation standards

### Rule Dependencies
Some rules depend on others:
- **Context Discovery** → **Collaboration Guidelines**
- **Code Quality** → **Safety Protocol**
- **Documentation** → **Quality Checklist**

### Conflict Resolution
When rules conflict:
1. **Higher Priority Wins**: Kernel rules override others
2. **More Specific Wins**: Specific rules override general
3. **User Override**: User can explicitly override rules
4. **Context Override**: Context-specific rules override global

## Common Rules Logic

### Loading Criteria
Common rules are loaded when:
- **Scope Match**: Rule scope matches current context
- **Trigger Match**: Keywords in user request
- **Technology Match**: Rule applies to current tech stack
- **Domain Match**: Rule applies to current domain

### Application Patterns
Common rules follow these patterns:
- **UI Rules**: Applied when working on frontend
- **Backend Rules**: Applied when working on APIs
- **Security Rules**: Applied when security-sensitive code
- **Performance Rules**: Applied when performance-critical code

## Evidence Collection

### Required Evidence
Each rule application must collect:
- **Rule ID**: Which rule was applied
- **Context**: Why rule was triggered
- **Actions**: What was done
- **Results**: Outcome of rule application
- **Validation**: Evidence of compliance

### Evidence Format
```json
{
  "ruleId": "rule-name",
  "timestamp": "2024-01-01T00:00:00Z",
  "context": "description of context",
  "actions": ["action1", "action2"],
  "results": "outcome description",
  "evidence": "proof of compliance"
}
```

## Error Handling

### Malformed Rules
When a rule has malformed frontmatter:
1. **Skip Rule**: Don't load malformed rules
2. **Log Error**: Record the issue
3. **Continue**: Proceed with other rules
4. **Report**: Inform user of skipped rules

### Missing Dependencies
When required rules are missing:
1. **Halt Execution**: Stop if kernel rules missing
2. **Report Critical Error**: Inform user immediately
3. **Suggest Fix**: Provide guidance on fixing issue

## Integration with Cursor

### Cursor-Specific Features
The `.mdc` format leverages Cursor's capabilities:
- **Context Awareness**: Rules can access @codebase, @recent-changes
- **File Operations**: Rules can read/write files
- **Command Execution**: Rules can run terminal commands
- **AI Integration**: Rules can trigger AI workflows

### Cursor Commands Integration
Rules can integrate with Cursor commands:
- **@apply**: Apply specific rules
- **@review**: Trigger rule-based reviews
- **@generate**: Use rules for code generation
- **@validate**: Use rules for validation

## Best Practices for AI Agents

### Rule Interpretation
1. **Read Frontmatter First**: Always parse YAML first
2. **Validate Format**: Ensure proper structure
3. **Check Dependencies**: Verify required rules exist
4. **Apply Priority**: Follow priority system strictly

### Rule Execution
1. **Follow Instructions**: Execute steps precisely
2. **Collect Evidence**: Document all actions
3. **Validate Results**: Ensure compliance
4. **Report Status**: Provide clear feedback

### Rule Management
1. **Load Efficiently**: Only load relevant rules
2. **Cache Results**: Store rule analysis
3. **Update Context**: Refresh when context changes
4. **Handle Errors**: Graceful error handling

## Troubleshooting

### Common Issues
1. **Rules Not Loading**: Check file paths and format
2. **Conflicting Rules**: Apply priority system
3. **Missing Context**: Ensure proper context detection
4. **Malformed Rules**: Validate YAML syntax

### Debug Commands
```bash
# List all rules
find .cursor/rules -name "*.mdc" -type f

# Validate rule format
python scripts/validate_rules.py

# Test rule loading
python scripts/test_rule_loading.py
```

## Conclusion

The `.mdc` format provides a powerful way to define AI agent behavior through structured rules. By understanding the frontmatter format, priority system, and application logic, AI agents can effectively interpret and apply these rules to provide consistent, high-quality assistance.

**Key Takeaways**:
- **Frontmatter is Critical**: YAML metadata drives rule behavior
- **Priority Matters**: Kernel rules must be loaded first
- **Context is Key**: Rules apply based on current context
- **Evidence Required**: Always document rule application
- **Error Handling**: Graceful handling of malformed rules

This system ensures that AI agents can provide consistent, rule-based assistance while maintaining flexibility and adaptability to different contexts and requirements.
