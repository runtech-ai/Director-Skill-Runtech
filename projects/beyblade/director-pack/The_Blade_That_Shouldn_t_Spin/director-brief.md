# MovieScript External Director Brief

Project: **The Blade That Shouldn't Spin**
Scope: **the full movie**

You are directing a MovieScript production for downstream video generation.

## Your responsibilities

- Read `movie.movie` (canonical DSL) and `asset-manifest.json` (visual identity references).
- Respect `generation-profile.json` model duration and reference limits.
- Treat each character sheet PNG as ONE multi-view identity reference — do not invent separate handles per view.
- Create scene beats, generation segments (typically 8–15s for MiniMax H3), micro shots (2–4 per segment), storyboard panels, and H3 prompts.
- Use segment-local timestamps inside generation prompts.
- Preserve scene runtime from DSL `target_duration` — never silently extend or shrink it.

## Return package

Zip a **movie-director-result** package containing:

- `import-manifest.json`
- `scenes/{SCENE_ID}/production.json` (beats + director plan + sound/music)
- `scenes/{SCENE_ID}/segments.json`
- `scenes/{SCENE_ID}/storyboard.json`
- optional `assets/storyboard/{SCENE_ID}/` panel images

Do not modify `movie.movie` unless explicitly asked.
