"""
Team 10 Voice Assistant - Media Controller Module
Component Owner: Hemant Ram Nelapati (T10VA-6)

Provides VLC-backed media playback control for 9 normalized intents:
PLAY, PAUSE, RESUME, STOP, NEXT, PREVIOUS, VOLUME_UP, VOLUME_DOWN, MUTE.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Union

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

    VOLUME_STEP = 10
    MIN_VOLUME = 0
    MAX_VOLUME = 100
    DEFAULT_VOLUME = 70

    SUPPORTED_INTENTS = {
        "PLAY",
        "PAUSE",
        "RESUME",
        "STOP",
        "NEXT",
        "PREVIOUS",
        "VOLUME_UP",
        "VOLUME_DOWN",
        "MUTE",
    }

    def __init__(
        self,
        media_files: Optional[Sequence[Union[str, Path]]] = None,
        vlc_instance: Optional[Any] = None,
        player: Optional[Any] = None,
    ) -> None:
        """Initialize the media controller with a playlist and VLC player.

        Args:
            media_files: Sequence of media file paths.
            vlc_instance: Optional injected VLC instance (for mocking/testing).
            player: Optional injected VLC media player (for mocking/testing).
        """
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
        """Return current volume percentage (0-100)."""
        return self._volume

    @property
    def is_muted(self) -> bool:
        """Return mute state."""
        return self._is_muted

    def get_current_track(self) -> Optional[str]:
        """Return path of current track if playlist is non-empty."""
        if 0 <= self._current_index < len(self._media_files):
            return self._media_files[self._current_index]
        return None

    def execute(self, intent: str) -> Dict[str, Any]:
        """Execute a normalized multimedia intent.

        Args:
            intent: String representing the multimedia action.

        Returns:
            Dict containing at minimum 'success' (bool) and 'status' (str).
        """
        if not intent or not isinstance(intent, str):
            return {
                "success": False,
                "status": "Invalid or empty intent provided.",
            }

        normalized_intent = intent.strip().upper()

        handlers = {
            "PLAY": self.play,
            "PAUSE": self.pause,
            "RESUME": self.resume,
            "STOP": self.stop,
            "NEXT": self.next_track,
            "PREVIOUS": self.previous_track,
            "VOLUME_UP": self.volume_up,
            "VOLUME_DOWN": self.volume_down,
            "MUTE": self.toggle_mute,
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
                "status": f"Media player error: {str(exc)}",
            }

    def play(self) -> Dict[str, Any]:
        """Start or resume playback of the current track."""
        if not self._media_files:
            return {
                "success": False,
                "status": "Playlist is empty. No media to play.",
            }

        if not self.vlc_available or self.player is None:
            return {
                "success": False,
                "status": "VLC media player is unavailable on this system.",
            }

        # If currently paused, resume instead of restarting track
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

            play_res = self.player.play()
            if play_res == -1:
                return {
                    "success": False,
                    "status": f"Failed to start playback for: {os.path.basename(track_path)}",
                }

            # Apply stored volume and mute settings to player
            self._apply_audio_settings()

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
                "status": f"Playback failure: {str(exc)}",
            }

    def pause(self) -> Dict[str, Any]:
        """Pause ongoing media playback."""
        if not self.vlc_available or self.player is None:
            return {
                "success": False,
                "status": "VLC media player is unavailable.",
            }

        if self._is_paused:
            return {
                "success": True,
                "status": "Playback is already paused.",
            }

        if not self._has_played_current and not self.is_playing():
            return {
                "success": False,
                "status": "No active media playback to pause.",
            }

        try:
            if hasattr(self.player, "set_pause"):
                self.player.set_pause(1)
            elif hasattr(self.player, "pause"):
                self.player.pause()

            self._is_paused = True
            current_track = self.get_current_track()
            track_name = os.path.basename(current_track) if current_track else "current media"
            return {
                "success": True,
                "status": f"Paused: {track_name}",
            }
        except Exception as exc:
            return {
                "success": False,
                "status": f"Pause failure: {str(exc)}",
            }

    def resume(self) -> Dict[str, Any]:
        """Resume playback if paused, or start if stopped."""
        if not self.vlc_available or self.player is None:
            return {
                "success": False,
                "status": "VLC media player is unavailable.",
            }

        if not self._media_files:
            return {
                "success": False,
                "status": "Playlist is empty. No media to resume.",
            }

        # If already actively playing and not paused
        if self.is_playing() and not self._is_paused:
            return {
                "success": True,
                "status": "Playback already in progress.",
            }

        if self._is_paused:
            try:
                if hasattr(self.player, "set_pause"):
                    self.player.set_pause(0)
                elif hasattr(self.player, "play"):
                    self.player.play()

                self._is_paused = False
                current_track = self.get_current_track()
                track_name = os.path.basename(current_track) if current_track else "current media"
                return {
                    "success": True,
                    "status": f"Resumed playback: {track_name}",
                }
            except Exception as exc:
                return {
                    "success": False,
                    "status": f"Resume failure: {str(exc)}",
                }

        # If not paused, start playback
        return self.play()

    def stop(self) -> Dict[str, Any]:
        """Stop playback completely."""
        if not self.vlc_available or self.player is None:
            return {
                "success": False,
                "status": "VLC media player is unavailable.",
            }

        try:
            if hasattr(self.player, "stop"):
                self.player.stop()

            self._is_paused = False
            self._has_played_current = False
            return {
                "success": True,
                "status": "Playback stopped.",
            }
        except Exception as exc:
            return {
                "success": False,
                "status": f"Stop failure: {str(exc)}",
            }

    def next_track(self) -> Dict[str, Any]:
        """Advance to the next track, wrapping around from end to beginning."""
        if not self._media_files:
            return {
                "success": False,
                "status": "Playlist is empty. Cannot navigate tracks.",
            }

        # Boundary wrap-around: last -> first
        self._current_index = (self._current_index + 1) % len(self._media_files)
        self._is_paused = False
        return self.play()

    def previous_track(self) -> Dict[str, Any]:
        """Navigate to the previous track, wrapping around from first to last."""
        if not self._media_files:
            return {
                "success": False,
                "status": "Playlist is empty. Cannot navigate tracks.",
            }

        # Boundary wrap-around: first -> last
        self._current_index = (self._current_index - 1) % len(self._media_files)
        self._is_paused = False
        return self.play()

    def volume_up(self, step: Optional[int] = None) -> Dict[str, Any]:
        """Increase volume by step (default 10), clamped at 100."""
        increment = step if step is not None else self.VOLUME_STEP
        self._volume = min(self.MAX_VOLUME, self._volume + increment)
        self._apply_audio_settings()
        return {
            "success": True,
            "status": f"Volume increased to {self._volume}%",
            "volume": self._volume,
        }

    def volume_down(self, step: Optional[int] = None) -> Dict[str, Any]:
        """Decrease volume by step (default 10), clamped at 0."""
        decrement = step if step is not None else self.VOLUME_STEP
        self._volume = max(self.MIN_VOLUME, self._volume - decrement)
        self._apply_audio_settings()
        return {
            "success": True,
            "status": f"Volume decreased to {self._volume}%",
            "volume": self._volume,
        }

    def toggle_mute(self) -> Dict[str, Any]:
        """Toggle mute state predictably."""
        self._is_muted = not self._is_muted
        self._apply_audio_settings()
        state_str = "Audio muted." if self._is_muted else "Audio unmuted."
        return {
            "success": True,
            "status": state_str,
            "is_muted": self._is_muted,
        }

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

    def is_paused(self) -> bool:
        """Return True if currently in paused state."""
        return self._is_paused

    def _apply_audio_settings(self) -> None:
        """Apply current volume and mute settings to the underlying player."""
        if not self.vlc_available or self.player is None:
            return
        try:
            if hasattr(self.player, "audio_set_volume"):
                self.player.audio_set_volume(self._volume)
            if hasattr(self.player, "audio_set_mute"):
                self.player.audio_set_mute(self._is_muted)
        except Exception:
            pass
