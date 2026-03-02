# Website Analysis Pipeline

## Workflow

1. **Serve** — `bundle exec jekyll serve -l -H localhost`
2. **Screenshot** — Capture full-page screenshot with headless Chromium to `claude_analysis/claude_captures/screenshot_<DATE>.png` (1440x5000)
3. **Analyze** — Read source (`_pages/about.md`, layouts, includes) and review screenshots
4. **Listen** — Get user feedback and specific suggestions
5. **Implement** — Apply changes to `_pages/about.md` (only file to edit for content)
6. **Re-serve** — Start server again for user validation
7. **Stop** — `pkill -f "jekyll serve"`

## Notes

- Only edit `_pages/about.md` for content/layout changes (all styling/structure is inline)
- **Text/phrasing**: Do not edit words or content without explicit permission—only formatting/spacing changes are freely allowed
- Screenshots go to `claude_analysis/claude_captures/`
- Reports go to `claude_analysis/claude_suggestions/`
