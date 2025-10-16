import { MdcRuleLoader } from './mdc-parser';
import { RuleMatcher } from './rule-matcher';

export interface WindsurfMdcPlugin {
  loadRules(): Promise<void>;
  getApplicableRules(filePath: string): any[];
}

export class MdcPlugin implements WindsurfMdcPlugin {
  private loader: MdcRuleLoader;
  private matcher: RuleMatcher;
  private rules: any[] = [];

  constructor() {
    this.loader = new MdcRuleLoader();
    this.matcher = new RuleMatcher();
  }

  async loadRules(): Promise<void> {
    // Scan for .mdc files in Windsurf and Cursor rule directories
    const rulePaths = [
      '.windsurf/rules/',
      '.cursor/rules/'
    ];
    
    this.rules = await this.loader.loadRules(rulePaths);
    console.log(`Loaded ${this.rules.length} MDC rules`);
  }

  getApplicableRules(filePath: string): any[] {
    return this.matcher.getApplicableRules(this.rules, filePath);
  }
}

// Plugin entry point
export function activate() {
  const plugin = new MdcPlugin();
  return plugin;
}
