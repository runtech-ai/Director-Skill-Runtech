# Beyblade Physics Bible

Director and generation reference for classic Plastic Generation Beyblade action. These rules are a hard validation gate whenever a Beyblade, launcher, ripcord, stadium, collision, knockout, or Bit Beast appears.

## 1. Core physical model

- A Beyblade is a palm-sized, solid, rigid spinning top. Its visible components stay assembled unless the script explicitly depicts damage or disassembly.
- The pointed performance tip is the ground-contact point. After landing, the tip remains in continuous contact with the stadium or support surface until a photographed impact causes a hop, ring-out, or fall.
- Axial rotation and travel across the stadium are separate motions. A top can spin rapidly while translating slowly, or travel rapidly while losing RPM.
- Right-spin and left-spin are persistent authored properties. They never reverse during a take or across a cut.
- Mechanical energy is causal and decreases through drag, tip friction, scraping, impacts, and deformation. A free top cannot gain RPM or restart without visible external torque.
- Scale, owner, design, colors, component stack, damage, spin direction, RPM state, path, contact state, and outcome must survive every cut.

## 2. Project ownership and identity

| Owner | Beyblade | Spin | Identity lock |
|---|---|---|---|
| Kaiden | Handmade Ebudhou Blade | Right | Blue-red metal Attack Ring, brown wooden lower ring, exposed worn metal, intact seated centre Bit Chip |
| Nanao | Dragoon | Left | Blue-red-yellow canonical design |
| Mocha | Driger | Right | White-red-purple canonical design |

- Never swap owners, colors, spin directions, or component designs.
- Never duplicate one design to stand in for another or create a hybrid from two tops.
- Catalogue/reference-sheet arrangement never dictates battle positions.
- A combined reference plate supplies identity only; the current shot controls population, ownership, orientation, and staging.

## 3. Launcher geometry and loading

### Hand ownership and holding pose — user rule, 2026-10-01

- The user's anatomical LEFT hand wraps around and grips the launcher handle. It stabilizes the launcher throughout loading, the pull, and release; fingers must grasp the actual handle rather than the housing or attached top.
- The user's anatomical RIGHT hand grips the ripcord/winder pull handle and performs the single outward pull along the gear channel. After extraction the complete ripcord stays in the right hand; the left hand retains the empty launcher.
- These are the character's left and right hands, not screen-left and screen-right. Choose camera staging that makes this pose readable without mirroring it or swapping hand ownership across cuts.
- Preserve the canonical grip silhouette and natural separate wrists, palms and fingers. Reject reversed hands, hand-role swaps, hands merged with the handle or winder, or a holding pose that prevents the prescribed pull.
- Apply this pose to prompts, storyboard references, loaded-state checks and full-motion validation unless the user explicitly authors an exception.

### Valid loaded state

- The top is level and flush against the launcher underside with zero visible air gap.
- Both launcher engagement posts are inserted into the top’s receiving slots and twist-locked.
- The performance tip points straight down.
- The launcher and attached top behave as one rigid assembly before release.
- The short, rigid, toothed plastic ripcord passes horizontally through the launcher gear channel. Its ring remains in the pulling hand.

### Forbidden geometry

- No string launcher unless the script explicitly specifies one.
- No cable, rope, tether, long shaft, rod, stem, spacer, hose, dangling connector, or floating gap.
- The top never hangs below the launcher from a cord.
- The launcher must not intersect the top, merge into it, or deform into a weapon or oversized machine.
- An empty launcher after release shows no top attached beneath it.

## 4. Ripcord and torque causality

1. Before the pull, the loaded top is stationary.
2. The anatomical left hand braces the launcher by its handle while the anatomical right hand pulls the complete ripcord once along its toothed axis.
3. The internal gear transfers torque while the top is still flush-mounted.
4. During the pull, the attached top accelerates around its authored spin axis.
5. The entire ripcord exits into the pulling hand; it does not remain embedded or become a string.
6. The launcher releases the already-spinning top once.

