import { promises as fs } from 'fs';
import { globby } from 'globby';
import { parse } from 'yaml';

export interface MdcRule {
  path: string;
  frontmatter: {
    description: string;
    globs?: string[];
    alwaysApply?: boolean;
    tags?: string[];
    priority?: number;
    version?: string;
  };
  body: string;
}

export class MdcRuleLoader {
  async loadRules(rulePaths: string[]): Promise<MdcRule[]> {
    const files = await this.discoverMdcFiles(rulePaths);
    const rules: MdcRule[] = [];

    for (const filePath of files) {
      try {
        const content = await fs.readFile(filePath, 'utf8');
        const rule = this.parseMdcFile(content, filePath);
        if (rule) {
          rules.push(rule);
        }
      } catch (error) {
        console.warn(`Failed to load rule file ${filePath}:`, error);
      }
    }

    return this.sortRules(rules);
  }

  private async discoverMdcFiles(rulePaths: string[]): Promise<string[]> {
    const patterns = rulePaths.map(path => `${path}/**/*.mdc`);
    return await globby(patterns, { gitignore: true });
  }

  private parseMdcFile(content: string, filePath: string): MdcRule | null {
    if (!content.startsWith('---\n')) {
      return null;
    }

    try {
      const [_, frontmatterText, body] = content.split('---\n', 3);
      const frontmatter = parse(frontmatterText);
      
      if (!frontmatter?.description) {
        return null;
      }

      return {
        path: filePath,
        frontmatter: {
          description: frontmatter.description,
          globs: frontmatter.globs || undefined,
          alwaysApply: frontmatter.alwaysApply || false,
          tags: frontmatter.tags || undefined,
          priority: frontmatter.priority || 3,
          version: frontmatter.version || undefined,
        },
        body: body || ''
      };
    } catch (error) {
      console.warn(`Failed to parse frontmatter in ${filePath}:`, error);
      return null;
    }
  }

  private sortRules(rules: MdcRule[]): MdcRule[] {
    return rules.sort((a, b) => {
      // Priority (lower number = higher priority)
      const priorityA = a.frontmatter.priority || 3;
      const priorityB = b.frontmatter.priority || 3;
      if (priorityA !== priorityB) {
        return priorityA - priorityB;
      }

      // Version (newer first)
      const versionA = a.frontmatter.version || '0.0.0';
      const versionB = b.frontmatter.version || '0.0.0';
      if (versionA !== versionB) {
        return this.compareVersions(versionB, versionA);
      }

      // Filename as tie-breaker
      return a.path.localeCompare(b.path);
    });
  }

  private compareVersions(a: string, b: string): number {
    const aParts = a.split('.').map(Number);
    const bParts = b.split('.').map(Number);
    
    for (let i = 0; i < Math.max(aParts.length, bParts.length); i++) {
      const aPart = aParts[i] || 0;
      const bPart = bParts[i] || 0;
      if (aPart !== bPart) {
        return aPart - bPart;
      }
    }
    return 0;
  }
}
