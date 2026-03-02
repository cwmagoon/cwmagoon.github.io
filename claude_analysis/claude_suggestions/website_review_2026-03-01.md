# Website Review & Suggestions — 2026-03-01

Screenshot saved to `captures/screenshot_2026-03-01.png` and `captures/screenshot_fullpage_2026-03-01.png`.

---

## What's Working Well

- **Clean single-page layout** — easy to scan, no unnecessary navigation depth.
- **Research section is strong** — figures, author lists, venue info, and pill-link buttons to papers/code/video are all present and well-organized.
- **Pill links** — the purple/blue pill system is a nice, compact way to surface external profiles and paper links.
- **Responsive grid** — the 3-column research grid with media query breakpoints is solid.

---

## Suggestions for Improvement

### 1. Typography: Replace Times New Roman

**Issue:** The global `font-family: "Times New Roman"` gives the site a dated, document-like feel rather than a modern academic web presence. Nearly every competitive academic site (e.g., those built on Hugo Academic / Wowchemy) uses a clean sans-serif.

**Suggestion:** Switch to a system sans-serif stack or a Google Font like `Inter`, `Source Sans Pro`, or `IBM Plex Sans`. Keep serif only if used intentionally for headings or body contrast.

```css
* { font-family: "Inter", "Segoe UI", system-ui, -apple-system, sans-serif !important; }
```

### 2. Add a "Teaching" or "Experience" Section

**Issue:** The site currently has About, Research, and Code. For a professional researcher's site, hiring committees and collaborators expect to see teaching experience, awards, or service.

**Suggestion:** Add one or two of:
- **Teaching** — list courses TA'd or taught, with semesters.
- **Honors & Awards** — the two APS DFD Gallery of Fluid Motion Awards are currently buried inside click-to-reveal figure descriptions. They deserve top-level visibility.
- **Talks / Presentations** — conferences where you've presented.

### 3. Surface Awards and Press Prominently

**Issue:** Two APS Gallery of Fluid Motion Awards are hidden behind click popups on research figures. These are meaningful distinctions.

**Suggestion:** Either add a small "Selected Awards" subsection, or tag the relevant project cards with a visible badge/icon (e.g., a small trophy or star icon next to the project title).

### 4. Improve the Bio / About Section

**Issue:** The blue info box is dense and reads like a single paragraph. Key information (affiliation, advisors, research themes) is hard to skim.

**Suggestions:**
- Break into 2-3 short paragraphs or use a lightweight structure:
  - **Line 1:** Name, position, institution.
  - **Line 2:** Research interests (1-2 sentences, with keywords bolded).
  - **Line 3:** Advisors, with links.
- Consider adding a one-line "research tagline" in slightly larger/bolder text above the detail paragraph, e.g., *"I study the geometry of physical phenomena — from galloping bubbles to neural surface mappings."*

### 5. Photo Quality and Presentation

**Issue:** The profile photo is decent but has an outdoor/casual background. The rounded rectangle crop is fine.

**Suggestion:** Consider a higher-contrast or more neutral-background headshot for a professional academic site. If keeping the current photo, a subtle CSS `object-fit` and `box-shadow` could make it feel more polished:

```css
box-shadow: 0 2px 12px rgba(0,0,0,0.10);
```

### 6. Add an "About Me" or News/Updates Snippet

**Issue:** There's no sense of recency on the page. Visitors can't tell if this is actively maintained.

**Suggestion:** Add a small "News" or "Recent Updates" list (3-5 items) near the top, e.g.:
- *Mar 2026 — Galloping Bubbles three-part series submitted*
- *Dec 2025 — dQP presented at NeurIPS 2025*
- *Oct 2025 — Galloping Bubbles published in Nature Communications*

This is a convention on most academic sites and signals active research output.

### 7. Code Section Feels Sparse

**Issue:** The Code section has only one project (dQP) with a performance plot. The `pip install` line is useful but the section feels like an afterthought relative to Research.