- A successful top’s first unsupported frame already shows high-RPM axial rotation and circumferential Attack Ring blur.
- A top may not detach motionless, land motionless, and then spin up by magic.
- A failed release that receives no usable torque remains non-spinning, falls under gravity, and stays stopped.
- Each pull produces at most one release of its attached top. No duplicate top may appear from one launcher.

## 5. Spin-start causality, release, descent, and landing

- A stationary Beyblade never begins spinning by itself. Spin must have a visible physical cause: deliberate hand rotation, a valid launcher release, or continuous carry-over from the immediately previous authored shot where the same top was already spinning.
- This causality lock also applies to dream, symbolic, magical, and Bit Beast imagery. Those forces may affect an already-spinning top only when separately authored; they do not replace the mechanical cause of initial spin.
- If a graphic beat needs to reveal multiple sides without an allowed spin cause, keep the top's orientation fixed and orbit the camera around it.

- Detachment is a single readable event after torque transfer.
- Gravity carries the spinning top downward immediately; it never floats or pauses in mid-air.
- The top lands tip-first. The Attack Ring and base remain above the contact tip.
- Rotation is continuous through descent and first contact.
- Landing may create a small hop, vibration, or path deflection, but the top must return to tip contact under gravity.
- After landing, no prolonged hovering, invisible support, glued pivot, or late spontaneous acceleration is allowed.

## 6. Observable spinning

### High RPM

- Strong circumferential blur appears around the Attack Ring and outer markings.
- The centre emblem may remain visually centred, but perimeter markings cannot stay crisp and frozen.
- The axis is mostly upright with small, rapidly rotating precession.
- This must be visible in storyboard pixels as well as generated video. An already-spinning/high-RPM beat cannot use a crisp stationary top image and defer its spin-up to the video model. Use the per-top board gate in [DIRECTOR_AUTHORING.md](DIRECTOR_AUTHORING.md); preserve explicit slower/stopped states and keep non-spinning tops unsmeared. Whole-frame camera blur, translation streaks, glow or duplicate rings are not substitutes for perimeter rotation cues.

### Medium RPM

- The ring remains visibly rotating while blur decreases.
- Precession becomes easier to see and the travel path may tighten or drift with stadium slope.

### Low RPM

- Precession widens continuously.
- The body tilts farther, with the lean direction rotating around the tip rather than freezing toward one compass direction.
- Rim/base scraping becomes possible and produces further speed loss.

### Stopped

- A free unsupported top cannot remain balanced upright on its tip.
- It falls onto its side or lies flat after the final wobble.
- It may remain level while stopped only when held by a hand, locked to a launcher, supported by a fixture, or resting on a broad flat surface in a physically stable orientation.
- A physical Beyblade never spins freely in a palm, between fingers, in a pocket, on bedding, or in unsupported air. Hand-held rotation is allowed only as deliberate low-speed manual inspection explicitly authored as such; it must not resemble powered spin.
- Dream and title coverage still obeys section 5's spin-start causality. A nonphysical background does not authorize self-rotation. For a reveal without an allowed cause, fix the top's orientation and use a specifically authored camera orbit; keep physical bodies and supports out of an isolated graphic.

## 7. Stadium interaction

- The stadium is an ordinary solid bowl with continuous surface geometry and gravity.
- The tip follows the local tangent of the bowl, producing smooth curved travel.
- Position changes continuously frame to frame. No teleporting, frozen staging, instant lane changes, or repeated resets.
- Outer-slope travel generally carries more translational speed; centre-zone travel may be more stable.
- A top cannot orbit a fixed invisible point while its body translation is frozen.
- Wall/rim contact causes a brief impact, path deflection, vibration, wobble, and energy loss.
- Ring-outs must cross the physical rim with a continuous ballistic path and land outside; a top cannot vanish or cut directly from inside to outside.
- Existing cracks, missing pieces, and deformation persist. A broken stadium never heals between shots.

