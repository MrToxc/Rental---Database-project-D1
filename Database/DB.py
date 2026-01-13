import json
import os

import pyodbc

from Database.Config import find_config

global_connection = None


def get_db_connection():
    if global_connection is None:
        return create_db_connection()
    else:
        return global_connection

def create_db_connection():
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


class ConnectionDecorator:

    connection = create_db_connection()

    def cursor(self):
        return self.connection.cursor()

    def commit(self):
        pass

    def rollback(self):
        pass

    def close(self):
        pass

    def really_commit(self):
        self.connection.commit()

    def really_rollback(self):
        self.connection.rollback()

    def really_close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass