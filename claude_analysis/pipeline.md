# Website Analysis Pipeline

## Steps

1. **Serve locally** — `bundle exec jekyll serve -l -H localhost` to build and host the site at `http://localhost:4000`.
2. **Screenshot capture** — Always capture a full-page screenshot (no browser chrome) using headless Chromium:
   ```
   chromium-browser --headless --disable-gpu --no-sandbox \
     --screenshot=claude_analysis/claude_captures/screenshot_<DATE>.png \
     --window-size=1440,5000 http://localhost:4000
   ```
3. **Read source** — Read `_pages/about.md`, `_config.yml`, `_data/navigation.yml`, layouts, and includes to understand the full rendering pipeline.
4. **Visual + source analysis** — Review the screenshots (Claude can read images) alongside the source. Assess:
   - Layout, typography, spacing, visual hierarchy
   - Content completeness (sections expected on an academic site)
   - UX patterns (interactions, responsiveness)
   - SEO/meta/accessibility
   - Code quality and dead code
5. **Write suggestions** — Save a dated Markdown report to `claude_analysis/claude_suggestions/` with:
   - What's working well
   - Numbered suggestions with rationale, code examples, and priority ranking
6. **Stop server** — `pkill -f "jekyll serve"`.
7. **Implement (if requested)** — Apply approved suggestions, then re-serve for evaluation.

## Folder Structure

```
claude_analysis/
├── pipeline.md              # This file
├── claude_captures/          # Headless Chromium screenshots
│   └── screenshot_2026-03-01.png
└── claude_suggestions/       # Dated review documents
    └── website_review_2026-03-01.md
```
