# STORYBOARD IMAGES — GENERATE, NAME, ZIP

Use this director-pack skill again to generate the boards. The finished director package is the source: shots, canonical references, timing, lighting, people, and props. Do not start a separate storyboard pipeline.

Prompts, specs, source-lock, and style rules stay in [storyboard.md](storyboard.md). This file overrides panel count, image filenames, and the storyboard zip layout.

Generating these images does not turn H3 storyboard reference on. `storyboardReferenceDefault` stays `false` unless the user explicitly enables it.

## Model route — best available built-in ChatGPT image generator

Use the best available built-in ChatGPT image generator under global/rules/storyboard-image-model.md (latest user instruction, 2026-10-02). Record exact backend as unreported when absent. Preserve all canonical-source and pixel-quality gates.

Official OpenAI documentation checked 2026-10-01 lists [GPT Image 2.5 Sunburst](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst) for detailed generation/editing and [GPT Image 2.5 image-generation guidance](https://developers.openai.com/api/docs/guides/tools-image-generation). Recheck current official guidance when updating the policy or selecting an explicitly controlled model. Built-in `image_gen` may not expose a model selector or exact variant: use its current route and record the variant as `unreported` when absent. Never invent a parameter/model ID or claim an API model is necessarily the built-in backend.

Use the best available built-in ChatGPT image generator under global/rules/storyboard-image-model.md (latest user instruction, 2026-10-02). Record exact backend as unreported when absent. Preserve all canonical-source and pixel-quality gates.

## Per-board preflight and repair

Read [storyboard-fidelity-gate.md](storyboard-fidelity-gate.md) before rendering and review. Freeze each panel's Director-derived expectations first, then compare the actual pixels for exact location, canonical assets and beat. Save separate evidence-backed results per panel; failed or unreadable required details block acceptance. Never silently pass, weaken a requirement or use a video soft threshold to excuse board mismatch.

For an already-moving beat, the board must depict its current motion state with the applicable project-defined visual cues, not a stationary asset-sheet pose. Include those cues in the beat/image prompt and inspect their actual rendering per object while retaining identity and support/contact. Do not rely on a later video prompt to introduce motion missing from the board. Load the project authoring/physics reference for domain-specific cues; preserve authored stationary and slower phases.

Use [director-storyboard-generator](../../director-storyboard-generator/SKILL.md) and [director-preflight-gate](../../director-preflight-gate/SKILL.md). Gate the owning segment before rendering and each board's actual pixels afterward. Review every panel, not just the composite thumbnail. Match identity, population/anatomy, wardrobe, location, camera/perspective, support, phase, effect emitter/window and boundary state to its exact micro-shot and applicable project autopilot rules.

For a failed board, record all defects, repair the earliest direction/spec/prompt/binding cause, synchronize representations, regenerate fresh from current canonical assets and recheck the complete board. Never attach a rejected/prior board as a repair source. Preserve accepted boards. Continue the loop until the required gates pass; no automatic waiver after a fixed retry count, and no unchanged blind retries. User stop, an explicit run/cost limit or an actual infrastructure/authority failure ends external retries with a recorded resume action.

Only accepted boards enter the final ZIP. Missing pixel evidence is unknown, not passed. A static board cannot validate continuous motion, audio or lip-sync; those remain exact-take gates when video generation is authorized. Project-specific physics and audio waivers stay in the project rather than becoming global film rules.

## One image, one panel per shot

Each segment gets exactly one composite image.

`beatCount` equals that segment's micro-shot count. One beat per micro-shot, in playback order (`displayShot` 1, 2, 3, …). Do not pick a 3–10 beat count from "visual progression" when the shot count is different. A 2-shot segment is a 2-panel board. A 12-shot segment is a 12-panel board.

Each beat's `sourceMicroShotId`, `displayShot`, `segmentTime`, and `visibleAssets` match that micro-shot. Do not draw a person who is not in that shot's `visibleAssets`. People, location, props, light, and panel time stay the same as that micro-shot.

The image uses the inverse aspect ratio of the movie delivery frame: a `16:9` movie uses a portrait `9:16` board; a `9:16` movie uses a landscape `16:9` board. Panel order is `TOP_TO_BOTTOM`: equal-height horizontal panels, one per micro-shot, read from top to bottom. No captions, panel numbers, speech bubbles, subtitles, timestamps, labels, watermarks, typography, grid, columns, gutters, or adjacent-panel fragments inside the image. Shot prose on the board is a photograph of that shot, not a speech event.

## Filename

The image file name is the segment id. Nothing else.

```text
SEG_SC001_001.png
SEG_SC001_002.png
```

Segment `SEG_SC001_001` is `SEG_SC001_001.png`. Do not add `_storyboard`, a scene folder, or a `storyboards/generated/` prefix in the storyboard zip. Do not use `shot1.png`, `board.png`, or one sheet that mixes segments.

Import assigns the board because the filename is the segment id.

On that segment's `storyboards/index.json` entry, set `beatCount` to the shot count and point both path fields at that filename:

```json
{
  "segmentId": "SEG_SC001_001",
  "sceneId": "SC001",
  "beatCount": 4,
  "promptFile": "storyboards/prompts/SEG_SC001_001_storyboard_prompt.txt",
  "specFile": "storyboards/specs/SEG_SC001_001_storyboard.json",
  "expectedOutputFile": "SEG_SC001_001.png",
  "generatedFile": "SEG_SC001_001.png",
  "h3StoryboardReferenceDefault": false
}
```

`generatedFile` is additive. Do not rename `segments`. The spec's `beatCount` matches this entry. Beats in the spec are the panels, one per micro-shot.

## Storyboard zip

The storyboard deliverable is its own zip, separate from the director package zip. Match this layout: files only, at the archive root, one png per segment.

```text
The_Floating_Land_40_Segment_Storyboards.zip
├── SEG_SC001_001.png
├── SEG_SC001_002.png
├── SEG_SC002_001.png
└── ...
```

Name the zip `<Movie_Title>_<N>_Segment_Storyboards.zip`. Replace spaces in the title with underscores. `N` is the number of segment images.

The zip contains those png files and nothing else. No folders. No JSON. No README.

## Generate, then zip

1. Read the finished director package with this skill. Write the storyboard prompt and spec from its shots.
2. Generate a real image with the image tool in this session. The file name is `<SEGMENT_ID>.png`.
3. Do not write a placeholder, empty file, copied frame, or another segment's board. If no image tool is available, stop and say the boards were not generated.
4. Inspect and gate each board; repair/regenerate failed boards under the loop above before zipping. Zip every accepted segment png at the archive root under `<Movie_Title>_<N>_Segment_Storyboards.zip`.
5. Reopen the zip. Member count equals the segment count. Every member is `<SEGMENT_ID>.png` at the root, and every segment id in the director package has exactly one image.


## Runtime composition images versus package boards

A single-shot runtime repair may use a landscape composition image when the supported input route and authorized task call for it. Record that role, actual dimensions and the owning shot explicitly. It is not automatically a compliant Director-package board: the inverse-movie aspect and one-panel-per-shot contract above remain in force unless an explicit supported override is recorded. Upload success is not a layout waiver. Resolve physical-state/identity conflicts even when an image is used only for composition. No skill-only update repairs or regenerates existing media.
