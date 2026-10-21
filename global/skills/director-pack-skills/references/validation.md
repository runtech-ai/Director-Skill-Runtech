# PACK VALIDATION

For action timing, support/contact transitions and storyboard temporal roles, apply [action physics and timing](action-physics-and-timing.md). Preserve existing fields and distinguish motion review from schema acceptance.

Do not write `"valid": true` only because your own paths resolve.

## Content convergence

Run [prompt-repair-loop.md](prompt-repair-loop.md) before H3 form validation and final handoff. Check every object's current state, permitted cause and effect window against source authority. Reject unsolicited motion/effects, visual event cues in audio fields, mixed-outcome generic locks and contradictory or duplicated repairs. Apply mechanics only to the relevant visible phase. Synchronize all redundant representations after a content repair, then recheck the complete pack and affected boundaries. Record text, pixels, runtime attachments and generated-take review separately; unavailable evidence is unknown, never a pass.

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

Run [storyboard-fidelity-gate.md](storyboard-fidelity-gate.md) on every panel's actual pixels. Require separate passing location, asset and beat records bound to the board hash and current Director/asset revisions. Any failed or unknown applicable requirement blocks accepted status and final ZIP inclusion. No silent waiver, inherited pass or aggregate-score substitution is allowed.

Run the zip checks in [storyboard-images.md](storyboard-images.md). Member count equals the segment count. Every member is `<SEGMENT_ID>.png` at the archive root.

Also run [direction-continuity-asset-lock.md](direction-continuity-asset-lock.md) against the rendered pixels. Report segment counts and ids under `PASS_NO_RESHOOT`, `PROMPT_ONLY`, `STORYBOARD_RESHOOT`, and `FULL_SEGMENT_REDIRECT`.

Also run [v9-common-movie-direction.md](v9-common-movie-direction.md): every board uses the inverse of the movie delivery aspect (16:9 movie → 9:16 board; 9:16 movie → 16:9 board), has an equal-height TOP_TO_BOTTOM stack, and contains exactly one panel per micro-shot. If the content is Beyblade, report the project Physics Bible hard-gate result for every applicable shot.

## Imported continuity

Run [the RunTech continuity import gate](runtech-continuity-import.md) before final handoff. Compare every effective normalized incoming/outgoing mode, predecessor, previous-frame flag and first-frame policy against the authored boundary. Include the HARD_CUT override regression and recheck exported ZIP records. If a live import is requested, read back saved fields and verify the stored artifact identity; keep local normalization and deployed evidence separate.

## Camera plausibility

Review [camera techniques](camera-techniques.md): bounded start/path/end, feasible support and clearance, coherent optics/focus, readable axis, and a motivated move or static composition. Keep the existing [action physics and timing](action-physics-and-timing.md) checks. Reject unexplained viewpoint teleportation, solid-object fly-throughs, geometry warping and unrequested motion/zoom drift. A still or a text validator cannot certify camera movement in a take.
