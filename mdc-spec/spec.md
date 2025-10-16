# MDC Extension Recognition Specification

## Purpose
Define an IDE-agnostic mechanism to detect, parse, and apply `.mdc` rule files containing YAML frontmatter that guide AI/editor behavior.

## Scope
- File discovery locations
- File type recognition and precedence
- Frontmatter schema
- Application flow and matching via `globs`

## Discovery Locations (ordered)
1. `.cursor/rules/`
2. `.windsurf/rules/`
3. Additional locations from config/env: `MDC_RULE_PATHS` (comma-separated)

Implementations MUST scan all configured roots recursively and consider only files ending with `.mdc`.

## File Type Recognition and Precedence
- Recognize `.mdc` as Markdown-with-frontmatter.
- If both `.md` and `.mdc` exist for the "same" rule domain, prefer `.mdc`.
- Tie-breakers:
  - Higher `priority` (lower number means higher priority)
  - Newer `version` (Semantic Versioning)
  - Lexicographic filename as final tie-breaker

## Frontmatter Schema (summary)
- `description` (string, required)
- `globs` (array of strings, optional)
- `alwaysApply` (boolean, optional; default false)
- `tags` (array of strings, optional)
- `priority` (integer, optional; default 3; 1 highest)
- `version` (string semver, optional)

See `frontmatter.schema.json` for canonical validation rules.

## Application Flow
1. Discover `.mdc` files from locations (above)
2. Parse YAML frontmatter; validate against schema
3. Rank rules using precedence
4. Determine applicability:
   - If `alwaysApply == true`, include for all contexts
   - Else, if `globs` defined, include when target files match any glob
5. Provide matched rule bodies and metadata to the host (IDE/tool) for integration

## Security and Robustness
- Reject files with invalid frontmatter or non-UTF-8 encoding
- Enforce schema validation; collect diagnostics
- Limit body size and parsing timeouts to avoid abuse

## References (evidence-backed)
- Cursor Rules directory and frontmatter usage (description, globs, alwaysApply):
  - https://docs.cursor.com/en/context/rules
- Community structure and naming conventions:
  - https://forum.cursor.com/t/optimal-structure-for-mdc-rules-files/52260
  - https://forum.cursor.com/t/my-best-practices-for-mdc-rules-and-troubleshooting/50526


