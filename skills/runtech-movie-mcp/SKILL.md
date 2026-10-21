---
name: runtech-movie-mcp
description: Operate the RunTech Movie MCP for film selection, director-package import, storyboards, H3 generation, exact-clip review, and video download. Use when querying or changing RunTech movies, scenes, segments, storyboards, presets, generation, reviews, or assembled output.
---

# Portable Director plugin entrypoint

Read and follow [the complete bundled procedure](../../global/skills/runtech-movie-mcp/SKILL.md). Resolve its references relative to its bundled file location.

The bundled global/director-contract.json supports Director v9. Preserve existing package provenance; do not silently convert an older package or claim v9 contract acceptance without the appropriate review.

Use bundled h3-prompt-writing for H3 validation. Read global/rules/storyboard-image-model.md and global/rules/asset-reference-authority.md from the plugin root before applicable work. This skills-only plugin does not install or authenticate a server. Use separately connected RunTech tools when needed. Project physics, canon and assets must come from the user's project or attachments; request missing required sources. Do not generate video unless explicitly authorized.
