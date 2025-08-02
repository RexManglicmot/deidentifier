from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern
# Took awhile, but got the right venv installed

# Importing logger object
from app.logger_config import logger


def detect_pii(text: str):
    """
    Fuction will take in text data and return detected PII entities
    """

    # Logging start
    # Logs a message with INFO level (not DEBUG or ERROR)
    logger.info("Starting PII detection...")

    # Create the default Presidio analyzer engine
    analyzer = AnalyzerEngine()

    # Create custom function for regex pattern for MRNs
    mrn_pattern = Pattern(
        name= "MRN Pattern",
        regex= r"\b[0-9]{6,10}\b",  
        score= 0.85
        )

    # Create a custom recognizer for the MRN entity
    mrn_recognizer = PatternRecognizer(
        supported_entity="MEDICAL_RECORD_NUMER",    # Custom entity name
        patterns=[mrn_pattern]                      # Patterns it will match
    )
    # Register custom recognizer into the analyzer
    analyzer.registry.add_recognizer(mrn_recognizer)

    # Analyze the text for PI entities using Presidio
    results = analyzer.analyze(
        text=text,
        language="en"
    )

    # Loging end with entity types
    # Logs a message with INFO level (not DEBUG or ERROR)
    # A LIST COMPREHENSION that loops through the results list and extracts the entity_type from each item
    # Example: Completed PII detection. Types: ['EMAIL_ADDRESS', 'MRN', 'EMAIL_ADDRESS']
    logger.info(f"Completed PII detection. Types: {[r.entity_type for r in results]}")  

    # Return list of detected entities
    return results

# COMPLETE