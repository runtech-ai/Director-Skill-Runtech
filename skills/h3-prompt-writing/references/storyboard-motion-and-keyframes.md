# Storyboard composition, action timing and continuity frames

Apply [action physics and timing](../../../global/skills/director-pack-skills/references/action-physics-and-timing.md) for phase timing, support/contact and panel roles. A panel is a selected instant; preserving its composition does not hold its transient pose for the shot.

Read when authoring video prompts from storyboards, repairing frozen action or resolving storyboard/keyframe confusion. These are role distinctions, not a new schema or provider guarantee.

## Preserve the requested board fidelity

When the user wants the video to reproduce the board, retain the storyboard as an attached composition reference. Disabling it loses visual framing/staging authority and is not a default repair for pose copying. Do not silently change the user's reference policy. If an input mode or reference budget cannot support the needed board, explain the constraint and prepare a supported alternative; do not claim text alone reproduces its exact composition.

Map every authored shot to its actual panel, using the inspected image's order. New boards follow the selected Director contract's layout; an existing board's left/center/right or top/middle/bottom order must be verified rather than guessed. Declare the board's stable picture label in subject definitions and retention analysis, then bind each shot to its panel. Render that panel's composition as one full-screen shot; the sheet, dividers and neighboring panels are not video content.

The board guides viewpoint, framing, character placement, screen direction and environment. A pictured pose may be an entry, representative intermediate key or exit only when that role agrees with the authored physical state. Do not automatically treat every panel as a first frame, last frame or full-shot pose hold. A later pose is usable only when the preceding action is explicit. Correct or regenerate a board that contradicts required location, identity, contact, ownership, damage or action phase; vague role language cannot waive a pixel mismatch.

## Animate the state change

Write distinct physical entry and exit states, with the causal movement between them. For a moving beat, use only the phases belonging to the authored interval: lead into an intermediate board pose and continue out of it, or continue directly from an opening pose already in motion. Do not replay completed anticipation or spread a brief flight/contact over the full shot. A locked camera does not freeze a body. Avoid repeating the same still pose as start, action and outcome. Do not add unnecessary motion to an intentionally stationary object or acting hold.

Example: the offered cloth begins in one person's hand; the recipient grips its near edge; the giver releases it; the recipient lowers it onto the stated support. The handover panel guides the framing and intermediate contact, not a permanent shared grip.

Reference-sheet instructions such as neutral background, multiple views, inactive sample state or “show front and side” belong to asset generation, not the target scene. Rewrite video subject definitions to retain the needed identity/design without copying sheet staging. Preserve the actual location from frame one. Match retention vocabulary and reference labels to the selected H3 guide rather than inventing enum tokens.

## Honor the requested animation style

When the user requests drawn or stepped animation, specify distinct key poses, anticipation, sharp breakdowns, short rhythmic cel holds and follow-through. Animation on twos can be requested as a style target; do not claim a prompt enforces an exact exposure sheet. Prefer stable drawn layouts and graphic shading when requested. Remove conflicting smooth-interpolation, live-action lens, optical depth-of-field and drifting-camera directions from that repair. A short cel hold is intentional timing; a whole unresolved action held in one pose is a failure. Do not impose limited animation, locked cameras or on-twos timing on unrelated styles.

## Keep continuity frames separate

A storyboard is shot planning; a canonical sheet is identity/design; a previous selected active take's final frame is physical-state continuity. A literal first/end-frame constraint is another role. Only name a role that the actual input mode and runtime support.

For same-scene state matching across a camera cut, retain compatible predecessor/state-reference settings without automatically forcing the predecessor's image as the new shot's exact first frame. Use direct first-frame continuation only when authored and supported. HARD_CUT location/time changes normally use CUT and no predecessor image; do not drag the previous setting into the new location to force continuity. Do not convert a genuine continuous cross-scene boundary to CUT merely because its scene ID changes. Preserve physical-state prose alongside explicit importer mode fields and compatible editorial boundaries.

