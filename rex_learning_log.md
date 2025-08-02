Notes/Tips, in other words, lessons learned through mistakes and debugging:

- name the `venv` specific to the project, not just `venv`, it took awhile to debug and config. Named the variable `.venv_deidentifier`
- write out plan first and then build in chunks and test code
- Create a central `logger_config.py` and import logger. Need to also put into relevant .py scripts. 
- from app.logger_config import logger. logger_config is not a variable, it's the name of the Python file:
👉 logger_config.py (located in the app/ folder). OK.
- `logger.info()` is used to log informational messages during the execution of your program. These messages: Do not interrupt the program. Help track what the code is doing, especially in production or debugging
- logging start and end comes: 1) after function is def and 2) before the return result.
- For every `function' there should be a type cast for all arguments and the output.

Next Steps:
- Create synthetic data
