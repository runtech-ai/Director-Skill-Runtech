# V9 HARDENING LOCK — VISUAL DIRECTION + DIALOGUE TIME OCCUPANCY

Live Ref2VA takes invented extra spoken words, copied voice-sample dialogue, cloned bodies, restaged close-ups into two-shots, bound the storyboard to Shot 1 only, and — after those were locked — still garbled the voice when a long line was parked in one shot while overlapping shots were marked silent or told to “continue the same spoken line.” Those failures share one cause: **the Director wrote the meaning of the scene instead of the picture, or wrote speech timing that the shots contradict**.

A package that violates any mandate below MUST fail validation and MUST NOT be delivered. Downstream compilers may clean leftovers. They are not allowed to be the place the rule is invented. You must author the pack correctly.

## MANDATE 0 — Direct the picture, never the speech event

Every Director field that describes a shot (`action`, `purpose`, `startState`, `endState`, `continuity`, `composition`, `POV`, storyboard prose, `summary`, `compiled_prompt` shot body) may contain only what a camera can photograph or a microphone can hear as **non-verbal** sound:

- bodies, faces, eyes, hands, posture, props, room, light, weather
- who is in frame and where they sit/stand/look
- expression that does not require quoting or summarizing a line
- camera size, move, and cut

They may **not** contain:

- a speech act (`says`, `asks`, `answers`, `promises`, `offers`, `acknowledges`, `admits`, `explains`, `declares`, `tells`, `names`, `credits`, `makes clear that`)
- a report of what was said, will be said, or was just asked
- a moral or plot summary of a line (`making the commitment`, `confidential offer`, `hero around here`, `credit will go`, `she realizes he is not trying to take her place`)
- a silence that is defined by speech (`hold the silence after the question`, `before answering`, `leaving space for her response`, `held silence after … question`)
- a keep-talking instruction (`continues the same spoken line`, `continues speaking`, `keeps the promise going`)
- any distinctive word that belongs to a structured `<d>` line in this segment or an adjacent one (`responsibility`, `price`, `credit`, `promise`, `offer` when those words are in the screenplay)

If you need the audience to hear words, put those exact words in structured `dialogue` for that micro-shot and nowhere else.

If a shot has no structured dialogue, it is a visual hold. Direct the hold as a picture. Do not direct it as “the pause after the question” or “the beat before he answers.”

Test: if you deleted every `dialogue` array in the segment, would the remaining prose still tell a reader what was said? If yes, the package fails.

## MANDATE 1 — Spoken words exist in one place

Exact scripted dialogue exists once: structured `dialogue` / micro-shot dialogue.

It is emitted once, in the **first occupied shot** (Mandate 8), in official MiniMax form:

```text
<Subject 1> (S1), using the voice timbre referenced from <Audio 1>, says, <d>[English] Exact authored line.</d>. <Subject 1> closes their lips after the line.
```

Required parts: `<Subject N> (Sx)` + timbre cite when an `<Audio N>` is attached + exact words only inside `<d>[Language] …</d>` + speaker closes lips after the line **only when this shot is the last occupied shot and the line ends with the shot**. If later shots still overlap the line, do not close lips yet and do not emit a second `<d>`.

Never write `@sharon (S1) says` or `Sharon (S1) says`.

Never put those words in `summary`, `retention_analysis`, `overall_soundscape`, `non_diegetic_music`, `action`, `purpose`, `startState`, `endState`, `sound`, or storyboard prose.

If stripping a speech paraphrase leaves no action, write a short physical hold: `The subject remains in frame.` Do not replace it with another speech paraphrase.

Empty `dialogue` means no spoken words are authorized. Do not invent listener lines, replies, or “he does not speak” essays on a shot that already has a `<d>`. Absence of a second `<d>` is enough for listeners.

## MANDATE 2 — Voice-timbre is a reference, not a script

```text
<Audio 1> is the voice-timbre reference for <Subject 1> (S1).
<Audio 1>: reference - its vocal timbre guides the dialogue delivery of <Subject 1> without copying the original signal.
```

Do not copy, paraphrase, or reperform the sample file’s words. Do not put sample words into `<d>`. Cite `<Audio N>` only in the first occupied shot.

## MANDATE 3 — Silent shots in a talking segment