**Suggestions:**
- If dQP is the only open-source project, consider folding the Code section into Research (link to repo from the research card — which you already do).
- Alternatively, if you have other code (simulation scripts, course projects, utilities), add them. Even linking to your GitHub profile with a brief description of activity would help.
- If keeping the section, add a brief description of what the performance plot shows.

### 8. Improve Click-to-Reveal Interaction (UX)

**Issue:** "Click figures for project descriptions" is a non-standard interaction. The popout appears to the right of the figure and can overflow or be missed. On mobile, it degrades to stacking below.

**Suggestions:**
- Consider replacing with a modal/lightbox overlay that centers on screen — more predictable across screen sizes.
- Alternatively, simply show descriptions inline below each figure (always visible), which is the most common academic site pattern. The mystery of hidden content adds friction.

### 9. Visual Hierarchy and Spacing

**Issue:** The sections (About, Research, Code) all use the same gray `#f3f3f3` rounded-rectangle treatment. There's no strong visual hierarchy between them.

**Suggestions:**
- Make the About/header section visually distinct — perhaps a white or very subtle gradient background, with a thin bottom border separating it from Research.
- Use slightly larger section headings with a colored left-border accent or underline to improve scannability.
- Add more vertical breathing room between the header section and Research.

### 10. Footer / Contact Information

**Issue:** There is no footer. The page just ends after the Code section. The email is in the pill links at the top.

**Suggestion:** Add a minimal footer with:
- Email (linked)
- Physical mailing address (department, university — standard for academic sites)
- Optional: a line like "Updated March 2026"

### 11. SEO and Meta

**Issue:** The `excerpt` and `title` in the frontmatter are blank. The `_config.yml` has a good `description` but `og_image` is empty.

**Suggestion:**
- Set `og_image` to your profile photo or a site banner so that link previews on Twitter/LinkedIn/Slack show a meaningful image.
- Fill in the page `title` and `excerpt` for better search indexing.

### 12. Accessibility

**Issue:** Images lack `alt` text. The pill links have no `aria-label` attributes. Color contrast on the light-purple pills (`#e6dbff` bg, `#4b2ca3` text) may be borderline.

**Suggestion:**
- Add descriptive `alt` attributes to all `<img>` tags.
- Add `aria-label` to icon-only or ambiguous links.
- Run a contrast check on pill colors (WCAG AA requires 4.5:1 ratio).

### 13. Small Polish Items

- The `font-family` on the `<pre>` code block uses `!important` globally for Times, which overrides the monospace font on the `pip install` snippet. The code box likely renders in serif — it should explicitly keep its monospace stack.
- The `matchPhotoHeight` script references `getElementById('profile-photo')` but the `<img>` tag doesn't have `id="profile-photo"` — this script is silently broken and does nothing.
- There are ~30 blank lines between the header section and the Research section in the source — no functional impact but clutters the source.
- The `about.md` file includes `<meta name="viewport">` and favicon `<link>` tags that likely duplicate what's already in `_includes/head.html`. Consider removing the duplicates.

---

## Priority Ranking

| Priority | Suggestion | Impact |
|----------|-----------|--------|
| High | #6 Add News/Updates | Signals active researcher |
| High | #2 Add Teaching/Awards section | Expected by hiring committees |
| High | #3 Surface awards prominently | Low effort, high signal |
| High | #4 Restructure bio for scannability | First impression |
| Medium | #1 Typography upgrade | Modern feel |
| Medium | #9 Visual hierarchy | Professional polish |
| Medium | #8 Improve click-to-reveal UX | Reduce friction |
| Medium | #10 Add footer | Completeness |
| Low | #7 Strengthen Code section | Content decision |
| Low | #5 Photo polish | Minor |
| Low | #11 SEO/meta | Background improvement |
| Low | #12 Accessibility | Important but less visible |
| Low | #13 Small polish items | Cleanup |
