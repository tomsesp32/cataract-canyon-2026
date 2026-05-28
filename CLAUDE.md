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
├── gallery.html        ← 6-card grid linking to per-family Google Photos albums
├── crew.html           ← The Guides: four-quadrant page (Tanner, Cam, Reina, Devon)
├── fun_stuff.html           ← Fun Stuff landing page: card grid linking to sub-pages
├── petrified_wood.html      ← How petrified wood forms (geochemistry article)
├── ancestral_puebloans.html ← Ancestral Puebloan history
├── cryptobiotic_soil.html   ← Desert living crust ecosystem
├── desert_varnish.html      ← Canyon wall coatings (biogeochemistry)
├── our_planes.html          ← Aircraft used for the trip
├── slideshow.html           ← Auto slideshow fed by photos.json (Under Construction until ready)
├── emails.html              ← Email roster grouped by family, with copy-all button
├── fetch_photos.py          ← Script to pull Google Photos albums → photos.json
├── push.sh                  ← One-command git add/commit/push helper
├── css/
│   └── style.css        ← Shared styles — all pages use this
├── js/
│   └── main.js          ← Shared scripts (hamburger nav, active link)
└── images/
    ├── group_shot.JPG       ← Hero image on index.html
    ├── the_river.jpeg       ← Card image for The River
    ├── route.png            ← Card image for Route
    ├── plane_banner.jpeg    ← Card image for Our Planes on Fun Stuff
    ├── petrified_wood.jpeg  ← Card image for Petrified Wood on Fun Stuff
    ├── ancestral_puebloans.jpeg
    ├── cryptobiotic_soil.jpeg
    ├── desert_varnish.jpeg
    ├── plane_small.png      ← Diagram of the little plane
    ├── plane_big.png        ← Diagram of the big plane
    ├── the_little_one.jpeg  ← Trip photo of the little plane
    ├── the_big_one.jpeg     ← Trip photo of the big plane
    └── highlights/          ← Curated images only; full galleries are in Google Photos
```

## Style conventions
- All pages share `css/style.css` — never inline styles
- Color scheme: canyon/river tones (deep rust, sandstone, river blue)
- Navigation bar appears on every page linking to all eight top-level pages
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

### crew.html — "The Guides"
Four-quadrant full-bleed page. Each quadrant has a circular photo, guide name, and short bio paragraph. Guides: Tanner, Cam, Reina, Devon. Replace emoji avatars with real photos and bios after the trip. Layout uses `.guides-grid` CSS class (2×2 grid, stacks to single column on mobile).

### hero image
Currently set to `images/group_shot.JPG` — the trip group photo.

## Navigation order
Pages should appear in the nav bar in this order:
1. Home (`index.html`)
2. The River (`river.html`)
3. Route (`route.html`)
4. Gallery (`gallery.html`)
5. The Guides (`crew.html`)
6. Fun Stuff (`fun_stuff.html`)
7. Slideshow (`slideshow.html`)
8. Emails (`emails.html`)

## Fun Stuff section
`fun_stuff.html` is a card-grid landing page. Each card links to a sub-page article.
Sub-pages also carry the shared nav and link back to `fun_stuff.html` in their footer.
Current sub-pages:
- `petrified_wood.html` — petrified wood geochemistry article
- `ancestral_puebloans.html` — history of Ancestral Puebloan peoples of the plateau
- `cryptobiotic_soil.html` — the living desert crust ecosystem
- `desert_varnish.html` — biogeochemical mystery of canyon wall coatings
- `our_planes.html` — the aircraft used for the trip (converted from Our_Planes.docx; images in images/)

All Fun Stuff sub-pages have their own inline styles + Google Fonts; shared nav and style.css are added on top. Each links back to `fun_stuff.html` in its footer.

## slideshow.html
Displays a 🚧 Under Construction message until `photos.json` is present in the root. Once `photos.json` exists, automatically switches to a full crossfade slideshow with play/pause, prev/next, speed control, and photo counter. `fetch_photos.py` generates `photos.json` from the six Google Photos albums.

## emails.html
Email roster grouped by family (Guides, McMoran, Redal, Muczynski, Baatzuela, Barron, Colbert). Each address is a clickable mailto: link. Includes a "Copy all addresses" button for group emails.

## fetch_photos.py
Python script that pulls all six Google Photos shared albums via the Google Photos Library API and writes `photos.json` for the slideshow. Requires one-time Google Cloud OAuth setup (credentials.json). token.json and credentials.json are in .gitignore — never commit them. Run with: `python3 fetch_photos.py`

## push.sh
Helper script: `./push.sh "commit message"` — stages all changes, commits, and pushes to origin/main in one step.

## main.js purpose
Handles shared nav behavior: mobile hamburger menu toggle, active link highlighting. No other logic planned at this time.

## GitHub repo
`https://github.com/tomsesp32/cataract-canyon-2026`

## Do not
- Add full-resolution photos to the repo
- Use external CSS frameworks (no Bootstrap, Tailwind, etc.)
- Break the shared navigation structure
- Commit without pushing
