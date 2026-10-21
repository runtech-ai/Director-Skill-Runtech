---
name: runtech-movie-mcp
description: Operate the RunTech Movie MCP for film selection, director-package import, storyboards, H3 generation, exact-clip review, and video download. Use when querying or changing RunTech movies, scenes, segments, storyboards, presets, generation, reviews, or assembled output.
---

# RunTech Movie MCP

Start every session with `tools/list`; the live registry is authoritative. Do not infer a tool's schema from a cached request, and do not expose configured credentials.

## Routing

1. Use `list_orgs` or `list_movies`, then `select_org` when an organization must be selected.
2. Use `get_movie(movie_id)` to resolve active scene UUIDs, clip IDs, active take paths, and current film state.
3. Use imported scene keys such as `SC002` for segment and storyboard reads. Use the resolved scene UUID plus exact `clip_id` for `generate_segment` when supported.
4. If a listed movie, segment, or preset returns 404, stop before mutation. Record the inconsistency and do not substitute IDs, presets, or old takes.

## Generation and review

- Before generation, retrieve the exact segment prompt and storyboard, verify asset bindings, and resolve the exact active clip.
- For H3, call `list_h3_presets`, then `get_h3_preset` for the selected returned ID. Pass only that resolved `preset_id`, or intentionally omit it to use saved film H3 settings. `quality` is label-only.
- Queue one clip with `generate_segment`; then use `get_generation_status` or `wait_until_idle`. A latent from `wait_until_reviewable` is not a completed take.
- Review only the newly versioned exact clip with `get_segment_review_bundle` and download it through `download_segment_video(movie_id, scene_id, segment_id, clip_id)`. Never replace an exact take with an older local file.

## Live tool groups

- Discovery: `list_skills`, `get_skill`, `export_authoring_skills`
- Organization and movie: `list_orgs`, `get_current_org`, `select_org`, `list_movies`, `get_movie`
- H3: `update_movie_quality`, `list_h3_presets`, `get_h3_preset`, `apply_h3_preset`
- MovieScript: `get_or_create_moviescript`, `get_script_dsl`, `update_script_dsl`, `validate_script_dsl`
- Director packages: `export_director_brief`, `begin_director_pack_upload`, `append_director_pack_chunk`, `inspect_director_pack`, `import_director_pack`, `download_director_source`
- Storyboards and segments: `upload_storyboard_zip`, `upload_segment_storyboard`, `get_production`, `get_scene_segments`, `update_scene_segments`, `get_scene_storyboard`, `update_segment_prompt`, `replace_segment_storyboard`
- Runtime: `generate_movie`, `generate_segment`, `stop_generation`, `get_generation_status`, `wait_until_reviewable`, `wait_until_idle`, `assemble_movie`
- Exact-take output: `get_segment_review_bundle`, `download_segment_video`

## Import verification

For archive delivery, import or missing-scene troubleshooting, follow [import routing and persistence verification](../director-pack-skills/references/import-verification.md). Keep local validation, live import, script-scoped persistence and deployment status separate.

## Episode-scoped prompt writes

Before each write through an active-episode endpoint, re-read the active script and the target segment, compare against the saved pre-edit prompt/action, and stop on a mismatch. A scene UUID or `get_or_create_moviescript(script_id=...)` response does not by itself prove activation or script-scoped routing. See the [active-episode mutation guard](../director-pack-skills/references/import-verification.md#active-episode-mutation-guard).

## Production repair scope

For timing, continuity, narration, prop-state, board or package repairs, follow [production repair lessons](../director-pack-skills/references/production-repair-lessons.md). Preserve explicitly locked episodes, separate generic rules from project preferences, and distinguish local checks from reviewed footage or deployed fixes.
