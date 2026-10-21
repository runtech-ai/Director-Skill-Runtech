# V9 COMMON MOVIE DIRECTION AND PREFLIGHT

Apply [action physics and timing](action-physics-and-timing.md): assign each panel an entry/intermediate/exit role, preserve causal motion through its pose, and review event duration separately from still-image fidelity.

Apply these rules to every Director package before authoring or generating any segment. They are additive to the importer-locked v9 contract and do not rename or move any schema field.

## Preflight is a hard gate

Before a segment is accepted for generation or storyboard rendering, verify the exact directed record against every micro-shot:

- canonical identity, wardrobe, location, prop ownership, population, and attachment mapping resolve;
- start/end state, screen direction, camera, cut, light, damage, motion causality, dialogue occupancy, silence, ambience, and music continuity agree;
- every action with real-world mechanics has an explicit physically causal state chain; and
- the storyboard spec, storyboard prompt, and rendered board match the same micro-shots.

Record a failure as `PROMPT_ONLY`, `STORYBOARD_RESHOOT`, or `FULL_SEGMENT_REDIRECT`; do not generate from a failing record. A corrected storyboard is generated fresh from the Director package's canonical assets and current beat specification. Never use a prior or rejected storyboard as a repair source.

## Inverse-aspect stacked storyboard standard

Every segment storyboard uses the **inverse aspect ratio of the movie delivery frame**: a 16:9 movie uses a portrait 9:16 storyboard; a 9:16 movie uses a landscape 16:9 storyboard. It contains exactly one panel for every authored micro-shot, in playback order.

- Panels are equal-height horizontal bands, stacked **TOP_TO_BOTTOM** and read from the top down, regardless of the board orientation.
- `beatCount`, spec beats, and the rendered panel count each equal the segment's micro-shot count. There is no independent 3–10 beat choice.
- The first panel is Shot 1; the last panel is the final shot. Each panel preserves the owning shot's timing, framing, lens intent, camera context, visible assets, state, and continuity.
- Use only clean horizontal dividers between panels. Never include captions, numbers, speech bubbles, subtitles, timestamps, labels, watermarks, typography, gutters, a grid, or adjacent-panel leakage.
- The board is a planning reference, not a video frame. When an H3 storyboard reference is explicitly enabled and attached, consume its panels sequentially as one full-screen moving shot at a time; never render the sheet, dividers, or multiple panels into the video.

## Conditional Beyblade physics authority

If the movie contents include a Beyblade, launcher, ripcord, stadium interaction, collision, knockout, spin-state change, damage, or Bit Beast, the Director must load the project-local **Beyblade Physics Bible** before direction, storyboard authoring, preflight, generation, or acceptance.

Treat every relevant Bible rule as a hard gate. Record the top's owner/design, spin direction, attachment/release state, RPM band, tip/contact state, stadium zone/path, collision result, damage, and Bit Beast state per shot. A visually strong result still fails when launch torque, release, gravity, tip contact, rotation, collision, knockout, population, identity, or Bit Beast anchoring is physically impossible.

Do not load Beyblade canon or physics for non-Beyblade movies. Project-specific knowledge remains in its project directory; this common rule only routes the Director to that authority when the content requires it.
