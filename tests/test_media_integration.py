
"""Integration tests for the command service and media controller."""

from pathlib import Path

from src.command_service import execute_validated_command
from src.command_validator import validate_command
from src.intent_processor import detect_intent
from src.media_controller import MediaController


class FakeVLCMedia:
    def __init__(self, path):
        self.path = path


class FakeVLCPlayer:
    def __init__(self):
        self.state = "STOPPED"
        self.volume = 0
        self.muted = False

    def stop(self):
        self.state = "STOPPED"

    def set_media(self, media):
        self.media = media

    def play(self):
        self.state = "PLAYING"
        return 0

    def set_pause(self, paused):
        self.state = "PAUSED" if paused else "PLAYING"

    def is_playing(self):
        return self.state == "PLAYING"

    def audio_set_volume(self, volume):
        self.volume = volume
        return 0

    def audio_set_mute(self, muted):
        self.muted = muted
        return 0


class FakeVLCInstance:
    def media_new(self, path):
        return FakeVLCMedia(path)


def make_controller(tmp_path: Path) -> MediaController:
    media_file = tmp_path / "sample.mp3"
    media_file.write_bytes(b"fake media data")

    return MediaController(
        media_files=[str(media_file)],
        vlc_instance=FakeVLCInstance(),
        player=FakeVLCPlayer(),
    )


def test_valid_play_command_reaches_real_media_controller(tmp_path):
    controller = make_controller(tmp_path)

    intent = detect_intent("play")
    validation = validate_command(intent, confidence=0.95)
    result = execute_validated_command(validation, controller)

    assert result.success is True
    assert "Playing track 1" in result.status
    assert controller.is_playing() is True


def test_low_confidence_command_does_not_execute(tmp_path):
    controller = make_controller(tmp_path)

    intent = detect_intent("play")
    validation = validate_command(intent, confidence=0.20)
    result = execute_validated_command(validation, controller)

    assert result.success is False
    assert result.status.startswith("rejected:")
    assert controller.is_playing() is False


def test_volume_command_reaches_real_media_controller(tmp_path):
    controller = make_controller(tmp_path)

    intent = detect_intent("volume up")
    validation = validate_command(intent, confidence=0.95)
    result = execute_validated_command(validation, controller)

    assert result.success is True
    assert controller.volume == 80
    assert "Volume increased to 80%" in result.status


def test_controller_failure_is_returned_by_command_service(tmp_path):
    controller = make_controller(tmp_path)
    controller.vlc_available = False
    controller.player = None

    intent = detect_intent("volume up")
    validation = validate_command(intent, confidence=0.95)
    result = execute_validated_command(validation, controller)

    assert result.success is False
    assert result.status == "VLC media player is unavailable."
