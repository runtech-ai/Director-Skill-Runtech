# H3 direction, reference planning and storyboard workflow

Read this when directing or repairing H3 film prompts. Load [camera techniques](camera-techniques.md) and the relevant [genre language](genre-camera-language.md), preserving [action physics and timing](action-physics-and-timing.md). Evidence, source links and limits are recorded in [research sources](cinematic-research-sources.md). This workflow improves authoring; it does not certify model compliance or authorize media generation.

## Keep the three instruction layers separate

1. **Director plan:** authored events, shot windows, physical states, camera, dialogue occupancy and continuity in the existing package fields. This is the semantic authority.
2. **Human/API brief:** the hosted service or MMX may accept a production brief and rewrite it. Its storyboard template is not automatically the final model prompt.
3. **Final H3 representation:** use the installed official base or Ref2VA guide for its actual mode and syntax. Keep attachment labels and wrappers out of planning-only fields. Inspect a compiler's resolved output before claiming it preserved the plan.

MiniMax's official CLI and model guides address different layers. Do not concatenate their two formats, replace the v9 importer contract with the CLI template, or assume legacy Hailuo camera tokens are H3 controls. Check the actual service interface for supported duration, reference limits, prompt length and available settings. Do not invent negative-prompt, seed, FPS, lens, motion-strength or camera-path API fields. Natural-language camera directions remain requests, not programmed rig controls.

## Plan the scene before writing its prompt

Identify the visible change and the viewpoint that makes it readable. Lay out geography, blocking, key contact/release events, necessary reaction and speech. Choose cuts because information or viewpoint changes, not because every segment needs a fixed number of shots. A single simple shot is a useful diagnostic baseline, not a universal limit on H3.

Allocate time from the performance and physical action. Preserve authorized dialogue windows; voiceover can bridge action and cuts without making bodies move slowly. A minimum generation duration does not make a short event longer. Keep camera speed independent of subject speed and of stepped animation cadence. Preserve an intentional quiet beat; remove empty padding. If a locked duration cannot fit the required actions, report that conflict or repartition within the authorized scope.

Use one coherent style opening and concrete changing events. Prefer a small number of useful visual details over competing style adjectives. “Cinematic, epic, dynamic, beautiful” does not specify blocking, speed or a feasible camera route. Reiterate a local invariant only when its failure would break the action; do not repeat the whole reference policy in every shot. Remove contradictions rather than surrounding them with negative instructions.

## Select the input mode deliberately

For T2VA, establish the opening from text. For I2VA, begin from the supplied image and describe what happens next. For FL2VA/L2VA, make the path and final arrival consistent with the actual endpoint; do not choose nearly identical endpoints for an action that must visibly change state unless the authored action returns there. Ref2VA separates reusable identity/design, composition, motion and audio roles. Use its official definitions and retention markers. The exact guide remains the syntax authority.

Before attaching a reference, answer what it supplies and what is allowed to change. A character sheet supplies design, not a neutral pose or studio background in the scene. A location plate supplies geography, not incidental people. A board supplies planning, not permanent limb positions. A motion video can supply a specific performance or temporal pattern without importing its cast or entire camera behavior. Use a relevant reference with compatible direction, speed and view; do not assume any exciting action clip is a good match. Separate voice timbre from copying the source's words. Match labels to actual upload order.

The final request must reflect the real attachments, not a hypothetical list. Missing or dropped references, stale prior takes and mismatched first-frame routes can defeat otherwise correct direction. Record exact prompt, model/service variant, duration, reference roles, attachment order and selected predecessor when troubleshooting. Keep provider defaults/rewrites visible when the interface exposes them; if it does not, mark them unknown.

## Storyboards are spatial evidence; timing needs a timeline

Begin with rough composition and blocking decisions, then resolve the shot's selected instant before polishing. Professional boards and layout work address framing, staging and timing, but a still sheet alone cannot demonstrate event duration or a moving camera path. A written timing walkthrough can expose a contradiction without generating media.

For each authored shot, record in existing prose or sidecar notes:

- entry, decisive action and exit; the panel's entry/intermediate/exit role;
- camera start/path/end, axis and focus behavior;
- subject motion versus camera motion, including foreground/background relationships;
- cut motivation and the state handed to the next shot;
- the source of dialogue, effects and any specifically timed sound.

