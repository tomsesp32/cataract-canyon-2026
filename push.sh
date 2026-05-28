#!/bin/bash
# push.sh — stage, commit, and push all changes to GitHub
# Usage: ./push.sh "your commit message"

cd "$(dirname "$0")"

MESSAGE="${1:-update site}"

git add -A
git commit -m "$MESSAGE"
git push origin main
