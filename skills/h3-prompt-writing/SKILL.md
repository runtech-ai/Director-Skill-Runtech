---
name: h3-prompt-writing
description: Write MiniMax H3 video generation prompts for T2VA, I2VA, FL2VA, L2VA, and Ref2VA. Use when rewriting multimodal requests into H3 prompt structures, composing integrated_multimodal_description, overall_soundscape, and non_diegetic_music, aligning keyframes, or defining reference labels for images, videos, and audio.
metadata:
  compatibility: Portable to any agent that can read local files — no external API calls, MiniMax Hub tools, or proprietary runtime required. The agents/openai.yaml file only adds optional ChatGPT/Codex UI metadata; it does not restrict the skill to OpenAI agents.
---

For physical action, timing or storyboard references, read [action physics and timing](../../global/skills/director-pack-skills/references/action-physics-and-timing.md) before direction or review. Speech silence never implies a motion hold; preserve authored movement and intentional stillness.


For H3 movie direction, camera selection, genre treatment or storyboard planning, read [cinematic direction](../../global/skills/director-pack-skills/references/h3-cinematic-direction.md). Select a physically plausible viewpoint and camera path; use its genre guidance only where relevant.

# H3 Prompt Writing

## Workflow

1. Identify the input mode: T2VA, I2VA, FL2VA, L2VA, or full-reference Ref2VA.
2. For base text/keyframe modes, read `references/base-en.txt` and follow its final prompt structure.
3. For full-reference mode, read `references/ref-en.txt` and follow its six-section rewrite format.
4. Preserve the exact field names, section order, labels, and timing notation from the selected guide.

## Base Modes

- T2VA: build the full audiovisual timeline from text.
- I2VA: start from the first frame and develop forward from it.
- FL2VA: describe the continuous path between the first and last frames.
- L2VA: infer a plausible opening and converge to the supplied last frame.

Use `integrated_multimodal_description`, `overall_soundscape`, and `non_diegetic_music` in the order shown in `references/base-en.txt`.

## Full-Reference Mode

Ref2VA rewrites use `subject_definitions`, `summary`, `retention_analysis`, `detailed_description`, `overall_soundscape`, and `non_diegetic_music` in that order. Reference labels stay consistent across all sections.

Read `references/ref-en.txt` for label rules, retention analysis, and complete examples.

## Output Rules

- Write rewrite sections in English; preserve dialogue, lyrics, and visible scene text in their original language.
- Describe each shot by composition, subjects, environment, actions, camera, sound, and the exact point where referenced content appears.
- Avoid plot summaries, unresolved reference labels, and timing that does not match the requested duration.
## Tips for Better Results
- Always match the total duration of the description to the requested video length (4–15 seconds).
- Keep reference labels consistent (e.g. `<Picture 1>`, `<Video 1>`, `<Audio 1>`) across every section.
- Prefer concrete visual and audio details over abstract words like "cinematic" or "beautiful".
- When using keyframes (I2VA / FL2VA / L2VA), clearly state how the first and/or last frame connects to the timeline.

## Character micro-expressions and emotional performance

For character performance authoring or review, read [references/character-microexpressions.md](references/character-microexpressions.md). Apply observable, timed facial changes and separate vocal direction while preserving the selected Director contract, exact dialogue, occupancy, continuity and pacing. In Director validation-only H3 passes, flag or repair genuine prompt defects; do not independently rewrite an approved performance or shot plan.

## Storyboard motion and keyframe roles

When using storyboards for video, repairing frozen poses, selecting animation timing, or checking continuity references, read [references/storyboard-motion-and-keyframes.md](references/storyboard-motion-and-keyframes.md). Preserve requested board composition, animate through its pictured poses, and distinguish identity sheets, storyboard guidance, state references and literal keyframes. In an H3 validation-only pass, flag semantic conflicts for the owning Director repair; do not restyle an approved prompt without authorization.

## Cadence and narration repairs

For stepped motion that fades after early segments, visible speech during voiceover, or prompt-only batch corrections, read [cadence and narration repairs](references/cadence-and-narration-repairs.md). Preserve working segments and separate suspected causes from verified request and rendered-take evidence.

## Cinematic direction repair

For direction, timing, camera, prop, speech or board repairs, follow [cinematic causality and timing](../../global/skills/director-pack-skills/references/cinematic-causality-and-timing.md). Apply project-specific timing, camera and style rules only to that project. For Stone Age Engineer, read the [current project locks](../../projects/stone-age-engineer/references/PROJECT_LOCKS.md).

## Final prompt style and runtime review

Ref2VA uses a brief one- or two-sentence style opening before Shot 1 in detailed_description; base modes follow their own selected guide. Keep observable motion in the shot directions. The full-reference guide’s typical 350–500-word main body is guidance, not a reason to delete essential contact, speech or timing. For prior-context audio, current-state props and immutable episode scope, read [production repair lessons](../../global/skills/director-pack-skills/references/production-repair-lessons.md).
