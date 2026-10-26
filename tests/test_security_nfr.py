
import pytest

from src.command_validator import validate_command
from src.command_service import execute_validated_command
from src.models import IntentResult, ValidationResult


class FakeMediaController:
    """Records calls without performing real media actions."""

    _DEFAULT = object()

    def __init__(self, response=_DEFAULT, should_raise=False):
        self.calls = []

        if response is self._DEFAULT:
            self.response = {
                "success": True,
                "status": "completed",
            }
        else:
            self.response = response

        self.should_raise = should_raise

    def execute(self, intent):
        self.calls.append(intent)

        if self.should_raise:
            raise RuntimeError("internal secret detail")

        return self.response


@pytest.mark.parametrize(
    "confidence",
    [-0.1, 1.1, True, None, "0.9"],
)
def test_invalid_confidence_is_rejected(confidence):
    result = IntentResult("PLAY", {})
    validation = validate_command(result, confidence)

    assert validation.allowed is False
    assert validation.reason == "invalid_confidence"


def test_low_confidence_is_rejected():
    result = IntentResult("PLAY", {})
    validation = validate_command(result, 0.69)

    assert validation.allowed is False
    assert validation.reason == "low_confidence"


def test_unsupported_intent_is_rejected():
    result = IntentResult("DELETE_FILES", {})
    validation = validate_command(result, 0.95)

    assert validation.allowed is False
    assert validation.reason == "unsupported_intent"


def test_invalid_intent_result_is_rejected():
    validation = validate_command("PLAY", 0.95)

    assert validation.allowed is False
    assert validation.reason == "invalid_intent_result"


def test_invalid_validation_never_calls_controller():
    controller = FakeMediaController()
    validation = ValidationResult(
        False, None, "low_confidence"
    )

    outcome = execute_validated_command(validation, controller)

    assert outcome.success is False
    assert outcome.status == "rejected:low_confidence"
    assert controller.calls == []


def test_accepted_command_reaches_controller():
    controller = FakeMediaController()
    result = IntentResult("PLAY", {})
    validation = validate_command(result, 0.95)

    outcome = execute_validated_command(validation, controller)

    assert outcome.success is True
    assert outcome.status == "completed"
    assert controller.calls == ["PLAY"]


def test_controller_exception_does_not_leak_details():
    controller = FakeMediaController(should_raise=True)
    validation = ValidationResult(
        True, IntentResult("PLAY", {}), "accepted"
    )

    outcome = execute_validated_command(validation, controller)

    assert outcome.success is False
    assert outcome.status == "controller_error:execution_failed"
    assert "internal secret detail" not in outcome.status


@pytest.mark.parametrize(
    "bad_response",
    [
        None,
        [],
        {"success": "yes", "status": "completed"},
        {"success": True, "status": 123},
        {},
    ],
)
def test_malformed_controller_response_is_rejected(bad_response):
    controller = FakeMediaController(response=bad_response)
    validation = ValidationResult(
        True, IntentResult("PLAY", {}), "accepted"
    )

    outcome = execute_validated_command(validation, controller)

    assert outcome.success is False
    assert outcome.status == "controller_error:invalid_result"
