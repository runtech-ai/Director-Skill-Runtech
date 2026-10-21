# Action physics, timing and storyboard roles

Use for moving subjects, object interactions, action timing and frozen-pose repairs. These are Director authoring and review rules, not H3 physics guarantees. Preserve the importer schema, authored events, exact dialogue and intentional stillness. Project canon may explicitly authorize stylized or supernatural mechanics; describe their causes and limits instead of silently replacing them with real-world physics.

## Speech and motion are independent

No dialogue means no authorized words; it does not mean no movement. Continue the authored action through silent shots and after speech ends. A physical hold needs an authored reason and duration, such as aiming, listening or settling after contact. Do not substitute a generic pose when removing a speech paraphrase: retain the existing visible action, or flag missing direction for the Director. A locked camera constrains the camera, not the subjects.

## Time the event before filling the shot

Allocate preparation, active movement, contact and consequence from the depicted action, distance and material response. Use normal physical speed unless the source requests slow motion, a speed ramp or another deliberate timing treatment. A segment's duration is not the duration of every action inside it. Do not stretch a reach, release, fall or projectile flight to occupy a long shot or speech window. Let completed movement lead into its authored consequence, or use a motivated cut. Do not invent filler activity, pad with a freeze or accelerate dialogue to meet a quota.

Record useful phase windows or completion landmarks in the existing action/state/timing fields or authoring notes. Keep them consistent with shot cuts and speech occupancy. These are direction targets, not frame-exact guarantees. If the action cannot fit the locked timeline naturally, flag the conflict; repartition only within the authorized repair scope and synchronize all timing copies. Short events can occur within a longer supported generation request. Do not assume the service permits a generation as short as the event.

Keep subject speed, camera speed, animation pose exposure and playback rate separate. Fast stepped animation uses larger pose-to-pose displacement during travel, not longer holds on airborne poses. Frame-rate conversion must preserve elapsed time unless retiming is expressly requested. Verify timestamps and duration before blaming prompts for slow playback; a container FPS value or still frame does not establish motion speed.

## Track the cause of every physical transition

For each action-critical object, author only the relevant phases:

`supported entry -> applied action -> release or transfer -> travel -> contact -> consequence/exit`

Track identity/count, owner or support, contact, orientation and direction. State the event that changes support or motion: grip closes, hand releases, foot plants, tip strikes, latch opens. A handover completes receiving contact before the giver releases. Detached objects move independently of their former support. Airborne travel proceeds to the authored contact or frame exit; it does not stop at a pictured pose. Contact produces the material-appropriate result specified by the source. Do not force every action to include release or impact, replay completed phases across cuts, or make an intentionally stationary object move.

Give body movement readable weight transfer and follow-through where relevant. Choose framing that reveals the governing interaction. Avoid conflicting directions such as simultaneous firm grip and free flight. A change in direction or speed needs its authored cause; explicit stylization is allowed, unexplained hovering or teleporting is not.

## A storyboard panel is a selected instant

Declare whether each panel depicts the shot's entry, an intermediate action moment, or its exit. Store this in existing beat description/continuity and shot-state prose; do not invent required importer fields or H3 enum tokens. An intermediate instant needs its preceding and following action described within the shot. If the shot opens during motion, continue from that phase instead of replaying anticipation.

Preserve the board's intended viewpoint, framing, geography, identity and screen direction while subjects move through the pictured pose. Transient limb positions and projectile locations are not full-shot invariants. A spear in midair can be a valid intermediate still; require a continuing trajectory and outcome in the motion plan. A still cannot prove speed, flight duration or acceleration. Preserve project-required visual cues, but do not universally demand blur or add it to a deliberately sharp animation style.

For Ref2VA, define the board as shot-planning guidance and map all relevant shots. Choose the official retention relationship within that defined role: `fully_preserved` can preserve the defined composition role without freezing the pose. Do not automatically weaken all references. Identify canonical design references, board guidance, predecessor state and literal keyframes separately. The actual runtime input route must agree: never pass a composite board as a literal first/end frame merely because it is attached. Keep requested board references enabled; repair contradictory pixels or routing rather than relying on an instruction to ignore them. Literal endpoint modes must describe a feasible path and arrival time consistent with the supplied endpoint.

## Compile and review the same action

Check that the final resolved H3 request preserves phase order, speed intent, completion state and reference roles from the Director. Check actual attachment slots and endpoint/predecessor routing when available; report unknown when unavailable. The H3 form-validation pass returns semantic conflicts to the Director rather than silently restyling approved direction. Apply project-specific cameras, segment limits and cadence only to that project.

Reject an action plan that turns silence into stillness, holds a transient flight pose for the shot, changes support without an event, or leaves a required action unfinished to fill time. Preserve legitimate aiming, rests, listening and deliberate slow motion. Review text, board pixels, runtime inputs and rendered motion as separate evidence layers. When footage is available and review is authorized, inspect full-speed playback and consecutive frames around release/contact; assess event duration, support, trajectory and follow-through. A passing schema or attractive board is not a motion pass. Skill maintenance authorizes no image/video generation or edits to existing movies.

## Example: intermediate spear-flight panel

The thrower plants the front foot, drives the arm and releases once. The spear separates from the hand and travels rapidly along its authored path to the target; the arm follows through. Contact produces the specified embedding, deflection or fall, followed by the corresponding recovery. The board captures an intermediate flight instant and retains its viewpoint and spatial arrangement while the action passes through it. Choose one source-consistent outcome, not a list of alternatives, in the final shot prose.

## Source and scope

The reference-role and continuous-path distinctions follow MiniMax's [Ref2VA guide](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/skills/h3-prompt-writing/references/ref-en.txt) and [base/keyframe guide](https://github.com/MiniMax-AI/MiniMax-H3/blob/main/skills/h3-prompt-writing/references/base-en.txt), reviewed 2026-10-21. The phase budgets and acceptance criteria above are production direction decisions, not official numerical model limits or evidence that a generated take is repaired.
