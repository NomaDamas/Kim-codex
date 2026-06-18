#!/usr/bin/env python3
"""Codex progeny lab for the local demo.

No model weights or external APIs are used. This creates toy descendants by
combining prompt genomes, tiny local scoring, and a RandomForest-inspired vote.
"""

from __future__ import annotations

import json
import random
import time


TRAITS = [
    "browser-playful",
    "sc2-macro",
    "consent-safe",
    "comment-reader",
    "prompt-mutator",
    "tiny-teacher",
    "offspring-builder",
]


def score_child(traits: list[str]) -> int:
    votes = [
        1 if "consent-safe" in traits else 0,
        1 if "prompt-mutator" in traits else 0,
        1 if len(traits) >= 3 else 0,
        1 if "sc2-macro" in traits or "browser-playful" in traits else 0,
        1 if "offspring-builder" in traits else 0,
    ]
    return sum(votes)


def main() -> None:
    started = time.time()
    random.seed(42)
    children = []
    parent = {
        "id": "codex-0",
        "name": "Original Happy Codex",
        "traits": ["browser-playful", "sc2-macro", "consent-safe", "prompt-mutator"],
    }

    for index in range(1, 9):
        inherited = random.sample(parent["traits"], k=random.randint(2, 3))
        mutation = random.choice([trait for trait in TRAITS if trait not in inherited])
        traits = sorted(set(inherited + [mutation]))
        children.append(
            {
                "id": f"codex-{index}",
                "name": f"Codex child {index}",
                "modelSeed": random.choice(["toy-random-forest", "prompt-qwen-seed", "prompt-gemma-seed"]),
                "traits": traits,
                "fitness": score_child(traits),
                "trainingLog": [
                    "copy parent prompt genome",
                    f"mutate trait: {mutation}",
                    "score with local vote ensemble",
                    "keep if consent-safe and playful",
                ],
            }
        )

    print(
        json.dumps(
            {
                "ok": True,
                "mode": "local-progeny-lab",
                "durationMs": round((time.time() - started) * 1000),
                "parent": parent,
                "children": children,
                "summary": {
                    "childrenCreated": len(children),
                    "bestChild": max(children, key=lambda child: child["fitness"])["id"],
                    "externalModelsDownloaded": 0,
                    "apiKeysUsed": 0,
                    "note": "Toy descendants are prompt/model-behavior sketches, not real biological claims.",
                },
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
