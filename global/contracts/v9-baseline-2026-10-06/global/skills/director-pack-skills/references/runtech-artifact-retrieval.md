# RunTech artifact retrieval

Use this reference only when validating a Director package or storyboard stored in RunTech MCP. It is a retrieval procedure; the v9 contract, package schema, and storyboard rules remain authoritative for content validation.

Apply [media-lifecycle.md](media-lifecycle.md) to every retrieval: write binary/base64 payloads directly to local files inside tool orchestration, expose only compact metadata, and release response buffers after saving. Stream archive chunks to disk rather than accumulating them in a response list or one giant string. Retrieve and review one segment's board at a time; do not return all boards or the full movie ZIP into conversation context.

## Session setup

For RunTech movie operations, select the intended organization, then call `list_movies`, then resolve the target movie. The list call refreshes the movie context used by later read operations.

## Stored Director ZIP

1. Call `get_director_pack_meta(movie_id)` and record `filename`, `bytes`, and `sha256`.
2. Call `download_director_pack(movie_id)` or `download_director_source(movie_id)` to stage the archive. Keep its `download_id`.
3. Retrieve chunks with either `download_director_pack(download_id, offset)` or `fetch_director_pack_chunk(download_id, offset, length)`. Advance with the returned `next_offset` until `done: true` when the full archive is required.
4. For a layout-only test of a large archive, retrieve the final chunk (at least 120 KB) and parse the ZIP central directory. Confirm the movie root contains `import-manifest.json`, `README.txt`, and `scene_packages/`; then apply the full importer validation to the archive contents.

Do not claim full-byte verification from a metadata response or a single chunk. Use the returned SHA-256 only after a complete local download is hashed.

## Segment storyboard PNG

Call `get_segment_storyboard(movie_id, scene_id, segment_id, clip_id?)` with the imported segment id, for example `SEG_SC001_001`—not `SEG_001_001`. The endpoint resolves in this order: clip take, stamped upload path, then a PNG inside the stored Director ZIP.

Require `ok: true`, `readable: true`, and a nonempty `image_base64` with the PNG signature `iVBORw0KGgo`. `get_scene_storyboard` is scene metadata only and may return no image bytes.

## Storyboard ZIP

Call `download_storyboard_zip(movie_id)`. It returns the attached/missing segment inventory and stages the ZIP. Read its final chunk using the same chunk mechanism, parse the central directory, and verify:

- one member per Director segment;
- every member is exactly `<SEGMENT_ID>.png`;
- every member is at the ZIP root; and
- no segment is in `missing`.

Use the per-segment PNG endpoint for pixel decode and visual review. The archive directory validates filenames and placement; it does not replace pixel review.
