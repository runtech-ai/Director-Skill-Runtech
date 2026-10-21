---
name: director-pack-skills
description: Build importer-locked movie Director packages with the v9 contract, shot plans, H3 prompts and one storyboard per segment. Use for direct microdrama, Director packages, movie direction, shot plans and package storyboard beats.
metadata:
  compatibility: Codex and Claude Code. Read the v9 contract; h3-prompt-writing validates compiled prompts only.
---

# Portable Director plugin entrypoint

For a comic adaptation of an existing package, use [Director to Manhwa / Manga PDF](../director-manga-export/SKILL.md). That workflow creates a separate comic page plan, artwork, lettering and PDF; it preserves the source package and does not run film generation or apply storyboard grid rules to comic pages.

Read and follow [the complete bundled procedure](../../global/skills/director-pack-skills/SKILL.md). Resolve its references relative to its bundled file location.

The bundled global/director-contract.json supports Director v9. Preserve existing package provenance; do not silently convert an older package or claim v9 contract acceptance without the appropriate review.

Use bundled h3-prompt-writing for H3 validation. Read global/rules/storyboard-image-model.md and global/rules/asset-reference-authority.md from the plugin root before applicable work. This skills-only plugin does not install or authenticate a server. Use separately connected RunTech tools when needed. Project physics, canon and assets must come from the user's project or attachments; request missing required sources. Do not generate video unless explicitly authorized.



## Direct microdrama option

When the user says **direct microdrama**, follow [the microdrama series workflow](../microdrama-series/SKILL.md). Start from a summary, develop full episode stories with chapter-writing and supporting story skills, then return here for v9 direction and packaging. This mode permits its named story and camera craft skills as supporting guidance; the v9 schema, occupancy and shot-plan authority remain unchanged.


## Bundled story development

When the request includes developing or revising a story, use the bundled [story-init](../story-init/SKILL.md), [plot-structure](../plot-structure/SKILL.md), [chapter-writing](../chapter-writing/SKILL.md), and [revision-continuity](../revision-continuity/SKILL.md), with the supporting story skills appropriate to the task. Follow the [story-writing handoff](../microdrama-series/references/story-writing-integration.md) when adapting into Director packages. Story development preserves the user's source language and canon; Director v9 remains authoritative for runtime, shot plans, H3 prompts, importer fields, and preflight. For a supplied finished script, proceed with direction without requiring a new story project.
