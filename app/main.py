# main.py
import os
import yaml
import json
import time
import requests
# import pandas as pd
# from requests.auth import HTTPBasicAuth


### do not put your code here - it will only run if you directly call main.py ###
def main():
    # example call - use run_local.py (will read secrets.yml) or run_remote.py for docker deployment (reads ENV)
    print("Starte Beispiel-Loop (nur für lokale Tests)...")

    FILE_PATH_SECRETS = '../secrets.yml' # 'c:/secrets/appname123.yml'
    # Default Secrets-File
    SECRETS_FILE = os.environ.get('SECRETS_FILE', FILE_PATH_SECRETS)
    if os.path.exists(SECRETS_FILE):
        with open(SECRETS_FILE, 'r') as f:
            config = yaml.safe_load(f)
    else:
        # secrets = {}
        raise RuntimeError(f"run_local.py failed to read secrets.yml from {FILE_PATH_SECRETS}")

    core_program(
        **config
    )


### put your code into core_program() which will be called ###
def core_program(**kwargs):
    print(kwargs)
    var1 = kwargs["projektname_var1"]


if __name__ == "__main__":
    main()
