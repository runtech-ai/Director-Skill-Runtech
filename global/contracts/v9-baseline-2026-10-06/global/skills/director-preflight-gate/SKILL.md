---
name: director-preflight-gate
description: Validate Director package text and rendered segment storyboards against source, canonical assets, per-shot states and current project autopilot gates before handoff or generation. Use with the Director pack and Director storyboard generators; does not generate media or approve unreviewed takes.
---

# Shared Director preflight gate

Use the best available built-in ChatGPT image generator under global/rules/storyboard-image-model.md (latest user instruction, 2026-10-02). Record exact backend as unreported when absent. Preserve all canonical-source and pixel-quality gates.

Read the current project autopilot skill and its gate policy before review. For Beyblade RunTech, read `projects/beyblade/skills/beyblade-director-autopilot/SKILL.md`, its `references/DIRECTOR_AUTHORING.md` and applicable Physics Bible sections. Resolve live authority through RunTech MCP when reviewing runtime attachments. Checkpoints are navigation caches.

Read the global Director [content repair loop](../director-pack-skills/references/prompt-repair-loop.md) and [validation contract](../director-pack-skills/references/validation.md). Preserve the v9 importer schema. User corrections and explicit review waivers override older conflicting rules.

## Select the evidence layer

Before media retrieval or generation, enforce [media-lifecycle.md](../director-pack-skills/references/media-lifecycle.md): segment-local attachment ledger, deduplicated required references, supported file/artifact transport, bounded serialized payload and a text-only resume record. A transport failure is not a content pass; never remove required evidence to fit. Review files in bounded batches without reducing required coverage.

- **Director text:** validate raw source, every micro-shot, exact structured dialogue/occupancy, asset closure, object support/ownership, motion causes, effect permissions, camera allowlist and boundary state. Check agreement across authoritative and redundant package files. Neither a correct schema nor a keyword scan proves semantic correctness.
- **Storyboard:** inspect the actual image and every panel against its owning micro-shot, not just its prompt or metadata. Verify inverse movie aspect, equal-height TOP_TO_BOTTOM bands, exact panel count/order, no text/divider leakage, canonical identity, population including partial bodies, natural hands, wardrobe, location geography, prop scale/support, phase of action, camera perspective and incoming/outgoing continuity. Verify that only the authorized emitter shows an effect. A still cannot prove full motion, lip-sync or audio; record those as deferred to exact-take review, never passed.
- **Generated take:** only when separately requested or already authorized, use the project's exact-clip full-motion and audio gates. Do not queue a video as part of a text-only or board-only gate. The current project defines hard gates, soft adherence thresholds and waived checks; do not impose a global numeric threshold or revive a waived audio requirement.

Review all applicable hard gates even when the soft scene score is high. A correct panel does not compensate for another failing panel. For a board, the timed intent must match the shot specification, but do not claim a still verifies exact cut timestamps or continuous motion.

For boards, enforce [storyboard-fidelity-gate.md](../director-pack-skills/references/storyboard-fidelity-gate.md) as a hard gate: exact Director location, asset identity/state and beat in every panel, with separate expected/observed pixel evidence. Required visual mismatches or unknowns block acceptance regardless of video soft thresholds. Never silently waive a requirement, accept by aggregate score or rewrite the Director to match the render. Record the board hash and Director/asset revisions; changes invalidate affected prior acceptance.

For each already-moving object, also verify the project-required visual motion/speed cues in the board pixels. A stationary-looking reference pose contradicts that beat and fails; unreadable required motion cues are unknown. Record these per object alongside support/contact, and never accept on the expectation that the video model will create the missing motion later. A still does not establish continuous motion or measured speed.

## Result and repair

Record scope, source revision, asset provenance, exact segment and shot/panel, expected versus observed state, evidence path, hard-gate results, soft score when applicable, defects and next repair. Use `pass`, `fail`, `unknown`, `not_applicable` or `not_required_by_user` accurately. `unknown` required evidence cannot authorize handoff.

Classify `PROMPT_ONLY`, `STORYBOARD_RESHOOT` or `FULL_SEGMENT_REDIRECT`. Feed the defect back to the owning generator. Repair the earliest source, synchronize affected representations and rerun this gate on the resulting text or actual pixels. Keep accepted work; replace only affected boards, using fresh canonical sources. Repeat until every applicable gate passes or the user stops, an explicit run/cost limit is reached, or a real authority/infrastructure blocker remains. Record that blocker and resume action instead of reporting completion.

A request to update these skills runs text/link validation only. It does not authorize repairing a movie pack, rendering boards or starting autopilot.
