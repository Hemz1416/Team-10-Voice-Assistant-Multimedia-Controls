
"""Coordinate validation and media-controller execution."""

from typing import Protocol

from src.models import (
    IntentResult,
    MediaActionResult,
    ValidationResult,
)


class MediaController(Protocol):
    def execute(self, command: IntentResult) -> MediaActionResult:
        """Execute one validated multimedia command."""
        ...


def execute_validated_command(
    validation: ValidationResult,
    controller: MediaController,
) -> MediaActionResult:
    """Execute only commands accepted by the validator."""

    if not validation.allowed or validation.intent is None:
        return MediaActionResult(
            success=False,
            status=f"rejected:{validation.reason}",
        )

    return controller.execute(validation.intent)
