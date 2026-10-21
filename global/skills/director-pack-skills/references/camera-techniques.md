# Cinematic camera: plausible movement and deliberate framing

Read before authoring `camera`, `lensIntent`, `POV` or a compiled camera sentence. Apply [action physics and timing](action-physics-and-timing.md), then choose relevant guidance from [genre camera language](genre-camera-language.md). The user's current preference is physically plausible camera behavior in every medium, including anime. A genre label does not authorize impossible movement.

## Direct a viewpoint, not a list of effects

Decide what the audience must discover, whose experience shapes the shot, and when attention changes. A useful move may reveal space, preserve a composition during blocking, approach a decision, follow a pursuit or leave someone behind. If moving adds no intended information or feeling, keep the camera settled. A locked shot can contain vigorous action. Handheld can also be quiet and controlled; it is not prohibited in dialogue.

Plan one coherent camera trajectory per shot. A coordinated pan while tracking, or a tilt during a crane rise, can be one feasible operation. Do not stack unrelated moves to fill time. When viewpoints require incompatible positions, cut instead of inventing a flight between them. A cut is an edit, not a camera teleport inside an uninterrupted shot.

For a moving shot, resolve these in existing camera/composition/continuity fields or authoring notes:

- **Start and finish:** camera side, approximate height and distance, initial framing and final framing.
- **Support and path:** plausible tripod pivot, operator walk, dolly/slider route, crane arc, vehicle mount or aerial route; identify obstructions and clearance when relevant. The equipment need not appear in the picture.
- **Timing:** the visible/audible trigger, travel pace, and landing or cut. Use distances or angles only when they resolve ambiguity; they are intent, not calibrated H3 controls.
- **Optics and focus:** fixed lens versus zoom, intended depth, and focus target. Keep the focal length stable unless a lens change is authored.
- **Continuity:** subject blocking, axis, foreground occlusion and what remains visible throughout the path.

Compile these decisions into short natural sentences. MiniMax's base guide expresses camera type with amplitude and speed when needed. Rig names and measurements below are descriptive film language, not new API commands. See [research sources](cinematic-research-sources.md).

## Working movement library

Choose by dramatic purpose and available space. These examples are adaptable shot fragments, not complete prompts or mandatory shot durations.

| Technique | Plausible operation and useful constraint | Example direction |
|---|---|---|
| Locked-off | Fixed camera position, orientation and lens; acting changes the frame. | A waist-height static wide shot lets the worker cross to the door and leave frame. |
| Pan / tilt | Pivot from one position; pan changes azimuth, tilt changes elevation. | From the doorway, pan right as she turns toward the window, stopping with both in frame. |
| Follow pan | Rotate to follow travel rather than translating with it. | The sideline camera pans with the runner while the near fence remains at the camera's fixed position. |
| Dolly push / pull | Translate closer/farther on a clear route; perspective and parallax change. | Push forward along the open aisle from medium-wide to medium, then settle as he stops. |
| Truck / lateral track | Translate sideways while maintaining a deliberate camera side. | Track parallel to the walkers along the pavement; foreground posts pass faster than the far buildings. |
| Slider reveal | Short translation uncovers a subject behind a foreground edge. | Slide left just beyond the door jamb to reveal the waiting visitor, then stop. |
| Lead / follow tracking | Operator or platform travels ahead of/behind the subject, with plausible clearance. | Follow at walking pace down the unobstructed hall, remaining behind her right shoulder. |
| Steadicam / gimbal | Stabilized travel with a traversable route, finite turns and coherent height. | Walk the curve of the corridor at chest height; turn with the actor and settle outside the next doorway. |
| Handheld / shoulder | Human-supported movement, ranging from nearly still to energetic. | Shoulder-held medium shot with small, irregular weight corrections; reframe only as the seated subject leans. |
| POV / body-mounted | Identify the viewpoint owner and mount; head, chest and handheld motion differ. | A chest-mounted view turns with the torso as the wearer steps back from the threshold. |
| Arc / partial orbit | Curved route with a defined radius and unobstructed sector. | Arc from front three-quarter to side view around the near end of the table, staying outside its edge. |
| Full orbit | Only for a deliberate circling beat with room and adequate time; preserve geography. | Complete one measured circle in the open courtyard, holding distance and returning to the starting side. |
| Pedestal / boom | Change camera height; state whether the lens tilts to retain the subject. | Raise the camera from seated to standing eye level as she rises, without moving closer. |
| Jib / crane | Bounded boom arc; head orientation can compensate, but the camera needs clearance. | Rise over the low fence on the near side to reveal the crowd beyond; stop before the canopy. |
| Aerial / drone | Aerial viewpoint from the start, with plausible speed, altitude and obstacle clearance. | From above the clearing, retreat and climb gradually to reveal the surrounding forest. |
| Vehicle-mounted / parallel pursuit | Camera belongs to a moving platform; ground motion, distance and turns agree. | A side-mounted view tracks the adjacent vehicle at matched road speed through a gentle bend. |
| Overhead / top-down | A viewpoint, not inherently a movement; establish how it is held. | Fixed overhead view shows the hands sorting components; framing remains unchanged. |
| Optical zoom | Stationary viewpoint, changing field of view; no invented dolly parallax. | From the back of the room, zoom gradually to the speaker and hold the new framing. |
| Snap / crash zoom | Brief motivated optical reframe with a readable landing; no universal millisecond recipe. | After the unexpected movement, snap-zoom to the open latch and settle sharply on it. |
| Dolly zoom | Coordinated translation and opposite focal-length change; subject size approximately stable. | Pull back along a clear straight track while zooming in to retain the face's size as the background compresses. |
| Rack focus | Focus change, not camera travel; establish foreground/background depths. | With framing fixed, shift focus from the near envelope to the person in the far doorway. |
| Whip pan | Rapid pivot between established positions, with a brief blurred transit and definite landing. | On the impact sound, whip-pan across the room to the fallen shelf and settle. |
| Dutch angle / roll | A canted composition or deliberate rotation; avoid automatic spiraling. | Begin at a modest fixed cant for the disoriented viewpoint; keep that angle through the shot. |
| Snorricam | Camera attached to the performer, body relatively stable while environment moves. | The torso-mounted camera keeps the chest in place while the corridor moves with each step. |
| Macro / detail insert | Respect close focus, clearance and shallow depth; usually a separate setup. | Cut to a stable close-focus insert of the catch closing under the thumb. |

