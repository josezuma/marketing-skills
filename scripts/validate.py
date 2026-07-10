#!/usr/bin/env python3
"""Validate all SKILL.md files."""
import os, re
skills_dir = 'skills'
valid = 0
for skill in os.listdir(skills_dir):
    path = os.path.join(skills_dir, skill, 'SKILL.md')
    if os.path.exists(path):
        with open(path) as f:
            content = f.read()
        if '---' in content and 'name:' in content:
            print(f'  ✅ {skill}')
            valid += 1
        else:
            print(f'  ❌ {skill}: invalid frontmatter')
print(f'\n{valid} skills valid')
