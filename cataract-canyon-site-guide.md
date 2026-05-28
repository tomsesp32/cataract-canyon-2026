# Cataract Canyon Trip Site — Workflow Guide
*GitHub Pages · Google Photos · Claude Cowork*

This guide covers how to integrate the three main tools for building and maintaining your river trip website: GitHub Pages for hosting, Google Photos for shared photo management, and Claude Cowork for building the HTML site.

---

## 1. Overall Architecture

Each tool does what it's best at:

| Component | Tool | Who manages it |
|---|---|---|
| Website hosting | GitHub Pages | You (via Claude Cowork) |
| Photo storage & uploads | Google Photos (6 albums) | All group members |
| Site HTML/CSS/JS | Claude Cowork | You |
| Version control | Git / GitHub | Claude Cowork handles commands |

---

## 2. GitHub Pages Setup (One-Time)

Do this once in the GitHub web interface — no command line needed.

### 2a. Create the repository
1. Go to [github.com](https://github.com) and click **New repository**
2. Name it something like **cataract-canyon-2026**
3. Set visibility to **Public** (required for free GitHub Pages)
4. Check **"Add a README file"** so the repo isn't empty
5. Click **Create repository**

### 2b. Enable GitHub Pages
1. In your new repo, click **Settings** (top tab bar)
2. Scroll down to **Pages** in the left sidebar
3. Under "Source", select **Deploy from a branch**
4. Set branch to **main**, folder to **/ (root)**
5. Click **Save**

Your site will be live within a minute or two at:
```
https://yourusername.github.io/cataract-canyon-2026
```
> Replace `yourusername` with your actual GitHub username. The URL is live immediately but will show a 404 until you push an index.html.

---

## 3. Google Photos Setup — One Album Per Family

Google Photos does not support nested albums or subfolders — it is a flat structure. The solution is **one shared album per family (six total)**. Each family uploads to their own album; your website gallery page presents all six with a card for each. This gives each family ownership of their photos and makes browsing more intentional.

### 3a. Create one album per family (repeat six times)
1. Open **Google Photos** on your phone or at [photos.google.com](https://photos.google.com)
2. Tap **Library → Albums → Create album**
3. Name it with the family name (e.g., *"Cataract 2026 — Henderson Family"*)
4. Tap the **share icon** and enable **Collaboration**
5. Set to **Anyone with the link can add photos**
6. Copy the share link — send it **only to that family**

> **Tip:** Do all six albums in one sitting. Keep a simple note with each family name and its corresponding Google Photos link — you'll need these when building gallery.html.

### 3b. Track your six album links

Fill this in as you create each album, then paste it into Claude Cowork when building gallery.html.

| Family | Album Name | Google Photos Share Link |
|---|---|---|
| Family 1 | Cataract 2026 — Family 1 | |
| Family 2 | Cataract 2026 — Family 2 | |
| Family 3 | Cataract 2026 — Family 3 | |
| Family 4 | Cataract 2026 — Family 4 | |
| Family 5 | Cataract 2026 — Family 5 | |
| Family 6 | Cataract 2026 — Family 6 | |

### 3c. How the gallery page works

Your `gallery.html` page presents six cards — one per family — each with the family name and a **View Photos** button linking to their Google Photos album. Example Claude Cowork brief:

```
"Build gallery.html with a 2-column card grid. Each card shows the family name,
a short caption, and a 'View Photos' button linking to their Google Photos album.
Use these six links: [paste your table of family names and URLs].
Match the site CSS. Push when done."
```

> Google Photos does not support true iframe embeds for shared albums. Styled link buttons are the correct approach — they open the album in a new tab.

---

## 4. Local File Structure

Claude Cowork will create and manage files in a local folder on your Mac, then push changes to GitHub. Recommended structure:

```
cataract-canyon-2026/
├── index.html          ← Landing page
├── river.html          ← Natural history of Cataract / Colorado R.
├── route.html          ← Map and route details
├── triplog.html        ← Day-by-day journal
├── gallery.html        ← 6-card grid, one per family → Google Photos
├── crew.html           ← Group members page
├── css/
│   └── style.css       ← Shared stylesheet
├── js/
│   └── main.js         ← Any interactivity
└── images/
    ├── hero.jpg        ← Landing page hero image
    └── highlights/     ← A few curated images (not full gallery)
```

> Keep the `images/` folder lean — just hero and highlight images. Full photo libraries stay in Google Photos to avoid bloating the repo.

---

## 5. Working with Claude Cowork

Claude Cowork builds the site page by page. You describe what you want and it writes the HTML/CSS, manages git commits, and pushes to GitHub. You never need to type git commands yourself.

### 5a. First session — project setup

```
"Clone my GitHub repo cataract-canyon-2026 to a local folder.
Create index.html with a hero section, navigation bar linking to
river.html, route.html, triplog.html, gallery.html, and crew.html,
and a css/style.css with a river/canyon color scheme.
Commit and push to GitHub when done."
```

### 5b. Building the natural history page

```
"In river.html, create a page covering: the geology of Cataract Canyon
(Permian/Pennsylvanian strata), the Colorado River watershed and pre-dam
vs. current hydrology, Lake Powell and the ongoing drawdown, desert bighorn
and peregrine falcon ecology, the Powell expeditions of 1869 and 1871,
and the Big Drop rapids lore. Use the shared CSS. Push when done."
```

### 5c. Updating the site after the trip

```
"Open triplog.html. Add a Day 3 entry: [paste your notes here].
Commit with message 'Add Day 3 trip log' and push."
```

---

## 6. The Deploy Workflow

Every time Claude Cowork pushes a commit to the main branch, GitHub Pages automatically rebuilds and serves the updated site. Changes are typically live within 1–2 minutes.

| Step | Action | Who/What |
|---|---|---|
| 1 | You describe a change to Claude Cowork | You |
| 2 | Claude Cowork edits the HTML/CSS files locally | Claude Cowork |
| 3 | Claude Cowork runs git add, commit, push | Claude Cowork |
| 4 | GitHub receives the push, triggers Pages build | GitHub (automatic) |
| 5 | Site is live at your .github.io URL | GitHub Pages |

---

## 7. Maps Integration

For the route page, a Google MyMaps embed works well and is free. You can plot the full route with named waypoints and embed it directly in the site.

### Create a custom Google Map
1. Go to [mymaps.google.com](https://mymaps.google.com) and create a new map
2. Add a layer for the river route (draw a line along the Colorado)
3. Add point markers: Moab put-in, Green/Colorado confluence, campsites, Big Drop 1/2/3, Hite takeout
4. Click **Share → Anyone with link**, then the 3-dot menu → **"Embed on my site"**
5. Copy the iframe code and give it to Claude Cowork to drop into `route.html`

---

## 8. Quick Reference Checklist

### Setup
- [ ] GitHub repo created (`cataract-canyon-2026`)
- [ ] GitHub Pages enabled (Settings → Pages → main branch)
- [ ] Google Photos album created — Family 1 + link sent
- [ ] Google Photos album created — Family 2 + link sent
- [ ] Google Photos album created — Family 3 + link sent
- [ ] Google Photos album created — Family 4 + link sent
- [ ] Google Photos album created — Family 5 + link sent
- [ ] Google Photos album created — Family 6 + link sent
- [ ] All 6 album URLs collected in Section 3b table above

### Site pages (Claude Cowork)
- [ ] `index.html` + `css/style.css` — landing page and shared styles
- [ ] `river.html` — natural history content
- [ ] `route.html` — Google MyMaps embed
- [ ] `triplog.html` — day-by-day journal
- [ ] `gallery.html` — 6-card grid linking to family albums
- [ ] `crew.html` — group member page

### Launch
- [ ] Share site URL with the group: `https://yourusername.github.io/cataract-canyon-2026`

---

*Generated by Claude · Cataract Canyon 2026 Trip Site Planning*
