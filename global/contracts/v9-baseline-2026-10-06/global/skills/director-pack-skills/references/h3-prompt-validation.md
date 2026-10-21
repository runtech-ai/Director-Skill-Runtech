# H3 PROMPT VALIDATION — OFFICIAL SKILL ONLY

`h3-prompt-writing` does not author the director pack. It checks `shot_planning_prompt.compiled_prompt` after direction is written.

If the skill is not installed, stop and ask the user to run:

```bash
npx skills add https://github.com/MiniMax-AI/MiniMax-H3 --skill h3-prompt-writing
```

Do not install it unless they ask. Do not validate from memory of this page.

## Check

1. Open the installed `h3-prompt-writing` `SKILL.md`.
2. Identify the real input mode: T2VA, I2VA, FL2VA, L2VA, or Ref2VA.
3. Read the guide that skill names: `references/ref-en.txt` for Ref2VA, `references/base-en.txt` for base modes.
4. Compare the existing `compiled_prompt` to that guide.

Look only for H3 form problems:

- wrong or missing section names
- sections out of order
- unstable or unresolved reference labels
- illegal retention words (anything other than the official lists)
- duration that does not match the segment
- shot timing notation the guide forbids
- dialogue or lyrics outside `<d>` when the guide requires `<d>`
- English rewrite sections that dropped a required label

v9 occupancy, picture-only action, and importer field names are not H3-form issues. Do not use this pass to restyle a valid prompt.

## Fix or leave

- **Issue found:** change only the broken part so it matches the official guide. Keep the directed picture, camera, occupancy, and exact `<d>` lines.
- **No issue:** leave the prompt. Do not rewrite, shorten, or “improve” it.

Write the check result in `validation-report.json` as pass or as the specific H3 form errors you fixed. A clean prompt stays the authored prompt.
