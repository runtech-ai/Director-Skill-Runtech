# V9 H3 authoring and generated-take lessons

Read before authoring or repairing v9 H3 prompts. These rules supplement the v9 hardening lock; keep exact dialogue, occupancy and official H3 syntax intact.

## Precise direction without repetition

- Define subject identity, reference mappings and unchanged retention once globally, as specified in `v9-hardening-lock.md`. Shots use those subject IDs and describe timing/cuts, framing, actual visible population, placement, eyelines, camera, action, relevant physical state and dialogue ownership. Repeat only action-critical details or a state change.
- Make staging concrete enough to draw: establish an axis, character/prop positions and fixed landmarks, then describe each camera crop. Do not paste the entire scene geography into every shot or force off-screen subjects into frame.
- Preserve canonical design, wardrobe, age/proportions and location geometry across cuts. Do not invent accessories, treatments or wardrobe changes; an intentional change requires source or user authorization and persists in subsequent states.
- Bind each required visual reference explicitly. A named prop or a text description is not proof of an attached image. Separate character/prop/location identity authority from state-reference authority: a damaged-object image can establish damage without overriding current weather, support, lighting or camera.

## Timing and continuity

- When video without storyboards is requested, make the compiled text and canonical references sufficient, disable optional storyboard conditioning, and do not make missing boards a delivery blocker. If boards are later requested, derive them from the same shot plan.
- Remove accidental entry freezes, repeated action and padded pauses. Holds need a dramatic or physical purpose. Meet a requested runtime through meaningful story/beat expansion within the authorized scope, rather than stretching shots or silently shortening the requested film.
- Set actual match-continuity fields for connected boundaries, not merely prose. Preserve temporal state while allowing the authored camera cut; continuity does not imply replaying or holding the predecessor frame.
- Review the selected predecessor before using it. Do not propagate incorrect design, wardrobe, placement, damage or physical state. Flag or repair it before continuing an authorized generation run.
- Track prop spin/motion, support/contact, ownership, damage and causal transitions per shot. Hidden objects retain their state but are not additional visible objects. Load project-specific physics and canon when applicable; do not put franchise rules in global instructions.

## Dialogue and sound

- Resolve every line to a defined character and stable speaker identity; verify Subject/Picture/Speaker/Audio mappings against actual attachments across the entire prompt. Remapping only definitions leaves stale shot references.
- Keep exact dialogue in structured records and emit official `<d>` once in its first occupied shot. Preserve line windows across cuts, off-screen status and silence rules. Visible listeners must not articulate another character's line; a hand insert must not invent a visible speaking face.
- Keep ambience and score separate. For connected segments, specify a continuing underscore with shared musical identity and timeline position; avoid restarting intros or fades at each segment. Prompt instructions alone do not guarantee sample-accurate joins: use a continuous master score in the final mix when seamless music is required.

## Verify the actual generation inputs and outputs

- After importing or changing prompts, read back the actual runtime compiled prompt, attachment mappings, continuity settings and exact active clip/take before generation. Package text, storyboard text and the prompt used by an existing take may differ. Do not present the current saved prompt as proven historical input unless the take record establishes that provenance.
- For RunTech, discover live tools, list organizations, explicitly select the intended organization, then resolve the movie and active scene/clip IDs. If listing succeeds but a read returns 404, verify/select that organization and retry the same known ID before declaring it unavailable. Persistent failures are blockers; never substitute unrelated IDs or old takes.
- Compare the exact completed take with its authored shot and dialogue timeline. Review cut boundaries, identity, age, wardrobe, staging, prop state, physics and added objects. Review audio alongside mouth motion for speaker ownership, exact words, omissions, repetitions and extra speech. Sparse stills or an open mouth do not prove lip-sync or voice identity; state any unavailable audio/video verification explicitly.
- Keep schema/import checks, runtime-input checks, rendered visual review and audio review as separate results. A locally valid ZIP does not establish correct generated media. Latent previews are not completed takes. Report the full evidenced defect set before an authorized retry.
- Updating skills or prompts changes future instructions, not existing pixels. Do not generate, replace takes or import a package merely because a skill update was requested.

## Storyboard review when requested

Use the authored shot plan and canonical assets for all panels. Check consistent age/proportions, wardrobe, geography, damage, weather, population and physical state across the full board set. Follow the user's selected image-generation workflow; do not switch to local compositing or image edits against an explicit image-generation-only preference. Keep rejected or unreviewed boards distinct from accepted deliverables.
