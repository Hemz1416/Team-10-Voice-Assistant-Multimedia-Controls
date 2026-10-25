
"""Continuous voice integration for the Team 10 multimedia assistant."""

import argparse
from pathlib import Path

from src.command_service import execute_validated_command
from src.command_validator import validate_command
from src.intent_processor import detect_intent
from src.media_controller import MediaController
from src.speech_input import SpeechInput


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Voice-controlled multimedia assistant"
    )
    parser.add_argument(
        "media",
        nargs="+",
        help="Paths to audio files for the VLC playlist",
    )
    args = parser.parse_args()

    media_files = [Path(path) for path in args.media]

    missing_files = [path for path in media_files if not path.is_file()]
    if missing_files:
        print("ERROR: These media files do not exist:")
        for path in missing_files:
            print(f"  {path}")
        return 1

    controller = MediaController(media_files=media_files)

    if not controller.vlc_available:
        print("ERROR: VLC could not be initialized.")
        return 1

    try:
        speech = SpeechInput()
    except (FileNotFoundError, OSError) as exc:
        print(f"ERROR: Could not initialize speech input: {exc}")
        return 1

    print("Voice assistant ready.")
    print("Speak a command after each listening prompt.")
    print("Press Ctrl+C to exit.")

    try:
        while True:
            try:
                recognition = speech.listen_and_transcribe()
            except (OSError, RuntimeError) as exc:
                print(f"ERROR: Microphone input failed: {exc}")
                continue

            text = recognition.get("text", "")
            confidence = recognition.get("confidence")

            if not isinstance(text, str) or not text.strip():
                print("REJECTED: No speech recognized.")
                continue

            print(f"Recognized command: {text}")
            print(f"Recognition confidence: {confidence}")

            intent_result = detect_intent(text)
            validation = validate_command(
                intent_result,
                confidence,
                minimum_confidence=0.70,
            )

            if not validation.allowed:
                print(f"REJECTED: {validation.reason}")
                continue

            result = execute_validated_command(validation, controller)
            label = "SUCCESS" if result.success else "ERROR"
            print(f"{label}: {result.status}")

    except KeyboardInterrupt:
        print("\nVoice assistant stopped.")
        controller.execute("STOP")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
