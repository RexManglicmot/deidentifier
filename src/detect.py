from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern


def detect_pii(text: str):
    """
    Fuction will take in text data and return detected PII entities
    """

    # Create the default Presidio analyzer engine
    analyzer = AnalyzerEngine()

    