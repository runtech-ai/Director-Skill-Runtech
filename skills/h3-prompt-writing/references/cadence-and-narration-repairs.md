# Cadence, narration and series prompt repairs

Read for stepped-motion drift, visible lip sync during narration, or a prompt-only series repair. These are authoring and diagnostic lessons; they do not establish a provider guarantee or permission to regenerate video.

## Keep the requested H3 structure

Use the selected official mode guide. Ref2VA uses `retention_analysis`, not `retention_details` or `retention_dedails`. When the user requests style-free shot prose, put rendering, lighting and exposure cadence under the style Subject in `retention_analysis`; keep storyboard-reference entries about staging, viewpoint and ordered action composition. `detailed_description` then carries physical actions, timing, eyelines and exact speech. This is a user-selected organization, not a change to the official guide for unrelated tasks. Do not rewrite the bundled official specification to encode a project preference.

## Stepped motion fading after early segments

Treat the user's report as evidence of the symptom, not proof that a prompt was dropped. Compare a working and failing exact active take, their persisted authored prompts, and the actual generation request/settings when exposed. A current saved prompt is not necessarily the prompt that produced an older take. If both contain the same cadence rule, report that fact; do not claim missing instructions, a preset change or an identified renderer bug without evidence.

Preserve working prompts and takes unless a shared defect justifies changing them. For the failing scope, express one coherent cadence for the complete segment, every shot after a cut, and every visible motion layer. If on threes at 24 fps is requested, distinguish three-frame pose exposure from physical speed: a 0.75-second gesture uses six poses, with wider spacing for fast travel. Longer holds belong to authored anticipation or settled reactions; do not say that *only* settled poses may be held, which conflicts with exposing every pose for three frames.

Explicitly address camera/parallax as well as bodies, hands, faces, cloth and environmental motion. Preserve an authored tracking path but describe discrete camera-position updates if stepped camera movement is intended. A continuous camera glide beneath held character poses can still look smooth. This is a plausible conflict to repair, not proof of the observed cause. A still storyboard or predecessor frame supplies pose/state, not temporal cadence. Do not disable continuity or change the storyboard merely to enforce a style.

Check new rendered motion across the full clip and cuts before calling the repair successful. Sparse screenshots cannot establish cadence. Decoded-frame differences can support review, but compression and camera motion confound exact duplicate-frame counts. Do not promise frame-exact exposure from text alone. Generation, retiming or optical-flow processing requires its own authorization.

## Voiceover does not make the visible character speak

Use authored delivery metadata to distinguish VO from actual on-screen dialogue; do not infer it from the speaker's name. Keep the original voice identity, Subject/Speaker IDs, words and windows. Describe VO as a separately heard internal or recorded narration layer, with the visible character silent: no syllable-shaped lips, speech-timed jaw movement or talking gestures. Other pictured characters do not mouth or answer that narration.

Keep the narrator's character visible wherever the board requires. Name a physical mouth action in the generated prompt only when that action is actually authored; it follows the action rather than the voiceover rhythm. Do not copy a generic cough/sip exception into every silent shot. Use relaxed closed-mouth VO direction when no mouth action is authored. Do not demand an absolutely closed mouth while requiring those actions. Apply the rule across cuts and only over the relevant VO intervals in mixed-delivery segments. Preserve lip sync for real ON dialogue. Runtime `speaking` occupancy alone is not proof of intended visible delivery: check source VO/ON records and final audio/shot attribution together.

## Batch repair without semantic drift

Preserve original actions, durations, dialogue and images unless the user authorizes changing them. Synchronize all serialized prompt copies, update derived hashes and distinguish current validation from inherited historical reports. A prompt-only repair can leave a contradictory board unresolved; disclose it rather than inventing an action to fit it. Verify attachment toggles and actual image bytes/labels separately. A sole-board local test does not prove the live slot when canonical and continuity images are added.

When using scripts to expand action direction, review the resulting semantics. Keyword matches can misread “drops his gaze” as a fall, “gives a smile” as a handover, “passes the table” as an object transfer, or “without dropping” as a release. Preserve negation, agency and existing support; arrival-only shots must not replay the launch. Separate completed local packages, successful live writes, verified read-back and rendered results. Report partial live updates by episode and segment; never summarize them as an all-episode live repair.

## Latent context and exact-exposure delivery

Read [production repair lessons](../../../global/skills/director-pack-skills/references/production-repair-lessons.md) for MATCH handoffs, prior audio tails and current-state prop references. A timbre-only Audio reference instruction does not govern previous AV latent audio. An exported stepped MP4 does not regenerate that latent. Retain native context pairing and verify the actual continuation request before attributing the failure.

For a user-authorized 20 fps/on-twos finish, [finish_performance.py](../scripts/finish_performance.py) selects existing poses at 10 Hz and duplicates them to 20 Hz without time-stretching. It refuses overwrites, frozen padding and incomplete exposure durations; audio replacement requires actual supplied recordings. [verify_stepped_cadence.py](../scripts/verify_stepped_cadence.py) checks decoded frame-pair equality, uniform timestamps and optional expected duration. Both require FFmpeg (PATH or imageio-ffmpeg). Example:

```sh
python3 finish_performance.py --video /absolute/input.mp4 --output /absolute/new-output.mp4 --cadence-only --duration 10
python3 verify_stepped_cadence.py /absolute/new-output.mp4 --duration 10
```

This is a separate external finish, not a RunTech runtime hook. Apply and verify it for both CUT and MATCH clips, after any motion processing, and recheck the final edit/export. A smooth 20 fps transcode must fail the held-pair test. Lossy re-encoding may invalidate exact pixel equality; investigate the final output rather than claiming a pass from container FPS. A frozen clip may pass cadence but fail performance. No interpolation, speed change or whole-clip freeze is an acceptable substitute for authored action. The tools cannot repair lip sync, topology, prop continuity, camera drift, repeated speech or missing action phases.
