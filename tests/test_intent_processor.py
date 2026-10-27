
import unittest

from src.intent_processor import detect_intent


class TestIntentProcessor(unittest.TestCase):
    def test_supported_commands(self):
        cases = {
            "play": "PLAY",
            "play music": "PLAY",
            "pause": "PAUSE",
            "please pause": "PAUSE",
            "resume playback": "RESUME",
            "stop": "STOP",
            "next song": "NEXT",
            "previous track": "PREVIOUS",
            "volume up": "VOLUME_UP",
            "volume down": "VOLUME_DOWN",
            "mute": "MUTE",
        }

        for phrase, expected in cases.items():
            with self.subTest(phrase=phrase):
                self.assertEqual(detect_intent(phrase).intent, expected)

    def test_case_and_whitespace(self):
        self.assertEqual(
            detect_intent("  PLAY MUSIC  ").intent,
            "PLAY",
        )

    def test_unsupported_command(self):
        self.assertIsNone(detect_intent("tell me a joke").intent)
        self.assertIsNone(detect_intent("open a browser").intent)

    def test_empty_input(self):
        self.assertIsNone(detect_intent("").intent)

    def test_non_string_input(self):
        self.assertIsNone(detect_intent(None).intent)


if __name__ == "__main__":
    unittest.main()
