# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Personal academic portfolio website for Connor Magoon (Applied Mathematics PhD student, UNC Chapel Hill). Originally based on the [Academic Pages](https://github.com/academicpages/academicpages.github.io) Jekyll template (a Minimal Mistakes fork), but heavily stripped down to a single-page site. Deployed via GitHub Pages.

## Local Development

Dependencies (on WSL/Linux):
```bash
sudo apt install ruby-dev ruby-bundler nodejs build-essential gcc make
bundle config set --local path 'vendor/bundle'  # install gems locally
bundle install
```

Serve locally with live reload:
```bash
bundle exec jekyll serve -l -H localhost
```

For development config overrides (disables analytics, uses localhost URL):
```bash
bundle exec jekyll serve -l -H localhost --config _config.yml,_config.dev.yml
```

The site is served at `http://localhost:4000`.

## Site Architecture

This is effectively a **single-page site**. The entire website lives in `_pages/about.md`.

- **`_config.yml`** — site-wide settings: author info, social links, plugins, permalink structure. No collections defined.
- **`_config.dev.yml`** — development overrides (localhost URL, disabled analytics)
- **`_pages/about.md`** — the homepage (`permalink: /`). Uses `layout: default` with `hide_header: true` and `hide_footer: true`. Contains all HTML/CSS/JS inline.
- **`_pages/404.md`** — 404 page. Uses `layout: default`.
- **`_layouts/compress.html`** — outermost layout; compresses HTML output
- **`_layouts/default.html`** — the only active layout. Wraps content with `<head>`, masthead, footer, scripts.
- **`_includes/`** — partials used by `default.html`: `head.html`, `head/custom.html`, `browser-upgrade.html`, `masthead.html`, `footer.html`, `footer/custom.html`, `scripts.html`, `analytics.html`, `seo.html`, `base_path`
- **`_sass/`** — SCSS stylesheets (compiled into `assets/css/main.scss`)
- **`_data/navigation.yml`** — top navigation menu links
- **`images/`** — profile photo and research figures
- **`files/`** — downloadable files (CV PDF, etc.)
- **`setup_notes.txt`** — personal dev notes; keep this file

## Content Updates

- **Edit content:** `_pages/about.md` (inline HTML/CSS/JS). This is the only file that controls what visitors see.
- **Add/replace assets:** `images/` and `files/` referenced in `_pages/about.md`.
- **Navigation:** `_data/navigation.yml` — only touch if adding nav links.
- **Author/site metadata:** `_config.yml` — only touch if updating social links, site title, etc.

## What NOT to Do

- Do not add collections, archive pages, or layouts beyond `default` and `compress` — those were intentionally removed.
- Do not add `_includes` beyond what `default.html` already references.
- Do not delete `setup_notes.txt`.

> **Mental model for Claude:** `_pages/about.md` is the entire website. Everything else either supports building it (Jekyll internals, SCSS, `_layouts/default.html`, `_includes/`) or provides assets (`images/`, `files/`). Keep changes minimal and focused on `about.md`.