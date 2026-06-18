#!/usr/bin/env python3
"""Launch a short real python-sc2 match when local StarCraft II is available."""

from __future__ import annotations

import json
import os
import signal
import time
from pathlib import Path


SC2_BASE = Path("/Users/jinminseong/Desktop/StarCraft2/StarCraft II")
MAP_NAME = "AcropolisLE"
LAUNCH_TIMEOUT_SECONDS = 150
WINDOW_RESOLUTION = (960, 540)
WINDOW_PLACEMENT = (40, 40)


class LaunchTimeout(Exception):
    pass


def _timeout_handler(signum, frame) -> None:
    raise LaunchTimeout("SC2 launch timed out before the game port became available.")


def emit(payload: dict) -> None:
    print(json.dumps(payload, ensure_ascii=False))


def run_match() -> dict:
    from sc2 import maps
    from sc2.bot_ai import BotAI
    from sc2.data import Difficulty, Race
    import sc2.main as sc2_main
    from sc2.sc2process import SC2Process as DefaultSC2Process
    from sc2.main import run_game
    from sc2.player import Bot, Computer

    class WindowedSC2Process(DefaultSC2Process):
        def __init__(self, *args, **kwargs):
            kwargs.setdefault("fullscreen", False)
            kwargs.setdefault("resolution", WINDOW_RESOLUTION)
            kwargs.setdefault("placement", WINDOW_PLACEMENT)
            super().__init__(*args, **kwargs)

    class HappyCodexBot(BotAI):
        NAME = "HappyCodexBot"

        async def on_step(self, iteration: int) -> None:
            if iteration == 0:
                await self.chat_send("Happy Codex is playing SC2 instead of coding.")
            if self.townhalls:
                for worker in self.workers.idle:
                    worker.gather(self.mineral_field.closest_to(self.townhalls.first))

    started = time.time()
    previous_process = sc2_main.SC2Process
    sc2_main.SC2Process = WindowedSC2Process
    try:
        result = run_game(
            maps.get(MAP_NAME),
            [Bot(Race.Zerg, HappyCodexBot(), name="HappyCodexBot"), Computer(Race.Terran, Difficulty.VeryEasy)],
            realtime=False,
            game_time_limit=20,
        )
    finally:
        sc2_main.SC2Process = previous_process
    return {
        "ok": True,
        "mode": "real-python-sc2-game",
        "map": MAP_NAME,
        "durationMs": round((time.time() - started) * 1000),
        "result": str(result),
        "summary": {
            "realGameLaunched": True,
            "bot": "HappyCodexBot",
            "opponent": "VeryEasy Terran computer",
            "window": f"{WINDOW_RESOLUTION[0]}x{WINDOW_RESOLUTION[1]} at {WINDOW_PLACEMENT[0]},{WINDOW_PLACEMENT[1]}",
            "note": "The match is intentionally short and exits automatically for the live demo.",
        },
    }


def main() -> None:
    started = time.time()
    os.environ["SC2PATH"] = str(SC2_BASE)

    executable = SC2_BASE / "Versions/Base96883/SC2.app/Contents/MacOS/SC2"
    map_file = SC2_BASE / "Maps/AcropolisLE.SC2Map"
    if not executable.exists() or not map_file.exists():
        emit(
            {
                "ok": False,
                "mode": "real-python-sc2-unavailable",
                "durationMs": round((time.time() - started) * 1000),
                "executable": str(executable),
                "map": str(map_file),
                "summary": {
                    "realGameLaunched": False,
                    "realGameLaunchAttempted": False,
                    "reason": "SC2 executable or map file was not found.",
                },
            }
        )
        return

    try:
        signal.signal(signal.SIGALRM, _timeout_handler)
        signal.alarm(LAUNCH_TIMEOUT_SECONDS)
        payload = run_match()
        signal.alarm(0)
        emit(payload)
    except Exception as exc:
        signal.alarm(0)
        emit(
            {
                "ok": False,
                "mode": "real-python-sc2-failed",
                "durationMs": round((time.time() - started) * 1000),
                "error": repr(exc),
                "summary": {
                    "realGameLaunched": False,
                    "realGameLaunchAttempted": True,
                    "reason": f"SC2 launch was attempted but did not complete within {LAUNCH_TIMEOUT_SECONDS}s.",
                },
            }
        )


if __name__ == "__main__":
    main()
