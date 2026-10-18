---
name: director-manga-export
description: Adapt an existing Director package into illustrated manhwa or manga and export a finished PDF. Use for Director-to-comic, manwa/manhwa, manga, graphic-novel or comic-book PDF requests, including selected scenes or full episodes. Preserves source story, dialogue ownership and canonical assets while creating a separate comic page plan.
metadata:
  compatibility: Requires image generation for new artwork and a file-capable Python runtime for PDF export. Bundled exporter uses Pillow, ReportLab and pypdf; no RunTech connection is needed for a complete local package.
---

# Director package to manhwa or manga

Turn an existing Director ZIP or extracted package into a readable, illustrated comic PDF. A request to add or edit this skill only changes the skill; it does not start a book or mutate a movie. A request to convert a package authorizes planning, artwork, lettering and local PDF export within the requested scope.

## Resolve the source and format

Inspect the actual manifest and its referenced scene, segment, shot, dialogue and asset records. Follow declared order, not filename sorting. For a series, qualify source IDs by episode. Record the package revision/hash and selected scope. Read the applicable Director schema only as needed to interpret the existing v9/v10/v11 package; do not re-author it under a different profile. Resolve conflicting redundant copies before using them as source.

Use the original canonical character, prop and location images. A text-only package may require the user's connected asset library or supplied images; discover supported retrieval tools when needed. Existing storyboards are staging evidence, not automatically canonical identity or finished comic art. If required source or canonical assets cannot be obtained, complete the supported planning work and report the precise gap; do not invent replacements or silently omit scenes.

Honor the requested language, style, reading direction, page size and scope. Treat “manwa” as manhwa in this context. When unspecified, use these stated, adjustable defaults: **manhwa = color, left-to-right paginated pages; manga = monochrome linework/screentones, right-to-left panels; A5 portrait PDF**. If no mode is implied, state a color manhwa default and proceed. These are workflow defaults, not rules about every comic. Preserve the source language unless translation is requested. A vertical-scroll request uses a scroll plan with a separate PDF pagination pass at panel/gutter boundaries.

## Adapt and illustrate

Read [comic adaptation](references/comic-adaptation.md). Save a compact `comic-plan.json` with the source map, ordered chapters/pages/panels, canonical assets, dialogue ledger and current acceptance state. Keep this derivative output outside the input Director package. Film shot counts, timings, inverse storyboard aspect and single-column board rules remain properties of the film; they do not dictate comic page layout.

Map every in-scope story beat and line to a page/panel. Merge redundant film coverage or split an action into readable setup/action/reaction panels when needed, without changing event order, outcomes, speaker, prop state or character knowledge. Preserve exact dialogue once in reading order, including lines that crossed film cuts. Do not silently abridge a long package to a sample or synopsis.

Use the available built-in image generator for new illustrations and visual repairs, following its current skill/tool contract. Generate page by page or panel by panel with a shared style brief and only the required canonical references. Inspect local references before edits. Reserve lettering space and prefer art without generated text; apply exact dialogue as a separate typeset layer. Do not invent image-model parameters, use an API fallback without the user's authorization, or claim a backend/resolution the tool did not report.

Review each page's identity, anatomy, location, physical causality, prop support, reading order and expression against its source. Carry accepted state between pages, not an unreviewed prior image. Preserve concealed props and silent listeners. If a repair introduces another defect, recheck the full page. After two unsuccessful repairs to the same defect, revise the layout/reference strategy before another attempt; if the available route cannot satisfy a required constraint, save progress and report the blocker.

## Letter, export and verify

Read [PDF production](references/pdf-production.md) for lettering, pagination and export. Use an available PDF skill/runtime when present; this reference and the bundled helper support environments without that skill. Generate actual page artwork and a finished PDF, not just prompts or a PDF of the shot-plan text.

The [PDF assembler](scripts/assemble_comic_pdf.py) combines already lettered page images in explicit manifest order. It validates files, geometry, resolution and PDF page count; it does **not** generate art, compose panels, add dialogue, certify story fidelity or make searchable text. Use a vector-text PDF workflow instead when searchable/selectable text is requested. Preserve editable lettering sources in either route.

Render and inspect every final PDF page at readable scale. Check source coverage, verbatim dialogue/speaker placement, legibility, tails, gutters, chapter/page order, margins, clipping and actual image resolution. Record separate source, artwork, lettering and PDF checks; file creation alone is not acceptance. For a long book, checkpoint per chapter and continue to the full requested scope; missing pages remain explicitly incomplete.

Deliver the PDF with a clickable file link, page/chapter count, chosen mode/reading direction and any material limitation. Keep the page plan, art, lettering source and validation report alongside it for revisions. Do not upload the comic, overwrite the Director package, generate video, or change RunTech records unless that is separately requested.
