"""
Team 10 Voice Assistant - Media Controller Module
Component Owner: Hemant Ram Nelapati (T10VA-6 / T10VA-13)

Sprint 1 Day 2 (Oct 20, 2026): PLAY handler with VLC media loading and missing file checks.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

try:
    import vlc
    _VLC_IMPORTABLE = True
except (ImportError, OSError):
    vlc = None  # type: ignore
    _VLC_IMPORTABLE = False


class MediaController:
    """VLC-backed multimedia controller executing validated voice intents.

    Adheres to Team 10 SAD v1.0 and SRS v1.0 specifications.
    Accepts normalized intents and returns structured execution results.
    """
    DEFAULT_VOLUME = 70

    def __init__(
        self,
        media_files: Optional[Sequence[Union[str, Path]]] = None,
        vlc_instance: Optional[Any] = None,
        player: Optional[Any] = None,
    ) -> None:
        """Initialize the media controller with a playlist and VLC player."""
        self._media_files: List[str] = [str(f) for f in media_files] if media_files else []
        self._current_index: int = 0
        self._volume: int = self.DEFAULT_VOLUME
        self._is_muted: bool = False
        self._is_paused: bool = False
        self._has_played_current: bool = False

        self.vlc_instance = vlc_instance
        self.player = player
        self.vlc_available: bool = False

        self._initialize_player()

    def _initialize_player(self) -> None:
        """Initialize or configure the VLC instance and player."""
        if self.player is not None and self.vlc_instance is not None:
            self.vlc_available = True
            return

        if not _VLC_IMPORTABLE or vlc is None:
            self.vlc_available = False
            return

        try:
            if self.vlc_instance is None:
                self.vlc_instance = vlc.Instance("--no-xlib", "--quiet")
            if self.player is None and self.vlc_instance is not None:
                self.player = self.vlc_instance.media_player_new()
            self.vlc_available = self.player is not None
        except Exception:
            self.vlc_available = False
            self.vlc_instance = None
            self.player = None

    @property
    def media_files(self) -> List[str]:
        """Return the current playlist."""
        return list(self._media_files)

    @property
    def current_index(self) -> int:
        """Return index of current track."""
        return self._current_index

    @property
    def volume(self) -> int:
        """Return current volume percentage within inclusive 0–100%."""
        return self._volume

    @property
    def is_muted(self) -> bool:
        """Return mute state."""
        return self._is_muted

    def is_paused(self) -> bool:
        """Return True if currently in paused state."""
        return self._is_paused

    def is_playing(self) -> bool:
        """Check if VLC is actively playing."""
        if not self.vlc_available or self.player is None:
            return False
        try:
            if hasattr(self.player, "is_playing"):
                return bool(self.player.is_playing())
            return False
        except Exception:
            return False

    def get_current_track(self) -> Optional[str]:
        """Return path of current track if playlist is non-empty."""
        if 0 <= self._current_index < len(self._media_files):
            return self._media_files[self._current_index]
        return None

    SUPPORTED_INTENTS = {
        "PLAY",
    }

    def execute(self, intent: str) -> Dict[str, Any]:
        """Execute a normalized multimedia intent."""
        if not intent or not isinstance(intent, str):
            return {
                "success": False,
                "status": "Invalid or empty intent provided.",
            }

        normalized_intent = intent.strip().upper()

        handlers = {
            "PLAY": self.play,
        }

        handler = handlers.get(normalized_intent)
        if not handler:
            return {
                "success": False,
                "status": f"Unsupported media intent: '{intent}'",
            }

        try:
            return handler()
        except Exception as exc:
            return {
                "success": False,
                "status": "An unexpected media player error occurred.",
                "error_details": str(exc),
            }

    def play(self) -> Dict[str, Any]:
        """Start media playback of current track."""
        if not self._media_files:
            return {
                "success": False,
                "status": "Playlist is empty. No media to play.",
            }

        if not self.vlc_available or self.player is None:
            return {
                "success": False,
                "status": "VLC media player is unavailable.",
                "error_details": "Player instance not initialized or VLC unavailable.",
            }

        if self._is_paused:
            return self.resume()

        track_path = self._media_files[self._current_index]
        resolved_path = os.path.abspath(track_path)

        if not os.path.exists(resolved_path):
            return {
                "success": False,
                "status": f"Media file not found: {track_path}",
            }

        try:
            if hasattr(self.player, "stop"):
                self.player.stop()

            if self.vlc_instance and hasattr(self.vlc_instance, "media_new"):
                media = self.vlc_instance.media_new(resolved_path)
                if hasattr(self.player, "set_media"):
                    self.player.set_media(media)

            if hasattr(self.player, "play"):
                self.player.play()

            self._is_paused = False
            self._has_played_current = True
            track_name = os.path.basename(track_path)
            return {
                "success": True,
                "status": f"Playing track {self._current_index + 1}: {track_name}",
                "track": track_path,
                "track_index": self._current_index,
            }
        except Exception as exc:
            return {
                "success": False,
                "status": "Failed to start media playback.",
                "error_details": str(exc),
            }
