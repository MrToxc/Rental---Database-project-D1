import json
import os
from pathlib import Path

import pyodbc


def get_db_connection():
    config_path = find_config()
    if not os.path.exists(config_path):
        raise Exception("Soubor config.json neexistuje! Vytvořte ho podle config.example.json.")

    with open(config_path, 'r') as f:
        config = json.load(f)

    conn_str = (
        f"DRIVER={config['driver']};"
        f"SERVER={config['server']};"
        f"DATABASE={config['database']};"
        f"UID={config['uid']};"
        f"PWD={config['pwd']}"
    )
    return pyodbc.connect(conn_str)

def find_config():
    current_path = Path(__file__).resolve().parent

    for parent in [current_path] + list(current_path.parents):
        config_path = parent / "config.json"
        if config_path.exists():
            return config_path

    raise FileNotFoundError("Could not find config.json in any parent directory.")
