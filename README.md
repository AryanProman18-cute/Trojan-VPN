# Trojan VPN website

Static site (HTML/CSS/JS, no build step).

## Run locally
Any static server works, e.g.:

    python3 -m http.server 8080

then open http://localhost:8080

## Deploy on GitHub Pages
Push this folder to a repo, then Settings > Pages > Deploy from branch (root).
`index.html` is the home page; the 12 subpages live alongside it. Assets are in `assets/`.

`build_pages.py` regenerates the subpages from the templates inside it (optional).
