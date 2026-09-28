# DIRECTION, CONTINUITY, PHYSICS, AND ASSET LOCK

Use this audit for every package. Apply the domain-specific physics section only when the story contains a mechanism, sport, vehicle, weapon, spinning top, or other rules-bound action.

## Direct states before shots

For each moving character and important object, write a compact state chain before composing camera prose:

```text
entry state -> initiating action -> transfer/release -> travel/contact -> exit state
```

Record who holds the object, which hand, where it is, its orientation, motion direction, contact point, and whether it is intact. A later shot or segment starts from the previous exit state. Do not reset an object merely because the camera cuts.

For every adjacent pair, require:

```text
segment[n].continuityOut == segment[n+1].continuityIn
```

Compare the actual meaning, not just matching prose. Preserve actor positions, eyelines, scene axis, screen direction, prop ownership, clothing, injuries, damage, weather, light, and time of day. Deliberately show any change on camera.

## Camera must explain the action

Choose the view that makes the governing motion readable:

- Use a side or three-quarter view for height, downward travel, lateral ejection, tipping, and whether an object is inside or outside a boundary.
- Use an overhead or high three-quarter view for circular paths, relative position, collision order, and arena occupancy.
- Use an insert for attachment, grip, latch, gear, trigger, ripcord, or handoff details.
- Keep screen direction stable across cuts unless the shot visibly crosses the axis or establishes a new one.

The storyboard shows the authored view. Do not use a more dramatic angle that hides or reverses the action being proved.

## Mechanical action and spinning-top physics

Do not direct a mechanism from visual association. Preserve its actual parts, sequence, and constraints.

For a launcher-driven spinning top:

1. Pre-launch: the top is locked to the launcher; it is not already on the ground or in the stadium. The short toothed ripcord is inserted through the launcher. It is a rigid strip, not a string.
2. Pull: one hand stabilizes the launcher while the other pulls the ripcord by its ring or handle. The internal gear imparts spin.
3. Release: the top detaches once and travels from the launcher toward the stadium. Do not show a duplicate top still attached or already spinning below.
4. Landing: the tip contacts the stadium first. The top spins about its tip, may precess or wobble as energy falls, and follows the stadium slope under friction and centripetal motion.
5. Collision: contact occurs at the rims or attack points. Deflection, rebound, wobble, and speed loss follow the impact direction. A knockout crosses the rim and finishes outside the stadium.
6. After the pull: the ripcord is removed and held or leaves frame. Do not leave a long cord stretched between the hand and launcher.

Do not eject a face bolt, chip, emblem, weight disk, or other physical part unless the scripted event is a real burst or break. A spirit, Bit Beast, aura, or essence emerges as energy from the intact spinning top; it is not a solid chip flying out.

Track each top separately by owner, design, color, spin state, path, and final location. Never duplicate or swap them between panels. If the stadium breaks, carry the same fractures and missing sections forward. If it remains intact, draw a complete rim on both sides.

When specialized knowledge is supplied, treat its factual mechanics as the action authority while keeping the screenplay and v9 contract authoritative for story, timing, and dialogue.

## Per-segment canonical asset closure

Build an asset ledger for every segment from the union of:

- every visible or speaking character;
- the location or set whose design is visible;
- every handled, launched, worn, ridden, damaged, or plot-relevant prop;
- every visible creature, vehicle, screen image, or mechanical device.

Every canonical ledger item must resolve through all applicable layers:

1. the scene import manifest `canonicalReferences`;
2. the segment JSON `canonicalReferences`;
3. the prompt bundle `canonical_references` with stable `imageIndex`, `assetId`, relative file path, `attach: true`, and the correct H3 role;
4. one H3 `subject_definitions` line mapping the handle to its `<Picture N>`;
5. `retention_analysis` when the referenced item appears in the generated image;
6. a real readable file at the declared package-relative path.

Mentioning `@asset` in action prose is not an attachment. A storyboard reference does not replace a canonical character, location, or prop reference. Do not give one picture index to two assets.

Prefer a clean movie-library or DSL asset when the runtime supplies one. An importer-locked package must still carry explicit attached canonical references for assets that may not exist in that library. When the actual importer/compiler is available, compile at least one prompt through the runtime resolver and inspect the resulting `subject_definitions`; checking JSON alone does not prove the runtime attached the asset. If the runtime drops an attached handle, report a resolver failure rather than claiming the package works.

## Storyboard continuity audit

For every panel, compare it to the owning micro-shot rather than to a loose scene summary:

- exactly the listed people are present; no crowd or extra bystander appears unless authored;
- each character keeps identity, wardrobe, handedness, pose intent, and gaze direction;
- every prop appears in the correct hand or physical location and at the correct phase of action;
- the location uses the declared canonical plate and stays spatially consistent;
- motion paths, impacts, launch direction, damage, debris, and inside/outside relationships agree with the state chain;
- the final panel state can become the next segment's first panel without an unexplained jump.

Review the rendered pixels, not only the prompt. If a required state is visually wrong, regenerate the board even when its prompt is correct. Do not repair one marked area by changing unaffected subjects or another panel.

## Dialogue source and lip synchronization

Keep the exact original authored words inside `<d>[Language] ...</d>`. Do not replace display dialogue with IPA. If a supported pronunciation field is needed, keep that guidance separate from the spoken text.

Classify every audible line as on-screen dialogue, off-screen dialogue, diegetic playback, or non-diegetic narration. Only the visible source that actually speaks may lip-sync. A television image, listener, crowd member, or silent character keeps lips closed during narration or off-screen speech. Do not make a visible screen lip-sync to the narrator merely because the screen is in frame.

## Audio continuity across generated clips

Within one continuous scene, carry a single music cue across segment boundaries: same cue identity, tempo, key, instrumentation, rhythmic phase, and intensity trajectory. Do not restart the track at each clip. Avoid boundary fades unless the edit explicitly calls for one. Record the incoming and outgoing music state so the next segment continues the tail.

Carry ambience and sustained mechanical sounds across cuts when the world remains continuous. One-shot effects occur at the visible event and do not repeat at the next segment boundary.

## Change classification

After the audit, label every segment:

- `PASS_NO_RESHOOT`: prompt, attachments, storyboard, physics, continuity, and audio state all agree.
- `PROMPT_ONLY`: pixels and directed state are correct; text or reference declarations need repair.
- `STORYBOARD_RESHOOT`: the direction is correct but rendered panels contradict population, identity, mechanics, camera, or continuity.
- `FULL_SEGMENT_REDIRECT`: timing, shot design, physical sequence, or boundary state is impossible or contradictory.

Return the `PASS_NO_RESHOOT` list separately so correct work is not regenerated.
