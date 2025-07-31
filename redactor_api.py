"""
The redactor_api.py acts as a logic wrapper.
It's the middle layer between your web/API interface (app.py) and your core logic modules (detect.py, redact.py).

"""

from app.detect import detect_pii
from app.redact import redact_text

def 