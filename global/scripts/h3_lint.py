#!/usr/bin/env python3
"""Lint compiled H3 prompts for the patterns that make takes look like AI shot-to-shot.

Checks the six-section structure, word budget, repeated or lock-heavy text,
default or repeated camera language, same-framing cuts and crowded dialogue
shots. FAIL blocks handoff; WARN needs a written reason in the segment notes.

Usage: h3_lint.py prompts/SEG_*_prompt_bundle.json [...]
"""
import json
import re
import sys
from pathlib import Path

SECTIONS = ["subject_definitions:", "summary:", "retention_analysis:", "detailed_description:",
            "overall_soundscape:", "non_diegetic_music:"]
# v9 per-shot locks that are required to repeat.
CONTRACT_REPEATS = ("no spoken words occur", "visible characters keep their lips closed", "exactly ")
LOCK_WORDS = re.compile(r"\b(?:LOCK|never|must not|do not|does not|no longer|preserve|remains? (?:exactly|unchanged)|exactly \d)\b", re.I)
SIZE_MODIFIERS = re.compile(r"\b(?:slightly|a little|marginally|lower|higher|tighter|wider|closer|looser|similar)\b", re.I)
WORD_WARN, WORD_FAIL, LOCK_RATIO_FAIL = 500, 700, 0.25


def shots_of(description):
    parts = re.split(r"(?=\[Shot \d+\])", description)
    return [p.strip() for p in parts if p.strip().startswith("[Shot")]


def framing_of(shot_text):
    m = re.match(r"\[Shot \d+\](?: At [\d:.]+, the camera cuts to| (?:An?|The))\s*(?:an? )?(.*?)(?: opens the sequence)?\.", shot_text)
    return SIZE_MODIFIERS.sub("", m.group(1)).strip().lower() if m else ""


def lint(prompt):
    issues = []
    add = lambda level, msg: issues.append({"level": level, "issue": msg})
    pos = [prompt.find(s) for s in SECTIONS]
    if -1 in pos or pos != sorted(pos):
        add("FAIL", "six H3 sections missing or out of order")
        return issues
    desc = prompt[pos[3] + len(SECTIONS[3]):pos[4]].strip()
    spoken = " ".join(re.findall(r"<d>.*?</d>", desc))
    words = len(desc.split()) - len(spoken.split())
    if words > WORD_FAIL:
        add("FAIL", f"detailed_description is {words} words excluding dialogue (limit {WORD_FAIL}; official guide 350-500)")
    elif words > WORD_WARN:
        add("WARN", f"detailed_description is {words} words excluding dialogue (official guide 350-500)")
    if re.search(r"\b[A-Z]{3,}(?: [A-Z]{2,})* LOCK\b|LOCK:", prompt):
        add("FAIL", "upper-case LOCK field-dump language in the prompt")
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", re.sub(r"<d>.*?</d>", "", desc)) if len(s) > 25]
    seen = {}
    for s in sentences:
        key = re.sub(r"\W+", " ", s.lower()).strip()
        if key.startswith(CONTRACT_REPEATS):
            continue
        seen[key] = seen.get(key, 0) + 1
    for key, count in seen.items():
        if count > 1:
            add("FAIL", f"sentence repeated {count}x: '{key[:70]}...'")
    lock_words = sum(len(s.split()) for s in sentences if LOCK_WORDS.search(s))
    total = sum(len(s.split()) for s in sentences) or 1
    if lock_words / total > LOCK_RATIO_FAIL:
        add("FAIL", f"{lock_words / total:.0%} of the description is restriction text (limit {LOCK_RATIO_FAIL:.0%}); move invariants to retention_analysis")
    shots = shots_of(desc)
    pushes = 0
    for i, shot in enumerate(shots, 1):
        if not re.search(r"\bcamera (?!cuts\b)", shot, re.I):
            add("FAIL", f"Shot {i} has no camera sentence")
        if re.search(r"nearly static|almost static", shot, re.I):
            add("FAIL", f"Shot {i} uses the default 'nearly static' camera; choose a static shot or a move and say why")
        if re.search(r"camera (?:slowly )?push(?:es)? (?:in|inward|toward)", shot, re.I):
            pushes += 1
        lines = re.findall(r"<d>", shot)
        speakers = set(re.findall(r"\((S\d+)\)[^<]*?says", shot))
        if len(lines) >= 3:
            add("FAIL", f"Shot {i} holds {len(lines)} dialogue lines; give the exchange shot/reverse-shot coverage")
        elif len(speakers) > 1:
            add("WARN", f"Shot {i} holds lines from {len(speakers)} speakers in one framing; cover the listener or justify the two-shot")
        if i > 1 and framing_of(shot) and framing_of(shot) == framing_of(shots[i - 2]):
            add("FAIL", f"Shot {i} cuts to the same framing as Shot {i - 1} ('{framing_of(shot)}'); move the camera instead or change angle/size")
    if pushes > 1:
        add("WARN", f"{pushes} slow push-ins in one segment; vary the camera grammar")
    if len(shots) > 1 and all(re.search(r"camera (?:holds|remains) (?:a )?static", s, re.I) for s in shots):
        add("WARN", "every shot is static; confirm the scene's camera plan chose this")
    return issues


def main():
    report, failed = {}, False
    for name in sys.argv[1:]:
        data = json.loads(Path(name).read_text())
        prompt = data.get("shot_planning_prompt", data).get("compiled_prompt", "")
        issues = lint(prompt)
        failed |= any(i["level"] == "FAIL" for i in issues)
        report[name] = issues or "PASS"
    print(json.dumps({"valid": not failed, "prompts": report}, indent=2))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
