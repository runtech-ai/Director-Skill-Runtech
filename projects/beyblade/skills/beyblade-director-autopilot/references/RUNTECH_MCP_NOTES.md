# RunTech MCP project notes

Read only when live RunTech behavior conflicts with the normal autopilot loop.

- Use the imported scene key such as `SC001` for `get_scene_segments` and `get_segment_review_bundle`. Use the timeline scene UUID plus exact `clip_id` for `generate_segment`.
- Always pass the exact active `clip_id` when the tool accepts it. Duplicate scene numbers exist and may otherwise bind an inactive clip.
- On the current deployment, `list_h3_presets` advertises `draft-anime` and `production-anime`, but passing either as `preset_id` returns `404 preset not found`. Use the quality-ladder values `Draft-Anime` and `Production-Anime` instead; confirm the queued response normalizes to `draft_anime` or `production_anime`.
- `wait_until_reviewable` may return while only a latent preview is available. Treat it as an early display checkpoint, not final validation. Wait for `clips_ready`, then require a newly incremented exact-clip path.
- Show one latent preview image per generation. Do not display an entire latent sequence unless explicitly requested.
- The minted `mk_` key can select the RunTech organization through MCP and includes the expected project movie. Keep it in a local ignored environment file and never commit it.
- `get_segment_review_bundle` currently exposes base64 for the storyboard and JPEG review frames plus the versioned clip path, but not MP4 bytes, an MCP resource link, or a signed URL. An extra `include_video_base64` argument is ignored. Raw `/media/{path}` is JWT-only and must not be used with the minted MCP key. The separate REST segment-download route rejects the multi-organization minted key with an organization-mismatch response even though MCP `select_org` succeeds.
- Never substitute an older locally available video. If temporal physics cannot be established from the exact new take, mark review blocked and do not advance to Production.
- Required MCP fix: expose a `download_segment_video`-style tool or resource returning `video/mp4` base64 (or a short-lived signed resource) scoped to `movie_id`, scene key, segment ID, exact `clip_id`, and exact take/version.
