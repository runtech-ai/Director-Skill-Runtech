# Segment-local media lifecycle

Apply this to Director authoring, storyboard generation, preflight review and authorized video retries. A reported failure reads `Encoded request body exceeds 67108864 bytes`: an encoded-request boundary of 64 MiB on that request path, not a measured RAM limit. Prevent accumulation; do not treat that observation as a documented universal platform limit or promise that a skill can erase conversation history.

## Recover an oversized conversation

When that exact error occurs, do not repeatedly resend the same request. Save available text findings and evidence paths without replaying media. If the failed request prevents further work, use the last successfully persisted record and explicitly mark any unpersisted work unknown.

Use supported host compaction if available. Otherwise, explain that the user must open a fresh conversation in the same project and provide only a short resume instruction pointing to the saved files. Do not fork or copy the oversized history as the recovery strategy. A fresh conversation is a recovery step, not a guarantee that an oversized individual tool result will fit.

On resumption, reconcile live runtime state before issuing any mutation: an earlier generation or upload may have completed despite the conversation failure. Reload only the current segment's source and evidence. Save detailed segment reports to disk and return concise findings and a report path; do not concatenate all prior reports into each continuation.

Keep binary results out of model-visible tool output at the retrieval boundary. Saving a base64 response after it has already been printed does not remove it from history. If orchestration cannot save a required result without exposing an oversized payload, record the missing transport capability and stop that retrieval rather than dumping the response.

## Keep files, carry references

- Keep canonical assets, archive bytes, rendered boards, video, audio and extracted frames on disk or in the tool's artifact store. Keep only IDs, paths/artifact handles, hashes, source revisions, compact findings and next actions in working summaries/checkpoints. Never include base64, data URLs, binary content, complete media tool responses or frame collections in a checkpoint, continuation prompt or cross-segment handoff.
- Resolve each segment's required asset ledger. Attach only the canonical images actually needed for that segment and its current accepted storyboard when enabled. Do not attach every movie asset, the complete Director/storyboard ZIP, prior segment boards, previous retries or all review frames. Deduplicate references to the same file. A prior active-take final frame is an exception only when explicitly required for continuity; attach that single verified frame, never the full previous video or storyboard collection.
- Cache verified canonical bytes by asset ID, revision and hash. Check the current binding through live MCP before reuse; retrieve new bytes when it changes or provenance is uncertain. Freshness checks do not require reloading the entire library into context. Keep shared cached files on disk across segments, not repeated in their conversation payloads.
- Prefer local paths/artifact references over inline bytes where the tool supports them. If an MCP endpoint returns base64, intercept and decode it to a local file in tool orchestration; return only small metadata to the assistant. Never print the full response or base64 to tool/chat output. Remove temporary in-memory response/base64 buffers after saving; preserve the evidence file.

## Bound each operation

Use metadata and per-segment endpoints first. Stream/chunk large archives to a file with bounded buffers; use central-directory reads for layout checks, not a full-archive dump. A full hash requires all bytes on disk, not all bytes in conversation or memory at once. Do not concatenate an archive's chunks into one giant base64 string or retain every download response.

Use one segment's media working set at a time. Estimate serialized attachment size before submission where measurable: base64 alone needs `4 * ceil(byte_count / 3)` bytes, plus request/envelope overhead. Use a conservative **48 MiB internal ceiling** for a single media operation/working set, below the reported 68 MB boundary; this is a workflow guardrail, not an API parameter or a proven platform maximum. Respect a lower tool limit when known. A disk archive can exceed this ceiling if streamed without an equivalent in-memory or inline payload.

If the operation would exceed the ceiling, first remove unrelated/duplicate attachments, use supported file/artifact transport and split independent segment requests or review evidence into bounded batches. Preserve required canonical identity, readable geometry and full review coverage. Never drop a required asset or weaken a gate to fit; if the required request still cannot fit, record the transport limitation and exact resume action rather than send a knowingly oversized payload. Do not invent tool parameters or compress away required detail.

For video review, save extracted frames locally and inspect sequential bounded batches, using denser evidence around causal events. Save the full transcript separately and carry concise dialogue/timing findings. Full-clip review remains mandatory when the project requires it; loading all frames simultaneously is not required.

## Before retry or next segment

1. Save the current prompt/spec, exact asset provenance, accepted/rejected media paths, validation results and unresolved defects to the current segment's record.
2. Update a compact index with segment/status, record path, accepted board/take reference, continuity-out digest and next action. Keep global instructions separate from project IDs and active state.
3. Release orchestration references to binary/base64 responses, decoded media buffers and prior frame batches; keep files. A retry reloads only current required canonical references and corrected intent, not every rejected attempt. Never use rejected media as a canonical repair source.
4. Continue with the next segment's text record and required asset ledger. Reload a prior evidence file only for a specific unresolved question or required continuity check.

Use a real host compaction/reset mechanism when available after flushing checkpoints. Clearing a script variable or writing a summary does not erase images already present in conversation history. Do not claim a reset without an actual supported action, or create a new chat without authorization. If accumulated history itself hits the host limit, persist a text-only resume checkpoint and report that host compaction/resumption is required; do not keep injecting media into the same oversized context.

Preserve local evidence and accepted assets; this rule is about memory/context lifetime, not deleting project files. Follow repository exclusions for media and archives. For a skill-only request, update and validate these instructions without downloading, rendering or generating movie media.


Provider image-count limits are separate from serialized byte ceilings. Count required canonical images, enabled composition boards and selected continuity frames together. Verify actual job attachments before claiming a board was delivered; flags, readable stored media and fewer assets are insufficient. Removing unused visual assets must preserve required voice references and synchronize all consuming definitions/shot records.
