# Scene direction pass

Run this before writing any micro-shot. It is the step that makes a segment play like a directed scene instead of a sequence of generated stills. The v9 contract still owns the schema, occupancy and dialogue rules; this pass decides what goes into `framing`, `composition`, `action`, `camera` and `sound`. Use [genre camera language](genre-camera-language.md) and the project's direction profile for the coverage style, and [action physics and timing](action-physics-and-timing.md) for physical events.

## 1. Read the scene as drama

Write these in the segment's authoring notes, not in the prompt:

- **Turn:** what is different at the end of the scene compared with the start (a decision, a hurt, a revealed fact, a won or lost exchange).
- **Whose scene:** the character whose experience the camera favors. Coverage leans toward their eyeline, and their reactions get the close shots.
- **Beats:** split the scene into 2–5 beats. A beat changes when a tactic, emotion or physical objective changes. Each beat needs a visible trigger: something seen, heard or touched.
- **Subtext:** what each character wants but does not say. Express it only through behavior, never by restating a line.

## 2. Block the space

Fix positions before choosing shots: who stands or sits where, the props between them, the doorway and the light source. Draw the action line (the 180-degree axis) between the main characters and keep the camera on one side of it unless a shot visibly crosses it. Note entrances, exits and every prop handover. Blocking is what produces motion inside a frame; a scene where nobody moves through space needs camera choices to carry it.

## 3. Plan coverage from the genre

Choose the scene's camera grammar once, from the genre profile, then assign shots to beats:

- **Establish** geography when it is new or has changed: a wide or medium-wide shot showing everyone who matters.
- **Dialogue** is covered by default as shot / reverse-shot: one line per speaking shot, framed from the listener's side of the axis. Matching sizes on both sides keep the exchange balanced; going tighter on one side shifts power to that character.
- **Reactions** belong to the listener. Cut to the person a line lands on when their response matters more than the speaker's delivery. A reaction shot is a silent shot under v9 Mandate 3; give it a specific visible response.
- **Inserts** show a detail the character notices (a phone screen, a cracked washer). They need an eyeline that motivates them.
- **Sound bridges:** use the official `<scenetrans>` form when a line or sound should continue across a cut (an L-cut or J-cut). Do not split a line just to put it on two shots.

Use a two-shot for an exchange only when the physical relationship between the two people is the point (a hand on a shoulder, a plate set down between them). Never put three lines in one static two-shot.

## 4. Give each cut a reason

A cut must add a new size and angle, a new subject, a reaction, a detail, or a change in time or place. If only the distance changes slightly, move the camera inside the shot instead. Consecutive shots must not share the same framing description with only a modifier changed ("medium two-shot" → "slightly lower medium two-shot" is a jump cut). Cut on an action or a look when you can: a hand finishes setting down the plate, a head turns, eyes move to an object.

## 5. Choose the camera with a motive

There is no default camera. For each shot write one of:

- **Static, with a reason:** "Static shot at Kaiden's seated eye level; the stillness lets Eema's entrance read." Static shots are good when blocking, performance or a reveal inside the frame carries the shot.
- **One move, with a trigger and a landing:** type, amplitude and speed in the official form, plus what starts it and where it ends. "As Eema's hand leaves the plate, the camera trucks right with small amplitude at slow speed until both faces share the frame."

Vary the grammar across a scene. A run of slow push-ins on faces is the most recognisable AI-video tell. Use height and angle for meaning: a slightly high angle from a standing character down to a seated one, a low angle for a challenger, eye level for equals.

## 6. Write the performance, not the outcome

Write a shot's `action` as 2–4 timed physical beats that fill its duration at natural speed:

- what the body does first (the trigger response), the main action, and how it finishes or settles;
- eyes and hands: where the character looks, what the hands do with props;
- one behavior that carries the subtext (he keeps rolling the top instead of looking up).

"Eema sets breakfast beside the cup" for a 6-second shot leaves 5 seconds for the model to fill with idle drift. Compare: "Eema crosses from the doorway with the plate, sets it down beside the steel cup with a small clack and lets her hand rest on the plate edge. Her eyes go from the toppled top to Kaiden."

Vocal delivery goes in the dialogue item's optional `delivery` field ("dry and unhurried", "quick and defensive, without looking up"). It describes how the line sounds, never what it means.

## 7. Time the shots from the performance

Read each line aloud and time it; leave room for the visible reaction before or after. Typical dialogue shots run 2–5 seconds, reaction shots 1.5–3 seconds, inserts 1–2 seconds; action follows the event's real duration. Match the cut points to the line windows so each line sits inside one shot where possible. Re-check v9 Mandate 8 occupancy after every retiming.

## 8. Compile and lint

Compile with `global/scripts/h3_compile.py` against the project's `h3/h3-locks.json`, then run `global/scripts/h3_lint.py` on the bundle. FAIL results block handoff. A WARN needs a one-line reason in the segment's authoring notes (for example, a deliberate static two-shot for a confrontation). Project invariants (wardrobe, no-glow rules, physics states) belong in the locks file, which states each one once; do not paste them into shot fields.

## Shot record checklist

For every micro-shot:

| Field | Contains |
|---|---|
| `framing` | Shot size plus angle or viewpoint: "medium close-up of Kaiden from Eema's standing eyeline". |
| `composition` | Who is where in frame, foreground/background, screen direction. |
| `action` | 2–4 timed physical beats, eyes and hands included. No speech acts (v9 Mandate 0). |
| `camera` | Static with a reason, or one move with trigger and landing. |
| `sound` | Physical sounds synchronized to this shot's events. |
| `objectStates` | Optional map such as `{"@beyblade": "stationary"}`, used by the compiler to place state locks once. |
| dialogue `delivery` | Optional vocal manner for the line. |