When the segment has any structured dialogue, every shot that does **not overlap that line’s start/end** (Mandate 8) must, in `compiled_prompt`, lock silence **immediately after the cut/composition sentence**, before any emotion prose:

```text
[Shot 2] At 00:04.330, the camera cuts to a TIGHT PORTRAIT composition. No spoken words occur in this shot. Visible characters keep their lips closed. Her expression turns exhausted.
```

Do not put that lock at the end of the shot. Do not write the lock on any shot that overlaps a line’s start/end (except `closes their lips after the line` on the last occupied shot after the line ends). Do not write the lock on a fully silent segment.

In Director JSON for that silent shot, write only visual hold / reaction. Do not mention questions, answers, offers, promises, credit, or “response.”

## MANDATE 4 — Occupancy follows the actual frame

`visibleAssets` lists bodies and objects **literally visible** in that micro-shot.

- Tight single (`MCU`, `medium close` on one person, `close-up`, `tight portrait`) → one human in the picture. Do not write two-person occupancy. Do not write `X remains nearby`.
- Two-shot, group, over-shoulder, `*-side eyeline` → those exact people, counted once: `Exactly two distinct human characters are visible: <Subject 1> (@sharon) and <Subject 2> (@terrance).`
- Eyeline / over-shoulder is already two bodies. Do not add a third wait, doorway figure, or second copy of a named person.

Never put occupancy in `subject_definitions`. Location plates do not define population. Narrative mention is not attachment.

Camera travel “between” two named people keeps those same two people in one frame. It does not cut them into two singles that H3 can populate as three bodies.

## MANDATE 5 — One-line subjects, class-first authority, all-shot storyboard

Each visual subject is one line. Multi-view stays on that line (`from <Picture 1> and <Picture 2>`). No second paragraph, no `one single character`, no `supplies authoritative`.

`canonicalReferences[].authority` names the class first: `character identity for Sharon`, `prop identity for the coffee`, `location identity for the ranch house`. Never bare `identity for the coffee`.

When storyboard is ON, list every mapped shot: `… storyboard reference for [Shot 1], [Shot 2], and [Shot 3]…`. Never `for Shot 1` only. Never `STORYBOARD EXECUTION LOCK`.

## Global retention and consistent references in H3 prompts

For v9 H3 authoring, define each subject-to-picture mapping once in `subject_definitions` and state unchanged identity, wardrobe, prop design, location identity, and reference retention once in the global `retention_analysis` section. Preserve the official H3 section order and retention vocabulary. Do not repeat these retention paragraphs or picture citations in every shot.

Shot prose contains the shot timing/cut, framing and visible occupancy, camera, physical action, relevant state changes, and the dialogue owner in the official form required by Mandates 1–3 and 8. Refer to the established `<Subject N>` identifiers. Repeat a specific retained detail only when a state transition or an action-critical constraint needs local emphasis; do not paste the full global retention block.

Use one consistent subject/picture/speaker mapping throughout each compiled segment prompt. A subject ID cannot identify both a character and a prop. Every dialogue owner must resolve to a defined character; every picture citation must agree with the global mapping and actual runtime attachments. If attachment order changes, remap all affected references throughout the prompt together, including shot prose, rather than updating only the definitions.

Before delivery, check the complete compiled prompt for conflicting or unresolved Subject/Picture/Speaker labels and duplicated per-shot retention boilerplate. Repair these in the Director authoring pass before H3 form validation. Concision must preserve exact dialogue, voice-timbre citations when attached, occupancy, timing, and action-critical continuity.

## MANDATE 6 — Audio layers stay in their bins

`sound` / `soundPlan` / `overall_soundscape`: physical and ambient only. No dialogue text. No score.

`non_diegetic_music`: audience-only score, or `N/A`.

Shot prose contains `<d>` or nothing spoken. Cup pour and room tone belong in `overall_soundscape`.

## MANDATE 7 — Summary is a visual gist

```text
[reference generation + audio reference] A 13-second three-shot sequence inside <Subject 4> in which <Subject 1> prepares coffee while Terrance waits.
```

No spoken content. No offer, promise, credit, question, answer, or “silence after.”

## MANDATE 8 — A line occupies every shot its time covers

`dialogue.start` / `dialogue.end` are occupancy, not decoration.

