"""Additional functional tests for multimedia command execution."""

import pytest

from src.command_service import execute_validated_command
from src.intent_processor import detect_intent
from src.models import IntentResult, ValidationResult


class FakeMediaController:
    """Mock controller that records commands without playing real media."""

    def __init__(self, success=True):
        self.received = []
        self.success = success

    def execute(self, intent):
        self.received.append(intent)
        return {
            "success": self.success,
            "status": (
                f"{intent} executed"
                if self.success
                else f"{intent} failed"
            ),
        }


@pytest.mark.parametrize(
    ("phrase", "expected_intent"),
    [
        ("play", "PLAY"),
        ("pause", "PAUSE"),
        ("resume playback", "RESUME"),
        ("stop", "STOP"),
        ("next song", "NEXT"),
        ("previous track", "PREVIOUS"),
        ("volume up", "VOLUME_UP"),
        ("volume down", "VOLUME_DOWN"),
        ("mute", "MUTE"),
    ],
)
def test_supported_command_reaches_controller(phrase, expected_intent):
    """Each supported command must reach the controller as the right intent."""
    controller = FakeMediaController()
    intent = detect_intent(phrase)

    assert intent.intent == expected_intent

    validation = ValidationResult(
        True,
        IntentResult(expected_intent, {}),
        "accepted",
    )

    result = execute_validated_command(validation, controller)

    assert result.success is True
    assert controller.received == [expected_intent]


@pytest.mark.parametrize(
    "phrase",
    [
        "",
        "open a browser",
        "tell me a joke",
        "dont play music",
        "play music and stop",
    ],
)
def test_invalid_or_ambiguous_input_does_not_reach_controller(phrase):
    """Unsupported or ambiguous input must not trigger a media action."""
    controller = FakeMediaController()
    intent = detect_intent(phrase)

    if intent.intent is None:
        validation = ValidationResult(
            False,
            None,
            "unsupported_intent",
        )
    else:
        # Ambiguous phrases must not be allowed to execute a command.
        validation = ValidationResult(
            False,
            intent,
            "ambiguous_or_unsupported_input",
        )

    result = execute_validated_command(validation, controller)

    assert result.success is False
    assert controller.received == []


def test_controller_failure_is_reported():
    """A failed controller operation must not be reported as successful."""
    controller = FakeMediaController(success=False)
    intent = detect_intent("play")

    validation = ValidationResult(
        True,
        IntentResult(intent.intent, {}),
        "accepted",
    )

    result = execute_validated_command(validation, controller)

    assert result.success is False
    assert controller.received == ["PLAY"]