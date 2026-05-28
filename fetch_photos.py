#!/usr/bin/env python3
"""
fetch_photos.py — Build photos.json for the Cataract Canyon 2026 slideshow
---------------------------------------------------------------------------
Pulls photos from all six family Google Photos shared albums using the
Google Photos Library API, then writes photos.json which the slideshow
page reads automatically.

FIRST-TIME SETUP (one-time only, ~10 minutes)
----------------------------------------------
1. Go to https://console.cloud.google.com and create a new project
   (name it anything, e.g. "Cataract Canyon")

2. Enable the Photos Library API:
   APIs & Services → Enable APIs → search "Photos Library API" → Enable

3. Create OAuth credentials:
   APIs & Services → Credentials → Create Credentials → OAuth client ID
   → Application type: Desktop app → Download the JSON file
   → Save it as "credentials.json" in this folder

4. Install dependencies (run once in Terminal):
   pip3 install google-auth-oauthlib google-auth-httplib2 google-api-python-client

5. Run this script:
   cd "/Users/tom_mckinnon/Library/Mobile Documents/com~apple~CloudDocs/Projects/Web sites/Rafting_26"
   python3 fetch_photos.py

   The first run will open a browser window asking you to authorize with
   your Google account. After that, a token.json file is saved and future
   runs are fully automatic (no browser needed).

USAGE
-----
Run any time you want to refresh the slideshow with new photos:
   python3 fetch_photos.py

Then push:
   ./push.sh "refresh slideshow photos"

OPTIONS
-------
--max N        Max photos to include (default: 100, set 0 for all)
--shuffle      Randomize order (default: chronological)
--families     Comma-separated list of families to include (default: all)
               e.g. --families McMoran,Redal

"""

import json
import os
import random
import argparse
import sys
from pathlib import Path

# ── Album IDs extracted from the Google Photos share URLs ──────────────────
# Format: the token after /album/ or the share key in goo.gl links
# These are resolved to album IDs at runtime via the API

ALBUMS = [
    {"family": "McMoran",   "share_url": "https://photos.app.goo.gl/7r7n1m3v4BnScXVc6"},
    {"family": "Redal",     "share_url": "https://photos.app.goo.gl/pj7CTDq1LLrfG5SP6"},
    {"family": "Muczynski", "share_url": "https://photos.app.goo.gl/SNULKKLS4spxjZX5A"},
    {"family": "Baatzuela", "share_url": "https://photos.app.goo.gl/DYmmSMn3Y5Kj2QX28"},
    {"family": "Barron",    "share_url": "https://photos.app.goo.gl/aBrRj4jPzvuHb4d46"},
    {"family": "Colbert",   "share_url": "https://photos.app.goo.gl/XgzCgbP67caGqnLGA"},
]

SCOPES = ["https://www.googleapis.com/auth/photoslibrary.readonly"]
SCRIPT_DIR = Path(__file__).parent
CREDENTIALS_FILE = SCRIPT_DIR / "credentials.json"
TOKEN_FILE = SCRIPT_DIR / "token.json"
OUTPUT_FILE = SCRIPT_DIR / "photos.json"


def get_credentials():
    """Load or create OAuth2 credentials."""
    try:
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request
    except ImportError:
        print("\n❌  Missing dependencies. Run:\n")
        print("    pip3 install google-auth-oauthlib google-auth-httplib2 google-api-python-client\n")
        sys.exit(1)

    if not CREDENTIALS_FILE.exists():
        print("\n❌  credentials.json not found.")
        print("    See the FIRST-TIME SETUP instructions at the top of this script.\n")
        sys.exit(1)

    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_FILE.write_text(creds.to_json())
        print("✓  Authorization saved to token.json")

    return creds


def fetch_shared_album_photos(session, share_url):
    """
    Join a shared album by its share URL and return its media items.
    Google Photos API requires joining shared albums before listing them.
    """
    import requests

    # Step 1: join the shared album to get the album ID
    join_resp = session.post(
        "https://photoslibrary.googleapis.com/v1/sharedAlbums:join",
        json={"shareToken": extract_share_token(share_url)},
    )

    if join_resp.status_code not in (200, 409):  # 409 = already joined, that's fine
        print(f"    Warning: could not join album ({join_resp.status_code}): {join_resp.text[:120]}")
        return []

    if join_resp.status_code == 200:
        album_id = join_resp.json()["sharedAlbum"]["id"]
    else:
        # Already joined — find it in the shared albums list
        album_id = find_joined_album_id(session, share_url)
        if not album_id:
            return []

    # Step 2: list all media items in the album
    photos = []
    page_token = None
    while True:
        body = {"albumId": album_id, "pageSize": 100}
        if page_token:
            body["pageToken"] = page_token

        resp = session.post(
            "https://photoslibrary.googleapis.com/v1/mediaItems:search",
            json=body,
        )
        data = resp.json()

        for item in data.get("mediaItems", []):
            meta = item.get("mediaMetadata", {})
            if "photo" in meta:  # skip videos
                photos.append({
                    "id":           item["id"],
                    "url":          item["baseUrl"] + "=w1600-h1200",  # max 1600px wide
                    "thumbnail":    item["baseUrl"] + "=w400-h300",
                    "filename":     item.get("filename", ""),
                    "created":      meta.get("creationTime", ""),
                    "width":        int(meta.get("width", 0)),
                    "height":       int(meta.get("height", 0)),
                    "description":  item.get("description", ""),
                })

        page_token = data.get("nextPageToken")
        if not page_token:
            break

    return photos


