# STORYBOARD IMAGES — GENERATE, NAME, ZIP

Use this director-pack skill again to generate the boards. The finished director package is the source: shots, canonical references, timing, lighting, people, and props. Do not start a separate storyboard pipeline.

Prompts, specs, source-lock, and style rules stay in [storyboard.md](storyboard.md). This file overrides panel count, image filenames, and the storyboard zip layout.

Generating these images does not turn H3 storyboard reference on. `storyboardReferenceDefault` stays `false` unless the user explicitly enables it.

## One image, one panel per shot

Each segment gets exactly one composite image.

`beatCount` equals that segment's micro-shot count. One beat per micro-shot, in playback order (`displayShot` 1, 2, 3, …). Do not pick a 3–10 beat count from "visual progression" when the shot count is different. A 2-shot segment is a 2-panel board. A 12-shot segment is a 12-panel board.

Each beat's `sourceMicroShotId`, `displayShot`, `segmentTime`, and `visibleAssets` match that micro-shot. Do not draw a person who is not in that shot's `visibleAssets`. People, location, props, light, and panel time stay the same as that micro-shot.

Panel order on the image is `LEFT_TO_RIGHT_THEN_TOP_TO_BOTTOM`. No captions, panel numbers, speech bubbles, subtitles, timestamps, labels, or watermarks inside the image. Shot prose on the board is a photograph of that shot, not a speech event.

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
4. Zip every segment png at the archive root under `<Movie_Title>_<N>_Segment_Storyboards.zip`.
5. Reopen the zip. Member count equals the segment count. Every member is `<SEGMENT_ID>.png` at the root, and every segment id in the director package has exactly one image.

## Runtime composition images versus package boards

A single-shot runtime repair may use a landscape composition image when the supported input route and authorized task call for it. Record that role, actual dimensions and the owning shot explicitly. It is not automatically a compliant Director-package board: the inverse-movie aspect and one-panel-per-shot contract above remain in force unless an explicit supported override is recorded. Upload success is not a layout waiver. Resolve physical-state/identity conflicts even when an image is used only for composition. No skill-only update repairs or regenerates existing media.
