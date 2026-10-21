# Exact Director-to-board fidelity gate

This is a mandatory board acceptance gate for both Director package and storyboard workflows. Judge the actual rendered pixels against the current authoritative Director micro-shot and canonical assets. A plausible scene, attractive image, correct prompt or successful render is not a pass.

## Freeze the expected picture before rendering

For every panel, record the segment ID, source micro-shot ID, Director record revision/hash, selected instant or physical phase within that shot, canonical asset IDs/revisions and expected visible picture. Derive this from the Director, not from whatever the model produced.

Include the following applicable requirements:

- **Location:** exact named set and its canonical geometry, landmarks, openings, furniture, spatial arrangement, weather, lighting and time of day. A similar-looking room, street or arena is a substitution. Preserve the authored camera perspective and geography; a location reference is not permission to invent unseen layout.
- **Assets:** every required visible character, creature, prop and mechanism, with exact identity/design, count, scale, colors, wardrobe, anatomical handedness, owner, support/attachment, orientation and damage. An asset's attachment in the request does not prove that its pixels were preserved. No extras, hybrids, missing required assets or substitutions.
- **Beat:** exact photographed action/state, physical phase, pose, gaze, blocking, screen direction, foreground/background relationships, effect emitter and extent, framing, composition and continuity. No added launch, spin, glow, reaction, contact or event, and no replacement of the required beat with a generic pose.
- **Depicted motion state:** for a subject already moving at the selected instant, require the project-defined visible motion cues in the actual image, with support/contact and identity retained. A sharp stationary design-reference pose plus motion prose is not sufficient. Do not defer missing motion-state depiction to downstream video generation. Check each object's own state; do not add motion cues to an authored stationary object or replace a slower phase with a faster one.
- **Panel mapping:** exactly one panel per micro-shot, correct playback order, required inverse aspect and equal-height stack. Choose an instant within the authored shot that clearly represents its beat. A still cannot prove the entire motion chain; do not claim it does. If the required action cannot be represented readably under the existing plan, record that conflict rather than silently change the shot or invent extra panels.

If Director fields or canonical assets conflict, fail text preflight and repair the source through the applicable authority before rendering. Do not silently choose a substitute location/design or rewrite the Director to excuse a generated mismatch. Clarifying how to depict the same authored beat is permitted; changing its location, assets, action, camera or outcome requires source authority and a recorded revision.

## Inspect and record each panel

Inspect every actual panel at sufficient resolution, with targeted crops when a required detail is small. Keep media on disk and inspect in bounded batches under [media-lifecycle.md](media-lifecycle.md). Occluded, cropped, blurry or too-small required evidence is `unknown`, not an assumed pass. If the Director intentionally excludes a subject or detail from the frame, record that exclusion and its source; do not force it into the image.

For each applicable requirement, save a compact textual record containing:

`segment / panel / micro-shot -> Director field + expected picture -> observed pixels + evidence path/region -> pass, fail or unknown -> defect and repair`

Bind the review to the exact board file/hash and Director/asset revisions. Record location, assets and beat as separate results per panel. Use `not_applicable` only with a source-grounded reason; never use it to hide missing or unreadable required content. Metadata, earlier reviews, another panel or an earlier board version cannot supply missing pixel evidence.

When motion cues are required, record each object's expected motion/speed band, observed pixel cue and support/contact result. A depicted stationary state in an already-moving beat is a failure; unreadable required cues are unknown. These records verify the still's depiction, not continuous motion or measured physical speed.

**Acceptance requires every applicable fidelity requirement in every panel to pass.** A 95% score or average across panels cannot waive a location, asset or beat mismatch. Video soft timing/action thresholds remain video policy; they do not make board fidelity approximate. Audio/lip-sync/motion checks that a still cannot establish remain explicitly deferred to take review rather than falsely passed.

## No silent acceptance

Any failed or unknown required result means the board is not accepted. Record all defects, repair the owning prompt/spec/binding or an independently demonstrated source contradiction, regenerate fresh from verified canonical assets when generation is authorized, then rerun the whole board gate. Recheck previously correct panels because a replacement can introduce new defects. Preserve accepted boards unaffected by a revision.

No silent waiver, auto-pass after retries, unexplained “close enough,” copied prior pass, or removal of a requirement to fit the output. A waiver or changed requirement must come from explicit user/source authority and be recorded as a changed requirement or `waived_by_user`, never relabeled as an exact match. User-authorized non-speech audio waivers do not waive visual board fidelity.

Publish an accepted status or include a board in the final ZIP only when its exact file has a complete passing panel record for the current Director/asset revisions. Any relevant source or board change invalidates the affected acceptance until rechecked. When blocked or a run limit is reached, report the unresolved defects and next action; do not report the board or package as complete. A skill-only update performs instruction validation, not board generation or acceptance.
