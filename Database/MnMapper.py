from dataclasses import asdict
from Database.DB import get_db_connection
from Database.Mapper import get_table_from_data_class, get_id_attribute_name_from_data_object, \
    get_table_from_data_object


def get_filtered(data_class, data_object):
    table = get_table_from_data_class(data_class)
    id_attribute_name = get_id_attribute_name_from_data_object(data_object)
    id_attribute_value = getattr(data_object, id_attribute_name)

    with get_db_connection() as connection:
        cursor = connection.cursor()
        sql = f"SELECT * FROM {table} WHERE {id_attribute_name} = ?"
        cursor.execute(sql, id_attribute_value)

        columns = [column[0] for column in cursor.description]
        results = []

        for row in cursor.fetchall():
            row_dict = dict(zip(columns, row))
            results.append(data_class(**row_dict))

        return results

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
    record = asdict(data_object)

    with get_db_connection() as connection:
        attributes = ", ".join(record.keys())
        question_marks = ", ".join(["?"] * len(record.keys()))
        sql = f"INSERT INTO {table} ({attributes}) VALUES ({question_marks})"
        cursor = connection.cursor()
        try:
            cursor.execute(sql, *record.values())
        except Exception as e:
            connection.rollback()
            raise RuntimeError(f"Chyba při vkladani do tabulky '{table}': {str(e)}") from e
        connection.commit()

def delete(data_object):
    table = get_table_from_data_object(data_object)
    record = asdict(data_object)
    condition = " AND ".join([f"{key} = ?" for key in record.keys()])

    with get_db_connection() as connection:
        cursor = connection.cursor()
        sql = f"DELETE FROM {table} WHERE {condition}"
        try:
            cursor.execute(sql, *record.values())
        except Exception as e:
            connection.rollback()
            raise RuntimeError(f"Chyba při mazani z tabulky '{table}': {str(e)}") from e
        else:
            connection.commit()
        return cursor.rowcount > 0

