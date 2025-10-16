import { globby } from 'globby';
import matter from 'gray-matter';

export type MdcFrontmatter = {
  description: string;
  globs?: string[];
  alwaysApply?: boolean;
  tags?: string[];
  priority?: number; // 1 (highest) .. 9 (lowest), default 3
  version?: string; // semver
};

export type MdcRule = {
  path: string;
  frontmatter: MdcFrontmatter;
  body: string;
};

export async function discoverMdcFiles(paths: string[]): Promise<string[]> {
  const patterns = paths.map((p) => `${p.replace(/\/$/, '')}/**/*.mdc`);
  const files = await globby(patterns, { gitignore: true });
  return files.sort();
}

export function parseMdcFile(content: string): MdcRule | null {
  const parsed = matter(content);
  const data = parsed.data as Partial<MdcFrontmatter>;
  if (!data || typeof data.description !== 'string' || data.description.trim() === '') {
    return null;
  }
  const fm: MdcFrontmatter = {
    description: data.description.trim(),
    globs: Array.isArray(data.globs) ? data.globs.map(String) : undefined,
    alwaysApply: typeof data.alwaysApply === 'boolean' ? data.alwaysApply : false,
    tags: Array.isArray(data.tags) ? data.tags.map(String) : undefined,
    priority: typeof data.priority === 'number' ? data.priority : 3,
    version: typeof data.version === 'string' ? data.version : undefined,
  };
  return { path: '', frontmatter: fm, body: parsed.content };
}

export function rankRules(a: MdcRule, b: MdcRule): number {
  const pa = a.frontmatter.priority ?? 3;
  const pb = b.frontmatter.priority ?? 3;
  if (pa !== pb) return pa - pb; // lower number = higher priority
  const va = a.frontmatter.version ?? '0.0.0';
  const vb = b.frontmatter.version ?? '0.0.0';
  if (va !== vb) return compareSemver(vb, va); // newer first
  return a.path.localeCompare(b.path);
}

export function compareSemver(a: string, b: string): number {
  const pa = a.split(/\.|-|\+/).map(seg => (isNaN(Number(seg)) ? seg : Number(seg)));
  const pb = b.split(/\.|-|\+/).map(seg => (isNaN(Number(seg)) ? seg : Number(seg)));
  const len = Math.max(pa.length, pb.length);
  for (let i = 0; i < len; i++) {
    const va = pa[i] ?? 0;
    const vb = pb[i] ?? 0;
    if (va === vb) continue;
    if (typeof va === 'number' && typeof vb === 'number') return va - vb;
    return String(va).localeCompare(String(vb));
  }
  return 0;
}
