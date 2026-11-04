import logging
from unittest.mock import patch

from src.event_logger import record_event


def test_record_event_logging():
    with patch.object(logging, "info") as mock_info:
        record_event("PLAY", True, "Playback started")
        mock_info.assert_called_once_with(
            "intent=%s success=%s status=%s",
            "PLAY",
            True,
            "Playback started",
        )


def test_record_event_none_intent():
    with patch.object(logging, "info") as mock_info:
        record_event(None, False, "Rejected")
        mock_info.assert_called_once_with(
            "intent=%s success=%s status=%s",
            "UNKNOWN",
            False,
            "Rejected",
        )

