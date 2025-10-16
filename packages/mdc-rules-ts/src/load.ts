import { promises as fs } from 'fs';
import { discoverMdcFiles, parseMdcFile, MdcRule, rankRules } from './index.js';

export async function loadMdcRules(roots: string[]): Promise<MdcRule[]> {
  const files = await discoverMdcFiles(roots);
  const rules: MdcRule[] = [];
  for (const path of files) {
    const content = await fs.readFile(path, 'utf8');
    const parsed = parseMdcFile(content);
    if (parsed) {
      rules.push({ ...parsed, path });
    }
  }
  return rules.sort(rankRules);
}
