# RunTech MCP project notes

Read only when live RunTech behavior conflicts with the normal autopilot loop.

- Use the imported scene key such as `SC001` for `get_scene_segments` and `get_segment_review_bundle`. Use the timeline scene UUID plus exact `clip_id` for `generate_segment`.
- Always pass the exact active `clip_id` when the tool accepts it. Duplicate scene numbers exist and may otherwise bind an inactive clip.
- On the current deployment, `list_h3_presets` advertises `draft-anime` and `production-anime`, but passing either as `preset_id` returns `404 preset not found`. Use the quality-ladder values `Draft-Anime` and `Production-Anime` instead; confirm the queued response normalizes to `draft_anime` or `production_anime`.
- `wait_until_reviewable` may return while only a latent preview is available. Treat it as an early display checkpoint, not final validation. Wait for `clips_ready`, then require a newly incremented exact-clip path.
- Show one latent preview image per generation. Do not display an entire latent sequence unless explicitly requested.
- `get_segment_review_bundle` currently exposes sample frames and the versioned clip path, but not the MP4 bytes or a signed URL. The raw `/media/{path}` endpoint returns `401` for the MCP credential. The REST segment-download route requires an organization API key and rejects the MCP credential when `X-Org-Id` selects this project organization.
- Never substitute an older locally available video. If temporal physics cannot be established from the exact new take, mark review blocked and do not advance to Production.
- A robust MCP fix is a segment-video artifact tool, resource link, embedded binary, or short-lived signed URL scoped to `movie_id`, scene key, segment ID, and exact clip/take.
