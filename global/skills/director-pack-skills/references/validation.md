# PACK VALIDATION

Do not write `"valid": true` only because your own paths resolve.

## Importer

Check the v9 contract and [package-schema.md](package-schema.md):

- root contains `scene_packages/`
- manifests use `movie-director-result` / `3.1-shotplan-only` and the established field names
- `canonicalReferences` are objects with class-first `authority`
- segment JSON uses `id`, `sceneStart`, `sceneEnd`
- prompt bundle uses `segment_id`, `scene_id`, `scene_time`, `shot_planning_prompt`
- v9 occupancy: one `<d>` on the first occupied shot; silent shots lock silence after composition; no “continue the same spoken line”
- transitions are one explicit value, never `INTERNAL CUT OR MOTIVATED MOVE`
- every canonical asset in the per-segment ledger resolves through manifest, segment JSON, prompt bundle, H3 subject definition, and a readable package file
- adjacent segment boundary states agree for people, props, screen direction, damage, light, and audio

If any of these fail, do not deliver the ZIP.

## H3 form

Run [h3-prompt-validation.md](h3-prompt-validation.md) on every `compiled_prompt`. Fix only a confirmed official-skill issue. Leave a clean prompt.

When the importer/compiler is available, run the package through its real reference resolver and inspect the compiled `subject_definitions`. A path check or a literal `@handle` in prompt prose is not proof that the runtime attached the picture. Report unresolved runtime attachments as failures.

## Storyboard

Run the zip checks in [storyboard-images.md](storyboard-images.md). Member count equals the segment count. Every member is `<SEGMENT_ID>.png` at the archive root.

Also run [direction-continuity-asset-lock.md](direction-continuity-asset-lock.md) against the rendered pixels. Report segment counts and ids under `PASS_NO_RESHOOT`, `PROMPT_ONLY`, `STORYBOARD_RESHOOT`, and `FULL_SEGMENT_REDIRECT`.
