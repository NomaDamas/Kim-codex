#!/usr/bin/env python3
"""Local python-sc2 adapter for the Happy Codex demo.

The script proves that python-sc2 can be imported and emits a deterministic
computer-use style bot loop. If a full StarCraft II binary/map environment is
not available, it returns a fallback play trace instead of failing the demo.
"""

from __future__ import annotations

import json
import random
import time


def main() -> None:
    started = time.time()
    random.seed(7)

    try:
        import sc2  # type: ignore

        sc2_status = {
            "installed": True,
            "module": getattr(sc2, "__file__", "unknown"),
        }
    except Exception as exc:  # pragma: no cover - depends on local machine
        sc2_status = {
            "installed": False,
            "error": str(exc),
        }

    actions = [
        "00:01 launch python-sc2 adapter",
        "00:04 choose Zerg macro personality: lazy but happy",
        "00:09 queue drone production",
        "00:16 send overlord scout across safe route",
        "00:22 mark enemy natural as unknown",
        "00:31 inject larva and spread creep",
        "00:44 hold ramp with queens",
        "00:58 stabilize two-base economy",
    ]
    minerals = 50
    larvae = 3
    apm = 84
    frames = []

    for index, action in enumerate(actions, start=1):
        minerals += random.randint(18, 42)
        larvae = max(0, larvae + random.choice([-1, 0, 1]))
        apm += random.randint(-4, 7)
        frames.append(
            {
                "step": index,
                "action": action,
                "minerals": minerals,
                "larvae": larvae,
                "apm": apm,
            }
        )

    mode = "python-sc2-adapter"
    note = "python-sc2 import verified; emitted local bot loop trace."
    if not sc2_status["installed"]:
        mode = "fallback-simulation"
        note = "python-sc2 import failed; fallback trace kept the demo running."

    print(
        json.dumps(
            {
                "ok": True,
                "mode": mode,
                "note": note,
                "sc2": sc2_status,
                "durationMs": round((time.time() - started) * 1000),
                "frames": frames,
                "summary": {
                    "race": "Zerg",
                    "strategy": "two-base macro into safe scout",
                    "realGameLaunched": False,
                    "reason": "Hackathon demo runs without maps, login, secrets, or external dependencies.",
                },
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
