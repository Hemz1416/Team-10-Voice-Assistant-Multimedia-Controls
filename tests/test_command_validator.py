
import unittest

from src.command_validator import validate_command
from src.models import IntentResult


class TestCommandValidator(unittest.TestCase):
    def test_valid_command(self):
        result = validate_command(IntentResult("PLAY", {}), 0.95)
        self.assertTrue(result.allowed)
        self.assertEqual(result.intent.intent, "PLAY")

    def test_low_confidence_is_rejected(self):
        result = validate_command(IntentResult("PLAY", {}), 0.40)
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "low_confidence")

    def test_unknown_intent_is_rejected(self):
        result = validate_command(IntentResult("DELETE_FILES", {}), 0.99)
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "unsupported_intent")

    def test_missing_intent_is_rejected(self):
        result = validate_command(IntentResult(None, {}), 0.99)
        self.assertFalse(result.allowed)

    def test_invalid_confidence_is_rejected(self):
        result = validate_command(IntentResult("PLAY", {}), 1.5)
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "invalid_confidence")

    def test_negative_minimum_confidence_is_rejected(self):
        result = validate_command(
            IntentResult("PLAY", {}),
            0.95,
            minimum_confidence=-0.1,
        )
        self.assertFalse(result.allowed)
        self.assertEqual(
            result.reason, "invalid_minimum_confidence"
        )

    def test_minimum_confidence_above_one_is_rejected(self):
        result = validate_command(
            IntentResult("PLAY", {}),
            0.95,
            minimum_confidence=1.1,
        )
        self.assertFalse(result.allowed)
        self.assertEqual(
            result.reason, "invalid_minimum_confidence"
        )

    def test_nan_minimum_confidence_is_rejected(self):
        result = validate_command(
            IntentResult("PLAY", {}),
            0.95,
            minimum_confidence=float("nan"),
        )
        self.assertFalse(result.allowed)
        self.assertEqual(
            result.reason, "invalid_minimum_confidence"
        )

    def test_nan_confidence_is_rejected(self):
        result = validate_command(
            IntentResult("PLAY", {}),
            float("nan"),
        )
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "invalid_confidence")

    def test_malformed_intent_is_rejected(self):
        result = validate_command(
            IntentResult(["PLAY"], {}),
            0.95,
        )
        self.assertFalse(result.allowed)
        self.assertEqual(result.reason, "invalid_intent")


if __name__ == "__main__":
    unittest.main()
