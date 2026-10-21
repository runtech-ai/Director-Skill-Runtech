# Genre direction profiles

Use during the [scene direction pass](scene-direction-pass.md) to choose how a scene is covered, cut, performed and heard. Camera moves themselves are described in [camera techniques](camera-techniques.md) and [genre camera language](genre-camera-language.md). These profiles are starting points drawn from established film and television practice, not model guarantees. A project picks a primary genre, a medium and a format, writes them into its direction profile, and may switch register scene by scene (a horror film still has a quiet kitchen scene).

Shot lengths below are typical ranges for that register. Contemporary mainstream features average roughly 2–5 seconds per shot; slower art-house and observational work runs much longer. Let the performance and the event set the actual duration, then check the range.

## How to build a project direction profile

Write `projects/<project>/references/DIRECTION_PROFILE.md` with these headings. Keep it under a page.

1. **Primary genre and registers:** for example "family sports anime: everyday register for home and school, match register for battles".
2. **Medium:** live action, 2D TV anime, feature animation, 3D CG, stop-motion, or a stated mix. Use the medium modifiers below.
3. **Format:** aspect ratio, segment duration limits, episode length, vertical or horizontal delivery.
4. **Camera baseline:** support style (tripod, handheld, animated layout), usual height, usual shot sizes, movement energy and any project bans (for example a project that forbids camera moves).
5. **Coverage defaults:** how dialogue, reactions and action are covered in each register.
6. **Rhythm:** typical shot lengths per register and where the rhythm changes.
7. **Performance style:** naturalistic, heightened, comic timing, anime acting conventions.
8. **Sound and music:** ambience beds, score style, where silence is used.
9. **Deliberate exceptions:** named scenes that break the baseline and why.

The compiler's locks file (`projects/<project>/h3/h3-locks.json`) holds the project's style opening, subject identities and invariants. The direction profile holds the directing choices. Do not mix the two.

## Genre profiles

Each profile lists: **Coverage**, **Camera**, **Rhythm**, **Performance**, **Sound**, **Avoid**.

### Drama
- **Coverage:** establish, then shot / reverse-shot at matching sizes; go tighter as stakes rise. Hold on the listener when a line lands.
- **Camera:** mostly static or slow, motivated moves tied to a shift in attention; eye-level.
- **Rhythm:** 3–6 s dialogue shots; longer holds for decisions.
- **Performance:** restrained, specific behavior with props; thoughts shown through eyes and hands.
- **Sound:** room tone, sparse score entering late in a scene.
- **Avoid:** push-ins on every face; score explaining the emotion.

### Romance
- **Coverage:** shared frames that measure distance between the pair; singles grow tighter as intimacy grows; over-the-shoulders keep both present.
- **Camera:** gentle lateral moves or slow approaches when the relationship shifts.
- **Rhythm:** unhurried; 3–7 s shots; let silences play.
- **Performance:** eye contact, near-touches, small hesitations.
- **Sound:** intimate room sound, close breath, warm score.
- **Avoid:** mandatory orbiting kisses; cutting away before a look is returned.

### Comedy
- **Coverage:** frame setup and payoff in the same shot when possible; wide enough to see physical gags; cut to the reaction for the laugh.
- **Camera:** stable, often static; a timed reframe or whip pan can be the joke.
- **Rhythm:** precise; hold a beat after the gag for the reaction, then cut. Sitcom style uses 2–4 s shots across a few fixed angles.
- **Performance:** clear intentions, deadpan or heightened by tone; reactions sell jokes.
- **Sound:** clean dialogue, light score stings, comic silence.
- **Avoid:** moving early and spoiling the reveal; cutting before the physical payoff lands.

### Thriller / suspense
- **Coverage:** point-of-view and eyeline shots that restrict what the audience knows; inserts of the threat object; foreground cover.
- **Camera:** controlled tracking, slow approaches, long-lens observation.
- **Rhythm:** stretched holds building tension, then sharp acceleration on release.
- **Performance:** watchful stillness, small tells.
- **Sound:** low drones, isolated sharp sounds, silence before the release.
- **Avoid:** revealing hidden information without a viewpoint that sees it; random tilts.

