---
name: beyblade-director-autopilot
description: Run or resume sequential RunTech generation for the Beyblade project, including exact-clip routing, asset-integrity preflight, Draft/Production review, physical launch and stadium validation, Bit Beast rules, and compact checkpoint updates. Use only for this Beyblade project; use the global director-pack skill for reusable package construction.
---

# Beyblade Director Autopilot

Read [production locks](references/PROJECT_LOCKS.md) and [repair review rules](references/REPAIR_REVIEW_RULES.md) for current scope and evidence rules. An explicit active generation request is required for this workflow; old checkpoints or skill updates do not authorize a new run. The current repair workflow leaves video regeneration to the user unless they request otherwise. Resolve the project repair ledger and live state rather than historical branch completion claims.

Treat skills and live RunTech MCP as authority. Do not reconstruct project state from prior chat. Read `../../PROJECT_INDEX.md` only if the active checkpoint does not identify the needed files.

Before work, read:

1. `../../checkpoints/AUTOPILOT_RULES.json` for the durable loop and acceptance rules.
2. `../../checkpoints/AUTOPILOT_CURRENT.json` for the current segment and take.
3. `../../checkpoints/DIRECTOR_CAPSULE.json` for compact Director constraints.

Whenever a segment contains a Beyblade, launcher, ripcord, stadium interaction, collision, knockout, spin-state change, damage, or Bit Beast, read [BEYBLADE_PHYSICS_BIBLE.md](references/BEYBLADE_PHYSICS_BIBLE.md) and apply every relevant rule as a hard gate. A 95% scene match cannot excuse a physics failure.

A stationary Beyblade may start spinning only from visible deliberate hand input, a Bible-valid launcher release, or continuous carry-over from the immediately previous authored shot where it was already spinning. Apply this to physical, dream, symbolic, magical, and Bit Beast imagery. If no allowed cause exists, keep the top stationary and move the camera; reject unexplained orientation change, circular trails, spin blur, or sudden RPM.

## Sequential generation

