# SUN / Kuafu project website

A concise project page for **SUN: Agentic Robot Policy Learning with Persistent Task Programs**, updated against the identified arXiv source at paper commit `9ca9469` (2026-09-23 website refresh).

The page features the paper's Figure 1 below the title and publication links, followed by the abstract, full project video, method workflow, four video-to-model examples, throughput, cost-parity and time-break-even plots, and a copyable citation. All plots are displayed directly on the page, with relevant passages from the main-text discussion of Table IV, panels A and B, in Section IV-C. The descriptions use the author's requested training terminology. It has no download links. Supporting source assets remain in the folder, unlinked. The site requires no build tools or runtime dependencies.

## Preview

From this folder:

```bash
python3 -m http.server 8000
```

Open http://localhost:8000/ and stop the server with Ctrl+C when finished. You can also open index.html directly, although clipboard behavior is more reliable through localhost.

## Host on your GitHub account

### 1. Create an empty public repository

Sign in to GitHub and create a repository named **USERNAME.github.io**, replacing USERNAME with your GitHub username. Choose **Public** and do not initialize it with a README, license, or .gitignore: this folder already contains the website files.

Each account has only one account-level Pages site. If you already use that repository for a personal website, do not replace it with these files without first deciding how to preserve the existing site.

### 2. Upload with Git

The full video is about **29.5 MB (28.2 MiB)**. It is below GitHub's 100 MiB per-file limit, but above the browser's 25 MiB upload limit. Use Git or GitHub Desktop, not the browser's file uploader.

Run the following in this website folder, substituting your username in the repository URL:

```bash
git init -b main
git add .
git commit -m "Publish SUN and Kuafu project website"
git remote add origin https://github.com/USERNAME/USERNAME.github.io.git
git push -u origin main
```

Authenticate using GitHub's supported sign-in/token or SSH flow; do not put credentials in any website file. As a graphical alternative, use GitHub Desktop to add this folder as a local repository and publish it publicly with the same repository name.

Upload this folder's **contents at the repository root**, so index.html sits beside README.md. Do not upload the enclosing ZIP, original 282 MiB video, or the separate website-check folder. Keep .nojekyll. Use ordinary Git for the web video; no Git LFS is needed.

### 3. Enable Pages

In the GitHub repository, open **Settings → Pages**:

1. Under **Build and deployment**, choose **Deploy from a branch**.
2. Select **main** and **/(root)**.
3. Click **Save**.

The site will be available at **https://USERNAME.github.io/** after deployment, which can take up to ten minutes. This is a static site: there is no npm install, build command, custom workflow, or hosting server to configure.

GitHub Pages is public. This package includes the named authors, complete paper/appendices, figures, and video; review them before making the repository public.

Official instructions: [Creating a Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site), [publishing from a branch](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site), and [file-size limits](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).

## Edit and maintain

