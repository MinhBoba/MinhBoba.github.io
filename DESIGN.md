---
name: mdrat
description: Notes and work in machine learning, math, data and systems, set as a research article's figures.
colors:
  ink: "#15171c"
  ground: "#fdfdfc"
  muted: "#545c6a"
  rule: "#dcdcd6"
  rule-strong: "#15171c"
  wash: "#f3f3ef"
  ink-ml: "#c8402a"
  ink-math: "#2f5bd3"
  ink-data: "#17784e"
  ink-system: "#7a4cc2"
  ink-lab: "#15171c"
  band: "#102a5c"
  band-ink: "#ffffff"
  band-muted: "#c9d4ea"
  code-ink: "#8a2d1c"
  ink-dark: "#e8e7e2"
  ground-dark: "#121417"
  muted-dark: "#a9afba"
  rule-dark: "#2c3038"
  rule-strong-dark: "#e8e7e2"
  wash-dark: "#1b1e23"
  ink-ml-dark: "#ff7a5c"
  ink-math-dark: "#8aaeff"
  ink-data-dark: "#4cc38a"
  ink-system-dark: "#b59aff"
  ink-lab-dark: "#e8e7e2"
  band-dark: "#1a3566"
  band-ink-dark: "#f2f4f8"
  band-muted-dark: "#b9c6e2"
  code-ink-dark: "#ffb199"
typography:
  display:
    fontFamily: "Hanken Grotesk, system-ui, sans-serif"
    fontSize: "31cqi"
    fontWeight: 800
    lineHeight: 0.82
    letterSpacing: "-0.04em"
  headline:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "1.5rem"
    fontWeight: 600
    letterSpacing: "-0.012em"
  title:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "1.05rem"
    fontWeight: 600
  body:
    fontFamily: "Source Serif 4, Georgia, Times New Roman, serif"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: 1.6
  lede:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "1.12rem"
    fontWeight: 400
    lineHeight: 1.55
  caption:
    fontFamily: "Source Serif 4, Georgia, serif"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Hanken Grotesk, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.8rem"
    fontWeight: 600
  chrome:
    fontFamily: "Hanken Grotesk, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1rem"
    fontWeight: 500
  code:
    fontFamily: "JetBrains Mono, ui-monospace, Cascadia Code, Consolas, monospace"
    fontWeight: 400
rounded:
  none: "0px"
  hairline: "2px"
spacing:
  title-rule-gap: "0.55rem"
  row: "0.7rem"
  plate-gap: "2rem"
  section: "3rem"
components:
  page-title-rule:
    backgroundColor: "{colors.rule-strong}"
    width: "2.75rem"
    height: "3px"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.chrome}"
  figure-caption:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  ledger-header:
    textColor: "{colors.muted}"
    typography: "{typography.label}"
    padding: "0 1rem 0.4rem 0"
  ledger-cell:
    textColor: "{colors.ink}"
    padding: "0.7rem 1rem 0.7rem 0"
  lab-plate-frame:
    backgroundColor: "{colors.wash}"
    rounded: "{rounded.none}"
  callout:
    backgroundColor: "{colors.ground}"
    rounded: "{rounded.hairline}"
    padding: "0.7rem 0.9rem 0.6rem"
  callout-header:
    backgroundColor: "{colors.wash}"
    typography: "{typography.label}"
    padding: "0.5rem 0.9rem"
  slot-published:
    backgroundColor: "{colors.ink-ml}"
    height: "1.6rem"
  domain-mark:
    backgroundColor: "{colors.ink-ml}"
    width: "0.9rem"
    height: "3px"
---

# Design System: mdrat

## Overview

**Creative North Star: "The Figure Journal"**

Every page is a page from a research article. The home page opens with a navy title card (mdrat, "Minh · Digital notebook for learning and researches") beside a Start-here list, then the notes map with one row per domain, the concept graph, and the Lab. No page carries numbered captions ("Figure 1", "Table 1") or a written-up / planned legend, and nothing unwritten is drawn (owner, 2026-11-22). Home follows the owner's image (owner's layout, 2026-11-22, replacing the collection-only Home of 2026-11-21). Tab pages carry the same notes map, one row per course; tab pages list their contents as ruled ledgers. Reading comes first: a serif body at a generous 18px, a grotesk only for labels and chrome, a mono only for code. The page is near-white paper (dark: near-black slate) with ink type and hairline rules.

