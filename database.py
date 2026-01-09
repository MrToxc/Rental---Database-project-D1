import json
import os
from dataclasses import asdict

import pyodbc

def get_db_connection():
    config_path = 'config.json'
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


def get_by_id(table, id_record):
    with get_db_connection() as connection:
        cursor = connection.cursor()

        sql = f"SELECT * FROM {table} WHERE {attribute_id_name(table)} = ?"
        cursor.execute(sql, id_record)

        row = cursor.fetchone()

        if row is None:
            return None

        # Získání názvů sloupců a vytvoření slovníku
        columns = [column[0] for column in cursor.description]
        return dict(zip(columns, row))

def get_by_id_as_object(table, id_record, obj):
    data = get_by_id(table, id_record)
    if data:
        return obj(**data)
    return None


def get_all(table):
    with get_db_connection() as connection:
        cursor = connection.cursor()
        sql = f"SELECT * FROM {table}"
        cursor.execute(sql)

        # Získání názvů sloupců z popisu kurzoru
        columns = [column[0] for column in cursor.description]

        # Sestavení výsledného seznamu slovníků
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))

        return results

def get_all_as_objects(table, data_class):
    with get_db_connection() as connection:
        cursor = connection.cursor()
        sql = f"SELECT * FROM {table}"
        cursor.execute(sql)

        columns = [column[0] for column in cursor.description]
        results = []

        for row in cursor.fetchall():
            row_dict = dict(zip(columns, row))
            results.append(data_class(**row_dict))

        return results

def insert(table, obj):
    record = asdict(obj)
    record.pop(attribute_id_name(table), None)

    with get_db_connection() as connection:
        attributes = ", ".join(record.keys())
        question_marks = ", ".join(["?"] * len(record.keys()))
        sql = f"INSERT INTO {table} ({attributes}) OUTPUT INSERTED.id_{table} VALUES ({question_marks})"

        cursor = connection.cursor()
        cursor.execute(sql, *record.values())

        id_record = cursor.fetchone()[0]
        connection.commit()
        return id_record

def delete(table, id_record):
    with get_db_connection() as connection:
        cursor = connection.cursor()
        sql = f"DELETE FROM {table} WHERE {attribute_id_name(table)} = ?"
        cursor.execute(sql, id_record)
        connection.commit()
        return cursor.rowcount > 0


def update(table, obj):
    record = asdict(obj)
    # Získáme hodnotu ID pro podmínku WHERE a následně ji odstraníme z dat k updatu
    if attribute_id_name(table) not in record:
        raise ValueError(f"Objekt neobsahuje primární klíč {attribute_id_name(table)}")

    id_record = record.pop(attribute_id_name(table))
    attributes_and_values = ", ".join([f"{key} = ?" for key in record.keys()])

    with get_db_connection() as connection:
        sql = f"UPDATE {table} SET {attributes_and_values} WHERE {attribute_id_name(table)} = ?"

        values = list(record.values())
        values.append(id_record)

        cursor = connection.cursor()
        cursor.execute(sql, *values)

        connection.commit()


def attribute_id_name(table) -> str:
    return f"id_{table}"
