# Python's standard logging module
import logging

# Basic configuration for logging
logging.basicConfig(
    level=logging.INFO,     # Set minimum log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",     # Log msg format with timestamp, level, and message
    handlers=[
        logging.FileHander("logs/app.log"),     # Sae logs to a file named app.log in the logs/directory
        logging.Streamhandler()                 # Also print in the terminal
    ]
)

# Create a logger object for use throughout the project
# This is what is imported!
# The object used is logger, which is what is importing from the module.
logger = logging.getLogger(__name__)
