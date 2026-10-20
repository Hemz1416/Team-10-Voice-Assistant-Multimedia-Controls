
import unittest

from src.command_service import execute_validated_command
from src.models import (
    IntentResult,
    MediaActionResult,
    ValidationResult,
)


class FakeMediaController:
    def __init__(self):
        self.received = []

    def execute(self, command):
        self.received.append(command)
        return MediaActionResult(True, "executed")


class TestCommandService(unittest.TestCase):
    def test_accepted_command_reaches_controller(self):
        controller = FakeMediaController()
        intent = IntentResult("PLAY", {})
        validation = ValidationResult(True, intent, "accepted")

        result = execute_validated_command(validation, controller)

        self.assertTrue(result.success)
        self.assertEqual(len(controller.received), 1)
        self.assertEqual(controller.received[0].intent, "PLAY")

    def test_rejected_command_never_reaches_controller(self):
        controller = FakeMediaController()
        validation = ValidationResult(False, None, "low_confidence")

        result = execute_validated_command(validation, controller)

        self.assertFalse(result.success)
        self.assertEqual(result.status, "rejected:low_confidence")
        self.assertEqual(controller.received, [])


if __name__ == "__main__":
    unittest.main()