### Horror
- **Coverage:** wide frames with negative space where something could appear; hold on the frightened face; withhold the threat.
- **Camera:** slow creeping moves or locked frames; a pan motivated by an offscreen sound.
- **Rhythm:** long holds (5–10 s) before scares, then a fast cut or none at all.
- **Performance:** listening, breathing, delayed reactions.
- **Sound:** silence and room tone carry dread; sound reveals before picture.
- **Avoid:** constant shake; showing the threat early; unearned jump scares.

### Action
- **Coverage:** establish attacker, target and direction; side or three-quarter angles that make contact readable; cut to consequence.
- **Camera:** follow pans, tracking alongside movement, handheld energy anchored to a clear subject.
- **Rhythm:** 1–3 s shots in fights; a longer wide holds geography between bursts.
- **Performance:** committed physical intent, weight, recovery after impact.
- **Sound:** specific impact sounds on the contact frame; score drops for the key hit.
- **Avoid:** hiding impacts behind blur; crossing the action axis without showing it; slow motion everywhere.

### Martial arts
- **Coverage:** wider frames that keep full bodies and footwork; longer takes to show real choreography.
- **Camera:** steady frames or measured lateral tracking; cut on the strike, not in the middle of a move.
- **Rhythm:** 2–5 s, longer than generic action, because the choreography is the spectacle.
- **Performance:** stances, breath, precise contact and recovery.
- **Avoid:** close shaky framing that hides technique.

### Crime / noir
- **Coverage:** layered staging with characters at different depths; partial concealment; interrogation-style singles.
- **Camera:** static frames, slow lateral reveals, low angles for power.
- **Rhythm:** measured, 4–8 s.
- **Performance:** guarded, economical.
- **Sound:** city ambience, sparse jazz or low synth, hard footsteps.
- **Avoid:** rain and smoke in every scene; automatic Dutch tilts.

### Mystery
- **Coverage:** inserts of clues framed so the audience can notice them; reaction shots of whoever notices.
- **Camera:** observant, unhurried; a rack focus to a clue.
- **Rhythm:** steady; let discovery beats breathe.
- **Avoid:** cameras that know the solution before a character does.

### Science fiction
- **Coverage:** establish the rules of the world (scale, technology) early with wides; ordinary coverage for human scenes.
- **Camera:** physical even when the world is not; cut for impossible changes of scale.
- **Rhythm:** depends on register; awe beats get long holds.
- **Avoid:** using technology as permission for camera teleportation.

### Fantasy / epic
- **Coverage:** landscape and crowd scale with wides, intimate singles for stakes.
- **Camera:** justified crane and landscape reveals; measured travel.
- **Rhythm:** slower for scale, faster in battle.
- **Avoid:** every exterior becoming a drone shot; losing faces in spectacle.

### War
- **Coverage:** perspective tied to a participant or a clear objective observer; cover-based viewpoints.
- **Camera:** handheld with purpose; tracking through trenches or streets at human height.
- **Rhythm:** chaotic bursts, then long aftermath holds.
- **Sound:** layered and directional; silence after blasts.
- **Avoid:** perpetual tremor; viewpoint jumping from shoulder to aerial.

### Western / period
- **Coverage:** deliberate geography, group staging, wide two-shots across distance.
- **Camera:** measured lateral travel, static landscapes, few moves.
- **Rhythm:** patient; standoffs stretch time.
- **Avoid:** modern camera styles without a stylistic decision.

### Family / children's
- **Coverage:** clear, readable staging; character eye level for children; reaction shots that make emotions legible.
- **Camera:** gentle, uncomplicated moves.
- **Rhythm:** clear and moderate, 2–5 s.
- **Performance:** expressive but sincere.
- **Avoid:** confusing geography; frightening imagery the story did not ask for.

