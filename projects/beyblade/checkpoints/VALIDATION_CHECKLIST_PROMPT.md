# Autopilot All-Validator Checklist Prompt

Use this checklist before every generation and after every completed take. Do not stop after finding the first defect. Return one complete defect inventory, then fix the full issue set together.

## A. Pre-generation gate

- [ ] Read the compact segment checkpoint and `director_intent_digest`; do not reconstruct intent from chat history.
- [ ] Confirm the exact movie, scene, segment and clip IDs.
- [ ] Confirm every required character, prop, location and voice asset is attached, resolved and mapped to the correct `<Picture N>` label.
- [ ] Confirm the current storyboard is attached, non-stale and matches every Director beat, composition and screen direction.
- [ ] Confirm the compiled prompt is authored, current, contradiction-free and contains only permitted camera/edit language.
- [ ] Confirm population counts per shot, identity, anatomy, wardrobe, prop state and location geography are explicit.
- [ ] For Beyblade content, check every action against the project Physics Bible: launcher attachment, ripcord path, torque source, launch direction, contact/support geometry, spin state, stadium interaction, collisions, stopping and Bit-Beast rules. A Beyblade never spins or self-starts without a visible valid cause or carried continuity.
- [ ] Confirm dialogue text, speaker, on/off-screen routing, mouth visibility, timing and no-extra-dialogue rule.
- [ ] Call `list_h3_presets`, then `get_h3_preset` for the exact chosen ID. A 404 means unusable. Never invent IDs or knobs. Pass the exact resolved ID, or intentionally omit it to use saved film settings.
- [ ] Generate only after every preflight item passes.

## B. Post-generation gate

- [ ] Download the exact completed take immediately through the MCP video-download tool and record the local path.
- [ ] Review the entire clip at a minimum of 2 frames per second.
- [ ] Review every cut, transition and ambiguous interval at a minimum of 8 frames per second.
- [ ] Check all authored shot beats and exact cut timing.
- [ ] Count complete and partial instances of every subject in every frame; reject clones, ghosts, reflections, double exposure and extra limbs/bodies.
- [ ] Check identity, face, hair, age, proportions, anatomy, wardrobe and continuity through every frame.
- [ ] Check prop identity, count, scale, orientation, support, contact shadows and state continuity.
- [ ] Check all camera and edit rules: framing, headroom, crop, screen direction, lens intent, movement allowlist, zoom/push, drift, reframing, hard cuts, dissolves and transition ghosts.
- [ ] Check temporal stability: jitter, morphing, flicker, scale pumping, pose drift, disappearing parts and unstable backgrounds.
- [ ] Re-run the complete Beyblade Physics Bible audit, including whether every spin has a valid cause and whether a stopped top has physically valid support.
- [ ] Validate the full audio track: correct speaker, exact dialogue, correct timing, no extra or repeated speech, silent characters do not mouth the line, required sound events and acceptable ambience/music continuity.
- [ ] Compare the complete result with `director_intent_digest`. Pass only if every Director beat is covered, every validator and hard gate passes, and overall scene adherence is at least 95 percent.
- [ ] Glossy Beyblade rendering alone is not a failure when the user has explicitly allowed it.
- [ ] If rejected, record every defect together; repair prompt/storyboard/assets as needed and repeat from section A.
- [ ] If passed, record the final take, local video path, concise outcome and Director-intent digest in the checkpoint ledger, then advance automatically in draft-only mode.