- **index.html**: narrative, publication data in the inline `site` object, navigation, lightbox, and citation-copy behavior. Keep static metadata/fallback text and CITATION.bib synchronized with the object.
- **styles.css**: responsive layout and academic styling.
- **assets/paper/SUN.pdf**: current identified arXiv manuscript, including appendices.
- **assets/videos/RAL_whole_long.mp4**: the complete 1080p project video.
- **assets/videos/poster.jpg**: an unaltered frame extracted at 12 seconds from the supplied full video.
- **assets/visual-models/**: four author-supplied source clips paired with textured-model turntables, their posters, and a provenance manifest. The example selector shows one pair at a time; all pairs remain visible without JavaScript.
- **assets/figures/**: original current-paper figures; PNGs for in-page display, with vector PDFs retained as unlinked source assets.
- **scripts/validate.py**: dependency-free file, link, terminology, and citation checks.

Code is marked **Code coming soon**, with no invented link. When a public repository exists, set `site.resources.code` to its real URL. No public arXiv identifier was supplied, so the arXiv label is inactive. Set `site.resources.arxiv` only to the real `https://arxiv.org/abs/...` landing page when available. Never substitute a direct PDF link. The citation uses a preprint BibTeX entry without an invented ID.

Do not add any download links or controls. Figures enlarge on the page, citations can be copied, and the video hides the native download control where supported. This removes download affordances; it is not access control over publicly served assets.

## Asset provenance

All scientific assets come from the supplied project materials. The cost-parity and time-break-even figures were regenerated from the paper's plotting script with the author's requested training terminology; their data, calculations, and layout are unchanged. Website assets are byte-for-byte copies of these current paper figures.

Figure 1 uses the author's updated 2252×1567 PNG (2026-09-23), with **MPC Verification** already embedded in the artwork. It is displayed unchanged on the page and in the lightbox, without a text overlay or generative edits.

| Website asset | Source |
| --- | --- |
| assets/paper/SUN.pdf | Compiled identified arXiv/main.tex and shared sections at 9ca9469 |
| assets/figures/chase_sun.png | Paper figures/chase_sun.png (Figure 1, shown prominently above the abstract) |
| assets/figures/pipeline1.png | Paper figures/pipeline1.png (main method figure) |
| assets/figures/sun_throughput.png and .pdf | Paper Appendix IV throughput figure |
| assets/figures/sun_cost_parity.png and .pdf | Paper Appendix IV cost-parity figure |
| assets/figures/sun_breakeven.png and .pdf | Paper Appendix IV time-break-even figure |
| assets/videos/RAL_whole_long.mp4 | Author-provided RAL_whole_long.mp4; approved full-length web encode |
| assets/videos/poster.jpg | Frame from the same author-provided video |
| assets/visual-models/ID/input.mp4 | Full-length 720×1280 web encode of kuafu_visual/video2assets/IMG_ID.mov, preserving frame count and audio |
| assets/visual-models/ID/input.jpg | Unchanged runs/ID/frames/frame_000.jpg from the same object recording |
| assets/visual-models/ID/model.mp4 and model.jpg | Unchanged runs/ID/turntable/turntable.mp4 and poster.jpg, rendered from the supplied photo-textured GLB |

The original website archive and original full-quality video are preserved outside this folder. Older website PDFs, figures, and video clips are not included in the rebuilt package.

The four video-to-model examples come from kuafu_visual commit `35f3e0e`: `0024` emergency-stop box, `0026` sage holder, `0028` bamboo organizer, and `0029` bamboo tray. Their model clips are eight-second, 720×720, 360° previews of the actual supplied photo-textured assets. They illustrate the visual-to-model component; they are not new experiments or accuracy measurements. Only the displayed clips and posters are copied into the website, not the original MOVs, GLBs, or ZIP packages.

`scripts/prepare_visual_examples.py /path/to/kuafu_visual` reproduces the web assets in a new/nonexistent assets/visual-models directory. It verifies upstream video/model hashes, preserves all source frames (158, 139, 194, and 151 respectively) and original AAC audio, and copies the turntables/posters unchanged. It requires FFmpeg/ffprobe and Python 3.11+, refuses to overwrite an existing output directory, and records file hashes and encoding details in the manifest. The original clips and model files are never modified.

The video retains all **3,928 frames**, at **1920×1080, 30 fps**, and its AAC audio is copied without re-encoding. It runs approximately **2 minutes 11 seconds**. MP4 container duration differs by about 0.03 seconds because of remuxed timing; no scene was cut. Web encoding uses H.264, CRF 23, maximum rate 4,600 kb/s, and fast-start metadata.

To reproduce the approved encoding from a source outside this repository, first choose a nonexistent output path:

```bash
ffmpeg -nostdin -n -i /path/to/original/RAL_whole_long.mp4 \
  -map 0:v:0 -map 0:a:0 \
  -c:v libx264 -preset medium -crf 23 \
  -maxrate 4600k -bufsize 9200k -pix_fmt yuv420p \
  -c:a copy -movflags +faststart /path/to/new-web-copy.mp4
```

## Result definitions

- **82.03%**: primary privileged controller's task-macro success over nine tasks.
- **10.57×**: task-macro successful trajectory minutes per active production hour relative to human teleoperation, after controller training.
- **+23.6 percentage points**: fixed-DP3 simulation, 500 successful demonstrations/task; Kuafu 46.02% versus SkillGen 22.44%.
- **34.0% / 106 physical trials**: six tasks and three robot–gripper configurations, DP3 trained with 1,000 generated trajectories/task, without real-world fine-tuning.
- **35.22 demonstrations**: mean taskwise whole-demonstration cost-parity threshold, including controller training; rounded to 35 in the main-text discussion.
- Cost assumptions: human teleoperation $7.25/hour; A6000 training and production $0.51/GPU-hour. Mean controller-training cost $6.95.
- **513 demonstrations / 29.1 minutes**: macro time-break-even summary, with collection time measured after training. This is distinct from monetary cost parity.

These are the paper's reported results and modeling assumptions, not new website experiments or current market-price quotations.

## Validate before publishing

```bash
python3 scripts/validate.py
```

Also test desktop/mobile layout, video playback and sound, figure enlargement, keyboard navigation, and citation copying. The finished package contains no analytics, third-party fonts, or external runtime scripts.
