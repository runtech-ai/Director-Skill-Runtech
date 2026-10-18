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

Manifest order is episode order. IDs and roots must be unique. ZIP root must contain `series-manifest.json` directly. Episode roots must equal `episodes/<id>`; episode IDs match `EP` plus at least three digits. Titles cannot be blank. Limit: 100 episodes, 5,000 archive entries, 512 MiB total decompressed data; split larger series into batches with distinct episode IDs. Nested ZIP files are not used.

Each episode retains its existing full-movie Director manifest, version, `scene_packages/` structure, source and asset manifests. Resolve all asset and storyboard references within that episode, using the existing child importer rules. Asset files shared across episodes must retain identical canonical identity and stable handles; self-contained copies are intentional so each episode can also be exported/imported separately. Do not move child assets into an outer folder without a corresponding importer extension.

`POST /api/movies/{movie_id}/microdrama-series/inspect` validates the complete upload without importing it. `POST /api/movies/{movie_id}/import-microdrama-series` appends new episode scripts under the movie. Existing episodes remain present and the selected episode is retained. Script names are `<id>: <title>`; a collision returns HTTP 409 rather than overwriting an episode. Import all relational rows in one transaction; storage uploads are outside that transaction and failed imports may leave unreferenced objects. Do not claim storage-level atomicity or idempotent retry support.

The importer's structural pass validates child loading and production/segment models. It does not replace the skill's H3 attachment smoke test, asset completeness checks or visual inspection. Supply those evidence reports inside each episode before declaring the ZIP ready for generation.
