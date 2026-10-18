# H3 validation and compiler layers

Direction remains owned by the selected Director contract. The official `h3-prompt-writing` skill validates the final H3 form; it does not independently restyle approved direction, occupancy, camera or exact dialogue.

## Identify the field before validating

RunTech has separate planning and final-prompt layers. The current normalized `ShotPlanningPrompt.compiled_prompt` and `StoryboardReferencePrompt.reference_prompt` are guidance: their validators reject `<Picture>`, `<Audio>`, `<Video>` attachment labels and `subject_definitions:` / `retention_analysis:` wrapper sections. Keep structured dialogue in its authored records and planning prose consistent with the planning schema. Do not paste a six-section Ref2VA prompt into a planning-only field.

The final H3 request packager owns actual attachment numbering and H3 syntax. Some importer versions recognize a complete packaged H3 prompt separately, even when the package envelope uses a similarly named `compiled_prompt` field. Inspect the actual importer/adapter and normalized result before choosing that route. Do not invent a new schema field or assume identical names imply identical contracts. Local schema acceptance does not establish deployed compatibility.

## Validate the final H3 output

1. Open the installed `h3-prompt-writing` skill. Read its selected guide: `references/ref-en.txt` for Ref2VA, `references/base-en.txt` for T2VA/I2VA/FL2VA/L2VA. If unavailable, report the missing dependency; install only if requested.
2. Check the actual final/runtime-resolved prompt for official section names/order, retention vocabulary, duration, timing notation and exact dialogue/lyrics in `<d>`.
3. Check definitions, retention, every shot, dialogue owners and actual attachment mappings together. Subject, Picture, Audio and clip-local speaker IDs are independent. First vocal occurrence sets speaker order; never infer Picture/Audio order from a library listing.
4. Repair only a confirmed H3 form defect. Preserve approved direction and exact dialogue/windows. No issue means no rewrite. Return semantic or state conflicts to the owning Director repair.

Record planning-schema checks, final H3 form checks, attachment-resolution checks and rendered audio/visual acceptance separately in the validation report. Unknown runtime inputs cannot be reported as validated attachment or voice identity.