Draw the line on the shot timeline. Every micro-shot that overlaps that window by a real interval is a **speaking shot**. Every shot that does not overlap is a **silent shot**. If the package and that drawing disagree, the package fails.

Rules:

- Pin `microShotId` / `displayShot` only when the line truly lives in **one** shot. Then set `start`/`end` to that shot’s window. Never write a 0–segment-duration blanket while pinning Shot 2.
- A long line meant to be heard across cuts has two legal authors:
  1. keep **one** exact line and time it across the overlapping shots — emit official `<d>` once in the first occupied shot; later occupied shots are visual action only (no second `<d>`, no “continue the same spoken line”);
  2. split into shorter exact lines, one structured line per speaking shot, each timed to that shot.
- Do not cram a ~10s line into a ~4s middle shot and mark the overlapping first/last shots as silent holds or reactions. That fight garbles the voice: H3 is told to speak and to keep lips closed at the same time.
- When the line’s end is before the last occupied shot ends, the remaining tail of that shot is a visual hold. After the line ends: no further words. Do not invent a spoken tail.
- Never write keep-talking direction (`continues the same spoken line`, `continues speaking`, `keeps the promise going`). That is Mandate 0 (directing a speech event) and it makes H3 invent extra words after the line should have stopped.

Director JSON for an occupied-but-not-first shot: visual action only. Do not attach a second copy of the line. Do not write a silent-shot lock.

Test: delete every “continue / still speaking / finish the promise” sentence. If speech timing still matches `start`/`end` vs shot windows, the pack holds. If speech only works because those sentences exist, the pack fails.

## How this failed in live takes (do not repeat the *kind* of direction)

These are examples of the banned *method*, not a complete phrase list. Any new wording that does the same thing also fails.

| Kind of wrong direction | Why H3 breaks |
|---|---|
| Action restates the line (`acknowledges`, `names him a hero`, `promises that credit will go`, `she realizes he is not trying to take her place`) | H3 speaks the paraphrase **and** the `<d>` |
| Silent shot defined by speech (`silence after the question`, `before answering`, `leaving space for her response`) | H3 speaks through the hold |
| Silent shot uses words from a nearby `<d>` (`responsibility`, `credit`, `offer`) | H3 speaks that line early |
| Long line timed across the clip but `<d>` parked in one middle shot; overlapping shots locked silent | Garbled / invented voice; lips move on “silent” shots |
| Later shots told to `continue the same spoken line` | H3 invents a spoken tail after `end` |
| Broad `start`/`end` (0–duration) plus `displayShot: 2` | Occupancy and pin contradict each other |
| MCU plus “exactly two people” or `remains nearby` | Extra body / clone |
| Storyboard bound to Shot 1 only | Later shots invent framing and people |
| `@handle (S1) says` without official form / Audio cite | Wrong voice, invented words |
| Prop authority `identity for the coffee` | Prop imported as a person |

Good visual action, speaking or silent:

```text
Sharon prepares coffee for both of them while Terrance waits.
Sharon holds his gaze across the table.
Her expression turns exhausted.
Terrance remains in frame, calm, facing her.
```

## Compiled-prompt hygiene (structural, not speech)

A package MUST fail if `compiled_prompt` contains field-dump or legacy lock language:

```text
STORYBOARD EXECUTION LOCK
SHOT PLAN (
Purpose:
Initial state:
During this interval:
By the end of this interval:
[Shot 1] 00:
design_reference
one single character
jointly defined
supplies authoritative
Exactly one human character exists
is the storyboard reference for Shot 1
@sharon (S1) says
continues the same spoken line
INTERNAL CUT OR MOTIVATED MOVE
```

`closes their lips after the line` after an official `<d>` is required on the last occupied shot, not forbidden. `continues the same spoken line` is forbidden hygiene.

## Occupancy never restages an MCU or portrait

`visibleAssets` may list both people for continuity. The compiled shot still follows the authored composition:

- `medium close on Sharon` / MCU / close-up / tight portrait → single-subject. No “exactly two humans visible.”
- `two-shot` / group / over-shoulder / `sharon-side eyeline` / any `*-side eyeline` → occupancy lock is required. An eyeline MCU is an over-shoulder. Skipping occupancy here created a third back-of-head.

A medium-close on one speaker plus “exactly two distinct human characters are visible” produced a two-shot with the listener’s back filling half the frame.

---
