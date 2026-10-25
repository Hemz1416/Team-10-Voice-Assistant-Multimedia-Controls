
from src.command_validator import validate_command


def test_valid_command_is_allowed():
    result = validate_command({
        "intent": "PLAY",
        "confidence": 0.90,
    })
    assert result["allowed"] is True


def test_unsupported_command_is_rejected():
    result = validate_command({
        "intent": None,
        "confidence": None,
    })
    assert result["allowed"] is False


def test_low_confidence_is_rejected():
    result = validate_command({
        "intent": "PLAY",
        "confidence": 0.20,
    })
    assert result["allowed"] is False


def test_unknown_intent_is_rejected():
    result = validate_command({
        "intent": "DELETE_FILES",
        "confidence": 0.99,
    })
    assert result["allowed"] is False


def test_missing_confidence_is_handled():
    result = validate_command({
        "intent": "PLAY",
        "confidence": None,
    })
    assert result["allowed"] is True