Preserve the existing Director board layout and one-panel-per-authored-shot contract. Do not create extra imported shots just to show phases of one movement. Optional separate planning sketches or an animatic require their own scope and must not be substituted for the imported board. Keep arrows, equipment diagrams, annotations and timing tables outside clean reference imagery unless the selected workflow explicitly supports them. A motion arrow is an explanation, not proof of movement and not a physical prop in the scene.

For a moving shot, one panel may depict the beginning, an important intermediate view or the destination. The other camera states remain in text; do not reject a correct intermediate panel merely because it is not the opening. Confirm that the intended path has enough environmental coverage. A front-only character image or flat room plate does not reliably define a full reverse-angle orbit.

When the user requires composition fidelity, keep the requested board reference and declare its planning role. If image conditioning repeatedly wins over movement, first inspect pose role, prompt state changes, endpoint routing and duration. A board-off comparison is an authorized diagnostic option, not a silent production-policy change. If literal keyframes contradict action, fix the reference or plan within scope; “ignore this image” is not a reliable repair.

## Compile sound and cuts without introducing new events

Use the selected official guide for speaker IDs, exact spoken content and shot timestamps. Keep voice identity stable; distinguish visible speech from offscreen narration. Put specific physical sounds at their causal event and summarize ambience separately. An impact sound cannot substitute for missing visible contact. Score tempo does not set physical speed unless a specific synchronization is authored.

For speech spanning a cut, the final guide provides cross-cut markers. Preserve the complete scripted utterance once in source data; if the adapter uses split final text, partition exact text without repeating or inventing words. Verify the real adapter and dialogue occupancy together. If the installed v9 route cannot represent the required continuity, return the conflict to Director authoring for a supported cut/line arrangement; do not paste incompatible wrappers into the planning schema. Do not discard essential action or speech to meet an arbitrary word-count target.

## A complete base-mode example

This original T2VA example assumes a six-second request, no references, no dialogue and no music. It illustrates a deliberate cut and natural-speed action; it does not define a universal template duration or camera restriction.

```text
integrated_multimodal_description: [Shot 1] Live-action observational documentary. An eye-level medium-wide view from the clear side of a workbench frames a mechanic holding a bicycle wheel beside its fork. Soft daylight enters from the workshop window. The shoulder-held camera makes small human weight corrections while the mechanic lifts the wheel into place at an ordinary working pace. Her fingers support the axle as it seats; she keeps the wheel supported. [Shot 2] At 00:03.500, the camera cuts to a steady close insert from the same side of the bench. Her thumb closes the fastening lever while the other hand steadies the wheel. A small metallic click coincides with the lever seating. She releases her support only after the fastening is secure, then checks the seated wheel with a short, firm touch. Camera position and lens remain fixed through the insert.

overall_soundscape: Low workshop room tone with distant street traffic. Clothing brushes the bench; the wheel fastening clicks once at closure.

non_diegetic_music: N/A
```

## Repair by observed failure, not folklore

| Observed problem | First useful checks | Focused correction |
|---|---|---|
| Slow/floaty action | Requested event time, hold instructions, endpoint separation, playback timestamps | Restore a brief active phase and its consequence; preserve real elapsed time. |
| Frozen board pose | Panel role, support state, start/end conditioning, final prompt | Animate through the selected instant; repair contradictory references. |
| Wandering camera | Missing landing, ambiguous support/path, conflicting style tokens | Define one bounded route and endpoint, or hold a purposeful fixed viewpoint. |
| Unreadable impact | Framing, occlusion, simultaneous camera/body changes | Show the interaction from a clearer side; simplify camera before adding adjectives. |
| Wrong shot order / panel sheet on screen | Actual labels and all-shot mapping; composite mistaken for keyframe | Correct mapping and route; state one full-screen shot per mapped panel. |
| Identity/prop drift | Wrong asset or reference role; incompatible design/state images | Keep canonical design and current state distinct; fix only the conflicting bindings. |
| Smooth motion in a stepped style | Style conflicts and inherited motion context | Specify pose cadence separately from speed; inspect sequences, not a still. |
| Voice duplication / mouth motion during VO | Final text versus structured line, audio role and occupancy | Repair speaker/audio ownership and the final compiler output. |

When generation is later authorized, compare a few controlled variants: same action with a static camera, same action with a motivated move, then one reference-role change if needed. Keep model, duration and other settings fixed where supported; retain seeds when available without promising reproducibility. Evaluate every take rather than selecting only an attractive frame. Avoid claims that a magic phrase, huge negative list, arbitrary CFG change, prompt-only FPS request or post-hoc speed-up guarantees realistic motion. No new generation is part of a skills-only update.