def extract_share_token(share_url):
    """Extract the share token from a photos.app.goo.gl URL by following the redirect."""
    import urllib.request
    try:
        req = urllib.request.Request(share_url, method="HEAD")
        req.add_header("User-Agent", "Mozilla/5.0")
        # goo.gl URLs redirect to photos.google.com/share/TOKEN
        with urllib.request.urlopen(req) as resp:
            final_url = resp.url
    except Exception:
        # Fallback: use the short URL path as a token hint
        final_url = share_url

    # Extract token from URL like https://photos.google.com/share/AF1Qip...
    parts = final_url.rstrip("/").split("/")
    return parts[-1]


def find_joined_album_id(session, share_url):
    """Search already-joined shared albums to find the one matching this share URL."""
    page_token = None
    while True:
        params = {"pageSize": 50}
        if page_token:
            params["pageToken"] = page_token
        resp = session.get(
            "https://photoslibrary.googleapis.com/v1/sharedAlbums",
            params=params,
        )
        data = resp.json()
        for album in data.get("sharedAlbums", []):
            if album.get("shareInfo", {}).get("shareableUrl", "") == share_url:
                return album["id"]
        page_token = data.get("nextPageToken")
        if not page_token:
            break
    return None


def build_photos_json(all_photos, max_photos, shuffle, families_filter):
    """Assemble the final photos.json structure."""
    if families_filter:
        keep = set(f.strip() for f in families_filter.split(","))
        all_photos = [p for p in all_photos if p["_family"] in keep]

    if shuffle:
        random.shuffle(all_photos)
    else:
        # Chronological, interleaved across families for variety
        all_photos.sort(key=lambda p: p.get("created", ""))

    if max_photos and len(all_photos) > max_photos:
        all_photos = all_photos[:max_photos]

    families_present = sorted(set(p["_family"] for p in all_photos))

    # Strip the internal _family key from output
    photos_out = []
    for p in all_photos:
        entry = {k: v for k, v in p.items() if k != "_family"}
        if not entry.get("caption"):
            entry["caption"] = p["_family"]
        photos_out.append(entry)

    return {
        "generated": __import__("datetime").datetime.utcnow().isoformat() + "Z",
        "total":     len(photos_out),
        "families":  families_present,
        "photos":    photos_out,
    }


def main():
    parser = argparse.ArgumentParser(description="Fetch Google Photos albums → photos.json")
    parser.add_argument("--max",      type=int, default=100, help="Max photos (0 = all)")
    parser.add_argument("--shuffle",  action="store_true",   help="Randomize order")
    parser.add_argument("--families", type=str, default="",  help="Comma-separated families to include")
    args = parser.parse_args()

    print("\n🏞  Cataract Canyon 2026 — Photo Fetcher\n")

    creds = get_credentials()

    import requests
    from google.auth.transport.requests import AuthorizedSession
    session = AuthorizedSession(creds)

    all_photos = []
    for album in ALBUMS:
        family = album["family"]
        print(f"  Fetching {family}...", end=" ", flush=True)
        photos = fetch_shared_album_photos(session, album["share_url"])
        for p in photos:
            p["_family"] = family
        all_photos.extend(photos)
        print(f"{len(photos)} photos")

    print(f"\n  Total: {len(all_photos)} photos across {len(ALBUMS)} families")

    result = build_photos_json(
        all_photos,
        max_photos=args.max if args.max > 0 else None,
        shuffle=args.shuffle,
        families_filter=args.families,
    )

    OUTPUT_FILE.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"\n✓  Wrote {len(result['photos'])} photos to photos.json")
    print(f"   Families: {', '.join(result['families'])}")
    print("\n  Now run:  ./push.sh \"refresh slideshow\"\n")


if __name__ == "__main__":
    main()
