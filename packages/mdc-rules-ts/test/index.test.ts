import { test } from 'node:test';
import assert from 'node:assert';
import { parseMdcFile, rankRules, compareSemver, MdcRule } from '../src/index.js';

test('parseMdcFile - valid frontmatter', () => {
  const content = `---
description: "Test rule"
alwaysApply: true
tags: [test]
priority: 1
version: 1.0.0
---

# Test Rule
This is the body.`;

  const result = parseMdcFile(content);
  assert(result !== null);
  assert.strictEqual(result.frontmatter.description, "Test rule");
  assert.strictEqual(result.frontmatter.alwaysApply, true);
  assert.deepStrictEqual(result.frontmatter.tags, ["test"]);
  assert.strictEqual(result.frontmatter.priority, 1);
  assert.strictEqual(result.frontmatter.version, "1.0.0");
  assert.strictEqual(result.body.trim(), "# Test Rule\nThis is the body.");
});

test('parseMdcFile - missing description', () => {
  const content = `---
alwaysApply: true
---

# Test Rule`;

  const result = parseMdcFile(content);
  assert.strictEqual(result, null);
});

test('parseMdcFile - invalid frontmatter', () => {
  const content = `# Test Rule
No frontmatter here.`;

  const result = parseMdcFile(content);
  assert.strictEqual(result, null);
});

test('rankRules - priority ordering', () => {
  const rule1: MdcRule = {
    path: 'test1.mdc',
    frontmatter: { description: 'Test 1', priority: 1 },
    body: ''
  };
  const rule2: MdcRule = {
    path: 'test2.mdc',
    frontmatter: { description: 'Test 2', priority: 2 },
    body: ''
  };

  assert.strictEqual(rankRules(rule1, rule2), -1); // rule1 has higher priority
  assert.strictEqual(rankRules(rule2, rule1), 1);
});

test('rankRules - version ordering', () => {
  const rule1: MdcRule = {
    path: 'test1.mdc',
    frontmatter: { description: 'Test 1', priority: 1, version: '2.0.0' },
    body: ''
  };
  const rule2: MdcRule = {
    path: 'test2.mdc',
    frontmatter: { description: 'Test 2', priority: 1, version: '1.0.0' },
    body: ''
  };

  assert.strictEqual(rankRules(rule1, rule2), -1); // rule1 has newer version
});

test('compareSemver', () => {
  assert.strictEqual(compareSemver('1.0.0', '1.0.0'), 0);
  assert.strictEqual(compareSemver('2.0.0', '1.0.0'), 1);
  assert.strictEqual(compareSemver('1.0.0', '2.0.0'), -1);
  assert.strictEqual(compareSemver('1.1.0', '1.0.0'), 1);
  assert.strictEqual(compareSemver('1.0.1', '1.0.0'), 1);
});
