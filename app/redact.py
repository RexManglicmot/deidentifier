from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine 

def redact_text(text: str, pii_entities):
    """
    Function takes in raq text and detected entities and returns a redacted version of the text

    """

    # Initiliaze Presidio anonymizer engine
    anonymizer = AnonymizerEngine()

    # Apply anonymizaiton, replace eached detected entity with a placeholder
    result = anonymizer.anonymize(
        text=text,                          # Original input text
        analyzer_results=pii_entities       # Entities returned by detect_pii()
    )

    #
    return result.text

# COMPLETE