# Character micro-expression direction

Craft source: [Astorie emotion and acting guide](https://astorie.ai/blog/minimax-h3-emotion-acting-guide), updated 2026-10-08; incorporated at the user's request on 2026-10-10. This is third-party performance advice, not an official H3 syntax specification or a guarantee of model behavior.

## Performance beats

Direct an evolving performance rather than a constant emotion label. At a meaningful turn, choose a small number of visible cues: eye focus shifts, a momentary brow contraction, compressed lips, a fleeting jaw tension or a restrained chin movement. State the initial expression, the change and the resulting expression. Use restraint appropriate to the character and situation; crying is only one possible performance.

Describe voice independently through audible changes in pressure, volume, steadiness or breath. Anchor facial and vocal transitions to specific performance beats. Put exact words in the supported dialogue representation and acting instructions outside spoken text. Use ordinary prose for pauses and breathing; experimental tags such as `<pause>` and `<breath>` are not established syntax.

Preserve composition and the intended cast. Emotional context must not introduce another visible person or replace the background. Review facial performance and vocal performance separately; improvement in one does not establish success in the other.

## Director and timing integration

The selected Director contract and official H3 mode guide remain authoritative. Keep schemas, language markers, subject labels, exact source dialogue and occupancy unchanged. Never add repetitions, ellipses, rewritten words or extra dialogue blocks merely to imitate the article. Under v9 emit each line's `<d>` only in its first occupied shot. Identify performance beats by shot ID and time in direction.md rather than duplicating or paraphrasing speech in picture-only fields.

Keep visual action/start/end/continuity fields picture-only. Put audible breaths and vocal delivery in supported audio/delivery locations. In silent-shot windows preserve the required silence lock: visible breathing need not become audible. Mouth acting must remain compatible with speaking occupancy and lip sync; do not demand pressed-shut lips while words are being spoken.

For microdrama, use quick, consequential reactions within the existing shot time; do not stretch every beat into a pause or a close-up. Select framing and focus that can actually reveal the intended expression. Wide shots need readable posture or larger reactions rather than invisible eyelid detail. Carry gaze, facial tension and any tears through matching cuts and keyframes; reset only for a motivated story change. A storyboard depicts a representative expression, not proof of temporal acting or vocal quality.

Example visual beat: `Medium close-up, 2.0–3.0s: her gaze snaps toward the doorway; her jaw briefly tightens, then eases into a controlled half-smile.` Assign any accompanying voice change separately in the supported audio direction. No new dialogue is implied.

## Review

Check character motivation, visible cue clarity, emotional progression, dialogue timing, vocal intelligibility, stable identity/background and continuity. Validate prompt structure separately from generated picture and sound. Do not mark acting fidelity verified without reviewing the actual clip; skill-only edits generate no media.
