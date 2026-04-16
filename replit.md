# MultiTools Pro — Blogger Theme Preview

## Project Overview

This project is a **Blogger XML theme** for a multi-tools online platform (PDF tools, image tools, text utilities, converters, etc.). The original theme file is:

- `blogger-theme-multitools-professional-animations (1).xml` — Full Blogger template to upload to the Blogger dashboard.

Since Blogger themes cannot run standalone, this Replit serves a **static HTML preview** of the theme's design and UI.

## Project Structure

```
├── blogger-theme-multitools-professional-animations (1).xml  # Original Blogger XML theme
├── index.html      # Static HTML preview of the theme
├── server.py       # Python HTTP server (serves index.html on port 5000)
└── replit.md       # This file
```

## Running the App

The app runs via a Python `http.server` on port 5000:

```bash
python server.py
```

## Tech Stack

- **Theme**: Blogger XML template with CSS3, HTML5, JavaScript
- **Preview Server**: Python built-in HTTP server
- **Fonts**: Google Fonts (Syne, DM Sans)
- **Design**: Dark/light mode, CSS variables, responsive layout, animations

## Deployment

- **Target**: Autoscale
- **Run Command**: `python server.py`

## How to Use the Blogger Theme

1. Go to your Blogger dashboard
2. Navigate to **Theme > Customize > Edit HTML**
3. Replace the existing theme XML with the content from `blogger-theme-multitools-professional-animations (1).xml`
4. Save and apply
