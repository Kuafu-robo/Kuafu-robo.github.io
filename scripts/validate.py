#!/usr/bin/env python3
"""Validate the dependency-free SUN / Kuafu website without third-party packages."""
from __future__ import annotations

from collections import Counter
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TITLE = "SUN: Agentic Robot Policy Learning with Persistent Task Programs"
LIMIT = 100 * 1024 * 1024
VIDEO = "assets/videos/RAL_whole_long.mp4"
EXPECTED = [
    "index.html", "styles.css", "README.md", "AGENTS.md", "CITATION.bib",
    "favicon.svg", "site.webmanifest", ".nojekyll", "404.html", "robots.txt",
    "assets/paper/SUN.pdf", VIDEO, "assets/videos/poster.jpg",
    "assets/figures/chase_sun.png", "assets/figures/pipeline1.png",
    *[f"assets/figures/{name}.{ext}" for name in
      ["sun_throughput", "sun_cost_parity", "sun_breakeven"] for ext in ["png", "pdf"]],
]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
        self.ids = []
        self.issues = []
        self.videos = []
        self.sources = []
        self.scripts = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.append(a["id"])
        for key in ("src", "href", "poster", "data-image"):
            if a.get(key):
                self.refs.append(a[key])
        if tag == "img":
            self.images.append(a)
            if "alt" not in a or (not a["alt"] and a.get("id") != "dialog-image"):
                self.issues.append("An informative image lacks alt text.")
        if tag == "video":
            self.videos.append(a)
        if tag == "source":
            self.sources.append(a)
        if tag == "script":
            self.scripts.append(a)
            if a.get("src"):
                self.issues.append("External runtime JavaScript is not expected.")
        if tag == "a" and a.get("target") == "_blank" and "noopener" not in a.get("rel", ""):
            self.issues.append("A new-tab link lacks rel=noopener.")
        if "download" in a:
            self.issues.append("Download controls are prohibited on this website.")
        if tag == "a" and re.search(r"\.(?:pdf|bib|png|jpe?g|svg|mp4|zip)(?:[?#]|$)", a.get("href", ""), re.I):
            self.issues.append("Direct file links are prohibited on this website.")

    handle_startendtag = handle_starttag


def main():
    errors = []
    for name in EXPECTED:
        if not (ROOT / name).is_file():
            errors.append(f"Missing file: {name}")

    files = [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]
    for path in files:
        if path.stat().st_size >= LIMIT:
            errors.append(f"File exceeds GitHub's 100 MiB limit: {path.relative_to(ROOT)}")
        if path.name in {".DS_Store", "cred.txt"} or "__MACOSX" in path.parts:
            errors.append(f"Unwanted file: {path.relative_to(ROOT)}")

    html = (ROOT / "index.html").read_text(encoding="utf-8")
    page = Page()
    page.feed(html)
    errors.extend(page.issues)
    for key, count in Counter(page.ids).items():
        if count > 1:
            errors.append(f"Duplicate HTML id: {key}")
    for reference in page.refs:
        if reference.startswith("#"):
            if reference[1:] not in page.ids:
                errors.append(f"Broken section link: {reference}")
        elif not re.match(r"^(https?:|mailto:|data:|//)", reference):
            path = reference.split("#")[0].split("?")[0]
            if path.startswith("/"):
                errors.append(f"Asset path must be relative: {path}")
            elif not (ROOT / path).is_file():
                errors.append(f"Broken local link: {path}")
    if len(page.scripts) != 1:
        errors.append("Expected exactly one inline script.")
    if len(page.videos) != 1 or len(page.sources) != 1:
        errors.append("Expected exactly one video and one source.")
    elif page.sources[0].get("src") != VIDEO:
        errors.append("The video source is not the approved full-length web copy.")
    for attrs in page.videos:
        if "nodownload" not in attrs.get("controlslist", "").split():
            errors.append("Video must suppress the native download control where supported.")
        for required in ["controls", "muted", "playsinline"]:
            if required not in attrs:
                errors.append(f"Video is missing {required}.")
    if sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob("*.mp4")) != [VIDEO]:
        errors.append("Unexpected additional MP4 file.")

    for stale in ["MPC screening", "SkillMimic", "Skill Mimic", "Anonymous Authors",
                  "Under Review", "REPLACE-ME", "canonical L42", "45.97%", "34.72%",
                  "SUNified", "GPT-6", "control-to-learning-to-real policies",
                  "readiness", "Appendix IV", "controller preparation"]:
        if stale.casefold() in html.casefold():
            errors.append(f"Stale terminology or metadata in page: {stale}")
    if f"<title>{TITLE}</title>" not in html:
        errors.append("Page title does not match the current manuscript.")
    manifest = json.loads((ROOT / "site.webmanifest").read_text(encoding="utf-8"))
    if manifest.get("name") != TITLE:
        errors.append("Manifest title does not match the current manuscript.")
    static_bib = re.search(r'<code id="bibtex">([\s\S]*?)</code>', html)
    script_bib = re.search(r"bibtex: `([\s\S]*?)`", html)
    bib = (ROOT / "CITATION.bib").read_text(encoding="utf-8").strip()
    if not static_bib or unescape(static_bib.group(1)).strip() != bib:
        errors.append("Static BibTeX and CITATION.bib disagree.")
    if not script_bib or script_bib.group(1).strip() != bib:
        errors.append("JavaScript BibTeX and CITATION.bib disagree.")
    for metric in ["82.03", "10.57", "23.6", "46.02", "22.44", "34.0", "106", "35.22"]:
        if metric not in html:
            errors.append(f"Expected current-paper result is missing: {metric}")
    if (ROOT / "assets/paper/SUN.pdf").is_file():
        with (ROOT / "assets/paper/SUN.pdf").open("rb") as source:
            if source.read(5) != b"%PDF-":
                errors.append("The archived paper is not a PDF.")
    if errors:
        for issue in errors:
            print(f"[ERROR] {issue}")
        return 1
    total = sum(path.stat().st_size for path in files)
    print(f"[PASS] {len(files)} files; {total / 1024**2:.1f} MiB total.")
    print("[PASS] Local links, anchors, metadata, citation, figures, and one full video.")
    print("[PASS] All files below 100 MiB; no stale page terminology or placeholders.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
