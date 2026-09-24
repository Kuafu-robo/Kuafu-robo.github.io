# Repository instructions

## Scope and architecture

This dependency-free project website accompanies **SUN: Agentic Robot Policy Learning with Persistent Task Programs**. The author requested a concise rewrite using the current identified arXiv manuscript and its figures, with the complete RAL_whole_long project video. The subsequent request adds four supplied video-to-model examples between the method pipeline and Data Generation. This supersedes the original archive's anonymous-release and legacy-asset instructions.

Before editing, read README.md, index.html, styles.css, and scripts/validate.py.

- Keep publication metadata and browser behavior in the single inline script's `site` object in index.html.
- Keep runtime dependency-free: HTML, CSS, native JavaScript, local media.
- Keep meaningful static HTML fallbacks, relative asset paths, and .nojekyll.
- Default deployment is the account-level USERNAME.github.io site, from main and /(root). No custom Actions workflow or build system is needed.
- Do not invent an arXiv identifier, public source-code URL, author profile links, or publication venue.
- The author prohibits all download links and controls. Do not add direct links to PDFs, images, videos, archives, or BibTeX files. Enlarge figures in-page, provide citation copying only, and keep the video control set to nodownload. The arXiv label stays inactive until a real arXiv abstract-page URL is supplied; never substitute a local PDF link.

## Scientific integrity

- SUN Program is the persistent typed task representation. Kuafu is the robotics execution and learning harness.
- Use MPC verification, Stage-BC, bounded residual RL, SkillGen, and Isaac SkillGen.
- Distinguish MPC objective terms, satisfaction predicates, and RL learning costs. Do not equate the RL reward with a negated MPC cost.
- The task-level agent repairs programs and calibrates permitted scalars. Controllers execute individual control steps.
- The visual learner receives observations and actions alone, not SUN stage labels or privileged state.
- Keep the 500-trajectory simulation budget distinct from 1,000 trajectories/task for physical deployment.
- Check results against the current paper tables. Do not infer a separate causal benefit for the agent packaging itself.
- Source mapping and metric definitions are documented in README.md.

## Assets and presentation

- Use project-owned figures unchanged, with meaningful alt text, captions, original aspect ratios, and full-resolution enlargement.
- Do not redraw experimental plots or alter raster figure labels without specific approval.
- Display the paper's Figure 1 (chase_sun.png) prominently below the publication links and before the abstract. Use the author's updated 2252×1567 PNG directly, including its MPC Verification label, in both the page and the lightbox; no text overlay is needed. The method workflow remains pipeline1.png. Do not regenerate or retouch the experimental imagery.
- Keep assets/videos/RAL_whole_long.mp4 as the sole full project video, using the approved full-length 1080p copy with its original audio. The author also approved the four object-video/model demonstrations from kuafu_visual. Include only their eight displayed clips and corresponding posters in assets/visual-models, with no raw model, archive, or video download links. Source materials remain untouched outside this website.
- Place the object comparisons after the method pipeline and before Data Generation. Pair the supplied source videos with their actual textured-model turntables. These are illustrative reconstruction examples, not additional task-performance measurements. Keep all four pairs accessible with scripting disabled; pause hidden clips and respect reduced motion.
- The local paper PDF is the identified current arXiv version, including appendices.
- Keep the page focused: publication metadata and Figure 1, abstract, full video, method, video-to-model examples, results/plots, citation. The three data-generation plots include relevant passages from the paper, with their table-panel and section references.
- Source the three plot descriptions from the main-text discussion in Section IV-C, not the appendix. Use the author's requested training terminology in the website descriptions and both break-even plots; preserve their reported data and calculations.
- Display all result plots directly on the page; do not hide them behind expandable headings or disclosure controls.
- Keep the workflow figure large at the full content width (1120px maximum), with its natural aspect ratio. Only the latter three data-generation plots use matching, centered display frames (900px maximum width, 1.8 aspect ratio), stacked vertically. Preserve plot proportions with object-fit: contain; do not crop or stretch the data.
- Use a white academic layout, restrained blue, thin rules, real research figures, and native video controls.
- Respect reduced motion. Preserve keyboard focus, the skip link, lightbox focus return, and citation status announcements.

## Verification

1. Run python3 scripts/validate.py.
2. Preview through a local HTTP server.
3. Check desktop and mobile, including 320px width, for horizontal overflow.
4. Exercise video playback/seeking, navigation, image enlargement/Escape, citation copying, and keyboard focus.
5. Check all assets, enforce the no-download-links requirement, and verify no file exceeds GitHub's 100 MiB limit.
6. Keep test dependencies, screenshots, original archives, and source videos outside the upload folder.
