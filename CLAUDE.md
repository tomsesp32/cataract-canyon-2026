# Cataract Canyon 2026 — Project Context

## What this is
A static trip website for a six-family Cataract Canyon river trip (May 2026).
Hosted on GitHub Pages. No backend, no frameworks — plain HTML/CSS/JS only.

## Deployment
- Push to `main` → GitHub Pages rebuilds automatically (~2 min)
- Live URL: `https://tomsesp32.github.io/cataract-canyon-2026/`

## File structure
```
cataract-canyon-2026/
├── index.html          ← Landing page with hero image and nav
├── river.html          ← Natural history: geology, wildlife, Powell expeditions, rapids
├── route.html          ← Google MyMaps embed of the float route
├── triplog.html        ← Day-by-day journal
├── gallery.html        ← 6-card grid linking to per-family Google Photos albums
├── crew.html           ← Group members
├── css/
│   └── style.css       ← Shared styles — all pages use this
├── js/
│   └── main.js         ← Shared scripts
└── images/
    ├── hero.jpg
    └── highlights/     ← Curated images only; full galleries are in Google Photos
```

## Style conventions
- All pages share `css/style.css` — never inline styles
- Color scheme: canyon/river tones (deep rust, sandstone, river blue)
- Navigation bar appears on every page linking to all six pages
- Mobile-friendly layout

## Google Photos — one album per family
Photos are hosted in Google Photos, not in this repo. The gallery page links out to six albums.

| Family | Google Photos URL |
|--------|-------------------|
| McMoran | `https://photos.app.goo.gl/7r7n1m3v4BnScXVc6` |
| Redal | `https://photos.app.goo.gl/pj7CTDq1LLrfG5SP6` |
| Muczynski | `https://photos.app.goo.gl/SNULKKLS4spxjZX5A` |
| Baatzuela | `https://photos.app.goo.gl/DYmmSMn3Y5Kj2QX28` |
| Barron | `https://photos.app.goo.gl/aBrRj4jPzvuHb4d46` |
| Colbert | `https://photos.app.goo.gl/XgzCgbP67caGqnLGA` |

## Google Map
`https://www.google.com/maps/d/embed?mid=1yH6RewnDhOF6k9tE930yvXqtdumzP6c&ehbc=2E312F`

## Page details

### crew.html
Lists all trip participants by family group — names and a short bio or fun fact per person. Placeholder text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."

### triplog.html
Day-by-day journal written by trip participants. Content will be pasted in after the trip. Placeholder text: "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

### hero image
Use a free stock canyon/river photo as a placeholder. Suggested source: https://unsplash.com/photos/aerial-view-of-river-between-brown-rocky-mountains-during-daytime (Unsplash, free to use). Replace with an actual trip photo after May 2026.

## Navigation order
Pages should appear in the nav bar in this order:
1. Home (`index.html`)
2. The River (`river.html`)
3. Route (`route.html`)
4. Trip Log (`triplog.html`)
5. Gallery (`gallery.html`)
6. Crew (`crew.html`)

## main.js purpose
Handles shared nav behavior: mobile hamburger menu toggle. No other logic planned at this time.

## GitHub repo
`https://github.com/tomsesp32/cataract-canyon-2026`

## Do not
- Add full-resolution photos to the repo
- Use external CSS frameworks (no Bootstrap, Tailwind, etc.)
- Break the shared navigation structure
- Commit without pushing
