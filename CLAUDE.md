# MJ2706 — Personal portfolio and learning hub

Static Quarto website on GitHub Pages. The full spec is in `MJ2706.pdf`; this file is its working summary.

## Stack and hosting
- Quarto website project, configured in `_quarto.yml`. Content is `.qmd` files with YAML headers.
- GitHub Actions (`quarto-dev/quarto-actions`) renders and publishes to the `gh-pages` branch. Never commit `_site/` or `docs/`.
- `freeze: auto` for executable notebooks; commit `_freeze/`.
- Reference structure: ickma2311/ickma2311.github.io (copy its structure, not its hand-written navbar, card grids, or committed `docs/`).

## Site map (six navbar items; sidebars auto-generated per tab)
| Tab | Folder | Extras |
|---|---|---|
| Home | `index.qmd` | About (name, role, bio), generated Start-here list, study map, featured Lab plates |
| Lab | `lab/papers/`, `lab/projects/` | status: planned / in progress / reproduced / partial |
| Machine Learning | `ml/<course>/` | |
| Math | `math/<course>/` | formula-heavy |
| Data | `data/<course>/`, `dsa/`, `problems/`, `reports/` | problem bank by pattern, Power BI reports |
| System | `system/<course>/`, `case-studies/`, `applications/` | Mermaid diagrams |

## Conventions
- One page per lecture: `{{< video URL >}}` at the top, then notes, then a `## Sources` section. One video per page. Notes and sources always live inside the lecture/topic page; there are no tab-level Notes sections or Sources pages.
- Each page's media lives in a sibling `<page>-assets/` folder, so a page and its media move together.
- Listings build cards and counts from page headers. Never hand-write card grids or navbar entries per lecture.
- Custom pieces: shortcodes `animate` (still PNG, then GIF/WebM on play; caption and alt text required), `algo` (step player; build only after 3–4 algorithm pages exist), `powerbi` (lazy, responsive 16:9 iframe); a Lua filter for the shared footer.
- Animations stay under about 2 MB; commit the generating Python script beside the output.
- Code blocks are static (highlighted, foldable), mainly Python and SQL. Nothing runs in the visitor's browser.
- Power BI embeds use public or synthetic data only; never employer or client data.
- No page transitions, scroll effects or decorative motion.

## Design
- Visual world: "The Figure Journal" (chosen 2026-11-15). Source of truth: `DESIGN.md`, `PRODUCT.md`, and the Home brief in `.impeccable/surfaces/`. Use `/impeccable` for any design change.
- Tokens live in `theme/light.scss` / `theme/dark.scss`; components in `styles.css`. Each tab folder's `_metadata.yml` sets `body-classes: domain-<tab>` so pages pick up their domain ink.
- Navbar tabs are dropdown menus (Overview, courses, sections) defined in `_quarto.yml`; Math is a plain link until it has a course. When you add a course folder, also add one menu item for it there. `_includes/nav-a11y.html` exposes the menu toggles as buttons.
- Home and tab index pages are built by custom listing templates in `_templates/` (study map, Lab plates, ledger). Course `index.qmd` needs `course: true` and `lectures-total: N`; lectures should set `lecture: N` so they land in the right slot.

## Commands
- `quarto preview`: local live reload
- `quarto render`: full build (CI does this on push)
- `python scripts/check_videos.py`: confirms every YouTube embed can play on-site. Many university channels (e.g. Stanford CS229) disable embedding; for those, embed a companion video and link the original.
- Index pages (tab, course, sources) carry `kind: index` so listings can exclude them.

## Roadmap
Six phases, each ending deployed: 1 Foundation · 2 Learning pages · 3 Animation · 4 Lab · 5 Data and System extras · 6 Polish and launch. See the checklist in the PDF.