### Slice-of-life / coming-of-age
- **Coverage:** observational wides and mediums; small domestic inserts (food, hands, objects).
- **Camera:** mostly static, eye-level; occasional slow lateral moves.
- **Rhythm:** relaxed, 4–8 s; pauses are content.
- **Performance:** naturalistic, small gestures.
- **Sound:** strong ambience (weather, fans, distant traffic).

### Sports
- **Coverage:** two registers. Off the field: drama coverage. In play: establish positions, follow the ball or object, cut between competitor, object and opponent, and show the scoreboard or result.
- **Camera:** sideline follow pans, low angles for power, parallel tracking for speed.
- **Rhythm:** 1–3 s in play; a quiet beat before the decisive moment.
- **Avoid:** losing who is where; speed shown only with blur.

### Musical / dance / music video
- **Coverage:** full bodies for choreography; cuts on musical accents, not on every beat.
- **Camera:** choreographed with performers; track or arc to keep footwork.
- **Rhythm:** follows the music's phrasing.
- **Avoid:** camera moves that hide footwork; auto beat-sync.

### Documentary / mockumentary
- **Coverage:** an operator finds the action; interviews at stable eyeline; cutaways that are connected to what is said.
- **Camera:** handheld or tripod with practical reframes; zooms from a fixed position.
- **Rhythm:** varies; interviews hold, observation follows events.
- **Avoid:** omniscient angles; polished advertising looks.

### Found footage
- **Coverage:** one or a few in-world cameras; no reverse angles that no camera could get.
- **Camera:** operator-height, believable reframing, partial occlusion.
- **Avoid:** cameras recording from impossible places; routine violent shake.

### Commercial / advertising (including toy spots)
- **Structure:** hook within the first 2 s, product in use, a clear payoff, then an end card with the product and one line of text. A 30 s spot usually has 12–18 shots.
- **Coverage:** hero inserts of the product at its best angle; the user's face reacting to it; one wide that shows how it is used. Toy spots shoot from the child's eye level or lower.
- **Camera:** clean, purposeful moves: a short arc or slide on hero shots, low angles for excitement, a locked frame for the end card.
- **Rhythm:** 1.5–3 s shots, cut to the music's accents; one held beat before the payoff.
- **Performance:** energetic and readable, real enthusiasm, friendly rivalry; no mean-spirited outcomes.
- **Sound:** punchy score, a short announcer voiceover, crisp product sounds (clicks, launches, impacts).
- **Avoid:** showing the product doing something it physically cannot; hiding the product in fast cuts; ending without the product on screen.

### Microdrama / vertical short drama
- **Coverage:** 9:16 favors singles and close two-shots; stack subjects vertically; open each episode on a hook within the first seconds.
- **Camera:** simple, readable framing; push-ins sparingly on reveals.
- **Rhythm:** fast, 1.5–3 s; each episode ends on a cliffhanger beat.
- **Performance:** heightened, readable on a phone.
- **Avoid:** wide landscape compositions that leave faces tiny; slow openings.

## Medium modifiers

Apply on top of the genre.

- **Live action:** natural lens behavior, depth of field and handheld physics; performance carries the shot.
- **2D TV anime:** layouts are designed drawings. Use held frames with small acting, camera slides across background art, pans over stills for travel, speed lines, smears and impact frames for velocity, and cuts rather than continuous 3D camera moves. Characters animate on twos or threes. Everyday scenes stay grounded and eye-level; heightened scenes push perspective and angle.
- **Feature animation (Western 2D or 3D):** continuous acting with anticipation, follow-through and squash-and-stretch; camera behaves like a physical camera.
- **3D CG:** keep the camera physical; avoid floating orbits that expose unbuilt geometry.
- **Stop-motion / miniature:** deliberate framing, stable scale, short supported moves; keep the frame-rate texture.
- **Vertical 9:16:** compose for height; fewer people per frame; keep text-safe areas clear.

## Switching registers inside a project

Name the register in each scene's authoring notes: "SC005 match register". The register sets coverage, rhythm and camera energy for that scene. Transitions between registers should be motivated (the first launch, a door opening onto the arena). Keep the project's medium and identity rules constant across registers.
