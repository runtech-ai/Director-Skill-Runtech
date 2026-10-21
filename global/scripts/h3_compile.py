#!/usr/bin/env python3
"""Compile one Director v9 segment into a six-section H3 Ref2VA prompt.

Direction comes from the segment's micro-shots (framing, composition, action,
camera, sound) and structured dialogue. Project invariants come from a locks
file and are stated once: identity/wardrobe in retention_analysis, style and
setting before or at their first appearance, object-state locks only on the
shot where that state first applies. Nothing is repeated per shot except the
v9 occupancy and silence locks, which are per-shot by contract.

Usage:
  h3_compile.py --segment segments/SEG.json --bundle prompts/SEG_prompt_bundle.json \
      --locks projects/<project>/h3/h3-locks.json [--write]
"""
import argparse
import json
import re
from pathlib import Path


def sentence(text):
    text = re.sub(r"\s+", " ", str(text or "")).strip()
    if text and text[-1] not in ".!?":
        text += "."
    return text


def split_sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]


def article(phrase):
    return ("an " if phrase[:1].lower() in "aeiou" else "a ") + phrase


def stamp(seconds):
    minutes, rest = divmod(float(seconds), 60)
    return f"{int(minutes):02}:{rest:06.3f}"


class Compiler:
    def __init__(self, segment, bundle, locks):
        self.segment = segment
        self.shots = segment["microShots"]
        self.refs = bundle["canonical_references"]
        self.locks = locks
        self.subject = {r["entity"]: r["subject"] for r in self.refs}
        self.picture = {r["entity"]: r["picture"] for r in self.refs}
        self.humans = set(locks.get("humans", []))
        dialogue = sorted(segment.get("dialogue", []), key=lambda d: d["start"])
        self.dialogue = dialogue
        self.speaker_id = {h: i + 1 for i, h in enumerate(dict.fromkeys(d["speaker"] for d in dialogue))}
        self.emitted_locks = set()

    def label(self, text):
        """Replace @handles and declared names with their Subject labels."""
        names = self.locks.get("names", {})
        for handle in sorted(self.subject, key=len, reverse=True):
            for alias in [handle, *names.get(handle, [])]:
                text = re.sub(r"(?<![\w@<])" + re.escape(alias) + r"(?![\w>])", self.subject[handle], text, flags=re.I)
        return text

    def occupied(self, shot):
        return [d for d in self.dialogue if d["start"] < shot["segmentEnd"] and d["end"] > shot["segmentStart"]]

    def first_and_last(self, line):
        hits = [s for s in self.shots if line["start"] < s["segmentEnd"] and line["end"] > s["segmentStart"]]
        return hits[0]["id"], hits[-1]["id"]

    def subject_definitions(self):
        defs = self.locks.get("subjects", {})
        out = []
        for r in self.refs:
            entity = r["entity"]
            body = defs.get(entity, {}).get("definition") or f"{entity}, {r.get('authority', 'asset identity and design')}"
            role = r.get("authority", "identity and design").split(" for ")[0]
            out.append(f"{r['subject']} is {body} from {r['picture']}, used for {role} and design.")
        return "\n".join(out)

    def retention(self):
        defs = self.locks.get("subjects", {})
        out = []
        for r in self.refs:
            shots = [f"[Shot {s['displayShot']}]" for s in self.shots if r["entity"] in s.get("visibleAssets", [])]
            if not shots:
                continue
            keep = defs.get(r["entity"], {}).get("retain", "the defined identity and design remain consistent")
            out.append(f"{r['subject']} (appears in {', '.join(shots)}): fully_preserved - {sentence(keep)[:-1]}; each shot controls pose, action and state.")
        return "\n".join(out)

    def setting(self, shot, previous):
        handle = shot.get("locationHandle")
        if not handle or (previous and previous.get("locationHandle") == handle):
            return ""
        place = self.locks.get("settings", {}).get(handle, {})
        scene = place.get("byScene", {}).get(self.segment["sceneId"], "")
        label = self.subject.get(handle, handle)
        text = " ".join(x for x in [f"The setting is {label}, {place.get('geography', 'as referenced')}.", sentence(scene)] if x.strip("."))
        return self.label(text)

    def state_locks(self, shot):
        out = []
        visible = set(shot.get("visibleAssets", []))
        states = shot.get("objectStates", {})
        for lock in self.locks.get("stateLocks", []):
            obj = lock["object"]
            if obj not in visible or states.get(obj) != lock["state"]:
                continue
            key = (obj, lock["state"])
            if key in self.emitted_locks:
                continue
            self.emitted_locks.add(key)
            out.append(self.label(lock["text"]))
        return out

    def speech(self, shot, people):
        out = []
        for line in self.occupied(shot):
            first, last = self.first_and_last(line)
            voice = self.locks.get("voices", {}).get(line["speaker"])
            who = self.subject.get(line["speaker"]) or voice or line["speaker"]
            sid = f"(S{self.speaker_id[line['speaker']]})"
            if first == shot["id"]:
                manner = f", {line['delivery']}," if line.get("delivery") else ""
                if line["speaker"] in shot.get("visibleAssets", []):
                    out.append(f"{who} {sid} says{manner} <d>[{line.get('language', 'English')}] {line['text']}</d>")
                    listeners = [p for p in people if p != line["speaker"]]
                    if listeners:
                        out.append(" and ".join(self.subject[p] for p in listeners) + " listens with lips closed.")
                else:
                    # Voiceover or off-screen speaker: no visible mouth carries the line.
                    kind = "in voiceover" if voice else "off-screen"
                    out.append(f"{who} {sid} says {kind}{manner} <d>[{line.get('language', 'English')}] {line['text']}</d>")
                    if people:
                        out.append("Visible characters keep their lips closed during the voiceover." if voice else
                                   " and ".join(self.subject[p] for p in people) + " keeps lips closed.")
            if last == shot["id"] and line["speaker"] in shot.get("visibleAssets", []):
                out.append(f"{who} closes their lips after the line.")
        return out

    def shot_prose(self, shot, previous):
        n = shot["displayShot"]
        framing = self.label(shot["framing"])
        cut = f"[Shot 1] {article(framing)[0].upper() + article(framing)[1:]} opens the sequence." if n == 1 else \
            f"[Shot {n}] At {stamp(shot['segmentStart'])}, the camera cuts to {article(framing)}."
        people = [a for a in shot.get("visibleAssets", []) if a in self.humans]
        parts = [cut]
        if self.dialogue and not self.occupied(shot):
            parts.append("No spoken words occur in this shot. Visible characters keep their lips closed.")
        if len(people) > 1:
            parts.append(f"Exactly {len(people)} distinct human characters are visible: " + " and ".join(self.subject[p] for p in people) + ".")
        parts.append(self.setting(shot, previous))
        parts.append(self.label(sentence(shot.get("composition", ""))))
        parts.append(self.label(sentence(shot.get("action", ""))))
        parts.extend(self.speech(shot, people))
        parts.append(self.label(sentence(shot.get("camera", ""))))
        if shot.get("sound"):
            parts.append(self.label(sentence(shot["sound"])))
        parts.extend(self.state_locks(shot))
        text = " ".join(p for p in parts if p)
        return text

    def compile(self):
        style = " ".join(sentence(s) for s in self.locks.get("style", []))
        prose, seen, previous = [], set(), None
        for shot in self.shots:
            kept = []
            for s in split_sentences(self.shot_prose(shot, previous)):
                key = re.sub(r"\W+", " ", s.lower()).strip()
                # Per-shot v9 locks may repeat; any other sentence is stated once.
                if key in seen and not key.startswith(("no spoken words", "visible characters keep", "exactly ")):
                    continue
                seen.add(key)
                kept.append(s)
            prose.append(" ".join(kept))
            previous = shot
        summary = self.label(sentence(self.segment.get("summary") or self.segment.get("purpose", "")))
        ambience = self.label(sentence(self.locks.get("ambience", {}).get(self.segment["sceneId"], "")))
        music = self.segment.get("musicPlan") or "N/A"
        medium = self.locks.get("medium", "").strip()
        kind = f"{medium} sequence" if medium else "sequence"
        return (
            f"subject_definitions:\n{self.subject_definitions()}\n\n"
            f"summary:\n[reference generation] A {self.segment['duration']}-second {len(self.shots)}-shot {kind}: {summary}\n\n"
            f"retention_analysis:\n{self.retention()}\n\n"
            f"detailed_description:\n{style}\n" + "\n".join(prose) + "\n\n"
            f"overall_soundscape:\n{ambience or 'Quiet room tone continues throughout.'}\n\n"
            f"non_diegetic_music:\n{music}"
        )


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--segment", required=True, type=Path)
    ap.add_argument("--bundle", required=True, type=Path)
    ap.add_argument("--locks", required=True, type=Path)
    ap.add_argument("--write", action="store_true", help="write compiled_prompt into the bundle and its shot_plan.txt")
    args = ap.parse_args()
    segment = json.loads(args.segment.read_text())
    bundle = json.loads(args.bundle.read_text())
    locks = json.loads(args.locks.read_text())
    prompt = Compiler(segment, bundle, locks).compile()
    if not args.write:
        print(prompt)
        return
    bundle["shot_planning_prompt"]["compiled_prompt"] = prompt
    args.bundle.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n")
    plan = args.bundle.with_name(args.bundle.name.replace("_prompt_bundle.json", "_shot_plan.txt"))
    plan.write_text(prompt + "\n")
    print(f"wrote {args.bundle} and {plan.name}")


if __name__ == "__main__":
    main()
