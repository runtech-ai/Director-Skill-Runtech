# RunTech continuity import gate for Director v9

Read this when authoring or repairing segment boundaries under the v9 contract and before exporting
the Director ZIP. Preserve the established importer fields and package hierarchy.

## Separate physical state from machine continuity

`continuityIn` and `continuityOut` hold photographed physical-state prose.
`continuityMode` records the intended incoming mode. RunTech's normalizer checks
`continuity_in`, then `continuityIn`, before `continuityMode`; prose can therefore
normalize to `CUT` even when `continuityMode` says `MATCH_CONTINUITY`.

Keep the prose and add explicit importer-supported `continuity_in` and
`continuity_out` enum fields. Do not replace state prose with a mode token or
rename the existing package fields. Author each boundary from the source and
physical sequence; a new segment does not imply a reset, and not every boundary
must match. Across continuous scenes, retain predecessor links across scene IDs.

## Editorial boundaries have higher priority

The final-edit mapping itself forces HARD_CUT to CUT and disables the previous-frame reference. Some current importer revisions first reconcile an explicit authored match by converting that boundary to MATCH_CUT. This behavior is version-sensitive: inspect the actual importer and final-edit output rather than relying on automatic repair or a keyword count. For an intended visual-state match, all declarations must agree:

```json
{
  "continuityMode": "MATCH_CONTINUITY",
  "continuity_in": "MATCH_CONTINUITY",
  "continuity_out": "MATCH_CONTINUITY",
  "editorialBoundaryIn": "MATCH_CUT",
  "editorialBoundaryOut": "MATCH_CUT",
  "previousSegmentId": "SEG_SC001_001",
  "referencePreviousLastKeyframe": true,
  "usePreviousLastKeyframeAsFirstFrame": false
}
```

This example assumes both adjacent boundaries match. Set the outgoing mode and
editorial boundary from the next segment's incoming intent. A deliberate reset
uses `CUT` and `HARD_CUT`; the film's end has no next reference and uses the
supported end boundary. Matching continuity can cut to a new camera angle; it
does not require an exact first-frame continuation. Use `DIRECT_CONTINUATION`
and its first-frame semantics only when that unbroken continuation is authored.

Synchronize the authoritative segment, scene index/plan, legacy segments,
production/directorPlan copies, prompt bundles and aggregate bundles. Match the
first micro-shot's incoming and final micro-shot's outgoing transition/machine
mode to the segment boundary. Internal editorial cuts retain their authored
intent. Keep storyboard expectations and H3 prose consistent with those states.

## Validate the imported meaning, not a keyword count

Before delivery, normalize the actual packaged records using the current
RunTech importer and its final-edit boundary mapping (or a supported live dry
run). Verify effective incoming/outgoing enums, predecessor IDs, previous-frame
flags and first-frame policy against the authored plan for every segment.
Reopen the exported ZIP and check those same records and their redundant copies.
Structural allocation tests and finding `MATCH_CONTINUITY` in JSON are not enough.

Keep a regression case with physical-state `continuityIn` prose plus
`continuityMode: MATCH_CONTINUITY` and `editorialBoundaryIn: HARD_CUT`: the
final-edit mapping resets it to CUT unless the current importer reconciles it first. Record which behavior the installed revision exhibits. The repaired case must include explicit machine
enums and `MATCH_CUT` and must normalize to the intended match with the previous
reference preserved. Report the importer revision and distinguish local parser
validation from a deployed import, frame resolution and rendered continuity.

When an import is requested, read back saved segment modes and flags afterward.
If the UI still shows `CUT`, compare stored ZIP filename/hash and active script
with the delivered artifact, then inspect field precedence. Do not assert a
successful live import from local files or update the wrong movie to bypass a 404.

Resolve a previous reference from the preceding selected active take's final
frame. Do not fabricate paths or attach an unsupported extra image. Budget that
reference along with canonical images and an enabled storyboard; exceeding the
provider limit is a generation preflight failure, not permission to drop needed
canonical references. Changes to directed boundary states require affected board
acceptance to be reviewed against the new revision; retain the original evidence.

