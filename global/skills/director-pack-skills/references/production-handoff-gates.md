# Direction, dialogue and production handoff gates

Apply to v9, v10 and v11; preserve each package's selected contract. These checks supplement H3 form validation, which cannot establish story, speaker or runtime correctness.

## Direct the shot before writing the prompt

Author each shot's dramatic purpose, visible people (including partial bodies), eyelines, anatomical hands, prop owners/counts, support/contact, motion phase, opening state and resulting ending state. Establish location geography and lighting once, then carry them through motivated camera changes. A different crop does not move people or props in world space. A stopped, pocketed, wrapped or off-camera object retains its state until an authored event changes it.

Use a camera that reveals the causal detail needed by the beat. Do not solve a wrong hand, hidden coupling or unreadable action by asserting it in prose. If the shot needs revision, revise the authoritative direction first with a reason independent of a failed render. Synchronize framing, action, physical-state ledger, prompt, board spec and panel instant. Do not keep stale physics ledgers or blanket camera instructions beside repaired actions.

## Author each inter-segment boundary

For every boundary record predecessor ID, predecessor ending state, next opening state, intended incoming/outgoing mode and the reason for a match or reset. State descriptions must identify actual object ownership, support/motion and location; do not fill every record with generic “preserve continuity” prose or copy a whole action as both start and end state.

Read [runtech-continuity-import.md](runtech-continuity-import.md) for field precedence. A new segment is not automatically a hard cut. Continuous action/reaction can use MATCH_CONTINUITY and MATCH_CUT while changing camera. Deliberate location/time/title breaks use CUT/HARD_CUT. Do not blanket-convert a film to either mode or target a fixed number of matches.

Align explicit continuity_in/out enums, continuityMode, editorial boundaries, predecessor links, previous-frame reference and first-frame policy. Keep physical-state prose separate. Carry links across scene IDs when the action remains continuous. A previous final frame informs world state; it is not a mandatory first frame unless direct continuation is authored. Resolve the preceding selected active take at generation time; never invent a frame path. Include this image in provider attachment budgets.

Reopen the actual ZIP and run current importer normalization AND final-edit boundary mapping. Compare effective modes, links and reference flags with the authored boundary ledger for every segment. HARD_CUT can erase a declared match. When the runtime is unavailable, report static checks only. A live import requires saved-state readback; local parser success is not deployed success.

## Dialogue occupancy, owner and saved voice

Build a line ledger from the approved script: exact text, character, visible/off-camera status, start/end window, occupied shots and voice authority. Use measured reference utterance duration where available; otherwise mark estimated delivery and budget pauses and final-word clearance. Do not squeeze an impossible line into a fixed window merely by instructing faster delivery. Preserve approved dialogue/durations during repairs unless a change is authorized; report a genuine conflict instead of silently truncating.

Keep story speaker, Subject identity, runtime Picture attachment and Audio reference as separate mappings. Assign clip-local speaker order from first vocal occurrence, including remote/off-camera lines, according to the current H3 guide. Use the user's selected voice authority; when saved character samples are selected, do not introduce competing invented timbres. Define only the mapped visible speaker's articulation in each occupied window. Listeners stay naturally silent; an off-camera voice does not borrow a visible mouth. Speech crossing a cut keeps the same owner and is emitted once, not restarted per shot.

Validate the final runtime-resolved prompt, not only its authored version. Saved-prompt enrichment can inject new Subject numbers that conflict with old definitions. Rebuild mappings from source entities and actual attachment order; check all injected annotations, retention descriptions and dialogue windows. Do not guess Audio order from the asset-library listing. A silent test fixture can test resolver labels only; it must never be shipped or described as a real voice sample.

For generated-take acceptance, listen against the selected saved sample and inspect mouth movement across the entire line and handoff when required by the current review scope. ASR establishes approximate words/times, not speaker identity or timbre. Separate authored timing, resolver validation and rendered timing acceptance. Never inherit an old episode's audio waiver into a new request that explicitly requires voice/timbre checks.

## Asset and pixel authority

Bind a new asset in every consuming segment, canonical-reference list, required-assets list, runtime label, manifest and prompt bundle; copying its file into a ZIP does not bind it. Pose references establish pose only. Generated pose sheets are not canonical prop replacements unless explicitly approved for that purpose. Do not let a reference sheet's layout become the opening composition or multiply alternative state views into simultaneous objects.

For mechanical props, inspect hand ownership, device orientation, ports/channel, attachment, object count and action phase separately. Anatomical left/right comes from connected arms, not screen coordinates. Device-space axes are distinct from projected screen axes. An obscured required detail is unknown. Recheck every panel after a retry; fixing one defect may introduce another. User correction revokes affected prior acceptance and its packaged copies.

## Package and report the actual state

Deliver a Director ZIP with exactly one root containing the valid importer manifest and its referenced plans/specs. Keep asset-only and storyboard-only archives clearly distinguished; storyboard-only root filenames follow their own importer contract. Synchronize authoritative segments, scene plans, legacy/production copies, prompt bundles/aggregates, physics ledgers and storyboard specs. Clean the build output or derive it from an explicit file list so superseded images cannot survive a copy-over rebuild.

Each accepted image needs evidence tied to its exact bytes and current direction/assets. Rejected or unknown boards stay out of final production image folders and archives. Do not call a package complete when a required board remains a text spec or pose study; a requested interim ZIP must prominently identify that gap. Do not inherit old PASS reports into changed output. Report text checks, importer checks, static pixel checks and rendered motion/audio checks separately. Importer compatibility never proves cinematic continuity or performance.


## Repair closure and attachment demand

Derive visible references from the authored shots. Keep offscreen or concealed state in the ledger; a dialogue mention does not require a visual attachment. Remove an unused asset from required/visible lists, definitions, retention and every shot use together, then resolve actual runtime labels. Preserve required voice inputs independently. Budget canonical images, requested board and selected predecessor frame together against the real provider limit. A reference flag or readable file does not prove payload inclusion; accumulated warnings do not identify a past job's exact inputs.

Check support and motion for each independent object throughout transfers. Moving one object must not move an unattached neighbor. Preserve concealed contents until an authored reveal. A state repair invalidates any retained board depicting a conflicting state; composition-only wording cannot waive that mismatch.

Keep one latest project repair entry per segment with superseded records linked as history. Record source, persistence, payload, board pixels, motion, dialogue words/timing, audible timbre and lip-sync separately. Saved instructions are not a corrected render. Skill-only changes update and validate text/routes without changing movie records or generating media.
