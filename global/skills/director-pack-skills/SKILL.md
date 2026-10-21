---
name: director-pack-skills
description: Direct any movie, series or microdrama in any genre and medium into importer-locked Director v9 packages, with scene direction, shot plans, compiled H3 prompts and one storyboard per segment. Use for direct microdrama, Director packages, movie direction, shot plans and package storyboard beats.
metadata:
  compatibility: Codex and Claude Code. Read the v9 contract; h3-prompt-writing validates compiled prompts only.
---

## Direct first, protect second

Every segment is directed before it is protected. First run the [scene direction pass](references/scene-direction-pass.md) with the project's direction profile, built from [genre direction profiles](references/genre-direction-profiles.md): beats, blocking, genre coverage, motivated cuts and camera, timed performance. Only then apply the v9 contract and the failure locks below. Project invariants (identity, wardrobe, physics states) go into the project's `h3/h3-locks.json` and are stated once by `global/scripts/h3_compile.py`; they never get pasted into each shot. A new project starts by writing `projects/<project>/references/DIRECTION_PROFILE.md` and `projects/<project>/h3/h3-locks.json` from the template in `global/scripts/h3-locks.example.json`.

For physical action, timing or storyboard references, read [action physics and timing](references/action-physics-and-timing.md) before direction or review. Speech silence never implies a motion hold; preserve authored movement and intentional stillness.


For H3 movie direction, camera selection, genre treatment or storyboard planning, read [cinematic direction](references/h3-cinematic-direction.md). Select a physically plausible viewpoint and camera path; use its genre guidance only where relevant.

# Director package generator

For a comic adaptation of an existing package, use [Director to Manhwa / Manga PDF](../../../skills/director-manga-export/SKILL.md). That workflow creates a separate comic page plan, artwork, lettering and PDF; it preserves the source package and does not run film generation or apply storyboard grid rules to comic pages.

Before authoring, repair or final handoff, read [production handoff gates](references/production-handoff-gates.md) for direction/state, dialogue ownership and timing, runtime reference closure, effective match continuity and archive freshness.

## Director v9 contract

Use [the v9 profile](../../director-contract.json) and the v9 procedure below. The profile is repository configuration, never an importer schema field. Preserve existing package provenance; a different historical authoring profile requires an explicit migration before claiming v9 contract acceptance.

For segment continuity and final ZIP handoff, read [the RunTech continuity import gate](references/runtech-continuity-import.md). Validate effective normalized modes; conflicting HARD_CUT boundaries can disable previous-frame references unless the installed importer explicitly reconciles them.

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
| Always, before any shot prose | [references/scene-direction-pass.md](references/scene-direction-pass.md), the project's `DIRECTION_PROFILE.md` and [references/genre-direction-profiles.md](references/genre-direction-profiles.md) |
| Always, before any shot prose | The v9 markdown, then [references/v9-hardening-lock.md](references/v9-hardening-lock.md) |
| Compiling and linting the H3 prompt | `global/scripts/h3_compile.py` with the project's `h3/h3-locks.json`, then `global/scripts/h3_lint.py`; FAIL blocks handoff |
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
2. Run the [scene direction pass](references/scene-direction-pass.md) for each scene using the project's direction profile: turn, beats, blocking, genre coverage, cut reasons, a motivated camera per shot, timed performance beats and dialogue `delivery`. Then read [references/direction-continuity-asset-lock.md](references/direction-continuity-asset-lock.md) and [references/prompt-repair-loop.md](references/prompt-repair-loop.md). Direct every shot from the contract. Draw dialogue occupancy before action or `compiled_prompt`. Write picture-only action. Write camera as v9 specifies: observable move or hold, not a field dump. Author per-object states, causal transitions and effect permissions before shot prose. Apply domain mechanics only to the relevant object and photographed phase; their presence in the movie does not authorize adding motion or effects to other beats. When the content is Beyblade, load its project-local Physics Bible and Director-authoring reference as hard gates.
3. Author the director ZIP from the schema file. Scene packages live under `scene_packages/`. Keep normalized `ShotPlanningPrompt.compiled_prompt` as label-free planning guidance. Validate the separately packaged/runtime-resolved H3 output against the official guide; inspect the importer adapter before using a package field that accepts complete H3 text. See `references/h3-prompt-validation.md` for the layer distinction. Do not serialize Director field labels into that prompt. Write the six-section prompt with `global/scripts/h3_compile.py --write` and run `global/scripts/h3_lint.py` on every bundle; repair the direction, not the linter, when it fails. Close the per-segment asset ledger across the manifest, segment JSON, prompt bundle, H3 subject definitions, and actual package files. A movie package also needs a root `asset-manifest.json` (`{"version": "1.0", "assets": {"@handle": {type, referenceType, files, assetLibraryIds, bindingStatus, description}}}`) listing every used handle, including voice-only characters; the RunTech importer registers project assets only from that file. Copy entries, including `assetLibraryIds`, from the project's source asset manifest so they bind to the existing library, and point `files` at sheets that are actually in the ZIP. When the user asks for a series ZIP or imports through the series uploader, wrap each complete package, including its `movie.movie`, as an episode under the [series contract](../../../skills/microdrama-series/references/series-contract.md).
4. Confirm `h3-prompt-writing` is installed. Read [references/h3-prompt-validation.md](references/h3-prompt-validation.md). Validate the final H3 prompt and check planning-schema compatibility separately. Fix only a confirmed H3 issue. If the prompt already matches the official skill, leave it. If the skill is missing, stop and ask for `npx skills add https://github.com/MiniMax-AI/MiniMax-H3 --skill h3-prompt-writing`.
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




## Direct microdrama option

When the user says **direct microdrama**, follow [the microdrama series workflow](../../../skills/microdrama-series/SKILL.md). Start from a summary, develop full episode stories with chapter-writing and supporting story skills, then return here for v9 direction and packaging. This mode permits its named story and camera craft skills as supporting guidance; the v9 schema, occupancy and shot-plan authority remain unchanged.


For v9 authoring and repair, read [v9 generation lessons](references/v9-generation-lessons.md) for concise retention, complete mappings and exact-take evidence. These supplement the selected contract.

## Import verification

For archive delivery, import or missing-scene troubleshooting, follow [import routing and persistence verification](references/import-verification.md). Keep local validation, live import, script-scoped persistence and deployment status separate.

## Cinematic direction repair

For direction, timing, camera, prop, speech or board repairs, follow [cinematic causality and timing](references/cinematic-causality-and-timing.md). This project uses variable shot and segment lengths, episodes around 90 seconds, fixed cameras, and evidence-based board reuse.

## Production repair scope

For timing, continuity, narration, prop-state, board or package repairs, follow [production repair lessons](references/production-repair-lessons.md). Preserve explicitly locked episodes, separate generic rules from project preferences, and distinguish local checks from reviewed footage or deployed fixes.