## 8. Beyblade-to-Beyblade collisions

- Contact occurs at the Attack Rings or another explicitly visible physical component—not centre-to-centre ghost overlap.
- At the collision frame, silhouettes touch without interpenetrating.
- Immediately afterward the tops separate, rebound or deflect along changed tangents.
- At least some combination of path change, wobble, RPM loss, vibration, scraping, or ring-out follows the impact.
- Momentum and spin direction determine the response; the weaker or less stable top usually shows the larger deflection and wobble.
- Tops never stick together, overlap, merge, magnetically cluster, or remain touching while spinning.
- A collision cannot create extra tops, swap designs, reverse spin direction, or restore lost energy.

## 9. Multiple-top population and continuity

- Count tops, launchers, ripcords, owners, and stadiums explicitly per shot.
- Each visible launcher owns one specific top and one specific ripcord before release.
- After release, the same top continues in the stadium; do not substitute, recolor, or duplicate it.
- Preserve each top’s incoming zone, path, RPM, damage, and outcome across cuts.
- Tops should occupy distinct physical paths rather than a staged row or synchronized formation.
- A stopped or ejected top remains stopped/ejected unless the script photographs a new launch.

## 10. Damage, knockout, and recovery

- Damage is cumulative and physically located: chips, cracks, bent parts, and scuffs persist.
- A knockout includes visible impact, rim crossing, outward trajectory, landing, and stopped state.
- A burst or disassembly happens only when explicitly authored; components follow separate gravity-driven trajectories.
- Recovery occurs only after the top has stopped or when a hand safely intercepts it as authored.
- A hand never grabs an invisible, duplicated, or still-high-RPM blade without an explicit dangerous-contact beat.

## 11. Bit Beast rules

- A Bit Beast is supernatural spirit essence, not a mechanical component leaving the top.
- Manifestation originates from and remains visibly anchored to the intact seated centre Bit Chip/emblem of its owner’s physical Beyblade.
- The energy connection remains readable between the enormous spirit image and the palm-sized spinning top below.
- The physical top, launcher, stadium, clothing, and environment remain solid and nonluminous unless a separate authored effect says otherwise.
- The Bit Chip/cap remains closed, seated, assembled, and attached. No solid lid opens and no physical creature or component ejects.
- The physical top continues obeying spin, tip contact, gravity, collision, and energy-loss rules during manifestation.
- Manifestation intensity follows authored state: dormant → glowing → manifesting → manifested → fading → dormant.
- A Bit Beast cannot teleport to another owner, duplicate, change species, or persist after its authored fade/return.
- Dream or symbolic imagery may be freer only when the shot is explicitly nonphysical; it must not silently alter real-world battle state.

## 12. Camera and edit requirements

- Keep the top large enough in frame to verify attachment, tip contact, ring blur, collision, and wobble when those are the beat.
- Do not hide the critical release or collision entirely behind hands, launcher housings, effects, or cuts.
- Preserve camera axis and top orientation; do not combine side-view launcher geometry with an impossible top-down attachment.
- A cut does not reset position, RPM, spin direction, damage, or contact state.
- Slow motion may reveal an event but cannot change its causal order.
- Motion blur must communicate rotation, not erase identity or create duplicate rings.

## 13. Director state chain

Write the mechanical state before shot prose:

`owner/design → spin direction → attached/stationary → torque while attached → single release → rotating descent → tip-first contact → axial spin + curved translation → collision/deflection → energy loss → widening precession → side fall/knockout/continued spin`

For each shot record:

- top count and owner mapping
- launcher and ripcord count
- attachment/release state
- spin direction and RPM band
- tip/stadium contact state
- stadium zone and travel direction
- collision partner and impact result
- damage and Bit Beast state
- exact incoming and outgoing state

## 14. Prompt locks

Use only the locks relevant to the photographed beat.

