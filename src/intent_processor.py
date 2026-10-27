
"""Map recognized text to predefined multimedia intents."""

import re

from src.models import IntentResult


SUPPORTED_INTENTS = {
    "PLAY", "PAUSE", "RESUME", "STOP", "NEXT", "PREVIOUS",
    "VOLUME_UP", "VOLUME_DOWN", "MUTE",
}

PHRASE_MAP = {
    "play": "PLAY",
    "start playback": "PLAY",
    "play music": "PLAY",
    "start playing": "PLAY",
    "start the music": "PLAY",

    "pause": "PAUSE",
    "pause playback": "PAUSE",
    "pause music": "PAUSE",

    "resume": "RESUME",
    "resume playback": "RESUME",
    "continue playback": "RESUME",
    "resume music": "RESUME",
    "continue playing": "RESUME",

    "stop": "STOP",
    "stop playback": "STOP",
    "stop music": "STOP",

    "next": "NEXT",
    "next track": "NEXT",
    "next song": "NEXT",

    "previous": "PREVIOUS",
    "previous track": "PREVIOUS",
    "previous song": "PREVIOUS",

    "volume up": "VOLUME_UP",
    "increase volume": "VOLUME_UP",
    "turn volume up": "VOLUME_UP",
    "turn the volume up": "VOLUME_UP",

    "volume down": "VOLUME_DOWN",
    "decrease volume": "VOLUME_DOWN",
    "turn volume down": "VOLUME_DOWN",
    "turn the volume down": "VOLUME_DOWN",

    "mute": "MUTE",
    "mute audio": "MUTE",
    "mute the sound": "MUTE",
}

POLITE_PREFIXES = (
    "could you please ",
    "would you please ",
    "can you please ",
    "will you please ",
    "could you ",
    "would you ",
    "can you ",
    "will you ",
    "please ",
    "hey assistant ",
)


def detect_intent(text: str) -> IntentResult:
    """Return a structured intent result or an empty result."""
    if not isinstance(text, str) or not text.strip():
        return IntentResult(intent=None, parameters={})

    normalized = re.sub(r"[^a-z0-9\s]", " ", text.lower())
    phrase = " ".join(normalized.split())

    # Remove polite introductions, not arbitrary extra words.
    changed = True
    while changed:
        changed = False
        for prefix in POLITE_PREFIXES:
            if phrase.startswith(prefix):
                phrase = phrase[len(prefix):].strip()
                changed = True
                break

    if phrase.endswith(" please"):
        phrase = phrase[:-7].strip()

    intent = PHRASE_MAP.get(phrase)

    if intent not in SUPPORTED_INTENTS:
        return IntentResult(intent=None, parameters={})

    return IntentResult(intent=intent, parameters={})
