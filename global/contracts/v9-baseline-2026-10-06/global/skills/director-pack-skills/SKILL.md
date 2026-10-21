---
name: director-pack-skills
description: Builds importer-locked movie Director packages (movie-director-result / 3.1-shotplan-only) with scene ZIPs, shot plans, MiniMax H3 compiled prompts, and a second-pass storyboard zip (one image per segment, file name is the segment id, files at the zip root) under the v9 dialogue-time occupancy lock. Direction, camera, and first compiled prompts come from the v9 markdown. Official h3-prompt-writing validates those prompts and fixes only confirmed H3 form issues. Use when the user asks for a director package, director pack, shot plan, scene package, H3 compiled prompt, storyboard image, storyboard beat sheet, or movie-director-result ZIP.
metadata:
  compatibility: Codex and Claude Code. Requires the v9 markdown for direction and h3-prompt-writing only to validate compiled prompts.
---

# Director package generator

Use the best available built-in ChatGPT image generator under global/rules/storyboard-image-model.md (latest user instruction, 2026-10-02). Record exact backend as unreported when absent. Preserve all canonical-source and pixel-quality gates.

Build a complete `movie-director-result` / `3.1-shotplan-only` Director ZIP from the v9 contract. Do not invent a new schema. Do not load a video skill or any other direction skill.

The body of this file is the procedure. The v9 markdown and the reference files are the contract. Do not deliver from memory of this page.

## Identity

```json
{"format":"movie-director-result","version":"3.1-shotplan-only"}
```

Read the full contract first: the repo file `Director_Package_Generator_System_Prompt_v9_H3_DIALOGUE_TIME_OCCUPANCY.md`, then [references/v9-hardening-lock.md](references/v9-hardening-lock.md) and [references/package-schema.md](references/package-schema.md).

Keep existing field names, `scene_packages/` placement, and this base version. Storyboard behavior is additive only.

## Who writes what

| Work | Source | Rule |
|---|---|---|
| Occupancy, dialogue, direction, camera, shot prose, first `compiled_prompt`, importer fields, ZIP layout | v9 contract | Fail closed if the pack disagrees |
| After the prompt exists | Installed `h3-prompt-writing` skill | Validate only. Fix a real H3 issue. If there is no issue, leave the prompt |
| Storyboard index, spec, images, zip | [references/storyboard.md](references/storyboard.md) and [references/storyboard-images.md](references/storyboard-images.md) | This is the only logic kept from the previous pack |

## Read map

| When | Read |
|---|---|
| Always, before any shot prose | The v9 markdown, then [references/v9-hardening-lock.md](references/v9-hardening-lock.md) |
| Always, before direction, preflight, or storyboard work | [references/v9-common-movie-direction.md](references/v9-common-movie-direction.md) |
| Direction, physical action, inter-segment continuity, asset closure, dialogue-source and audio continuity | [references/direction-continuity-asset-lock.md](references/direction-continuity-asset-lock.md) |
| Always, before authoring and final handoff; any prompt or generated-media repair | [references/prompt-repair-loop.md](references/prompt-repair-loop.md) |
| Always, before media retrieval, rendering, review or advancing to another segment | [references/media-lifecycle.md](references/media-lifecycle.md) |
| Always, before segment handoff and after any repair; every rendered board | [director-preflight-gate](../director-preflight-gate/SKILL.md) |
| Storyboard generation or repair pass | [director-storyboard-generator](../director-storyboard-generator/SKILL.md) |
| ZIP layout, manifests, segment JSON, prompt-bundle envelope | [references/package-schema.md](references/package-schema.md) |
| After `compiled_prompt` is written | [references/h3-prompt-validation.md](references/h3-prompt-validation.md) |
| Storyboard index, spec, prompt | [references/storyboard.md](references/storyboard.md) |
| Always, for storyboard expectations, pixel review and acceptance | [references/storyboard-fidelity-gate.md](references/storyboard-fidelity-gate.md) |
| One `<SEGMENT_ID>.png` per segment at the zip root | [references/storyboard-images.md](references/storyboard-images.md) |
| Validating a Director ZIP or attached storyboard through RunTech MCP | [references/runtech-artifact-retrieval.md](references/runtech-artifact-retrieval.md) |

## Procedure

Apply [references/media-lifecycle.md](references/media-lifecycle.md) throughout this procedure: one segment's required media at a time, files outside conversation context, and compact textual checkpoints between segments. Never carry a movie-wide media bundle or accumulated retries into each generation request.

