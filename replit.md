# ToolsHub Pro — Blogger XML Theme Preview

## Project Overview

This project is a **Blogger XML theme** for a multi-tools online platform (PDF tools, image tools, text utilities, converters, calculators, AI tools, etc.).

**Main deliverable**: `toolshub-pro-blogger-theme.xml` — upload this to Blogger Dashboard → Theme → Edit HTML.

Since Blogger themes cannot run standalone, this Replit serves a **static HTML preview** of the theme's design and UI.

## Project Structure

```
├── toolshub-pro-blogger-theme.xml   # MAIN Blogger XML theme (use this)
├── blogger-theme-multitools-professional-animations (1).xml  # Old version
├── index.html      # Static preview — homepage
├── blog.html       # Static preview — blog listing page
├── all-tools.html  # Static preview — all tools page
├── attached_assets/ # Public image assets
├── server.py       # Python HTTP server (port 5000)
└── replit.md       # This file
```

## Running the App

```bash
python server.py
```

Server runs on port 5000 (or `$PORT`). Only serves preview pages, XML files, and `attached_assets/`.

## Tech Stack

- **Theme**: Blogger XML template (CSS3, HTML5, Vanilla JS)
- **Preview Server**: Python built-in HTTP server
- **Fonts**: Google Fonts (Syne, DM Sans)
- **Design**: Dark/light mode with smooth transitions, CSS variables, responsive layout, particle canvas, scroll reveal animations

## Deployment

- **Target**: Autoscale
- **Run Command**: `python server.py`

## Completed Features (toolshub-pro-blogger-theme.xml)

1. **Logo gradient** — ToolsHub Pro shows as blue-purple gradient (CSS var(--grad) with background-clip:text)
2. **Smooth dark/light transitions** — body has `transition: background-color .3s ease, color .3s ease`
3. **All Tools nav — no navigate** — href changed to `javascript:void(0)` so clicking won't navigate away
4. **Mega dropdown** — 6-column professional dropdown with category headers + individual tool links per category
5. **Latest Articles hidden on homepage** — `<section class='bp-sec'>` block fully removed
6. **Blogger posts auto-populate** — Blog1 widget handles post listing; Blog2 (sidebar) shows recent posts
7. **Clear comments in XML** — Each section has Bengali + English instructions for adding new tools/categories
8. **Blogger upload compatibility fixes** — tool/page links now use `data:blog.homepageUrl`, search redirects are homepage-safe, search overlay and hero search animations were strengthened, mobile search is visible, and a built-in tool library section was added so key categories remain visible after Blogger upload without external files.
9. **Blogger blank-section fix** — reveal animation is now fail-safe: all `.rv` text/cards are visible by default, so Blogger JavaScript or scroll observer issues cannot hide homepage sections and create large blank areas.
10. **Blog post listing fallback** — if Blogger's Blog1 widget returns no visible posts on `/search` or label pages, the theme now loads real public posts from the Blogger JSON feed and renders them as professional post cards.

## How to Add a New Tool (XML)

Inside the nav dropdown (`<div class='dd-mega'>`), find the relevant `.dd-col` category block and add:
```html
<a class='dd-tool' href='/p/your-tool-page-slug.html'>Tool Name</a>
```

For best Blogger compatibility, use homepage-relative expressions like:
```html
<a class='dd-tool' expr:href='data:blog.homepageUrl + "p/your-tool-page-slug.html"'>Tool Name</a>
```

## How to Add a New Category (XML)

Copy an existing `<div class='dd-col'>` block, change the icon/color/name, and add your tool links inside.

## How to Use the Blogger Theme

1. Go to Blogger Dashboard → **Theme → Edit HTML**
2. Select all existing code and delete it
3. Paste the full contents of `toolshub-pro-blogger-theme.xml`
4. Click **Save theme**
5. Your blog posts will automatically appear via the Blog1/Blog2 widgets or the JSON feed fallback
6. Create Pages (`/p/tool-name.html`) for each tool page
