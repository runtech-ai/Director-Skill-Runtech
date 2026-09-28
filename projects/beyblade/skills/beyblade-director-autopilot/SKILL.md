---
name: beyblade-director-autopilot
description: Run or resume sequential RunTech generation for the Beyblade project, including exact-clip routing, asset-integrity preflight, Draft/Production review, physical launch and stadium validation, Bit Beast rules, and compact checkpoint updates. Use only for this Beyblade project; use the global director-pack skill for reusable package construction.
---

# Beyblade Director Autopilot

Treat skills and live RunTech MCP as authority. Do not reconstruct project state from prior chat. Read `../../PROJECT_INDEX.md` only if the active checkpoint does not identify the needed files.

Before work, read:

1. `../../checkpoints/AUTOPILOT_RULES.json` for the durable loop and acceptance rules.
2. `../../checkpoints/AUTOPILOT_CURRENT.json` for the current segment and take.
3. `../../checkpoints/DIRECTOR_CAPSULE.json` for compact Director constraints.

Whenever a segment contains a Beyblade, launcher, ripcord, stadium interaction, collision, knockout, spin-state change, damage, or Bit Beast, read [BEYBLADE_PHYSICS_BIBLE.md](references/BEYBLADE_PHYSICS_BIBLE.md) and apply every relevant rule as a hard gate. A 95% scene match cannot excuse a physics failure.

## Sequential generation

- When asked to autopilot from a segment, start at that exact segment and continue in package order through the final segment.
- Resolve the exact active scene UUID and clip ID from live MCP. Never generate against an inactive duplicate.
- Before every individual generation request, verify required assets, subject bindings, picture labels, storyboard attachment/readability/freshness, exact scene/clip ownership, and authored prompt source. Then read the complete compiled prompt against the exact Director record and confirm identities, blocking, camera, timing, dialogue or silence, sound, causal order, transitions, and every intended shot beat. Fix every confirmed issue before generating.
- Generate Draft-Anime, validate the complete causal action, make only evidence-based corrections, repeat asset preflight, then generate Production-Anime.
- Production is forbidden until the exact new Draft passes the 97% Director-shot-beat review and all applicable Physics Bible gates. After repeating both preflight gates, call `list_h3_presets`, resolve the live preset named `Production-Anime`, and pass that returned `preset_id` to `generate_segment`; never invent or cache a preset ID.
- Accept only when every Director shot beat is covered, the rest of the scene intent matches at least 97%, all applicable Physics Bible hard gates pass, and the newly versioned take belongs to the exact active clip.
- After each successful generation, download and expose the exact newly versioned video through authenticated MCP instead of displaying a latent image. Never substitute an older take; a stopped or failed run with no new take has no video result.
- Update `../../checkpoints/AUTOPILOT_CURRENT.json` and `../../checkpoints/SEQUENTIAL_VALIDATION_STATUS.md` after each material result.

## Context discipline

Use `../../checkpoints/LOOKUP_INDEX.md` for targeted retrieval. Open only the current segment prompt, relevant package record, and relevant Bible section. Do not reread the full Director package unless a validation failure cannot be resolved from those sources.

The text-only package under `../../director-pack/The_Blade_That_Shouldn_t_Spin/` intentionally excludes media assets. Resolve actual live assets through MCP.

If preset routing, duplicate clips, latent previews, or artifact download behaves unexpectedly, read [RUNTECH_MCP_NOTES.md](references/RUNTECH_MCP_NOTES.md) before retrying.
