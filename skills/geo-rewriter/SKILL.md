---
name: geo-rewriter
description: Rewrites existing content for Generative Engine Optimization (GEO). Improves citability by adding structured data references, statistics, author EEAT signals, and llms.txt compatibility. Use when updating legacy content for AI search visibility.
license: MIT
metadata:
  author: brandvirality
  version: "1.0.0"
---

# GEO Content Rewriter

Rewrites existing content to improve AI-search visibility and citation likelihood.

## When to Use

- Updating legacy blog posts for GEO
- Preparing content for AI citation audits
- Improving EEAT signals in existing content

## What It Does

1. **Adds citability hooks** — statistics, definitions, verifiable claims
2. **Improves structure** — clear H2/H3 hierarchy for LLM parsing
3. **Adds EEAT signals** — author bylines, publish dates, credentials
4. **Schema recommendations** — suggests relevant JSON-LD types
5. **llms.txt entry** — generates the entry for this page

## Key Changes

| Before | After |
|--------|-------|
| "Many companies benefit" | "78% of surveyed companies report 40% efficiency gains (Source: McKinsey 2025)" |
| "Contact us" | Author: Dr. Jane Smith, AI Visibility Specialist |
| No schema | Article + FAQ schema recommended |