- When asked to autopilot from a segment, start at that exact segment and continue in package order through the final segment.
- When the project checkpoint marks temporary Draft-only mode active, generate and validate only Draft quality. After an accepted Draft, checkpoint and advance directly to the next segment. Never queue Production until the user explicitly lifts Draft-only mode.
- While autopilot is active, a user correction, question, failed take, prompt repair, storyboard repair, or checkpoint update never ends the generation task. Apply the correction and immediately resume the active segment's Draft-to-Production loop. Continue through the final segment unless the user explicitly says stop or a real infrastructure/authority blocker prevents progress.
- Resolve the exact active scene UUID and clip ID from live MCP. Never generate against an inactive duplicate.
- Before every individual generation request, verify required assets, subject bindings, picture labels, storyboard attachment/readability/freshness, exact scene/clip ownership, and authored prompt source. Then read the complete compiled prompt against the exact Director record and confirm identities, blocking, camera, timing, dialogue or silence, sound, causal order, transitions, and every intended shot beat. Fix every confirmed issue before generating.
- For every shot, enumerate the Director-permitted camera movement, speed, duration, lens behavior, screen direction and transition. Reject or rewrite unspecified, unmotivated, unusable, contradictory or overly fast zooms, pushes, dollies, orbits, rolls, whips, speed ramps, panel interpolation and focal-length changes. Hard cuts have no transitional camera travel. Pans preserve distance and focal length and may not masquerade as zooms. Any generated movement outside the per-shot allowlist is a hard failure regardless of the 95% scene score. If one allowed pan is generated as an unapproved zoom, push or scale change, do not retry that ambiguous move; fall back to locked usable coverage that preserves subject priority and screen direction before the next generation.
- Before acceptance, derive the exact permitted human, creature, Beyblade, launcher and stadium count for each shot. Review the entire clip at no less than 2 fps, then inspect every cut neighborhood and ambiguous motion at 8 fps or higher in full-resolution frames. Count complete and partial bodies, faces, heads, hands and silhouettes. Reject clones, same-identity duplicates, double exposures, transitional ghosts, extra partial bodies, repeated faces, unintended reflection copies, merged identities and unlisted subjects. Population failure is a hard gate regardless of the 95% score.
- Never stop validation at the first confirmed failure. Finish the whole-clip defect inventory across every Director beat, framing, composition, population, identity, anatomy, wardrobe, object count, asset fidelity, camera/edit rule, temporal transition, Beyblade causality/support geometry, dialogue, speaker-mouth routing, extra speech, sound intent and visual style. Correct the complete evidence-backed issue set together before spending a retry.
- If a visible silent character mouths an off-screen speaker's line, reject the take. Preserve the action but reframe the non-speaker back/three-quarter-away or keep their mouth outside the composition on retry; the off-screen speaker stays unseen and remains the only voice.
- The user authorizes recreating a current segment storyboard when its visual instruction conflicts with corrected canon, physics, wardrobe, anatomy, blocking, prop coverage, camera intent, or repeatedly causes grounding failures. Generate every replacement fresh from original Director source asset sheets plus the current authoritative beat specification. Never edit, trace, recolor, composite, or recursively regenerate from a previous storyboard or rejected output; stacked pixels cause color, identity, geometry and composition drift. Preserve valid Director beats and timing, replace and reattach the storyboard on the exact segment, verify it decodes and is non-stale, then repeat every pre-generation gate before spending the next run.
- Enumerate and lock every visible subject's canonical body traits and exact per-shot wardrobe, while treating blankets, coverings, garments, limbs and props as separate objects. Reject clothing-category or length changes, shorts becoming trousers, bedding becoming clothing or limbs, covering substitutions, and any morph or merge between a subject, garment, blanket, limb or prop. Project-specific exceptions or corrections belong in the project checkpoint and exact segment prompt before generation.
- Before every generation, classify every Beyblade appearance as physical action, stable supported handling, stopped/resting, or explicitly symbolic imagery. Reject prompts that permit a physical top to spin in a hand, fingers, pocket, bedding, or unsupported air; reject stopped tops without visible gravity/contact support; and isolate symbolic rotation from all hands, bodies, launchers, stadiums, bedding, and real-world surfaces. Also preflight visible anatomy for the correct count of complete, distinct limbs, including two separate readable legs when both should appear. Rewrite ambiguity before spending a run.
- Before choosing H3 settings, call `list_h3_presets`, select only an id it returns, then call `get_h3_preset` on that exact id. Treat any listed id that returns 404 as unusable. Pass only a successfully resolved exact `preset_id`; never invent preset ids or individual Comfy/H3 knobs.
- Omitting `preset_id` means intentionally using the film's saved `h3_settings` unchanged. `quality` and `update_movie_quality` are labels only and never select generation knobs. Use `apply_h3_preset(movie_id, preset_id)` only when the resolved pack should become the saved film default.
- Generate and validate the complete causal action, make only evidence-based corrections, and repeat asset preflight before every retry. Production is forbidden until the exact new Draft covers every Director beat, reaches at least 95% scene adherence, and passes every validator and hard gate; when Production is authorized, resolve its intended preset through the same list-plus-get gate before generation.
- Accept only when every Director shot beat is covered, overall scene adherence is at least 95%, every validator and applicable Physics Bible hard gate passes, and the newly versioned take belongs to the exact active clip.
- Validate every completed take at no less than two evenly spaced frames per second (30 frames for a 15-second segment), plus the frames immediately surrounding each authored cut. Reject frame jitter, malformed or duplicated transition frames, identity drift, missing/merged/duplicated/malformed limbs, prop/population popping, geometry breaks, storyboard-grid leakage, dialogue-mouth routing errors, or physics discontinuities.
- Audit the completed take's entire audio track against the exact Director dialogue and sound intent. Require each scripted line exactly once from the assigned speaker only, with matching on-screen lip movement when visible. Reject missing, duplicated, reassigned, paraphrased, or extra dialogue; any speech in silence/ambience-only beats; and any non-speaker lip-sync.
- After each successful generation, download and expose the exact newly versioned video through authenticated MCP instead of displaying a latent image. Never substitute an older take; a stopped or failed run with no new take has no video result.
- Update `../../checkpoints/AUTOPILOT_CURRENT.json` and `../../checkpoints/SEQUENTIAL_VALIDATION_STATUS.md` after each material result.

## Context discipline

Use `../../checkpoints/LOOKUP_INDEX.md` for targeted retrieval. Open only the current segment prompt, relevant package record, and relevant Bible section. Do not reread the full Director package unless a validation failure cannot be resolved from those sources.

The text-only package under `../../director-pack/The_Blade_That_Shouldn_t_Spin/` intentionally excludes media assets. Resolve actual live assets through MCP.

If preset routing, duplicate clips, latent previews, or artifact download behaves unexpectedly, read [RUNTECH_MCP_NOTES.md](references/RUNTECH_MCP_NOTES.md) before retrying.

## Episode continuity corrections

For The Blade That Listens, read [references/EPISODE_CONTINUITY_LESSONS.md](references/EPISODE_CONTINUITY_LESSONS.md) before prompt or storyboard work. These explicit user corrections supersede conflicting older checkpoint assumptions.

For launcher handedness, rack geometry or current saved-voice repairs, read [repair lessons](references/LAUNCHER_AND_VOICE_REPAIR_LESSONS.md). The current explicit voice/timbre request supersedes historical audio waivers.
