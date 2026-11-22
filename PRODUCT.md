# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Two audiences, weighted equally (confirmed 2026-11-15):

- **Hiring managers and recruiters** evaluating an ML engineer / data scientist. They scan quickly for proof of skill: reproduced papers, shipped projects, depth of study.
- **Peers and learners** (engineers, students) who come for the lecture notes, formulas, algorithm animations and the Python/SQL problem bank, and return to them.

The owner also uses the site as a personal, public study hub.

## Product Purpose

A static portfolio and learning hub. It shows hands-on work (paper reproductions and GitHub projects in Lab) and organises learning material by domain (Machine Learning, Math, Data, System), with lecture videos, notes, formulas, code and animations on the same page. Success: a hiring visitor sees credible depth within a minute, and a learner finds and returns to useful notes.

## Positioning

Learning in the open, structured: each lecture page puts the video, the owner's notes, the maths and the code together, and Lab pages report reproduced results against the paper's reported ones. Home opens with the mdrat title card and Start here, then the lectures written up per domain, the concept graph of published pages, and the Lab; the work is the proof.

## Operating Context

- Content is authored as Quarto `.qmd` files in the Git repo; one file per page, folder decides the tab.
- Listings build index pages and cards from page headers; new content appears automatically.
- Hosted on GitHub Pages, rendered by GitHub Actions on every push.

## Capabilities and Constraints

- Six tabs: Home, Lab, Machine Learning, Math, Data, System. Data adds DSA, a problem bank by pattern, and Power BI reports; System adds case studies and applications.
- Static only: no backend, no runnable code in the browser. One approved exception (2026-11-21): a small inline script that lets visitors drag the Home concept graph's nodes; everything else, including its hover trace, is static. Formulas via KaTeX; code is static, highlighted.
- YouTube embeds only where the owner allows embedding (many university channels, e.g. Stanford CS229, do not).
- No page transitions, scroll effects or decorative motion; animation is limited to animated figures and algorithm step players inside notes.
- Power BI embeds show public or synthetic data only.
- English only for now; Vietnamese may be added later (undecided).
- Open decisions (from the build plan): custom domain, Manim vs matplotlib only, Power BI account, own vs curated lecture videos.

## Brand Commitments

- Site name: mdrat (renamed from MJ2706 on 2026-11-21). The owner presents as an ML engineer / data scientist.
- Owner presents as "Minh" (changed from "MinhJ" on 2026-11-21); Home's line under the name is "Digital notebook for learning and researches". GitHub: https://github.com/MinhBoba; site at https://minhboba.github.io.
- Public email, LinkedIn, photo and CV are not yet provided; do not invent them, and do not publish the owner's private email without confirmation.

## Evidence on Hand

- One complete lecture page: `ml/cs229/lecture02-linear-regression.qmd`.
- No Lab papers or projects written yet; no metrics, testimonials, employers or results exist. Do not fabricate any.

## Product Principles

1. Lead with the notebook: the title card, where to start, and only what has been learned and written up (no course totals or planned lectures), then the concept graph (owner, 2026-11-22).
2. Every claim of skill links to an artifact (a reproduction, a repo, a notes page).
3. Adding content must stay as cheap as dropping one Markdown file into a folder; no hand-maintained card grids or counts.
4. Reading comes first: notes, formulas and code must be comfortable to study in both light and dark themes.

## Accessibility & Inclusion

WCAG 2.2 AA: contrast, keyboard navigation, alt text on every figure and animation, reduced-motion respected.
