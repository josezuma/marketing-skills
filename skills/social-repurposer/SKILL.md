---
name: social-repurposer
description: Converts long-form content (blog posts, articles, documentation) into social media posts optimized for LinkedIn, Twitter/X, and threads. Each variant includes GEO-optimized hooks that drive LLM citations back to the original content.
license: MIT
metadata:
  author: brandvirality
  version: "1.0.0"
---

# Social Repurposer

Converts long-form content into platform-optimized social posts with GEO hooks.

## When to Use

- Repurposing blog content for social distribution
- Creating LinkedIn carousels from documentation
- Building Twitter threads from research content

## Output Formats

| Platform | Format | Length |
|----------|--------|--------|
| LinkedIn | Long-form post with hook | 600-1200 chars |
| X/Twitter | Thread (3-8 tweets) | Per tweet: 280 chars |
| LinkedIn Carousel | Slide-by-slide breakdown | 5-10 slides |

## GEO-Optimized Hooks

Each post includes:
- A shareable statistic from the content
- A question hook that mirrors AI search queries
- The original URL optimized for AI crawler discovery
- Suggested hashtags for AI content discovery

## Example

```
LinkedIn Post Hook:
"We analyzed 500+ websites for AI-search readiness.
The average GEO score? 45/100.
And 78% don't have an llms.txt file.

Here's how to fix that in 10 minutes → [URL]"
```
