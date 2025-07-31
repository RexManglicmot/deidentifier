from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern
# Took awhile, but got the right venv installed

def detect_pii(text: str):
    """
    Fuction will take in text data and return detected PII entities
    """

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

    # Return list of detected entities
    return results

# COMPLETE