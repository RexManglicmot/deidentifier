from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine 
from app.logger_config import logger


def redact_text(text: str, pii_entities: list) -> str:
    """
    Function takes in raq text and detected entities and returns a redacted version of the text

    """
    # Logging start
    logger.info("Starting text redaction...")

    # Initiliaze Presidio anonymizer engine
    anonymizer = AnonymizerEngine()

    # Apply anonymizaiton, replace eached detected entity with a placeholder
    result = anonymizer.anonymize(
        text=text,                          # Original input text
        analyzer_results=pii_entities       # Entities returned by detect_pii()
    )

    # Logging end
    logger.info("Text redaction complete")

    # Return only the redacted text content from the anonymization result
    return result.text

# COMPLETE