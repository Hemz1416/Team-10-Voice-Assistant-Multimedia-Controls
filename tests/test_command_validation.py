
import unittest


SUPPORTED_COMMANDS = {
    "play",
    "pause",
    "resume",
    "stop",
    "next",
    "previous",
    "volume up",
    "volume down",
    "mute",
}


def validate_command(command):
    """Accept only supported multimedia commands."""
    if not isinstance(command, str):
        return None

    normalized_command = " ".join(command.lower().split())

    if normalized_command in SUPPORTED_COMMANDS:
        return normalized_command

    return None


class TestCommandValidation(unittest.TestCase):

    def test_supported_command_is_accepted(self):
        self.assertEqual(validate_command("play"), "play")

    def test_command_is_case_insensitive(self):
        self.assertEqual(validate_command("PLAY"), "play")

    def test_extra_spaces_are_handled(self):
        self.assertEqual(validate_command("  volume   up "), "volume up")

    def test_unsupported_command_is_rejected(self):
        self.assertIsNone(validate_command("open browser"))

    def test_malformed_command_is_rejected(self):
        self.assertIsNone(validate_command("play music; delete files"))

    def test_os_command_injection_is_rejected(self):
        self.assertIsNone(validate_command("play && shutdown"))

    def test_empty_command_is_rejected(self):
        self.assertIsNone(validate_command(""))

    def test_whitespace_only_command_is_rejected(self):
        self.assertIsNone(validate_command("   "))

    def test_non_string_input_is_rejected(self):
        self.assertIsNone(validate_command(None))


if __name__ == "__main__":
    unittest.main(verbosity=2)
