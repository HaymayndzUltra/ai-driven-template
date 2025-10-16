# MDC Extension Integration Guide

## Overview

This guide explains how to integrate `.mdc` (Markdown with frontmatter) rule file support into any IDE or development tool.

## Specification

The `.mdc` format extends Markdown with YAML frontmatter containing rule metadata:

```yaml
---
description: "Rule description"
alwaysApply: false
globs: ["**/*.ts", "**/*.tsx"]
tags: ["typescript", "frontend"]
priority: 3
version: "1.0.0"
---

# Rule Content
Markdown content here...
```

## Implementation Steps

### 1. File Discovery

Scan these directories for `.mdc` files:
- `.cursor/rules/` (Cursor IDE)
- `.windsurf/rules/` (Windsurf IDE)
- Custom paths from configuration

### 2. Parsing

Parse YAML frontmatter and extract:
- `description` (required): Human-readable rule description
- `globs` (optional): File pattern matching rules
- `alwaysApply` (optional): Apply to all contexts
- `tags` (optional): Categorization tags
- `priority` (optional): 1-9, lower = higher priority
- `version` (optional): Semantic version

### 3. Rule Precedence

Sort rules by:
1. Priority (ascending)
2. Version (descending, newer first)
3. Filename (lexicographic)

### 4. Application Logic

Apply rules when:
- `alwaysApply: true` (always)
- File matches any `globs` pattern
- Tags match context requirements

## Reference Implementations

### TypeScript/JavaScript
```bash
cd packages/mdc-rules-ts
npm install
npm run build
npm test
```

### Python
```bash
cd packages/mdc-rules-py
pip install -e .
pytest test_mdc_rules.py
```

## IDE Integration Examples

### Windsurf Plugin
See `windsurf-plugin-spike/` for a complete plugin implementation.

### VS Code Extension
```typescript
import { MdcRuleLoader } from '@mdc-rules/core';

const loader = new MdcRuleLoader();
const rules = await loader.loadRules(['.vscode/rules/']);
```

### CLI Tool
```python
from mdc_rules import discover_mdc_files, parse_mdc_text

files = discover_mdc_files([Path('.rules/')])
for file_path in files:
    with open(file_path) as f:
        rule = parse_mdc_text(f.read())
```

## Testing

Use the provided sample files:
- `mdc-spec/samples-001-always-apply.mdc`
- `mdc-spec/samples-002-globs.mdc`

Run tests to validate parsing and precedence logic.

## Schema Validation

Use `mdc-spec/frontmatter.schema.json` for JSON Schema validation of frontmatter.

## Security Considerations

- Validate file size limits
- Sanitize glob patterns
- Limit parsing timeouts
- Validate YAML structure

## Future Enhancements

- Rule inheritance
- Conditional application
- Dynamic rule loading
- Rule composition
- Performance optimization
