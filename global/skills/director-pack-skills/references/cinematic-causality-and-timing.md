# Cinematic causality, timing and reference discipline

Use [action physics and timing](action-physics-and-timing.md) for shared physical direction. The project preferences below do not establish global fixed-camera, duration or cadence defaults.

The project-specific preferences below apply to The Stone Age Engineer. Read its [current locks](../../../../projects/stone-age-engineer/references/PROJECT_LOCKS.md); use other projects’ own timing, camera and style choices elsewhere. These are editorial requirements, not model guarantees.

## Author the movie before compiling the prompt

State the dramatic change of each shot in one sentence. Give each character a physical objective, a visible trigger, a continuous action, a completion state and a reason to remain in the shot. A reaction follows something the character can see, hear or feel. Set the eyeline and action axis explicitly when spatial understanding matters. Do not fill time with a frontal portrait, presentation pose, idle hands, an unnecessary glance or a repeated gesture. A deliberate pause is allowed only when it expresses a specific decision or listening beat.

Write opening and closing object states before prose: object identity, count, owner, hand, position, orientation, state and the event permitting the change. Pocketed items stay concealed. Possession does not authorize appearance. Show retrieval when needed; an established carried object can continue across a matched cut. Complete receiving contact before release in a handover. No new props or actors to illustrate narration. In this project, indigenous materials are Stone Age unless the story has already established a new craft; only Kenji's authored original belongings are initially modern. Do not list all his possessions in unrelated video prompts.

## Camera and editing

For this project the camera position, lens and framing remain fixed within each shot. No zoom in/out, dolly push/pull, orbit, floating tracking, automatic subject centering or digital scale pumping. Blocking creates motion inside the composition. A cut must reveal a new cause, consequence, reaction, useful detail, space or elapsed time. Avoid redundant close-up resets. Preserve useful match continuity; use a cut when continuity would require an unnatural camera journey or incompatible geography, time or object state. Never convert every boundary to CUT by default. Preserve eyelines and screen direction over necessary edits.

## Time follows action

For The Stone Age Engineer, preserve EP1 unchanged; from EP2 onward cap segments at 10 seconds, retaining shorter natural segments. Keep episodes around 90 seconds by rebalancing only the authorized remainder. Shots have action-led variable lengths. Allocate time from the actual movement and spoken performance. Do not enforce three five-second shots or six fifteen-second segments. Keep generation requests within the current supported duration. If more short segments are needed, repartition and update all IDs, timing mirrors, dialogue occupancy and board mappings. Never lengthen a simple reach, fall or transfer to satisfy a quota. Do not accelerate or cut off speech to fit an arbitrary visual grid. Narration can bridge cuts without restarting. Episode runtime must be calculated from the delivered timeline, not left at the old nominal value.

## H3 compilation and evidence

Read the current official MiniMax-AI/MiniMax-H3 base and full-reference guides. Use the selected mode's real format. For Ref2VA use six sections; each retention entry names a real reference and its preservation relationship. Keep style and observable performance in the detailed shot prose. Start later shots with their actual cut times. Distinguish character appearance, location geometry, storyboard staging, literal endpoints and audio roles. Identity-sheet backgrounds and neutral poses never become film content. A storyboard is planning guidance unless explicitly chosen as a literal keyframe. Verify actual attached reference bytes and label order; text mentioning a location is not an attachment.

Keep prompts specific, not bloated: describe the visible starting state, action trajectory, physical contact, result and sound. Avoid duplicating the same restrictions in every section. Do not compress away causal information simply to reach a word limit. The official guide's normal detail range is guidance, not permission to invent events.

Dialogue occurs once in the complete request. Keep stable speaker IDs and assign articulation only to the actual visible speaker during their window. Off-screen narration never drives a visible mouth. Inspect the final compiled request for duplication between structured dialogue and authored text. Official cross-cut syntax and importer behavior are separate concerns: test the real compiler before splitting an utterance. If native VO repeats or triggers lip motion, provide a silent-picture variant and an independently timed narration cue sheet; never pretend it is already voiced. Preserve intentional physical mouth actions such as sipping or coughing.

## Animation

Use the user's hand-painted 2.5D aesthetic, visible brushwork, faceted forms, chiaroscuro and volumetric light. Plan readable anticipation, contact, weight shift and recovery at normal action speed. The current project target is 20 fps with two-frame exposures (10 pose changes per second); it supersedes the earlier on-threes request. Frame holds do not mean the actor freezes for seconds. Do not promise exact exposure from text alone. Review consecutive frames for cadence and full motion for weight and contact. A post-process can enforce repeated frame exposure but cannot repair bad acting, object topology, drifting camera, wrong characters or lip movement.

## Reuse boards carefully

Retiming alone need not change a board when shot count, order, subjects, location, framing, physical phase and object states still agree. Record reuse and preserve image hashes. Regenerate only conflicting boards, preserving the user's 16:9 canvas with separated shot columns. Inspect actual pixels before acceptance. A failed video does not automatically mean its board is wrong: compare board, authored prompt, actual request, attached references and rendered take. If shot grouping changes, old panel count/mapping is no longer valid. Never relabel stale evidence as a fresh pixel pass.

## Preflight and reporting

Validate complete source-to-package timing, speech ownership, prop introductions, action/reaction order, occupied hands, canonical reference closure and board mapping. Remove contradictory old rules and absolute times after retiming. Record structural validation, local importer validation, actual request verification, board pixel review and rendered take review separately. Do not call prompt-only changes a corrected movie. Do not run paid generation, stop an active batch, deploy or refresh live series when the user requests local preparation.

Sources checked 2026-10-20:
- https://github.com/MiniMax-AI/MiniMax-H3/blob/main/skills/h3-prompt-writing/references/ref-en.txt
- https://github.com/MiniMax-AI/MiniMax-H3/blob/main/skills/h3-prompt-writing/references/base-en.txt

The project camera ban, approximate 90-second episodes, object ledgers, board-reuse gates and exposure acceptance rules are project decisions informed by observed failures, not official MiniMax guarantees.

For protected-episode hashes, latent/audio handoffs, current-state references and repair evidence, follow [production repair lessons](production-repair-lessons.md).
