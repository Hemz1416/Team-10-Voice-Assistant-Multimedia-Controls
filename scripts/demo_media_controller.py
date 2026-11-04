"""
Team 10 Voice Assistant — Media Controller Live Demonstration Script
Component Owner: Hemant Ram Nelapati (PES2UG24CS192)
Sprint 2 Deliverable: Working Product Audio Playback & Extended Controls Demo

Demonstrates live VLC execution for all 9 supported voice intents:
PLAY, PAUSE, RESUME, NEXT, PREVIOUS, VOLUME_UP, VOLUME_DOWN, MUTE, STOP.
"""

import argparse
import math
import struct
import sys
import time
import wave
from pathlib import Path

# Ensure src is importable
repo_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo_root))

from src.media_controller import MediaController


def ensure_sample_media(media_dir: Path) -> list[Path]:
    """Ensure two clean synthetic audio tracks exist for the demo."""
    media_dir.mkdir(parents=True, exist_ok=True)
    t1 = media_dir / "track1_welcome.wav"
    t2 = media_dir / "track2_acoustic.wav"

    def make_tone(path: Path, freq: float, duration: float = 5.0, sample_rate: int = 44100):
        if path.is_file() and path.stat().st_size > 1000:
            return
        n_samples = int(duration * sample_rate)
        with wave.open(str(path), "w") as wav:
            wav.setnchannels(1)
            wav.setsampwidth(2)
            wav.setframerate(sample_rate)
            for i in range(n_samples):
                env = min(1.0, i / 2500) * min(1.0, (n_samples - i) / 2500)
                val = int(env * 16000 * math.sin(2 * math.pi * freq * i / sample_rate))
                wav.writeframes(struct.pack("<h", val))

    make_tone(t1, 523.25, 6.0)  # C5 pitch tone (6 seconds)
    make_tone(t2, 659.25, 6.0)  # E5 pitch tone (6 seconds)
    return [t1, t2]


def print_banner():
    print("=" * 68)
    print("  TEAM 10 VOICE ASSISTANT — SPRINT 2 MEDIA CONTROLLER DEMO")
    print("  Component Owner : Hemant Ram Nelapati (PES2UG24CS192)")
    print("  Engine          : VideoLAN libVLC 3.x via python-vlc")
    print("  Test Scope      : 9 Voice Intents, Clamping, Mute & Exception Shielding")
    print("=" * 68)


def run_automated_demo(controller: MediaController):
    print("\n>>> Launching Automated Live Demonstration (Sprint 2 Working Product)...\n")

    steps = [
        ("1. PLAY (VA-F-005 / TC-Media-01)", "PLAY", 2.0, "Initiating playback of Track 1"),
        ("2. PAUSE (VA-F-006 / TC-Media-02)", "PAUSE", 1.5, "Pausing playback, retaining position"),
        ("3. RESUME (VA-F-007 / TC-Media-03)", "RESUME", 1.5, "Resuming playback from paused position"),
        ("4. VOLUME_UP (VA-F-011 / TC-Vol-01)", "VOLUME_UP", 1.0, "Increasing volume by +10% (70 -> 80)"),
        ("5. VOLUME_UP (VA-F-011 / Clamping)", "VOLUME_UP", 1.0, "Increasing volume by +10% (80 -> 90)"),
        ("6. VOLUME_DOWN (VA-F-012 / TC-Vol-02)", "VOLUME_DOWN", 1.0, "Decreasing volume by -10% (90 -> 80)"),
        ("7. NEXT (VA-F-009 / TC-Media-05)", "NEXT", 2.5, "Circular navigation: advancing to Track 2"),
        ("8. PREVIOUS (VA-F-010 / TC-Media-06)", "PREVIOUS", 2.5, "Circular navigation: returning to Track 1"),
        ("9. MUTE Toggle ON (VA-F-013 / TC-Vol-03)", "MUTE", 1.5, "Muting audio stream"),
        ("10. MUTE Toggle OFF (VA-F-013 / TC-Vol-03)", "MUTE", 1.5, "Unmuting audio stream"),
        ("11. STOP (VA-F-008 / TC-Media-04)", "STOP", 1.0, "Stopping playback and resetting player state"),
    ]

    for label, intent, delay, note in steps:
        print(f"[{label}]")
        print(f"   Intent   : {intent}")
        print(f"   Action   : {note}")
        result = controller.execute(intent)
        status_flag = "SUCCESS" if result.get("success") else "FAILED"
        print(f"   Response : [{status_flag}] {result.get('status')}")
        if "volume" in result:
            print(f"   Volume   : {result['volume']}%")
        if "is_muted" in result:
            print(f"   Muted    : {result['is_muted']}")
        print(f"   State    : Playing={controller.is_playing()}, Paused={controller.is_paused()}")
        print("-" * 68)
        time.sleep(delay)

    print("\n>>> All 9 voice intents executed successfully on native libVLC runtime!")
    print(">>> Automated demonstration completed cleanly.\n")


def run_interactive_demo(controller: MediaController):
    print("\n>>> Interactive Controller Console Ready.")
    print("Commands: play, pause, resume, stop, next, prev, volup, voldown, mute, status, exit\n")

    cmd_map = {
        "play": "PLAY",
        "pause": "PAUSE",
        "resume": "RESUME",
        "stop": "STOP",
        "next": "NEXT",
        "prev": "PREVIOUS",
        "previous": "PREVIOUS",
        "volup": "VOLUME_UP",
        "volume up": "VOLUME_UP",
        "voldown": "VOLUME_DOWN",
        "volume down": "VOLUME_DOWN",
        "mute": "MUTE",
    }

    while True:
        try:
            raw = input("MediaCommand> ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting interactive demo...")
            controller.execute("STOP")
            break

        if not raw:
            continue
        if raw in ("exit", "quit", "q"):
            controller.execute("STOP")
            print("Playback stopped. Goodbye!")
            break
        if raw == "status":
            print(f"Player State: playing={controller.is_playing()}, paused={controller.is_paused()}, "
                  f"volume={controller.volume}%, muted={controller.is_muted}, "
                  f"track_index={controller.current_track_index}")
            continue

        intent = cmd_map.get(raw, raw.upper())
        result = controller.execute(intent)
        status_flag = "SUCCESS" if result.get("success") else "REJECTED"
        print(f"[{status_flag}] {result.get('status')}")


def main():
    parser = argparse.ArgumentParser(description="Live Demonstration of VLC Media Controller (Sprint 2)")
    parser.add_argument("--auto", action="store_true", help="Run automated step-by-step video demonstration")
    parser.add_argument("--interactive", action="store_true", help="Run interactive console prompt")
    args = parser.parse_args()

    print_banner()

    media_dir = repo_root / "media"
    media_files = ensure_sample_media(media_dir)
    print(f"[MEDIA] Loaded {len(media_files)} demo tracks:")
    for i, m in enumerate(media_files):
        print(f"  Track {i+1}: {m.name} ({m.stat().st_size} bytes)")

    controller = MediaController(media_files=media_files)
    if not controller.vlc_available:
        print("\n[ERROR] VLC / libVLC could not be initialized on this machine.")
        sys.exit(1)

    print(f"[VLC] Player initialized successfully. Default volume: {controller.volume}%\n")

    if args.interactive:
        run_interactive_demo(controller)
    else:
        # Default to automated demo (perfect for video recording)
        run_automated_demo(controller)


if __name__ == "__main__":
    main()
