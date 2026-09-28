# RunTech compact lookup index

Start with `CHECKPOINT.json`. Do not reload the whole project or full movie timeline.

Runtime/status work: read only `CHECKPOINT.json`.

Prompt/compliance work: additionally read `DIRECTOR_CAPSULE.json`. Open full skill/contract material only when mandatory or the capsule cannot resolve an ambiguity.

Auto Pilot runs: read `AUTOPILOT_RULES.json`, load the applicable skills, and query MCP as the live source of truth. Never reconstruct project state from prior chat context.

## Current work

- Active segment: `SEG_SC001_002`
- Runtime anomaly notes: `RUNTECH_MCP_NOTES.md`
- Active clip: `827da4d1-e9ee-4111-adb3-454520406960`
- Prompt: `SEG_SC001_002_draft_prompt.txt`
- Storyboard: `../director_v9_current/storyboards/SEG_SC001_002.png`
- Status history: `SEQUENTIAL_VALIDATION_STATUS.md`

## Stable IDs

- Movie: `82e1e29d-cf5f-48de-802b-478422125ef7`
- Org: `f28933d2-53c6-4320-ba0b-f83775e11aed`
- Active SC001 scene UUID: `c0656174-fc90-4d0a-bc3a-19134d76a8c2`
- Inactive duplicate scene UUID: `5f99b4eb-ea56-4658-85fa-b21f7d76ca40`
- Inactive duplicate clip: `f9eb9ce1-6e4f-42db-a86f-9bbac4f4faad`

## Minimal MCP reads

1. Poll `get_generation_status`, filtered to the active clip ID.
2. When done, call `get_segment_review_bundle` with `scene_id: SC001`, the active segment ID, and exact clip ID.
3. Review only saved `latent_*` and `clip_t=*` frames.
4. Update `CHECKPOINT.json` and the one-line status ledger.

## Acceptance

Pass when primary shot beats and the overall scene match at least 95%. Secondary design substitutions do not block unless they break the main beat, population, action, or continuity.
