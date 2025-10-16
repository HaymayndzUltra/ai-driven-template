import { MdcRule } from './mdc-parser';
import { minimatch } from 'minimatch';

export class RuleMatcher {
  getApplicableRules(rules: MdcRule[], filePath: string): MdcRule[] {
    return rules.filter(rule => this.isRuleApplicable(rule, filePath));
  }

  private isRuleApplicable(rule: MdcRule, filePath: string): boolean {
    // Always apply rules
    if (rule.frontmatter.alwaysApply) {
      return true;
    }

    // Check glob patterns
    if (rule.frontmatter.globs) {
      return rule.frontmatter.globs.some(glob => 
        minimatch(filePath, glob) || minimatch(filePath, glob, { dot: true })
      );
    }

    return false;
  }
}
