---
version: 1
slug: "index-qmd"
primary_target: "index.qmd"
related_targets: ["styles.css","theme/light.scss","theme/dark.scss","_templates/start-here.ejs","_templates/concept-graph.ejs","_templates/lab-plates.ejs","_templates/notes-map.ejs"]
---

# Home (index.qmd)

Scope: the site's front door. Mode: Experience. Audiences equal: hiring visitors (credible depth in a minute) and learners (find and return to notes). World: the Figure Journal.

Constraints: no invented stats, logos, employers or testimonials; no flashy motion; not a CV page; not plain. Owner surname, photo, contact links and CV pending; "Minh" awaits confirmation. User decisions (2026-11-16): About content opens Home (no separate About page); no "Recently published" table; notes and sources live inside lecture/topic pages, not at tab level; navbar tabs open dropdown menus; Decision 2026-11-21 (supersedes the study map): Home is a collection, not a roadmap. No course list, no progress counts, no planned or empty slots on Home. "Start here" became "Latest additions"; Figure 1 became a concept graph (pages joined to the topics they work through); the Lab section is kept as is (owner reconfirmed 2026-11-21, empty skeleton and all). Later the same day: no numbered "Figure N." captions on Home; the concept graph carries a drawn key instead. Later again: the graph is a hierarchy, Domain → Topic → Page → Concept; labels are hidden at rest and pointing at a node reveals it, all its ancestors and its direct children (CSS only). Concept dots open their entry on a generated Concepts page (concepts.qmd). Later (owner's call): the opening is "Minh", "Digital notebook for learning and researches" (owner's wording), the introduction paragraph and GitHub, with Latest additions in the right column; a masthead title card was tried and reverted.

Redesign 2026-11-21 (owner): new visual world, keep the ideas (notebook, collection not roadmap, concept graph, Latest additions, Lab). Must stay exactly: the graph's behaviour (labels hidden at rest, hover/focus trace of ancestors + next level, node drag, domain-only legend). Success: a visitor trusts the depth within seconds. Text kept: "Minh", "Digital notebook for learning and researches", the introduction, GitHub. Owner decisions 2026-11-22: "The Lab" row removed from Latest additions (only real pages); index.qmd `description` kept as is, reproductions clause included; the Lab panel and its empty table stay; DESIGN.md is overwritten with this world (other pages still wear the Figure Journal until redesigned).

Owner's layout 2026-11-22 (from an annotated image; supersedes every earlier Home decision it conflicts with, including Poster Session, "collection, not a roadmap" and the removed Lab row): a navy mdrat title card where name, job title and introduction stood; Start here beside it; GitHub beneath; lecture counts kept but grouped by domain; then the concept graph (behaviour unchanged) and From the Lab.

Later 2026-11-22 (owner): no legends, no numbered captions on any page, no planned or total lecture counts ("I only note down what I learned"); wider writing area and left menu, more space between menu entries.

Also 2026-11-22 (owner): the notes map has the head "Overview" and no latest lecture on Home; a 2px rule opens each section; the graph is Tab → Topic → Lecture only, with smaller labels.

Also 2026-11-22 (owner): "Minh · " removed from the card, "mdrat" smaller, no job title or introduction; the Concepts A-Z page removed.

## Direction contract

THESIS: Home is the first page of a notebook-journal: the site's name as a title card, where to start, what is written per domain, then the concepts as a figure. It refuses the hero-plus-project-cards portfolio.

OWN-WORLD: The Figure Journal (near-white page, ink, Source Serif 4, hairline and 2px rules, four semantic domain inks, no shadows or gradients) plus one navy title card in Hanken Grotesk 800.

STORY: The visitor reads whose notebook this is, picks a starting point, sees the lectures written up per domain, and traces a topic into a lecture.

FIRST VIEWPORT: Left two thirds, the navy card with "mdrat" at under half of its width and "Digital notebook for learning and researches" beneath; right third, Start here under a 2px rule; GitHub under the card; then the notes map.

FORM: seed: none (pinned). "I want the design to be like the image"; "left the lecture count in, but group by machine learning / data/math/.... instead of small lecture/topic"; "add the new concept graph to this version".

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
