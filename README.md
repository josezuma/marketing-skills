<div align="center">
  <h1>📦 Marketing Skills Pack</h1>
  <p><em>6+ agent skills for marketers doing GEO (Generative Engine Optimization). Content briefs, GEO rewriting, schema generation, competitor analysis, headline optimization, and social repurposing.</em></p>
  <p><a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a></p>
  <p>by <a href="https://brandvirality.com">BrandVirality</a></p>
</div>

---

## Skills

| Skill | Description |
|-------|-------------|
| [content-brief](skills/content-brief/SKILL.md) | Generates GEO-optimized content briefs with query clusters, schema recommendations, and competitor gaps |
| [geo-rewriter](skills/geo-rewriter/SKILL.md) | Rewrites existing content for AI-search visibility — adds citability hooks, EEAT signals, and structure |
| [schema-generator](skills/schema-generator/SKILL.md) | Outputs copy-paste JSON-LD schema markup with AI extraction annotations |
| [competitor-snapshot](skills/competitor-snapshot/SKILL.md) | Analyzes competitor GEO readiness — llms.txt, robots.txt, schema, EEAT signals |
| [headline-optimizer](skills/headline-optimizer/SKILL.md) | Scores and improves headlines for AI citation likelihood |
| [social-repurposer](skills/social-repurposer/SKILL.md) | Converts long-form content into platform-optimized social posts with GEO hooks |

## Installation

### As Agent Skills

Clone this repo and reference skills in your agent configuration:

```bash
# Claude Code
claude code --skill /path/to/marketing-skills/skills/content-brief
claude code --skill /path/to/marketing-skills/skills/geo-rewriter
```

### As a Plugin Collection

Install the full pack via the plugin manifest:

```bash
# Copy to your .claude/plugins/ or skills/ directory
cp -r skills/* ~/.claude/skills/
```

## Usage Examples

### Content Brief

```
"Generate a content brief for 'AI Search Optimization Guide' that targets small business owners"
```

### GEO Rewriter

```
"Rewrite our 'About Us' page for AI-search visibility — add EEAT signals and citability hooks"
```

### Schema Generator

```
"Generate Article schema for our latest blog post about AI automation"
```

## Related

- [awesome-ai-visibility](https://github.com/josezuma/awesome-ai-visibility)
- [schema-for-ai](https://github.com/josezuma/schema-for-ai)
- [geo-audit-skill](https://github.com/josezuma/geo-audit-skill)
- [BrandVirality](https://brandvirality.com)

## License

[MIT](LICENSE) © 2026 Jose Zuma / BrandVirality
