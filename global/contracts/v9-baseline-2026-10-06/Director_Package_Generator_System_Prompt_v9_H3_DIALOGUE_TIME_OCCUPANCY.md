# Director Package Generator System Prompt v9 — H3 Dialogue-Time Occupancy

This file is the stable compatibility entrypoint referenced by
`global/skills/director-pack-skills/SKILL.md`.

The normative contract is composed by the following repository files. Read each
one completely before creating or validating a Director package:

1. `global/skills/director-pack-skills/references/package-schema.md`
2. `global/skills/director-pack-skills/references/v9-hardening-lock.md`
3. `global/skills/director-pack-skills/references/validation.md`
4. `global/skills/director-pack-skills/references/h3-prompt-validation.md`

All constraints in those files are binding. In particular, a final package must
use the `movie-director-result` / `3.1-shotplan-only` identity, preserve exact
dialogue-time occupancy, validate compiled H3 prompts, close all referenced
assets, and fail closed when any required field or packaged dependency is
missing.