Resolve the prior frame from the selected active take, not the newest unselected retry, a shared overwritten filename or a board panel. An enabled checkbox, null path or prose reference does not prove that bytes reached the model. Verify routing before claiming successful continuity.

## Repair and verify

Synchronize segment records, scene/production/index copies, per-segment and aggregate prompts, shot-plan text, board specs/prompts, attachment defaults and continuity controls. Reopen the delivered archive and check actual image paths, stable labels, panel mapping, provider reference limits and effective modes. Preserve exact dialogue and allocated windows unless a separately authorized repair changes them.

Keep evidence layers separate: local text and attachment checks, board pixel fidelity, importer/frame routing, and generated-take motion/audio. Diagnose pose copying from observed samples without asserting an uninspected runtime cause. Text changes and a passing ZIP check do not establish a corrected generated clip. This reference grants no permission for video generation or publication.


## Lessons from exact-take repairs

A latent preview can disagree with the finished clip opening. Inspect both and identify their source/version before diagnosing identity or shot-order errors. When an authored camera cut is contaminated by a predecessor portrait, inspect effective prior-AV-latent routing; disabling that reference may be appropriate for that boundary, while preserving physical-state continuity in prose. This is not a blanket rule to turn all continuity off.

For loading-only segments, remove launch instructions from retention text as well as shot prose. Define support until coupling, mounted zero-RPM exit state and an inserted rack that stays still. Generic phrases such as “right pulls” or “after release” can conflict with preparation even if the shot says not to launch. Prop definitions must describe geometry/materials, not facial features or wardrobe. Keep dialogue speakers' faces in the authored crop.

Serialize handovers: recipient grips, giver releases, then the freed hand performs the next action. Track the one object, owner, anatomical support hand and screen orientation across cuts. Do not narrate a second handover inside a later insert after it already completed.

A mismatched action-phase board remains unresolved until replaced or confirmed excluded by effective runtime routing. Marking it stale or writing “ignore this board” is not proof of exclusion. If generation is prohibited, save the text repair and report that remaining reference limitation without generating a replacement.


For portrait duplication, distinguish visible occupants from offscreen eyeline targets in shot prose and occupancy fields. A character looking toward someone does not authorize rendering that person or a duplicate at the frame edge. Anchor the first speaking face at time zero when repairing a wrong-person lead-in; retain full-face framing through the dialogue window, including any authored rise. Keep observed failures separate from inferred carryover causes.


When an offscreen continuity prop repeatedly materializes as a malformed object in a portrait, keep its state in authoring notes and make the generation shot's visible-prop inventory explicit. Use crop boundaries that exclude equipment through the full movement. Do not repeat detailed unbound prop descriptions merely to say they are offscreen; this is an observed-case mitigation, not a guaranteed model behavior. Recheck the latest take rather than declaring the prior prompt repair successful.

## Attachment and state repair checks

Attach only identities/props visible in the authored shot or otherwise required by a justified reference role. A named person in dialogue does not become visible. Keep concealed or offscreen objects in the state ledger without forcing an exposed visual instance. Removing an unused asset also removes its Subject/retention/shot uses; re-resolve actual attachment labels and preserve required voice samples.

Budget canonical images, requested board and selected predecessor frame together against the actual provider limit. An enabled board, readable image or reduced asset count does not prove inclusion in the exact request; omission warnings can be historical. Report payload inclusion unknown when it cannot be inspected.

Check every independent object's support and motion through the action. A detached prop must not inherit another prop's movement. When a repair changes visible entry state, recheck the retained board as well as the prompt; a contradictory board is not cured by saying composition-only.

Keep normalized planning fields separate from final H3 syntax. RunTech planning schemas reject attachment labels/final wrapper sections; the runtime H3 packager resolves them. Inspect any supported packaged-H3 adapter before using a similarly named field. Preserve exact dialogue and selected Director contract.
