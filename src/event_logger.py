
import logging
from pathlib import Path

Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


def record_event(intent, success, status):
    logging.info(
        "intent=%s success=%s status=%s",
        intent or "UNKNOWN",
        success,
        status,
    )