1. Read the v9 contract, `references/v9-hardening-lock.md`, `references/v9-common-movie-direction.md`, and `references/package-schema.md`.
2. Read [references/direction-continuity-asset-lock.md](references/direction-continuity-asset-lock.md) and [references/prompt-repair-loop.md](references/prompt-repair-loop.md). Direct every shot from the contract. Draw dialogue occupancy before action or `compiled_prompt`. Write picture-only action. Write camera as v9 specifies: observable move or hold, not a field dump. Author per-object states, causal transitions and effect permissions before shot prose. Apply domain mechanics only to the relevant object and photographed phase; their presence in the movie does not authorize adding motion or effects to other beats. When the content is Beyblade, load its project-local Physics Bible and Director-authoring reference as hard gates.
3. Author the director ZIP from the schema file. Scene packages live under `scene_packages/`. Write `shot_planning_prompt.compiled_prompt` as the directed picture in H3-ready prose. Do not serialize Director field labels into that prompt. Close the per-segment asset ledger across the manifest, segment JSON, prompt bundle, H3 subject definitions, and actual package files.
4. Confirm `h3-prompt-writing` is installed. Read [references/h3-prompt-validation.md](references/h3-prompt-validation.md). Validate each `compiled_prompt`. Fix only a confirmed H3 issue. If the prompt already matches the official skill, leave it. If the skill is missing, stop and ask for `npx skills add https://github.com/MiniMax-AI/MiniMax-H3 --skill h3-prompt-writing`.
5. Run [director-preflight-gate](../director-preflight-gate/SKILL.md) on the authored segment. Read `references/storyboard.md` and write each segment’s index, spec, and prompt. Use the inverse aspect ratio of the movie delivery frame (16:9 movie → 9:16 board; 9:16 movie → 16:9 board), with an equal-height TOP_TO_BOTTOM stack and exactly one panel per micro-shot. Match each panel to its micro-shot state, physical phase, axis, screen direction, population, prop ownership, damage state, and boundary continuity. Use [director-storyboard-generator](../director-storyboard-generator/SKILL.md) for this same package's rendering/review pass; it cannot rewrite the shot plan independently.
6. Read `references/storyboard-images.md`. When images are authorized, use the latest available ChatGPT image model through built-in `image_gen` to generate one real composite image per segment, one panel per micro-shot, file name `SEG_SC001_001.png`. Run the shared preflight gate on every board's actual pixels; repair and regenerate failed boards until all applicable gates pass. Then zip them as `<Movie_Title>_<N>_Segment_Storyboards.zip` with only those pngs at the archive root. For skill-only work, update instructions and validate links without changing the movie pack or generating media.
7. Reopen both zips. Every segment id is a storyboard filename. Run [references/validation.md](references/validation.md), including runtime H3 attachment smoke tests when the importer/compiler is available. Review, repair and recheck under `references/prompt-repair-loop.md` until all applicable checks pass. Never delegate a known authoring contradiction to the renderer or mark missing pixel/runtime evidence passed. Compatibility is the v9 contract, not the version string.

When the package is stored in RunTech rather than on disk, use the artifact-retrieval reference to validate its metadata, chunked ZIP central directory, and exact per-segment storyboard PNG. Do not treat scene-level storyboard metadata as image bytes.

## Occupancy

For each structured dialogue line, compare `start` / `end` with every micro-shot window. A shot that overlaps is a speaking shot. A shot that does not is silent. Emit official `<d>` once, in the first occupied shot only. Later occupied shots are visual action only. In a talking segment, a silent shot locks silence right after the composition sentence. Close lips after the line only on the last occupied shot when the line ends with that shot.

If deleting every `dialogue` array would still tell a reader what was said, the package fails. `references/v9-hardening-lock.md` wins if this page disagrees.

## Storyboard

The storyboard pass is a second use of this skill on the finished director package. File name is the segment id. Panel count is the shot count. Details are only in `references/storyboard.md` and `references/storyboard-images.md`.

Acceptance also requires [references/storyboard-fidelity-gate.md](references/storyboard-fidelity-gate.md): exact Director location, canonical assets and beat for every panel, backed by current pixel evidence. A failed or unknown required detail blocks board handoff and final ZIP inclusion. No silent pass or aggregate-score waiver is allowed.


## Latest user override — 2026-10-02
Use the best available built-in ChatGPT image generator. This supersedes all Image 2.5-only blocking instructions above. Record backend as unreported; keep all pixel and source quality gates. See global/rules/storyboard-image-model.md.

