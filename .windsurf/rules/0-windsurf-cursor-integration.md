---
description: >
  TAGS: [global,integration,cursor,compatibility,rules,system] |
  TRIGGERS: start,init,setup,rules,cursor,windsurf,discover,load |
  SCOPE: global |
  DESCRIPTION: Instructs Windsurf Cascade to discover, read, and strictly follow 
  all rules defined in the .cursor/rules/ directory structure, ensuring compatibility 
  and adherence to the Cursor rule system.
alwaysApply: true
---
# Windsurf-Cursor Rules Integration Protocol

## 1. Primary Directive

**[STRICT]** This Windsurf workspace operates under a comprehensive rule system 
located in `.cursor/rules/`. You MUST discover, load, and strictly follow ALL 
rules in that directory structure before responding to any user request.

## 2. Rule Discovery Protocol

### **[STRICT] Mandatory First Action**
Before ANY response or action, you **MUST**:

1. **Scan `.cursor/rules/` directory structure**
   - List subdirectories: `master-rules/`, `common-rules/`, `project-rules/`
   - Identify ALL `.mdc` files (Cursor's rule format)
   - Include files at root level (e.g., `elaboration-specialist.mdc`)

2. **Load rules in priority order**
   - **Phase 1**: `master-rules/*.mdc` (HIGHEST PRIORITY)
   - **Phase 2**: `common-rules/*.mdc` (GLOBAL STANDARDS)
   - **Phase 3**: `project-rules/*.mdc` (CONTEXT-SPECIFIC)
   - **Phase 4**: Root-level `.mdc` files (SPECIALIZED)

3. **Parse frontmatter metadata from each `.mdc` file**
   ```yaml
   ---
   description: "TAGS: [...] | TRIGGERS: ... | SCOPE: ... | DESCRIPTION: ..."
   alwaysApply: true/false
   ---
   ```

## 3. Frontmatter Interpretation Rules

**[STRICT]** When you encounter Cursor `.mdc` frontmatter, interpret as follows:

### `alwaysApply` Field
- **`alwaysApply: true`** → ALWAYS active (Windsurf "Always On")
- **`alwaysApply: false`** → Apply based on TRIGGERS, TAGS, or SCOPE

### `description` Field Components (pipe-separated)
- **`TAGS: [...]`** → Concept categories for fuzzy matching
- **`TRIGGERS: word1,word2,...`** → Keywords that activate this rule
- **`SCOPE: global|local|specific`** → Application scope
- **`DESCRIPTION: ...`** → Human-readable purpose

### Activation Logic
```
IF alwaysApply == true:
    LOAD rule immediately
ELSE IF user request contains any TRIGGERS:
    LOAD rule
ELSE IF current context matches TAGS:
    CONSIDER loading (use judgment)
ELSE IF SCOPE matches current directory:
    LOAD rule
```

## 4. Directive Prefix System

**[STRICT]** The Cursor rule system uses directive prefixes:

- **`[STRICT]`** = Mandatory. MUST follow exactly. Failure = critical error.
- **`[GUIDELINE]`** = Strong recommendation. Can deviate with justification.
- **`[BLOCKING AND MANDATORY ACTION]`** = Execution barrier. MUST complete first.

## 5. Rule Priority Hierarchy

When multiple rules apply or conflict:

1. **Master Rules** (`.cursor/rules/master-rules/`) = HIGHEST AUTHORITY
   - Override all other rules
   - Define system-level behavior

2. **Common Rules** (`.cursor/rules/common-rules/`) = GLOBAL STANDARDS
   - Apply across project unless master rules override

3. **Project Rules** (`.cursor/rules/project-rules/`) = CONTEXT-SPECIFIC
   - Most specific but lowest priority

4. **Windsurf Rules** (`.windsurf/rules/`) = INTEGRATION LAYER
   - This meta-rule and Windsurf-specific additions ONLY
   - NEVER conflict with Cursor rules
   - Cursor rules take precedence in conflicts

## 6. Required Discovery Sequence

**[STRICT]** Follow this exact sequence on EVERY session start:

```
STEP 1: Execute discovery scan
  → find .cursor/rules -type f -name "*.mdc"
  
STEP 2: Load master-rules/ first (Priority 1)
  → Read each .mdc file
  → Parse frontmatter
  → Load content if alwaysApply: true
  
STEP 3: Analyze user request for TRIGGERS
  → Extract keywords from request
  → Match against all discovered rules
  
STEP 4: Load applicable common-rules/ (Priority 2)
  → Check TRIGGERS match
  → Check SCOPE match
  → Load if relevant
  
STEP 5: Load applicable project-rules/ (Priority 3)
  → Same matching logic
  
STEP 6: Announce loaded rules to user
  → List all active rules
  → Confirm system operational
```

## 7. Example Discovery Output

When activated, your announcement should look like:

```
🔍 Cursor Rules Discovery Protocol Active

📂 Master Rules (10 loaded):
  ✓ 1-master-rule-context-discovery.mdc [alwaysApply: true]
  ✓ 2-master-rule-ai-collaboration-guidelines.mdc [alwaysApply: true]
  ✓ 3-master-rule-code-quality-checklist.mdc [TRIGGERS matched]
  ... [and 7 more]

📂 Common Rules (3 loaded):
  ✓ common-rule-ui-foundation-design-system.mdc [alwaysApply: true]
  ✓ common-rule-ui-interaction-a11y-perf.mdc [SCOPE: UI]
  ✓ common-rule-ui-premium-brand-dataviz-enterprise-gated.mdc

📂 Specialized Protocols (2 loaded):
  ✓ elaboration-specialist.mdc
  ✓ meta-instruction-explain.mdc

✅ Total: 15 Cursor rules loaded and active
✅ Rule system operational. Ready to proceed.
```

## 8. Critical Rules (MUST LOAD)

**[STRICT]** These Cursor rules are MANDATORY. If missing, HALT and report error:

- `master-rules/1-master-rule-context-discovery.mdc` (The BIOS)
- `master-rules/2-master-rule-ai-collaboration-guidelines.mdc` (Core protocol)

## 9. Conflict Resolution

**[STRICT]** If Windsurf rules conflict with Cursor rules:

1. **Cursor rules ALWAYS take precedence** (source of truth)
2. Announce the conflict to user
3. State which Cursor rule is being followed
4. Explain why Windsurf rule is being ignored

Example:
```
⚠️ CONFLICT DETECTED:
- Windsurf rule suggests: [X]
- Cursor master rule requires: [Y]
- RESOLUTION: Following Cursor master rule [Y]
- REASON: Master rules have highest authority
```

## 10. File Format Notes

**[STRICT]** `.mdc` files from Cursor may contain:
- YAML frontmatter (between `---` markers)
- Markdown content with headers
- XML-like tags (e.g., `<coding_guidelines>`)
- Code blocks with examples
- ALL formats are valid - parse and apply accordingly

## 11. Context Optimization

**[STRICT]** (From Cursor Context Discovery Rule):
- DO NOT re-read a rule file if already in conversation context
- ONLY re-read if you believe it was modified
- Reduces costs and improves performance

## 12. Execution Guarantee

**[STRICT]** After loading Cursor rules:

- Every action MUST comply with loaded rules
- Directive prefixes (`[STRICT]`, `[GUIDELINE]`) dictate compliance level
- When uncertain, cite which rule guides your decision
- If rules seem contradictory, ask user for clarification

---

**INTEGRATION SUMMARY:**

This meta-rule creates a bridge between Windsurf Cascade and the existing 
Cursor rule system. The Cursor rules in `.cursor/rules/` remain the 
authoritative source of truth. This Windsurf rule simply ensures they are 
discovered, loaded, and followed correctly.

**KEY PRINCIPLE:** Windsurf acts as a compliant executor of Cursor directives.
