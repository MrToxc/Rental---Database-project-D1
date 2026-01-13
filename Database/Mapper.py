from dataclasses import asdict
from Database.DB import get_db_connection


def get_by_id_raw(data_class, id_record):
    table = get_table_from_data_class(data_class)
    id_attribute_name = get_id_attribute_name_from_data_class(data_class)

    with get_db_connection() as connection:
        cursor = connection.cursor()

        sql = f"SELECT * FROM {table} WHERE {id_attribute_name} = ?"
        cursor.execute(sql, id_record)

        row = cursor.fetchone()

        if row is None:
            return None

        # Získání názvů sloupců a vytvoření slovníku
        columns = [column[0] for column in cursor.description]
        return dict(zip(columns, row))


def get_by_id(data_class, id_record):
    data = get_by_id_raw(data_class, id_record)
    if data:
        return data_class(**data)
    return None

def get_all(data_class):
    table = get_table_from_data_class(data_class)
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

def insert(data_object):
    table = get_table_from_data_object(data_object)
    id_attribute_name = get_id_attribute_name_from_data_object(data_object)
    record = asdict(data_object)
    record.pop(id_attribute_name, None)

    with get_db_connection() as connection:
        attributes = ", ".join(record.keys())
        question_marks = ", ".join(["?"] * len(record.keys()))
        sql = f"INSERT INTO {table} ({attributes}) OUTPUT INSERTED.id_{table} VALUES ({question_marks})"
        cursor = connection.cursor()

        try:
            cursor.execute(sql, *record.values())
            id_record = cursor.fetchone()[0]
        except Exception as e:
            connection.rollback()
            raise RuntimeError(f"Chyba při vkládání do tabulky '{table}': {str(e)}") from e
        else:
            connection.commit()
            return id_record

def delete(data_object):
    table = get_table_from_data_object(data_object)
    id_attribute_name = get_id_attribute_name_from_data_object(data_object)
    id_record = getattr(data_object, id_attribute_name)

    with get_db_connection() as connection:
        cursor = connection.cursor()
        sql = f"DELETE FROM {table} WHERE {id_attribute_name} = ?"
        try:
            cursor.execute(sql, id_record)
        except Exception as e:
            connection.rollback()
            raise RuntimeError(f"Chyba při mazani z tabulky '{table}': {str(e)}") from e
        else:
            connection.commit()
        return cursor.rowcount > 0


def update(data_object):
    record = asdict(data_object)
    id_attribute_name = get_id_attribute_name_from_data_object(data_object)
    # Získáme hodnotu ID pro podmínku WHERE a následně ji odstraníme z dat k updatu
    if id_attribute_name not in record:
        raise ValueError(f"Objekt neobsahuje primární klíč {id_attribute_name}")

    id_record = record.pop(id_attribute_name)
    attributes_and_values = ", ".join([f"{key} = ?" for key in record.keys()])

    table = get_table_from_data_object(data_object)

    with get_db_connection() as connection:
        sql = f"UPDATE {table} SET {attributes_and_values} WHERE {id_attribute_name} = ?"

        values = list(record.values())
        values.append(id_record)

        cursor = connection.cursor()
        try:
            cursor.execute(sql, *values)
        except Exception as e:
            connection.rollback()
            raise RuntimeError(f"Chyba při aktualizaci tabulky '{table}': {str(e)}") from e
        else:
            connection.commit()
        return cursor.rowcount > 0


def get_table_from_data_object(data_object) -> str:
    return get_table_from_data_class(type(data_object))

def get_table_from_data_class(data_class) -> str:
    return data_class.__name__.lower()

def get_id_attribute_name_from_data_object(data_object) -> str:
    return get_id_attribute_name_from_data_class(type(data_object))

def get_id_attribute_name_from_data_class(data_class) -> str:
    return get_id_attribute_name_from_table(get_table_from_data_class(data_class))

def get_id_attribute_name_from_table(table) -> str:
    return f"id_{table}"