Read [DIRECTOR_AUTHORING.md](DIRECTOR_AUTHORING.md) for beat-specific motion/effect permissions and upstream repairs. Constraints describe the current state; never append launch, collision, high-RPM blur or Bit Beast language to an unrelated stationary hold. In a mixed launch, describe successful tops and the failed top separately. A visible light effect never starts a stationary top spinning.

### Loaded launcher

`The stationary top is level and flush beneath the launcher with zero gap, both engagement posts inserted, tip down, and the short rigid toothed ripcord passing horizontally through the gear channel.`

### Successful launch

`The ripcord pulls once; the top accelerates while still attached, releases once already at high RPM, descends under gravity, and lands tip-first while preserving continuous axial rotation.`

### Stadium spin

`The tip stays visibly in contact with the bowl while the top spins about its axis and translates along a continuous curved path; perimeter markings blur and mechanical energy decreases.`

### Collision

`The Attack Rings make one visible physical contact, then immediately separate along changed tangents with recoil, wobble, and speed loss; the tops never overlap or stick.`

### Wobble and stop

`As RPM falls, precession widens, the rim begins to scrape, and the unsupported top tips onto its side after stopping.`

### Bit Beast

`Luminous spirit essence remains connected to the intact seated Bit Chip of the same palm-sized physical top; the top and stadium stay solid, nonluminous, and mechanically grounded.`

## 15. Hard-fail checklist

Reject the take if any applicable answer is yes:

- Is there a gap, cord, shaft, or invented connector between launcher and top?
- Does the top spin up only after detachment or landing?
- Does a successful launch show a crisp, motionless top in unsupported flight?
- Does the top hover, lose tip contact without a physical hop, or pivot on an invisible fixed point?
- Are perimeter markings frozen while high RPM is claimed?
- Does a tilted top hold one fixed lean rather than precess?
- Does a collision lack visible contact, immediate separation, deflection, wobble, or energy loss?
- Do tops overlap, merge, cluster, teleport, duplicate, change owner/design, or reverse spin?
- Does a stopped unsupported top remain upright on its tip?
- Does a ring-out skip the rim-crossing trajectory?
- Does damage reset across a cut?
- Does a Bit Beast detach as a solid object, open the Bit Chip, lose its physical anchor, or make the top/stadium glow without authorization?

If any answer is yes, the take fails even when the overall scene match exceeds 95 percent.

## 16. Review evidence

- Inspect at least one frame before pull, during attachment, first detached frame, landing, stable spin, each collision, post-collision response, and final state when those phases exist.
- Sparse samples are insufficient when a failure could occur between them. Use denser temporal evidence or fail closed.
- Verify exact active clip and newly versioned path before judging.
- Asset integrity is checked before every generation run; motion physics is checked after every generated take.

## Latest user-supplied launcher mechanics reference — 2026-10-02

Read projects/beyblade/references/LAUNCHER_RIPCORD_MECHANICS_REFERENCE.md and inspect its original photo for pending loading, pre-pull and launch beats. Replicate the braced handle grip, separate ripcord-hand grip, straight continuous toothed rack through housing and directly supported top/release geometry. Do not infer an arbitrary hand-length rack limit. Keep project left-grip/right-ripcord ownership, owner-specific canonical designs and the authored phase. The illustrative repeated tops in the photo are successive states; render one solid top per current phase.
Latest user launch-pose hard gate (2026-10-02): the actual original launcher handle remains horizontal to ground; anatomical left hand wraps the grip behind housing, and the black butterfly ripcord handle faces inward toward the connected blader body in the anatomical right hand. Keep the original mounting underside down with one flush stationary top beneath it before pull. See projects/beyblade/references/LAUNCHER_RIPCORD_MECHANICS_REFERENCE.md. User also requires use_storyboard_ref enabled and read back on each verified repaired upload; see projects/beyblade/rules/storyboard-reference-upload.md.
