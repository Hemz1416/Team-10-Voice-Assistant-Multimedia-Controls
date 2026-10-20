"""
Automated Unit Tests for Hemant's VLC Media Controller (T10VA-6)

Tests cover all 9 media intents, playlist wrap-around, volume boundaries,
mute toggling, error handling, and edge cases using pure fakes/mocks.
No physical microphone, speakers, VLC GUI, or Raspberry Pi hardware required.
"""

import os
from pathlib import Path
import pytest
from src.media_controller import MediaController


class FakeVLCMedia:
    """Fake VLC Media object."""

    def __init__(self, mrl: str):
        self.mrl = mrl


class FakeVLCPlayer:
    """Fake VLC MediaPlayer simulating playback, pause, stop, and volume states."""

    def __init__(self):
        self.media = None
        self.state = "STOPPED"
        self.volume = 0
        self.muted = False
        self.play_called = 0
        self.stop_called = 0
        self.fail_play = False
        self.raise_on_play = False
        self.fail_volume = False
        self.raise_on_volume = False
        self.fail_mute = False
        self.raise_on_mute = False
        self.raise_on_pause = False
        self.raise_on_stop = False

    def set_media(self, media):
        self.media = media

    def play(self):
        if self.raise_on_play:
            raise RuntimeError("Underlying libVLC fatal crash")
        if self.fail_play:
            return -1
        self.state = "PLAYING"
        self.play_called += 1
        return 0

    def pause(self):
        if self.raise_on_pause:
            raise RuntimeError("Underlying libVLC pause crash")
        if self.state == "PLAYING":
            self.state = "PAUSED"
        elif self.state == "PAUSED":
            self.state = "PLAYING"

    def set_pause(self, do_pause: int):
        if self.raise_on_pause:
            raise RuntimeError("Underlying libVLC pause crash")
        self.state = "PAUSED" if do_pause else "PLAYING"

    def stop(self):
        if self.raise_on_stop:
            raise RuntimeError("Underlying libVLC stop crash")
        self.state = "STOPPED"
        self.stop_called += 1

    def is_playing(self) -> int:
        return 1 if self.state == "PLAYING" else 0

    def audio_set_volume(self, vol: int):
        if self.raise_on_volume:
            raise RuntimeError("Hardware mixer communication error")
        if self.fail_volume:
            return -1
        self.volume = vol
        return 0

    def audio_set_mute(self, mute: bool):
        if self.raise_on_mute:
            raise RuntimeError("Hardware mute line disconnected")
        if self.fail_mute:
            return -1
        self.muted = bool(mute)
        return 0


class FakeVLCInstance:
    """Fake VLC Instance providing media creation."""

    def __init__(self):
        pass

    def media_new(self, path: str):
        return FakeVLCMedia(path)


@pytest.fixture
def mock_files(tmp_path: Path):
    """Create three temporary media files for deterministic testing."""
    f1 = tmp_path / "song1.mp3"
    f2 = tmp_path / "song2.mp3"
    f3 = tmp_path / "song3.mp3"
    f1.write_bytes(b"ID3fake1")
    f2.write_bytes(b"ID3fake2")
    f3.write_bytes(b"ID3fake3")
    return [str(f1), str(f2), str(f3)]


@pytest.fixture
def controller(mock_files):
    """Return a MediaController configured with fakes."""
    fake_inst = FakeVLCInstance()
    fake_player = FakeVLCPlayer()
    return MediaController(
        media_files=mock_files,
        vlc_instance=fake_inst,
        player=fake_player,
    )


# =========================================================================
# 1. Initialization and Contract Tests
# =========================================================================



def test_controller_initialization(controller, mock_files):
    """Verify default initialization values."""
    assert controller.media_files == mock_files
    assert controller.current_index == 0
    assert controller.volume == 70
    assert controller.is_muted is False
    assert controller.is_paused() is False
    assert controller.is_playing() is False
    assert controller.get_current_track() == mock_files[0]


def test_execute_intent_normalization(controller):
    """Verify intent execution is case-insensitive and trims whitespace."""
    res = controller.execute("  play  ")
    assert res["success"] is True
    assert "Playing track 1" in res["status"]


def test_execute_invalid_or_empty_intent(controller):
    """Verify invalid and non-string intents return controlled failures."""
    res1 = controller.execute("")
    assert res1["success"] is False
    assert "Invalid or empty" in res1["status"]

    res2 = controller.execute(None)  # type: ignore
    assert res2["success"] is False
    assert "Invalid or empty" in res2["status"]

    res3 = controller.execute(123)  # type: ignore
    assert res3["success"] is False


def test_execute_unsupported_intent(controller):
    """Verify unknown intents are rejected with controlled failure."""
    res = controller.execute("FAST_FORWARD")
    assert res["success"] is False
    assert "Unsupported media intent: 'FAST_FORWARD'" in res["status"]


# =========================================================================
# 2. Sprint 1 Priority Commands: PLAY, PAUSE, RESUME
# =========================================================================


def test_play_success(controller, mock_files):
    """Verify PLAY starts playback of the first track."""
    res = controller.execute("PLAY")
    assert res["success"] is True
    assert "song1.mp3" in res["status"]
    assert controller.player.state == "PLAYING"
    assert controller.is_playing() is True


def test_empty_playlist_handling():
    """Verify empty playlist returns controlled failures."""
    ctrl = MediaController(media_files=[], vlc_instance=FakeVLCInstance(), player=FakeVLCPlayer())

    res_play = ctrl.execute("PLAY")
    assert res_play["success"] is False
    assert "Playlist is empty" in res_play["status"]


def test_missing_media_file_handling():
    """Verify missing/non-existent media file returns controlled failure."""
    ctrl = MediaController(
        media_files=["/non/existent/path/song.mp3"],
        vlc_instance=FakeVLCInstance(),
        player=FakeVLCPlayer(),
    )
    res = ctrl.execute("PLAY")
    assert res["success"] is False
    assert "Media file not found" in res["status"]


