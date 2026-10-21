# Import routing and persistence verification

Read for package delivery, import, reimport or a missing-production-scene error. Preserve the current Director schema. Instructions and patch files inside an archive do not execute or install server fixes.

## Identify the target and archive

Discover the current movie and organization before reusing saved IDs. Keep movie ID, episode/script ID, MovieScript project ID, scene ID and segment ID separate. `SC001` is script-local; changing its spelling cannot create a production row. Do not substitute a same-named film after a 404 without resolving the intended target. A default DSL scene or a visible script in the editor is not evidence of a Director import.

Classify the deliverable from its contents and observed importer support:
- An individual Director package goes to the Director importer for its intended episode.
- A series envelope goes to the series importer. Each episode remains independently loadable and scoped to its own script, even if all use SC001.
- A delivery collection is not automatically an importable series. Nested episode ZIPs and wrapper folders are accepted only when the target series importer demonstrably supports that format. A local loader pass does not establish deployed support.
- Storyboard-only ZIPs attach stills; they do not create a missing Director segment plan.

Document the required import surface beside each delivered archive. Do not package a server patch as if it makes a ZIP self-repairing. Keep plugin update archives, service patches and film packages explicitly distinguished.

## Check persistence when import is authorized

Before mutation, identify the intended episode and existing content. Use supported episode selection or an explicit script-scoped operation. Never import multiple episodes into the same active SC001 to work around missing series support.

After the import response, read back stored package metadata and production scenes for the intended script. Compare every expected scene and segment ID, duration, authored prompt, boundary settings, storyboard attachment and required asset binding against the archive. Save episode-qualified evidence with movie/script IDs, archive hash, inspected scope and observed counts. Verify real storyboard bytes or actual takes, not only an authoring path or thumbnail counter. Sheet attachment, extracted shot thumbnails and video-conditioning flags are separate checks. Honor the user's storyboard/keyframe choices; a supplied board need not be enabled as video input.

For a series, verify all requested episodes. Record any unverified episode rather than extrapolating success from the active one. If available tools cannot select/read other scripts, report that limit; do not claim series-wide live verification. Distinguish imported, updated and skipped results. A resume response that skips an existing name does not apply corrected prompts or boards. Use a supported refresh/update option only after confirming it exists on the deployed service; preserve episode IDs and existing takes unless replacement is requested.

## Diagnose failures without changing the story

- `import a director package for this scene first`: production lookup found no matching row in its current scope. Check the selected script, expected scene keys and import persistence; do not rewrite scene IDs or create placeholder segments merely to suppress the error.
- `no stored director package`: no source package is available for the queried scope. Do not infer that every episode is absent or that the archive itself is malformed.
- `movie not found`: rediscover identity/org, record the mismatch and stop writes until resolved.
- `Depends ... org_id` or another server exception: runtime/API failure; do not present repackaging as its fix.
- An upload ID returned by begin but missing at append: transport/session persistence failure. Stop blind retries and inspect routing/shared storage if server repair is authorized. A chunk must be acknowledged before sending the next; an uncertain append is not safe to repeat without idempotency support.

Server diagnosis, local patching, deployment and live data refresh are separate states. Respect a local-only request. Do not modify or deploy a service as an automatic side effect of skill/package authoring. If an unresolved service defect prevents import, say so and deliver the valid artifact plus the exact remaining operation.

## Report the evidence honestly

Report separately: archive structure checked; actual local loader tested; live import accepted; script-scoped persistence verified; board pixels reviewed; generated motion/audio reviewed. Mark missing evidence unknown. Never describe a local mock-storage test as a live import, a saved prompt as a corrected render, or a skill update as a deployed repair.

## Active-episode mutation guard

Observed RunTech behavior: `get_or_create_moviescript` can retrieve an existing episode project without changing `active_script_id`; even a scene UUID may be resolved through the active episode. Verify the deployed tool behavior rather than treating either as an episode-selection guarantee.

For active-episode-only writes, retain the intended movie/script ID, source segment action, prompt and storyboard path before editing. Re-read the active script and target segment immediately before EACH mutation, including later writes in a batch. Compare current content with the saved source; stop affected writes if the episode or content changed. Prefer a genuinely script-scoped or conditional endpoint when available. These checks reduce but do not eliminate a read/write race; they are not atomic concurrency control. If routing cannot be established, finish a local repair artifact and report the unapplied scope.

Read back after each write and compare the target prompt and unchanged board/action data. On a timeout or uncertain response, inspect current state before retrying. If an unintended episode was changed, stop subsequent writes and restore from the exact captured pre-write value when safely targeted. A checksum-matched imported source is a fallback reconstruction, not proof of byte-identical prior runtime content; disclose that distinction and the restoration result. Never overwrite a newer concurrent user edit to force a rollback.

For storyboard inputs, distinguish package defaults, clip-level overrides, resolved labels and actual attached bytes. A generic `enabled` key may not be the deployed default switch. Inspect the supported fields and effective clip state; do not globally enable or disable boards based only on this observation. Asset-library order and saved omission warnings are not a verified provider label map.

For final archive dispatch, nested-ZIP size limits, updated mirror hashes and immutable episode checks, use [production repair lessons](production-repair-lessons.md#review-and-delivery-evidence). Test the actual final outer archive after its last edit.
