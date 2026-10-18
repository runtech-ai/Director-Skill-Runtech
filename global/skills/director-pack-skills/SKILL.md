---
name: director-pack-skills
description: Builds importer-locked movie Director packages (movie-director-result / 3.1-shotplan-only) with scene ZIPs, shot plans, MiniMax H3 compiled prompts, and a second-pass storyboard zip (one image per segment, file name is the segment id, files at the zip root) under the v9 dialogue-time occupancy lock. Direction, camera, and first compiled prompts come from the v9 markdown. Official h3-prompt-writing validates those prompts and fixes only confirmed H3 form issues. Use when the user asks for a director package, director pack, shot plan, scene package, H3 compiled prompt, storyboard image, storyboard beat sheet, or movie-director-result ZIP.
metadata:
  compatibility: Codex and Claude Code. Requires the v9 markdown for direction and h3-prompt-writing only to validate compiled prompts.
---

# Director package generator

For a comic adaptation of an existing package, use [Director to Manhwa / Manga PDF](../director-manga-export/SKILL.md). That workflow creates a separate comic page plan, artwork, lettering and PDF; it preserves the source package and does not run film generation or apply storyboard grid rules to comic pages.

Before authoring, repair or final handoff, read [production handoff gates](references/production-handoff-gates.md) and [RunTech continuity import gate](references/runtech-continuity-import.md). Apply them under the selected contract; H3 form approval alone does not validate direction, dialogue ownership or effective continuity.

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
| Direction, physical action, inter-segment continuity, asset closure, dialogue-source and audio continuity | [references/direction-continuity-asset-lock.md](references/direction-continuity-asset-lock.md) |
| ZIP layout, manifests, segment JSON, prompt-bundle envelope | [references/package-schema.md](references/package-schema.md) |
| After `compiled_prompt` is written | [references/h3-prompt-validation.md](references/h3-prompt-validation.md) |
| Storyboard index, spec, prompt | [references/storyboard.md](references/storyboard.md) |
| One `<SEGMENT_ID>.png` per segment at the zip root | [references/storyboard-images.md](references/storyboard-images.md) |

## Procedure

1. Read the v9 contract, `references/v9-hardening-lock.md`, and `references/package-schema.md`.
2. Read [references/direction-continuity-asset-lock.md](references/direction-continuity-asset-lock.md). Direct every shot from the contract. Draw dialogue occupancy before action or `compiled_prompt`. Write picture-only action. Write camera as v9 specifies: observable move or hold, not a field dump. For mechanical or rules-bound action, write the object-state and screen-direction transitions before shot prose.
3. Author the director ZIP from the schema file. Scene packages live under `scene_packages/`. Keep normalized `ShotPlanningPrompt.compiled_prompt` as label-free planning guidance. Validate the separately packaged/runtime-resolved H3 output against the official guide; inspect the importer adapter before using a package field that accepts complete H3 text. See `references/h3-prompt-validation.md` for the layer distinction. Apply the global-retention rule in `references/v9-hardening-lock.md`: declare identity/reference retention once, keep shots focused on their changing picture and dialogue ownership, and verify consistent labels throughout the prompt. Do not serialize Director field labels into that prompt. Close the per-segment asset ledger across the manifest, segment JSON, prompt bundle, H3 subject definitions, and actual package files.
4. Confirm `h3-prompt-writing` is installed. Read [references/h3-prompt-validation.md](references/h3-prompt-validation.md). Validate the final H3 prompt and check planning-schema compatibility separately. Fix only a confirmed H3 issue. If the prompt already matches the official skill, leave it. If the skill is missing, stop and ask for `npx skills add https://github.com/MiniMax-AI/MiniMax-H3 --skill h3-prompt-writing`.
5. Read `references/storyboard.md` and write each segment’s index, spec, and prompt. Match each panel to its micro-shot state, physical phase, axis, screen direction, population, prop ownership, damage state, and boundary continuity. A board that contradicts the directed state must be regenerated.
6. Read `references/storyboard-images.md`. Generate one real composite image per segment, one panel per micro-shot, file name `SEG_SC001_001.png`. Zip them as `<Movie_Title>_<N>_Segment_Storyboards.zip` with only those pngs at the archive root.
7. Reopen both zips. Every segment id is a storyboard filename. Run [references/validation.md](references/validation.md), including runtime H3 attachment smoke tests when the importer/compiler is available. Compatibility is the v9 contract, not the version string.

## Occupancy

For each structured dialogue line, compare `start` / `end` with every micro-shot window. A shot that overlaps is a speaking shot. A shot that does not is silent. Emit official `<d>` once, in the first occupied shot only. Later occupied shots are visual action only. In a talking segment, a silent shot locks silence right after the composition sentence. Close lips after the line only on the last occupied shot when the line ends with that shot.

If deleting every `dialogue` array would still tell a reader what was said, the package fails. `references/v9-hardening-lock.md` wins if this page disagrees.

## Storyboard

The storyboard pass is a second use of this skill on the finished director package. File name is the segment id. Panel count is the shot count. Details are only in `references/storyboard.md` and `references/storyboard-images.md`.

## V9 generation lessons

Before authoring or repairing H3 prompts, read [references/v9-generation-lessons.md](references/v9-generation-lessons.md). Apply its concise staging, continuity, runtime-input and exact-take review rules alongside the hardening lock. Load applicable project canon and physics separately.

## Direct microdrama option

For **direct microdrama**, read [microdrama-series](../microdrama-series/SKILL.md). Develop the full story with chapter-writing and supporting story skills before v9 direction. The named supporting craft skills are permitted for this mode; v9 remains the schema and shot-plan authority.
