# STORYBOARD INDEX — EXACT CONTRACT

For runtime prompts, enforce [attached asset authority](../../../rules/asset-reference-authority.md): bound canonical attachments determine character, prop and location design; the storyboard supplies composition, framing, staging and pose intent only. Resolve any design or background discrepancy from the attached asset using the actual runtime Picture label.

Scene `storyboards/index.json`:

```json
{
  "sceneId": "SC001",
  "mode": "OPTIONAL_FILM_STILL_BEAT_SHEET",
  "generator": "GPT Image 2",
  "storyboardImageRequiredForH3": false,
  "panelCountRangePerSegment": {"min": 1, "max": "MICRO_SHOT_COUNT"},
  "segments": [
    {
      "segmentId": "SEG_SC001_001",
      "sceneId": "SC001",
      "beatCount": 3,
      "promptFile": "storyboards/prompts/SEG_SC001_001_storyboard_prompt.txt",
      "specFile": "storyboards/specs/SEG_SC001_001_storyboard.json",
      "expectedOutputFile": "storyboards/generated/SEG_SC001_001_storyboard.png",
      "h3StoryboardReferenceDefault": false
    }
  ]
}
```

Use `segments`.
DO NOT rename it to `entries`.

Movie-root `storyboard-index.json` uses the same concept, with each item also carrying:

```json
"packageRoot": "scene_packages/SC001_Scene_Title_director_shotplans"
```

---

# STORYBOARD SPEC CONTRACT

Each segment has exactly one storyboard spec:

```json
{
  "segmentId": "SEG_SC001_001",
  "sceneId": "SC001",
  "mode": "SINGLE_IMAGE_MULTI_BEAT_FILM_STILLS",
  "generator": "GPT Image 2",
  "required": false,
  "beatCount": 3,
  "allowedBeatRange": {"min": 1, "max": "MICRO_SHOT_COUNT"},
  "panelOrder": "TOP_TO_BOTTOM",
  "promptFile": "storyboards/prompts/SEG_SC001_001_storyboard_prompt.txt",
  "expectedOutputFile": "storyboards/generated/SEG_SC001_001_storyboard.png",
  "assetReferences": [],
  "beats": [],
  "authority": {
    "directorEditorData": "AUTHORITATIVE_FOR_STORY_ACTION_TIMING_DIALOGUE_AND_CONTINUITY",
    "canonicalAssets": "AUTHORITATIVE_FOR_IDENTITY_AND_DESIGN",
    "storyboard": "VISUAL_PLANNING_REFERENCE_ONLY"
  },
  "optionalH3StoryboardReference": {}
}
```

Beat objects must use:

```text
panel
sourceMicroShotId
displayShot
segmentTime
timeLabel
framing
lensIntent
cameraContext
pov
lighting
visibleAssets
description
continuity
```

Do not substitute `beat`, `microShotId`, `timeRange`, `cameraView`, `visualMoment`, or `spatialState` for those fields.

Beat `visibleAssets` must match the owning micro-shot occupancy. Do not draw a third person into a two-character beat.

---

# STORYBOARD PROMPT REQUIREMENT

Each segment gets one prompt for the latest available ChatGPT image model under [storyboard-images.md](storyboard-images.md), for ONE composite storyboard image whose aspect ratio is the inverse of the movie delivery frame: 16:9 movie → portrait 9:16 board; 9:16 movie → landscape 16:9 board. Its panel count equals the segment's micro-shot count, with one film-still beat per micro-shot. Historical `GPT Image 2` schema examples do not pin the generation model.

Panels are equal-height horizontal bands stacked `TOP_TO_BOTTOM`, read from top to bottom in playback order. Do not use a grid, columns, captions, numbers, speech bubbles, subtitles, timestamps, labels, watermarks, typography, gutters, or adjacent-panel fragments.

Storyboard prompts must explicitly declare asset attachment order:

```text
<Image 1> = canonical @character file: canonical_refs/characters/...png
<Image 2> = canonical @location file: canonical_refs/locations/...png
```

Only attach assets actually needed by the storyboard.

The storyboard is a VISUAL PLANNING REFERENCE ONLY.
It never overrides director action, exact timing, dialogue, occupancy, continuity, prop ownership, or canonical identity.

Apply [storyboard-fidelity-gate.md](storyboard-fidelity-gate.md): each panel must depict the Director's exact location, canonical assets and beat. Freeze its expected picture before rendering and save expected-versus-observed pixel evidence afterward. Missing, substituted, contradictory or unreadable required content is not accepted. Never modify the authoritative description merely to make an existing board pass.

Do not duplicate exact screenplay dialogue into storyboard prompt prose.
Do not illustrate extra people who are not in that beat's `visibleAssets`.

---

# STORYBOARD SOURCE-ISOLATION + STYLE-LOCK METADATA

