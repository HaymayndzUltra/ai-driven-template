# Windsurf Plugin Spike: MDC Rules Reader

This is a minimal spike demonstrating how Windsurf could integrate `.mdc` rule detection and parsing.

## Architecture Overview

Windsurf plugins can be built using their plugin system. This spike shows:
1. Scanning for `.mdc` files in `.windsurf/rules/` and `.cursor/rules/`
2. Parsing YAML frontmatter
3. Applying rules based on `alwaysApply` and `globs` patterns
4. Providing rule context to Windsurf's AI features

## Plugin Structure

```
windsurf-mdc-plugin/
├── package.json
├── src/
│   ├── index.ts
│   ├── mdc-parser.ts
│   └── rule-matcher.ts
└── README.md
```

## Key Integration Points

1. **File Discovery**: Use Windsurf's file system APIs to scan rule directories
2. **Rule Parsing**: Parse `.mdc` files with YAML frontmatter
3. **Context Injection**: Provide parsed rules to Windsurf's context system
4. **Pattern Matching**: Apply `globs` patterns to determine rule applicability

## Implementation Notes

- Windsurf plugins use TypeScript/JavaScript
- File system access through Windsurf's plugin APIs
- Context injection via Windsurf's context management system
- Rule precedence follows the spec (priority, version, filename)

## Usage Example

```typescript
import { MdcRuleLoader } from './mdc-parser';

const loader = new MdcRuleLoader();
const rules = await loader.loadRules(['.windsurf/rules/', '.cursor/rules/']);
const applicableRules = loader.getApplicableRules(rules, currentFilePath);
```

## Next Steps

1. Research Windsurf's specific plugin APIs
2. Implement file system integration
3. Add context injection mechanisms
4. Test with sample `.mdc` files
5. Package as installable Windsurf plugin
