# Verified production repair workflow

Use for Director timing, continuity, narration, prop or packaging repairs. These are workflow lessons from actual package and take reviews, not guarantees of model behavior. Project preferences belong in a project profile. For The Stone Age Engineer, read [current project locks](../../../../projects/stone-age-engineer/references/PROJECT_LOCKS.md).

## Protect approved material and time the performance

Identify the immutable scope before rebuilding. If an episode must remain unchanged, preserve its complete archive byte-for-byte and verify the hash after packaging; do not run it through the new compiler. Rebalance only the authorized remainder. Maintain a source-to-new episode/scene/segment map with no missing or repeated beats. Episode numbers are not stable identities after rebalancing.

A segment cap is an authoring constraint, not a command to trim every existing video or accelerate audio. Allocate preparation, movement, contact, consequence and necessary reaction first. Preserve speaking time, speaker ownership, complete words and causal cue placement. Check where the speaker is visible after changing cuts. Avoid stretching a simple reach or crouch to fill the segment; start from the phase already pictured in the board and continue to the next result. Do not replay a completed action. If the performance cannot fit, repartition within scope or flag the conflict instead of silently cutting speech or padding frozen frames.

Recompute scene/episode totals, shot windows, dialogue occupancy, sound/music windows, DSL durations, prompt clocks, board timing labels and all mirrors from one authoritative timeline. Remove obsolete prose clocks. A per-segment 10-second request does not authorize a one-second squeeze of a complex action merely because a numerical validator passes. Review unusually short setup/action windows.

## References must describe the current story state

Compile asset descriptions for the current scene, not the whole character's future biography. A sentence saying hunters carry crossbows later can introduce a crossbow now. Omit future inventions, future injuries, repaired states and equipment that are not established. Keep canonical design data separate from current presence/possession. Mentioning a carried kit does not authorize retrieving or displaying it.

Track object count, owner, occupied hand, orientation, hinge/attachment state, support, grip, contact and release. For a lighter: establish retrieval, closed case, opening hinge, wheel stroke, flame at wick, use, lid closure/extinguishing and return to pocket only where authored. Do not repeat the full procedure in unrelated shots. For threats and reactions, name the actual target and screen direction; the reacting subject must perceive the triggering event. Avoid semantic keyword rules that interpret “drops his gaze” as a fall or “without dropping” as a release.

Verify canonical character, location and prop attachment bytes and their final provider slots. In an authored-prompt branch, adding a character picture can shift both location and storyboard indices. Bind previously unbound character definitions, synchronize the storyboard after reference restoration and test repeated synchronization for idempotence. Inspect every definition and use, not merely the number of Picture tokens. Test representative added-character and continuation inputs. A sole-board local test does not validate a live request containing extra pictures, audio or latent context. Do not claim an included code patch is installed.

## MATCH is not a style or audio gate

Keep useful matches. A state-preserving match, a literal first frame and a latent continuation are different mechanisms. Inspect the deployed resolver/generator and the actual request; a false literal-first-frame flag does not prove no AV latent is attached. Do not invent inert package flags to promise a runtime behavior change.

In the inspected RunTech implementation, MATCH can reuse native AV latent plus its corresponding predecessor video. Exporting a stepped MP4 does not re-encode that latent. Keep the native pair consistent; do not replace only the context video and assume the latent is now stepped. Smooth inherited motion is a plausible contributor, not a confirmed diagnosis without request/take evidence. Test the join and every subsequent shot. A static starting frame cannot establish temporal style.

Use a cut only when geography, time, incompatible state or required framing would otherwise demand an unnatural camera journey. Avoid blanket MATCH-to-CUT changes. A genuine composition cut must be authored and verified at the runtime handoff; adding “cut” to prose may not overcome a forced latent join. Preserve continuity flags during a prompt-only repair and disclose a remaining runtime conflict.

## Narration, vocal context and action are separate

Write each spoken utterance once, with exact speaker and timing. Across cuts, refer to the already-started utterance without duplicating its dialogue payload. Check the assembled runtime prompt plus structured dialogue for repetition. Repeated speech is not fixed merely by changing frame rate.

Do not insert a generic allowance such as “Only a separately authored cough or other physical mouth action is permitted” into every shot. It unnecessarily names an unrequested vocal event. If no mouth action is authored, use a relaxed closed-mouth direction during VO. Where a sip, cigarette placement or other mouth action really is authored, specify only that action and separate it from narration articulation. A closed-lip smile must not become a talking smile. ON dialogue retains its intended lip movement.

An Audio reference's timbre-only instruction governs that reference, not automatically the prior clip's latent audio context. When a predecessor vocal event recurs, compare the actual prior audio tail, request continuation settings and the new onset. A short nonvocal opening and explicit narration start may clarify intent; use the scene's real sounds and timings, not a copied universal cough/surf preamble. Do not claim the prompt blocks inherited audio. Preserve ambient/music continuity where intended. Disabling audio continuation or changing live settings needs scope authorization and verification; it is not an automatic skill side effect.

## Review and delivery evidence

Resolve the episode/script and exact clip/take ID before review; scene numbers repeat across episodes. A saved review prompt is not necessarily the immutable prompt used for that take. Compare board pixels, reference bindings, authored actions, available request metadata and rendered results separately. Sample each cut and contact densely enough to observe initiation and completion. Mouth-open screenshots establish a pose violation, not phoneme-level synchronization. Listening/transcription is required to confirm repeated words or coughs; if unavailable, mark audio unverified.

Retiming alone permits board reuse only while panel count/order, cast, location, framing, action phase and object state agree. Preserve reused bytes/hashes. Regenerate actual conflicts such as duplicated background principals, incorrect hand ownership or an unauthorized prop; a prompt patch does not repair those pixels. Flag unresolved boards instead of certifying every board from a schema pass.

Validate the final combined archive through the actual applicable loader, including nested episode ZIPs, byte/file limits and board count. For a nested Director-chunk route, an unintended root series manifest can select a different parser: place a reference manifest under documentation only when that route has been verified. Do not impose this layout on classic series importers. Regenerate source hashes and import/runtime evidence after changes. Read back any authorized live writes by script; skipped episodes are not updated episodes. Distinguish local artifact, saved skill release, deployed server patch, live import and newly reviewed footage in the handoff.
