import pytest
from pathlib import Path
from mdc_rules import parse_mdc_text, rank_rules, MdcRule, MdcFrontmatter

def test_parse_mdc_valid_frontmatter():
    content = """---
description: "Test rule"
alwaysApply: true
tags: [test]
priority: 1
version: 1.0.0
---

# Test Rule
This is the body."""
    
    result = parse_mdc_text(content)
    assert result is not None
    assert result.frontmatter.description == "Test rule"
    assert result.frontmatter.alwaysApply is True
    assert result.frontmatter.tags == ["test"]
    assert result.frontmatter.priority == 1
    assert result.frontmatter.version == "1.0.0"
    assert result.body.strip() == "# Test Rule\nThis is the body."

def test_parse_mdc_missing_description():
    content = """---
alwaysApply: true
---

# Test Rule"""
    
    result = parse_mdc_text(content)
    assert result is None

def test_parse_mdc_invalid_frontmatter():
    content = """# Test Rule
No frontmatter here."""
    
    result = parse_mdc_text(content)
    assert result is None

def test_rank_rules_priority():
    rule1 = MdcRule(
        path=Path("test1.mdc"),
        frontmatter=MdcFrontmatter(description="Test 1", priority=1),
        body=""
    )
    rule2 = MdcRule(
        path=Path("test2.mdc"),
        frontmatter=MdcFrontmatter(description="Test 2", priority=2),
        body=""
    )
    
    assert rank_rules(rule1, rule2) == -1  # rule1 has higher priority
    assert rank_rules(rule2, rule1) == 1

def test_rank_rules_version():
    rule1 = MdcRule(
        path=Path("test1.mdc"),
        frontmatter=MdcFrontmatter(description="Test 1", priority=1, version="2.0.0"),
        body=""
    )
    rule2 = MdcRule(
        path=Path("test2.mdc"),
        frontmatter=MdcFrontmatter(description="Test 2", priority=1, version="1.0.0"),
        body=""
    )
    
    assert rank_rules(rule1, rule2) == -1  # rule1 has newer version
