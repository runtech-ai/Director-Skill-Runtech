---
name: director-storyboard-generator
description: Execute the storyboard pass of an existing v9 Director package, using the latest available ChatGPT image model and shared autopilot preflight gates to inspect, repair and regenerate each segment board before handoff. Use for Director-pack storyboard creation or repair; does not invent a separate shot plan or generate video.
---

# Director storyboard generator

Use the best available built-in ChatGPT image generator under global/rules/storyboard-image-model.md (latest user instruction, 2026-10-02). Record exact backend as unreported when absent. Preserve all canonical-source and pixel-quality gates.

This is the storyboard pass of [director-pack-skills](../director-pack-skills/SKILL.md), not a separate direction pipeline. The current Director micro-shots and canonical assets are the source. Read that skill and its routed storyboard references before work. Load the current project autopilot skill, authoring/physics references and review policy for project content.

Read [media-lifecycle.md](../director-pack-skills/references/media-lifecycle.md) before any media call. Work on one segment at a time, attach only its required references, save each board/review outside conversation context and flush a compact checkpoint before advancing. Do not carry all movie assets, boards or rejected retries into later requests. Keep full pixel validation through bounded review batches.

Read and enforce [storyboard-fidelity-gate.md](../director-pack-skills/references/storyboard-fidelity-gate.md). Every panel must match the Director's exact location, canonical assets and photographed beat. Save expected-versus-observed pixel evidence for each applicable requirement. A mismatch or unreadable required detail blocks acceptance; never silently pass, average away a defect or rewrite the Director to fit the output.

Depict an already-moving subject in its current authored motion state, using the project's required visible motion cues. Do not copy a stationary canonical design pose into a moving beat and expect the video model to initiate the missing motion later. Gate those cues in the actual pixels separately for each object; canonical references supply identity, not current motion. Preserve stationary objects and explicitly authored slower/stopped phases.

1. Run [director-preflight-gate](../director-preflight-gate/SKILL.md) on the owning segment text, attachments, per-object states and effect permissions. Repair contradictions upstream before making a board. Do not add rotation, blur, glow or a mechanism to fill a still panel.
2. Follow [storyboard-images.md](../director-pack-skills/references/storyboard-images.md) for the latest-image-model route, canonical-source isolation, inverse aspect, equal-height stacked panels and exact filenames. Generate only when the user's request authorizes images; a skill-only request does not.
3. Run the same preflight gate on each actual generated board, inspecting every panel at useful resolution against the exact shot. Save failed panel findings with expected/observed state. Never accept from prompt correctness, thumbnail appearance or generation success alone.
4. For failure or unknown required evidence, record all defects and repair the relevant spec/prompt or canonical binding. Change Director direction only for an independently demonstrated source contradiction under its authority, with the revision recorded; never change the beat to excuse the render. Synchronize copies, generate a fresh replacement from current canonical assets and rerun the complete board gate on every panel. Do not use a failed board as an image source. Preserve already accepted boards. Repeat until all applicable gates pass; repeated unchanged failures require clearer depiction of the same authored beat, not a blind retry or unauthorized simplification.
5. Record accepted image provenance, model route/reported variant, gate evidence and revision. Reopen and validate the final storyboard ZIP only after all boards pass. Board acceptance does not accept a video, prove motion/audio, enable H3 storyboard reference automatically or resume a separately deferred autopilot run.