Colour is semantic, never decorative. Four domain inks name the four study domains, Machine Learning, Math, Data and System, and appear wherever that domain is meant: lane labels, slots, the rule under a tab's title, the domain mark in a ledger row, prose links inside that tab. The Lab has no hue of its own; it is set in ink. Everything else is ink, muted grey and rule.

Depth comes from rules and overlap. Heavy 2px ink rules open a figure or table; 1px hairlines separate its rows. Nothing floats: no shadows, no gradients, no card chrome. Status is drawn, not coloured: a solid fill is written up, a dotted outline is in progress, a dashed outline is planned. On Home it shows only as the filled and dashed parts of each domain's bar.

**Key Characteristics:**
- Serif reading voice (Source Serif 4) for body, headings and captions; Hanken Grotesk for labels and chrome; JetBrains Mono for code only.
- Four semantic domain inks, each with a light and a dark value; Lab in ink.
- Status by line form (solid, dotted, dashed), never by hue.
- Flat paper: 2px ink rules open blocks, 1px hairlines divide rows, no shadows or gradients.
- A short domain-ink rule under every page title.

## Colors

Ink on paper, with four semantic inks that each mean exactly one domain.

### Primary
- **Ink** (#15171c; dark #e8e7e2): body text, headings, default link colour, the Lab's domain ink, heavy opening rules, and the navbar's active underline outside a domain.

### Secondary
- **Vermilion, Machine Learning** (#c8402a; dark #ff7a5c): everything that belongs to the ML domain.
- **Cobalt, Math** (#2f5bd3; dark #8aaeff): everything that belongs to Math; also the selection tint on pages without a domain.
- **Field Green, Data** (#17784e; dark #4cc38a): everything that belongs to Data.
- **Violet, System** (#7a4cc2; dark #b59aff): everything that belongs to System.

### Neutral
- **Paper** (#fdfdfc; dark #121417): page, navbar and footer ground.
- **Graphite** (#545c6a; dark #a9afba): captions, ledger dates, table headers, lane notes, ledes, legend samples.
- **Hairline** (#dcdcd6; dark #2c3038): 1px row rules, navbar and footer rules, plate frames, callout borders.
- **Wash** (#f3f3ef; dark #1b1e23): code background, empty plate frames, callout headers. The only tinted surface.
- **Code Rust** (#8a2d1c; dark #ffb199): inline code text.

### Named Rules
**The One Ink Per Domain Rule.** A domain ink appears only where that domain is meant, set through the `domain-*` class (lane, ledger row, tab page body). It never decorates a neutral element, and two domains never share an ink.

**The Status Is Line Form Rule.** Written up, in progress and planned are told apart by solid fill, dotted 2px outline and dashed 1.5px outline. The legend draws its samples in ink and graphite so it keys form, not colour.

## Typography

**Display Font:** Source Serif 4 (with Georgia, serif)
**Body Font:** Source Serif 4 (with Georgia, Times New Roman, serif)
**Label/Chrome Font:** Hanken Grotesk (with system-ui, Segoe UI, sans-serif)
**Code Font:** JetBrains Mono (with ui-monospace, Cascadia Code, Consolas, monospace)

**Character:** A journal serif carries every sentence a reader studies; a plain grotesk does the cataloguing work of labels, axes, headers and navigation, the way a journal sets its figure furniture.

### Hierarchy
- **Display** (Hanken Grotesk 800, 31% of the title card's inner width, 0.82, -0.04em): the site's name on Home's title card only; every other heading is serif.
- **Headline** (600, 1.5rem on Home; Bootstrap scale elsewhere, -0.012em, balanced wrap): section heads, each sitting under a 1px hairline on Home.
- **Title** (600, 1.05–1.1rem): ledger page links and listing titles, in serif.
- **Body** (400, 18px root, 1.6): all reading text. Ledes run 1.12rem at 1.55 in graphite, held to 58–60ch.
- **Caption** (italic 400, 0.9–0.95rem, 1.5): figure and table captions in graphite, held to 72ch.
- **Label** (Hanken Grotesk 600, 0.8rem): table headers, axis text (0.75rem), legend (0.82rem), lab status (0.8rem). Lane labels step up to 700 at 1.02rem in their domain ink.

### Named Rules
**The No Numbers Rule.** Figures, tables and plates carry no "Figure N" or "Table N" label and no status legend. Tables keep an accessible name.

**The Mono Is For Code Rule.** JetBrains Mono appears only in code blocks and inline code; numbers in tables use the grotesk with tabular figures instead.

## Layout

Home runs full-width with every block held to a 74rem measure. The opening is a two-column grid: the title card at minmax(0, 1fr) and the Start-here list at minmax(14rem, 18rem), gap clamp(1.25rem, 2.2vw, 2rem). The list opens with a 2px ink rule. The concept graph is centred at its natural size within the measure, directly under its section head.

The notes map is three columns per row: name (10.5 to 16rem), blocks (1fr), note (12 to 18rem), 1.5rem gutter. Lab plates use an auto-fill grid of minmax(16rem, 1fr) with a 2rem gap; the empty state spans the row. Ledgers are fixed-layout tables with date (8.5rem) and domain (11rem) columns so stacked ledgers align; undated ledgers give the page column 45% and extra field columns share the rest.

Sections on Home and tab pages share one rhythm: 3rem between level-2 sections, with listings adding no margin of their own.

Below 760px the opening and the empty Lab plate collapse to one column; the notes map stacks name, blocks and note; ledgers drop the domain column (and its ink mark), keeping date and page.

## Elevation & Depth

The system is flat. There are no shadows and no gradients anywhere; Bootstrap's navbar and callout shadows are explicitly removed. Hierarchy and grouping come from rules: a 2px ink rule opens each figure, table header and the Start-here list (on Home the same 2px rule opens Overview, Concepts and From the Lab); 1px hairlines separate rows, the navbar, the footer and section heads. The one tonal surface is Wash, used for code, empty plate frames and callout headers. In-progress slots use a 14% mix of the domain ink as a faint fill under the dotted outline.

### Named Rules
**The Paper Rule.** Nothing lifts off the page. If an element needs separation, give it a rule, not a shadow; if it needs emphasis, give it ink weight, not elevation.

## Shapes

Square by default. Listing cards, plate frames and category labels have 0 radius; callouts, code blocks and focus outlines take a 2px (hairline) corner at most. Recurring geometry is linear: the 2.75rem × 3px title rule, the 0.9rem × 3px domain mark in ledger rows, and slot rectangles separated by 3px gaps.

## Components

### Navigation
- **Style:** Paper ground, 1px hairline below, no shadow. Brand set in Source Serif 4 700 at -0.01em; links in Hanken Grotesk 500.
- **Menus:** Lab, Machine Learning, Data and System open dropdown menus (Overview, courses, sections) rather than navigating; Math is a plain link until it has a course. Menus are paper with a 1px hairline and a 2px top rule in the tab's domain ink, no shadow, 0 radius; items hover to Wash with domain-ink text; headers are grotesk 600 at 0.75rem in graphite, sentence case. Toggles are exposed to assistive tech as buttons.
- **States:** Hover, an open menu and the tab you are inside keep the text in ink and draw a 2px underline in the tab's domain ink (ML, Math, Data, System); Home and Lab underline in ink.

### Page Title
- **Style:** Serif title at -0.02em with a short domain-ink rule beneath (2.75rem × 3px, 0.55rem gap). Pages without a domain draw the rule in ink. Home hides the title block and leads with the owner's name instead.

### Links
- **Default:** Ink, 1px underline offset 0.18em; hover thickens the underline to 2px.
- **Inside a tab:** Prose and list links and the active sidebar item take the tab's domain ink; the Lab keeps them in ink.
- **Focus:** 2px outline in the domain ink (ink outside a domain), 3px offset.

### Concept Graph (Home, signature)
A static SVG laid out at render time by `_templates/concept-graph.ejs` (deterministic force layout; no browser JS), from published pages only. It is a hierarchy: **Tab → Topic → Lecture** (owner, 2026-11-22; concept nodes were removed).
- **Levels:** a tab (Machine Learning, Math, Data, System) is a 9px filled dot in its ink and links to the tab; a topic (the course folder, labelled by the page subtitle, e.g. "Classical ML") is a 6px ring (2.5px stroke) and links to the course page; a lecture is a 5px filled dot and links to itself.
- **Labels are hidden at rest.** Pointing at or focusing a node shows its label, the labels of all its ancestors (every path up to its domains) and of its direct children only; everything else dims to 18% opacity. The reveal is CSS: the template emits one `:has()` rule per node, and the dim rule sits in `:where()` so the reveal outranks it. Touch screens (`hover: none`) show every label instead. Every link carries an `aria-label`, so hidden text never leaves a link unnamed.
- **Label type:** tab serif 600 14px; topic grotesk 600 12px; lecture serif 600 12.5px. A label sits on the side away from its node's lines (below the dot when they leave upwards), on a paper box. Layout reserves every label's box, so no reveal overlaps another.
- **Layout:** a force layout with tabs pinned at stable anchors; no label overlaps another and no line touches a dot it does not join (checked on mocks of 23 and 36 nodes).
- **Key:** an HTML row above the graph (so it never pans away): only the domains present, each as a dot in its ink with its name (grotesk 0.85rem graphite). No shape legend and no hint text (owner's call, 2026-11-21).
- **Edges:** 1.25px lines at 70% graphite on paper (3.3:1 light, 4.7:1 dark). The pointed-at label is its domain ink mixed 92% with ink.
- **Focus:** a separate 2px ink ring on an invisible hit circle (dot radius + 7), which is also the pointer target.
- **Structure and keyboard:** dots and links sit in hierarchy order (tab, topic, lecture), which is the tab order; labels live in a separate top layer (`.cg-labels`, pointer-events off), so a revealed label is never painted under another dot and the pointer always targets dots. Every label keeps 16px clear of other dots, so it reads as its own dot's. A visually hidden "Skip the concept graph" link (shown on focus) jumps past the graph. Dragging has no keyboard equivalent by design; every node remains a link.
- **Dragging nodes:** the one script on the site (inline, no library; progressive enhancement). Grabbing a node moves it, with its label, and its edges stay attached; the dot stays inside the figure; a click without a drag still follows the link. The canvas itself does not move or zoom. Moved nodes are not saved; a reload restores the layout (no Reset button, owner's call 2026-11-21). The script also undoes Quarto's `link-external-newwindow`, which misreads SVG links as external and would open every node in a new tab.
- **Size:** centred, up to 1.1 times natural width on Home. In a column narrower than 80% of natural width it becomes a ruled list (domain dot, serif page title, "Domain · Topic" in ink).

### Concepts page (`concepts.qmd`)
Generated by `_templates/concepts.ejs` from each page's `index:` header (fallback: categories minus the topic label). No page links to it since the graph dropped its concept nodes; it is reachable through search. A–Z under serif letters (1.5rem) in a 2.5rem gutter, one hairline-separated row per letter. Each concept is an anchored entry (serif 600 term) listing its pages as ink links underlined in the domain ink, each with a grotesk graphite locator (topic label behind a 0.9rem × 3px domain mark). An entry opened by its anchor is marked on Wash via `:target`, without motion.

### Lab Plates
Each item is one complete captioned plate: a 4:3 frame with a 1px hairline (ink on hover), image covering, or a large serif initial on Wash when there is none; then a serif title and a grotesk status tag marked by a left border in line form (3px solid, 2px dotted, 2px dashed). The empty state is a skeleton table with dashed placeholder cells beside its caption: Metric / Paper / Mine for reproductions, Problem / Approach / Stack for projects. On Home (`caption: false`) figure numbers and the empty caption are dropped; the empty plate is the table with an "Open the Lab" link beneath and an accessible name of its own.

### Ledger (tab pages)
A ruled table with the caption below, generated from page headers; an empty ledger keeps its header and one italic "nothing yet" row. Optional columns (time and space for DSA; language, difficulty and pattern for problems) render in graphite. Grotesk headers in graphite under a 2px ink rule; 1px hairline rows; dates in graphite with tabular figures; domain column with a 3px ink mark before the domain name; page titles as serif 600 links in ink whose hover underline takes the domain ink; subtitles in graphite.

### Listing Cards (tab pages)
No card chrome: transparent ground, no border except a 2px ink rule on top, 0 radius, body padded 0.75rem above only. Title underlines on hover. Categories render as plain graphite text at 0.85rem with no pill, no border and no uppercase.

### Callouts
- **Style:** 1px hairline box on all four sides, 2px radius, transparent body, no side stripe and no shadow. Header in grotesk on Wash with a hairline below.

### Title Card (Home)
The left two thirds of the opening: a square navy card (--mj-band #102a5c; dark #1a3566) holding "mdrat" (the page's h1) in Hanken Grotesk 800 at 31% of the card's inner width, -0.04em, 0.82 line height, in --mj-band-ink, and the owner's line beneath in 600 at 4.05% (1rem to 1.6rem) in --mj-band-muted. Type uses container units, so the name keeps the same share of the card at every width. GitHub sits under the card. No shadow, border or gradient. The band tokens appear nowhere else.

### Start Here (Home)
A generated list under a 2px ink rule beside the title card: the latest lecture, up to two courses with written-up lectures ("Course, 1 lecture written up"), and the Lab. Each item is a serif 600 link in ink with a grotesk graphite line beneath, led by a 0.9rem × 3px domain mark; rows separated by hairlines. Drafts never appear.

### Notes Map (Home and tabs)
Only lectures written up (`_templates/notes-map.ejs`). One row per domain on Home, one per course on a tab: the name in its domain ink, one filled block per lecture (2.4 x 1.6rem, 5px apart, linking to it; a dotted block for `status: in progress`), and a note with the count ("2 lectures"), plus the latest lecture on tab pages only. On Home it sits under an "Overview" head. No totals, planned slots, axis, legend or caption. A domain or course with nothing written is left out; a tab with none says "Nothing written up yet." Below 760px each row stacks.

### Page widths
Set in `_quarto.yml` (`grid`): left menu 340px, body up to 1200px, right-hand list 140px, gutter 0.75rem, so the writing area is 987px at a 1440px window. Menu entries sit about 38px apart.

## Do's and Don'ts

### Do:
- **Do** put a domain's work under its `domain-*` class so lane labels, slots, title rules, focus rings and prose links pick up the right ink automatically.
- **Do** show only what is written; never a course's full lecture list as placeholders.
- **Do** separate with rules: 2px ink to open a block, 1px hairline between rows.
- **Do** keep reading text in Source Serif 4 at 18px / 1.6 and hold captions and ledes to 58–72ch.

### Don't:
- **Don't** use shadows or gradients on any element.
- **Don't** use hue to encode status, and don't give the Lab a colour of its own.
- **Don't** use a domain ink outside that domain, or as decoration on neutral elements.
- **Don't** put eyebrow or kicker labels above headings.
- **Don't** list individual courses in Home's lecture map; it is grouped by domain (Start here may name a course).
- **Don't** set body, headings or captions in the grotesk, or anything but code in the mono.
- **Don't** add card chrome (borders, fills, rounded corners) to listings; a top rule is the whole container.
- **Don't** use pill or uppercase category tags, or callouts with a coloured side stripe.

### Study-page tools

- **Notation panel:** on Math and Machine Learning pages only. A paper tab on the right edge (a corner label on phones) opens a flat paper panel with a 2px domain-ink rule, grotesk section heads in domain ink, and hairline rows of KaTeX symbol and graphite meaning. No shadow, no slide; it opens closed on every page. KaTeX loads on demand (`_includes/katex-loader.html`) on pages without maths of their own.
