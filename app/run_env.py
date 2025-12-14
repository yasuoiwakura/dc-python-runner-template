# run_main.py
import os
from main import core_program

# Präfix für ENV-Variablen, die an core_program gehen
PREFIX = "PYTHON_KWARG_"

# Alle ENV mit dem Präfix sammeln
kwargs = {}
for key, value in os.environ.items():
    if key.startswith(PREFIX):
        # Entferne PREFIX und mach Key lowercase oder snake_case
        param_name = key[len(PREFIX):].lower()
        kwargs[param_name] = value

# core_program aufrufen
core_program(**kwargs)