Split screen, match cut, dissolve, speed ramp and time-lapse are editorial/temporal treatments, not camera moves. Use only when authored and supported. A storyboard sheet must never turn into an accidental split screen. A tight eye insert does not authorize pushing the camera through a face. “Super dolly” and “yo-yo zoom” are not special H3 controls: translate any requested effect into a feasible path/lens operation or replace it with an authored edit.

## Lens, staging and lighting

Choose shot size and camera distance together. Wide/normal/long-lens language is often enough; numeric focal lengths need a stated format or equivalent basis if exact comparison matters. Perspective is governed by camera position. A long-lens close-up from farther away differs from a wide-lens close-up at arm's length. Do not ask a zoom alone to create lateral parallax.

Use depth to separate planes when the scene benefits. Do not demand both razor-thin depth of field and crisp simultaneous action at widely separated distances. A rack needs distinct focus targets. Specify focus holds through a critical hand/contact action; avoid gratuitous autofocus hunting. Match depth and shading to the requested animation medium rather than adding photographic bokeh automatically.

Give light a credible source, direction, hardness and stable relationship to the setting. Shadows/reflections change with subject and camera motion; they do not spin because the camera arcs. Exposure adaptations belong to an authored camera behavior, such as a consumer camera moving from a dark hall into daylight, not arbitrary flicker. Do not add fog, smoke, rain or flares merely to signal cinematic quality.

## Cuts and geography

Keep an axis and eyelines through coverage. If crossing the axis, show a readable crossing or establish the new geography before reverse coverage. Preserve action direction and match the physical phase across a cut, without replaying a completed impact. An objective close-up is not automatically a character POV; an eyeline target does not add that person to the frame.

Give a cut new information: a consequence, reaction, detail, viewpoint, location or authored time change. Avoid compulsory wide-medium-close ladders and arbitrary cuts on every spoken phrase. A moving shot can cut while still moving when deliberately matched; it need not settle at every boundary. Across generations, do not promise an invisible join from text alone.

## Camera plausibility review

Reject world geometry bending around the camera; passage through solid objects; an unexplained handheld-to-drone transformation; instantaneous height/distance changes inside a continuous shot; unsupported acceleration, radius changes or direction reversals; subject auto-centering that erases intended blocking; and zoom/focus breathing that was not authored. A named gimbal or crane does not make an impossible route feasible.

Correct the source path or simplify to a cut. Preserve useful energy and deliberate handheld character. Do not impose locked cameras globally to solve drift. Before acceptance, compare the planned start/path/end with actual footage when available; review parallax, horizon, occlusion and landing through the full shot. A still verifies only its selected instant. Record untested behavior rather than claiming cinematic realism from prompt validation.
