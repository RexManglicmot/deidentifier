"""
The redactor_api.py acts as a logic wrapper.
It's the middle layer between your web/API interface (app.py) and your core logic modules (detect.py, redact.py).

"""

from app.detect import detect_pii
from app.redact import redact_text
from app.logger_config import logger

def deidentify_pipeline(text: str) -> str:
    """
    Function detects and redacts in a single pipeline
    Input: Raw text data with possible PII
    Output: Rredacted text with PII removed
    """

    # Logging start
    logger.info("Logging start")

    pii_entities = detect_pii(text)                     # Detect PII entities
    redacted_text = redact_text(text, pii_entities)     # Redact those entities

    # Logging end
    logger.info("Logging end")

    return redacted_text

# COMPELTE