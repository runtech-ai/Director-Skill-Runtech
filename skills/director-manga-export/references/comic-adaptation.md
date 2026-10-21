# Adapt the film into a comic

## Source and traceability

Read the root manifest and referenced authoritative shot/dialogue records. Do not assume every package uses the same nested keys, or scan all duplicate JSON copies as separate scenes. The source package stays immutable. Work in a sibling `comic-export/` directory with `comic-plan.json`, `art/`, `lettering/`, `pages/`, `output/` and `validation.json` as needed.

The comic plan is an internal authoring record, not a new RunTech importer schema. Record:

- Source path/hash, recorded Director profile, episode and selected scenes/segments.
- Format brief: manhwa/manga, color treatment, language, panel reading direction, trim size, intended screen/print use and page style.
- Ordered chapters/pages/panels with stable comic IDs; each panel maps to episode-qualified scene/segment/shot IDs and the pictured instant or state transition.
- For each panel: narrative purpose, framing, occupants/eyelines, expression, anatomical hand ownership, props/support, entry/exit state, canonical reference roles and reserved text space.
- A dialogue ledger with unique source line IDs, exact text, speaker, on/off-panel delivery and ordered bubble assignments; include captions and meaningful source sound effects separately.
- Page image paths/hashes, lettering source, coverage decisions, review results and pending repairs.

Match source coverage by IDs and meaning, not by number of panels. Repeated source records are not repeated lines. Mark coverage as represented, merged into a named panel, or explicitly omitted by the user's requested scope. Every necessary event, reveal, injury, transfer and causal outcome must remain understandable without the film. If the source lacks stable line IDs, create local IDs from episode/segment/line index; do not write them into the source package.

## Page grammar

Apply [dialogue and page design](dialogue-page-design.md) as the default for both modes unless the user specifies another layout. Record the layout preset, balloon groups, gutter dialogue regions, border-break bounds and safe pagination boundaries in the comic plan. The bundled examples provide layout and rendering guidance only; they never supply story, cast or dialogue to a Director adaptation.

Use panel size, gutters, close-ups, silent reaction panels and page turns to control reading pace. Film duration is a rhythm cue, not a fixed seconds-to-panels conversion. Avoid packing every micro-shot onto a rigid grid. A sustained action can become several readable instants; multiple camera views of one unchanged beat can become one panel.

For manga, establish right-to-left panel and balloon order when selected, with clear row grouping and screen-tone values that separate characters and props. For manhwa, use the selected left-to-right page flow or top-to-bottom scroll flow and a consistent color/lighting palette. Neither mode requires changing the characters' ethnicity, clothing, age or setting. In monochrome, translate canonical colors to consistent distinguishable values/patterns while retaining source color metadata for identity.

Never mirror finished artwork merely to change reading direction: that swaps anatomical hands, prop mechanisms, injuries and signs. Compose the panel for the reading direction instead. Preserve world geography across camera changes. A reaction insert must not reset a handover or restart an already completed action.

Use an establishing panel at meaningful location changes and larger panels for consequential actions/reveals. Page turns should support the source reveal order. A cover, title page or chapter opening may be added when useful, but must not replace story pages, invent story events or spoil a protected reveal. Record covers separately from narrative coverage.

For the default vertical layout or any requested webtoon/vertical strip, plan the scroll's spacing and transitions first. Repaginate the PDF at deliberate gutters; recompose oversized panels before export. Never slice through a balloon, face or action merely to fit a standard sheet. Keep PDF pages in logical reading order even for right-to-left manga; reading direction does not mean reversing the book's page list.

## Continuity and mechanics

Load applicable project canon/physics when the package needs it, rather than baking one franchise into this global skill. Preserve identity, costume, anatomy, injuries, population, prop count, support, ownership, orientation, motion and damage across panels. A hidden object remains hidden until the source reveals it; its canonical image does not require an extra visible instance.

Show causal action in readable instants: preparation, the decisive interaction and its consequence. Motion lines cannot justify floating detached parts, changed hand ownership, teleportation or spontaneous movement. Use only the canonical references needed by the current panel/page and identify whether each supplies identity, design, layout or physical state. Multiple views of one subject do not authorize multiple bodies.

## Dialogue and lettering plan

Keep exact line text and ownership. When a long line crosses multiple film shots, distribute it once across successive balloons; concatenating the assigned pieces in reading order must reproduce the original line, allowing only layout whitespace. Do not silently translate, paraphrase, rewrite punctuation or add conversation to fill a page. If a page is crowded, add space or panels/pages before reducing type below a readable size.

Give speech balloons unambiguous tails to their speaker; off-panel voices use an appropriate off-panel tail or source-supported label. A listener is not a speaker because their face is visible. Preserve silence beats. Voice identity/timbre cannot be heard in a PDF: convey authored delivery through expression, posture and restrained typography without promising audio fidelity or changing the words. Music instructions do not become invented lyrics or narration. Keep source-supported sound effects distinct from dialogue.

Make illustration prompts picture-specific: page/panel intent, exact visible cast and props, canonical references, composition, style, light, action instant, state and reserved balloon regions. Keep source identifiers, camera metadata and H3 labels out of visible artwork. When generating a page, specify its panel order/gutters; when generating individual panels, compose them according to the page plan. Validate actual pixels before lettering or promoting any image to accepted state.

