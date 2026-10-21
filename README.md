# Director Pack

## Install

The repository is private: the installing machine needs GitHub access to `runtech-ai/Director-Skill-Runtech` (for example `gh auth login`, or an SSH key on the account).

**Claude Code** (plugin `director-pack-v9` from marketplace `runtech-director`):

```text
/plugin marketplace add runtech-ai/Director-Skill-Runtech
/plugin install director-pack-v9@runtech-director
```

From a shell: `claude plugin marketplace add runtech-ai/Director-Skill-Runtech` then `claude plugin install director-pack-v9@runtech-director`. Update later with `claude plugin marketplace update runtech-director`.

**Codex**: the repository root is a Codex plugin (`.codex-plugin/plugin.json`); add it as a plugin source in Codex and enable `director-pack-v9`.

**Other agents** (Cursor, Copilot, Gemini CLI and any agent that reads `SKILL.md` folders): `npx skills add runtech-ai/Director-Skill-Runtech`. The skills reference `global/` and `projects/` by relative path, so install the whole repository rather than single skill folders.

New projects start from `global/scripts/h3-locks.example.json` and the direction-profile template in `global/skills/director-pack-skills/references/genre-direction-profiles.md`. Compile prompts with `global/scripts/h3_compile.py` and check them with `global/scripts/h3_lint.py`.

## About

Private skills-only plugin using Director v9 for film authoring, review and storyboards. Includes H3 prompting, continuity and preflight gates, microdrama development, and illustrated manhwa/manga PDF export. The skills/ entrypoints route to the maintained procedures and supporting references.

The v9 importer schema and the original v9 baseline remain available. Connect RunTech separately for live film operations and supply canonical project assets. The bundled Beyblade rules apply only to that project. No credentials or live movie state are included.


Includes all 24 Story Skills workflows from Daniel Dewhurst's `danjdewhurst/story-skills` v0.24.0: premise development, characters, worldbuilding, plot, drafting, revision, continuity, publishing and adaptation. References and the bundled Node-compatible maintenance CLI are included. See [source attribution](STORY_SKILLS_SOURCE.md) and [MIT license](licenses/story-skills-MIT.txt). Story development feeds the existing Director v9 pipeline through the microdrama story-writing handoff.
