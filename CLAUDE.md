# save_claude_md.py
claude_md_content = """# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Personal academic portfolio website for Connor Magoon (Applied Mathematics PhD student, UNC Chapel Hill). Originally based on [Academic Pages](https://github.com/academicpages/academicpages.github.io) (Minimal Mistakes fork), but stripped down to a **single-page site**. Deployed via GitHub Pages.

## Local Development

Install dependencies (once, on WSL/Linux):

    sudo apt install ruby-dev ruby-bundler nodejs build-essential gcc make
    bundle install

Serve locally for debugging only (run this after all changes are complete):

    bundle exec jekyll serve -l -H localhost

The site will be available at http://localhost:4000.

Debugging locally should be the final step after making all content, layout, or asset changes.

## Site Architecture

This is a single-page site. The website content lives in `_pages/about.md`.

- `_pages/about.md` — the homepage (permalink: /), layout: default. Contains all HTML/CSS/JS inline. This is the only file you edit to change content.
- `_layouts/` — layouts for the site. Refer to /docs for layout reference.
- `_includes/` — partials used by default.html (head, masthead, footer, scripts, Google tracking, SEO, favicon). Preserve these.
- `_sass/` — SCSS stylesheets (compiled into assets/css/main.scss).
- `_data/navigation.yml` — top navigation links (edit only if adding nav links).
- `images/` and `files/` — profile photo, research figures, downloadable files. Preserve these.
- `setup_notes.txt` — personal dev notes; do not delete.

## Content Updates

- Edit content: `_pages/about.md` only.
- Add/replace assets: `images/` and `files/`.
- Navigation: `_data/navigation.yml` if adding links.
- Metadata/social links: `_config.yml` if updating site info.

## Restrictions / What NOT to Do

- Do not add new collections, layouts, or archive pages.
- Do not add new `_includes/` beyond what `default.html` references.
- Preserve Google tracking, favicon, files, and images.
- `_pages/about.md` is effectively the entire site.

**Mental model for Claude:** Focus edits on `_pages/about.md`. Everything else supports building, styling, or provides assets. Only serve locally at the very end for debugging.
"""

with open("CLAUDE.md", "w", encoding="utf-8") as f:
    f.write(claude_md_content)

print("CLAUDE.md has been written successfully!")