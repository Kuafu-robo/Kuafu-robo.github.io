# Repository instructions

## Scope and architecture

This dependency-free project website accompanies **SUN: Agentic Robot Policy Learning with Persistent Task Programs**. The author requested a concise rewrite using the current identified arXiv manuscript, its existing figures, and only the complete RAL_whole_long video. This supersedes the original archive's anonymous-release and legacy-asset instructions.

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
- The current main method figure is pipeline1.png. The older collage is deliberately excluded because its embedded terminology is stale.
- The only video is assets/videos/RAL_whole_long.mp4. The author approved a smaller full-length 1080p copy with the original audio. The source video and original ZIP remain outside this website, untouched.
- The local paper PDF is the identified current arXiv version, including appendices.
- Keep the page short: publication metadata, full video, method, results/plots, citation.
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
