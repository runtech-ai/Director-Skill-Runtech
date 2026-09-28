# Agent routing

Keep reusable Director-package rules under `global/`. Keep franchise-, film-, and episode-specific knowledge under the matching `projects/<project>/` directory. Never move project physics, canon, runtime identifiers, or active progress into the global Director skill.

For Director-package creation or validation, read `global/skills/director-pack-skills/SKILL.md` first and load only the references it routes to.

For Beyblade RunTech generation, also read `projects/beyblade/skills/beyblade-director-autopilot/SKILL.md`. Resolve live state through RunTech MCP; use project checkpoints only as compact navigation caches. Do not use prior chat history as project state.

Do not commit image, audio, video, archive, render, or generated-asset files. Preserve only textual instructions, prompts, manifests, validation reports, and compact checkpoints.

