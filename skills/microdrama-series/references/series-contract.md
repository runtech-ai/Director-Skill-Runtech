# RunTech microdrama envelope 1.0

The new outer format is distinct from the existing Director schema. Each child is independently importable with the existing Director ZIP loader.

```text
series-manifest.json
series-bible.md
continuity.json
episodes/
  EP001/
    import-manifest.json
    movie.movie
    asset-manifest.json
    assets/characters/...
    assets/props/...
    assets/locations/...
    scene_packages/...
    storyboards/SEG_SC001_001.png
  EP002/
    ...
```

```json
{
  "format": "microdrama-series",
  "version": "1.0",
  "title": "Series title",
  "episodes": [
    {"id": "EP001", "title": "The discovery", "packageRoot": "episodes/EP001"},
    {"id": "EP002", "title": "The price", "packageRoot": "episodes/EP002"}
  ]
}
```

Manifest order is episode order. IDs and roots must be unique. ZIP root must contain `series-manifest.json` directly. Episode roots must equal `episodes/<id>`; episode IDs match `EP` plus at least three digits. Titles cannot be blank. Limit: 100 episodes, 5,000 archive entries, 512 MiB total decompressed data; split larger series into batches with distinct episode IDs. This is the classic flattened layout. Some newer importers additionally accept nested episode ZIPs under episodes/ and an optional wrapper. Verify the target implementation or inspect response before selecting that alternative; test both outer and child archive limits. Do not infer live acceptance from local support.

Each episode retains its existing full-movie Director manifest, version, `scene_packages/` structure, source and asset manifests. Resolve all asset and storyboard references within that episode, using the existing child importer rules. Asset files shared across episodes must retain identical canonical identity and stable handles; self-contained copies are intentional so each episode can also be exported/imported separately. Do not move child assets into an outer folder without a corresponding importer extension.

`POST /api/movies/{movie_id}/microdrama-series/inspect` validates the complete upload without importing it. `POST /api/movies/{movie_id}/import-microdrama-series` appends new episode scripts under the movie. Existing episodes remain present and the selected episode is retained. Script names are `<id>: <title>`. Collision and transaction behavior are version-dependent: implementations may reject duplicates, skip existing names for resume, or commit each episode separately. Inspect the deployed behavior and response. Skipped episodes are not refreshed. A local refresh_existing patch is unavailable live until deployed; never assume that form field is supported. Preserve episode IDs and takes during an authorized supported refresh. Storage writes can outlive failed transactions; do not claim atomicity or idempotent retries without evidence.

Two child checks fail most often. Each episode needs a non-empty `movie.movie` that the MovieScript parser accepts, and every `files` entry in its `asset-manifest.json` must name a file that exists at exactly that path inside the episode (for example `scene_packages/SC001_.../canonical_refs/assets/characters/hero.png`, or `assets/characters/hero.png` when the sheet is also stored at the episode root). Voice-only characters still need their declared file. A single standalone production, such as a commercial, can be delivered as a one-episode series (`EP001`) when the user imports through the series uploader.

The importer's structural pass validates child loading and production/segment models. It does not replace the skill's H3 attachment smoke test, asset completeness checks or visual inspection. Supply those evidence reports inside each episode before declaring the ZIP ready for generation.

For delivery and live checks, follow [import verification](../../../global/skills/director-pack-skills/references/import-verification.md).
