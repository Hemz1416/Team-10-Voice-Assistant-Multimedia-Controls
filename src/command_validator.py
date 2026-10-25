
ALLOWED_INTENTS = {
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

# Initial prototype threshold; validate and tune with test data.
MIN_CONFIDENCE = 0.50


def validate_command(intent_result):
    intent = intent_result.get("intent")
    confidence = intent_result.get("confidence")

    if intent not in ALLOWED_INTENTS:
        return {
            "allowed": False,
            "intent": None,
            "reason": "Unsupported command",
        }

    if confidence is not None and confidence < MIN_CONFIDENCE:
        return {
            "allowed": False,
            "intent": None,
            "reason": "Confidence too low",
        }

    return {
        "allowed": True,
        "intent": intent,
        "reason": "Supported command",
    }
