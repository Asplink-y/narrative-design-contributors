#!/usr/bin/env python3
"""Lint branching dialogue JSON against the anti-patterns in references/dialogue-patterns.md.

Usage:
    python check_dialogue.py dialogue.json
    python check_dialogue.py dialogue.json --json
    python check_dialogue.py --self-test

Exit code: 0 clean, 1 findings, 2 bad input.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

QUESTION_WORDS = (
    "吗", "呢", "什么", "谁", "哪", "怎么", "为什么", "是不是", "有没有",
    "what", "who", "where", "when", "why", "how", "which", "do you", "is it",
)


def infer_kind(text: str, declared: str | None = None) -> str:
    """Return 'question' or 'statement' for one dialogue option."""
    if declared in ("question", "statement"):
        return declared
    stripped = text.strip()
    if stripped.endswith("?") or stripped.endswith("？"):
        return "question"
    lowered = stripped.lower()
    if any(word in lowered for word in QUESTION_WORDS):
        return "question"
    return "statement"


def count_exits(data: dict) -> int:
    total = 0
    for node in data.get("nodes", []):
        if node.get("is_exit"):
            total += 1
        for option in node.get("options", []):
            if option.get("is_exit"):
                total += 1
    return total


def lint(data: dict) -> list[dict]:
    findings: list[dict] = []
    nodes = data.get("nodes", [])
    if not isinstance(nodes, list) or not nodes:
        return [{"code": "SCHEMA", "message": "nodes must be a non-empty list"}]

    hubs = [node for node in nodes if node.get("type") == "hub"]

    counts = [len(node.get("options", [])) for node in hubs]
    if len(hubs) >= 2 and len(set(counts)) == 1 and counts[0] >= 2:
        findings.append({
            "code": "A-1",
            "message": (
                f"all {len(hubs)} hubs have exactly {counts[0]} options; "
                "vary count and ordering so players keep reading (P-4)"
            ),
        })

    stance_sequences = [
        tuple(o.get("stance") for o in node.get("options", []) if o.get("stance"))
        for node in hubs
    ]
    stance_sequences = [seq for seq in stance_sequences if len(seq) >= 2]
    if len(stance_sequences) >= 2 and len(set(stance_sequences)) == 1:
        findings.append({
            "code": "A-1",
            "message": "moral stance order repeats across hubs; rotate or remove stances (P-4)",
        })

    for node in nodes:
        kinds = [
            infer_kind(option.get("text", ""), option.get("kind"))
            for option in node.get("options", [])
        ]
        if "question" in kinds and "statement" in kinds:
            findings.append({
                "code": "A-2",
                "message": (
                    f"node '{node.get('id', '?')}' mixes questions with statements; "
                    "players will almost always pick the question (P-7)"
                ),
            })

    exits = count_exits(data)
    if exits > 2:
        findings.append({
            "code": "A-3",
            "message": f"{exits} exit points found; keep a small controlled number (P-5)",
        })
    elif exits == 0:
        findings.append({
            "code": "A-3",
            "message": "no explicit exit point found; players need a predictable way out (P-5)",
        })

    for check in data.get("checks", []):
        if check.get("type") != "red":
            continue
        label = check.get("node", "?")
        if check.get("retryable"):
            findings.append({
                "code": "A-5",
                "message": f"red check at '{label}' is retryable; red checks are one-shot (P-9)",
            })
        if not check.get("failure_advances"):
            findings.append({
                "code": "A-5",
                "message": f"red check at '{label}' has no advancing failure branch (P-9)",
            })
        if not check.get("reflection_option"):
            findings.append({
                "code": "A-7",
                "message": f"red check at '{label}' offers no reflection after failure (Q-6)",
            })

    seen: set[tuple[str, str]] = set()
    unique: list[dict] = []
    for finding in findings:
        key = (finding["code"], finding["message"])
        if key not in seen:
            seen.add(key)
            unique.append(finding)
    return unique


CLEAN_SAMPLE = {
    "title": "clean hub",
    "nodes": [
        {
            "id": "greeting",
            "type": "greeting",
            "is_exit": True,
            "options": [{"text": "Hello.", "kind": "statement", "leads_to": "hub"}],
        },
        {
            "id": "hub",
            "type": "hub",
            "options": [
                {"text": "I think you are hiding something.", "kind": "statement", "leads_to": "accuse"},
                {"text": "Leave.", "kind": "statement", "is_exit": True},
            ],
        },
        {
            "id": "origin",
            "type": "hub",
            "options": [
                {"text": "Tell me about the harbour.", "kind": "statement", "leads_to": "hub"},
                {"text": "Tell me about the strike.", "kind": "statement", "leads_to": "hub"},
                {"text": "Back.", "kind": "statement", "leads_to": "hub"},
            ],
        },
    ],
    "checks": [
        {"type": "red", "node": "accuse", "failure_advances": True, "reflection_option": True, "retryable": False},
        {"type": "white", "node": "origin", "retryable": True},
    ],
}

BROKEN_SAMPLE = {
    "title": "broken hub",
    "nodes": [
        {
            "id": "greeting",
            "type": "greeting",
            "is_exit": True,
            "options": [{"text": "Hello.", "kind": "statement", "leads_to": "hub"}],
        },
        {
            "id": "hub",
            "type": "hub",
            "options": [
                {"text": "Where are you from?", "kind": "question", "leads_to": "origin", "stance": "good"},
                {"text": "I think you are lying.", "kind": "statement", "leads_to": "accuse", "stance": "neutral"},
                {"text": "Leave.", "kind": "statement", "is_exit": True, "stance": "evil"},
            ],
        },
        {
            "id": "origin",
            "type": "hub",
            "options": [
                {"text": "What happened?", "kind": "question", "leads_to": "hub", "stance": "good"},
                {"text": "That sounds unlikely.", "kind": "statement", "leads_to": "hub", "stance": "neutral"},
                {"text": "Forget it.", "kind": "statement", "is_exit": True, "stance": "evil"},
            ],
        },
    ],
    "checks": [
        {"type": "red", "node": "accuse", "failure_advances": False, "reflection_option": False, "retryable": True},
    ],
}


def self_test() -> int:
    clean = {f["code"] for f in lint(CLEAN_SAMPLE)}
    broken = {f["code"] for f in lint(BROKEN_SAMPLE)}
    expected = {"A-1", "A-2", "A-3", "A-5", "A-7"}
    if clean:
        print(f"FAIL: clean sample produced findings: {sorted(clean)}", file=sys.stderr)
        return 1
    if broken != expected:
        print(f"FAIL: broken sample produced {sorted(broken)}, expected {sorted(expected)}", file=sys.stderr)
        return 1
    print("self-test OK: 5 rule families triggered on the broken sample, 0 on the clean sample")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Lint branching dialogue JSON for narrative-design anti-patterns")
    parser.add_argument("path", nargs="?", help="path to a dialogue JSON file")
    parser.add_argument("--self-test", action="store_true", help="run built-in fixtures instead of a file")
    parser.add_argument("--json", action="store_true", help="emit findings as JSON")
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()
    if not args.path:
        parser.error("provide a dialogue JSON file or --self-test")

    try:
        data = json.loads(Path(args.path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if not isinstance(data, dict):
        print("error: top-level JSON value must be an object", file=sys.stderr)
        return 2

    findings = lint(data)
    if args.json:
        print(json.dumps(findings, ensure_ascii=False, indent=2))
    elif findings:
        for finding in findings:
            print(f"[{finding['code']}] {finding['message']}")
        print(f"\n{len(findings)} finding(s)")
    else:
        print("OK: no anti-patterns detected")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
