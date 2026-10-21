---
name: director-storyboard-generator
description: Execute the storyboard pass of an existing v9 Director package, using the current built-in ChatGPT image route and shared preflight gates. Derive one panel per authored shot; do not invent a separate shot plan or generate video.
---

# Portable Director plugin entrypoint

Read and follow [the complete bundled procedure](../../global/skills/director-storyboard-generator/SKILL.md). Resolve its references relative to its bundled file location.

The bundled global/director-contract.json supports Director v9. Preserve existing package provenance; do not silently convert an older package or claim v9 contract acceptance without the appropriate review.

Use bundled h3-prompt-writing for H3 validation. Read global/rules/storyboard-image-model.md and global/rules/asset-reference-authority.md from the plugin root before applicable work. This skills-only plugin does not install or authenticate a server. Use separately connected RunTech tools when needed. Project physics, canon and assets must come from the user's project or attachments; request missing required sources. Do not generate video unless explicitly authorized.


## Cinematic direction repair

For direction, timing, camera, prop, speech or board repairs, follow [cinematic causality and timing](../../global/skills/director-pack-skills/references/cinematic-causality-and-timing.md). This project uses variable shot and segment lengths, episodes around 90 seconds, fixed cameras, and evidence-based board reuse.