The storyboard generator must be able to render a segment without borrowing any surrounding Project context. Therefore every storyboard spec MUST be self-grounding.

This is an additive extension only. Do NOT change the stable importer-facing base schema or existing required field names.

Inside each `storyboards/specs/<SEGMENT_ID>_storyboard.json`, add package-local grounding metadata such as:

```json
{
  "sourceIsolation": {
    "mode": "PACKAGE_LOCKED",
    "allowProjectContext": false,
    "allowUnlistedAssets": false,
    "allowPriorStoryboardsAsStyleReference": false,
    "onMissingReference": "FAIL_CLOSED"
  },
  "storyboardVisualStyle": {
    "medium": "<derive from this movie/scene>",
    "styleText": "<concise explicit package-specific visual style>",
    "authority": "DIRECTOR_PACKAGE"
  },
  "styleReferences": []
}
```

The exact values MUST be derived from the CURRENT movie package. Never fill these fields from the surrounding ChatGPT Project, another movie, or a previous storyboard.

## Visual style requirement

Do not rely on a generic storyboard-generator default such as `photorealistic live action`.

Every segment storyboard spec must explicitly communicate the intended medium/style. Examples of possible values include:

```text
cinematic anime film still
photorealistic live-action film still
stop-motion miniature film still
```

Only use the value that belongs to the current Director package.

If the source movie/scene does not define enough visual style to determine the intended medium, the package generator must record a validation error instead of borrowing project context.

## Asset-reference roles

Each `assetReferences[]` entry should include an explicit role where possible, for example:

```json
{
  "imageIndex": 1,
  "assetId": "@sharon",
  "file": "canonical_refs/characters/sharon.png",
  "attach": true,
  "role": "CHARACTER_IDENTITY"
}
```

Allowed/additive role vocabulary may include:

```text
CHARACTER_IDENTITY
LOCATION_DESIGN
PROP_DESIGN
VEHICLE_DESIGN
CREATURE_IDENTITY
STYLE_REFERENCE
CONTINUITY_REFERENCE
```

A canonical character/location image is NOT automatically a `STYLE_REFERENCE`.

A previously generated storyboard must NEVER be added as a style reference automatically. It may be used only when the Director package deliberately declares it or the user explicitly requests it.

## Storyboard prompt source-lock header

Every `storyboards/prompts/<SEGMENT_ID>_storyboard_prompt.txt` must begin with a compact package lock similar to:

```text
PACKAGE SOURCE LOCK
Use only this Director package and the package assets explicitly mapped below for story, visual style, identity, location and continuity. Ignore unrelated project branding, project-default imagery, UI, other movies, and previous storyboard renders unless explicitly declared below as a reference. Do not substitute missing assets.
```

Then include an explicit style line derived from the current package:

```text
VISUAL STYLE
<exact package-specific storyboardVisualStyle.styleText>
```

Then list the exact attachment mapping and the beat panels.

Do not mention unrelated project names or assets even negatively. The generic source-lock sentence is enough.

## Fail-closed asset behavior

If a storyboard beat requires a canonical identity/design asset and the package cannot resolve it, validation must fail.

Do not instruct the storyboard renderer to search the surrounding Project for a substitute.

## Storyboard retries

Run [director-preflight-gate](../../director-preflight-gate/SKILL.md) before rendering and on every actual board afterward. Apply the content-repair loop in [prompt-repair-loop.md](prompt-repair-loop.md), then regenerate/recheck each failed board until applicable gates pass. A generation-success response does not satisfy this gate.

Do not encode any rule that permits the storyboard renderer to use the last generated storyboard as a fallback visual target. Retries must remain grounded to the same package assets and style unless the user explicitly changes the reference set.

---

# OPTIONAL H3 STORYBOARD REFERENCE

Every storyboard spec and prompt bundle may contain an optional H3 storyboard-reference prompt.

Default is always OFF:

```json
"storyboardReferenceDefault": false
```

Only inject storyboard reference behavior when BOTH are true:

```text
storyboardRefEnabled == true
AND
storyboard image is actually attached/resolved
```

When OFF, the final H3 prompt must be identical to the no-storyboard path.

When ON, inject only the concise storyboard shot-planning definition that lists every mapped `[Shot N]`. Never `for Shot 1` alone when the segment has multiple shots.

Do not inject a `STORYBOARD EXECUTION LOCK`, repeated panel exclusions, or additional storyboard boilerplate.

The one concise definition must also prevent the storyboard sheet from appearing in the video: read the visual panels sequentially, use one corresponding panel per listed shot, and render exactly one full-screen moving shot at a time. In the same definition exclude the multi-panel grid, split screen, borders, divider lines, gutters, white margins, page edges, adjacent-panel fragments, captions, labels, timestamps, and typography. State this once rather than repeating it in every shot.
