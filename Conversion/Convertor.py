import csv
from pathlib import Path
from typing import Type, List, TypeVar

# Type hint for the data objects
T = TypeVar("T")


def convert_csv_to_data_objects_if_exist(input_file_path: str, data_class: Type[T]) -> List[T]:
    if not Path(input_file_path).resolve().exists():
        return []
    return convert_csv_to_data_objects(input_file_path, data_class)


def convert_csv_to_data_objects(input_file_path: str, data_class: Type[T]) -> List[T]:
    """
    Reads a CSV file and converts each row into an instance of the provided data_class.

    :param data_class: The dataclass type to instantiate (e.g., Customer, Car).
    :param input_file_path: Path to the .csv file.
    :return: A list of data_class instances.
    """
    data_objects = []

    try:
        with open(input_file_path, mode='r', encoding='utf-8') as csvfile:
            # DictReader uses the first row as keys for the resulting dictionaries
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Filter out keys that aren't in the dataclass fields if necessary,
                # but usually, DictReader keys match the dataclass attributes.
                # We convert numeric strings to floats/ints if the dataclass expects them.

                # Clean the row data (optional: handling empty strings as None)
                clean_row = {k: (v if v != "" else None) for k, v in row.items()}

                # Instantiate the dataclass using dictionary unpacking
                obj = data_class(**clean_row)
                data_objects.append(obj)

    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {input_file_path} was not found.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while processing the CSV: {e}")

    return data_objects

# NEXTVERSION napsat metody obecne a pro více CSV souboru
def store_old_id(brands):
    for brand in brands:
        brand.old_id = brand.id_brand

def find_new_brand_id(old_brand_id, brands):
    for brand in brands:
        if brand.old_id == old_brand_id:
            return brand.id_brand
    raise RuntimeError(f"Brand {old_brand_id} not found")

def correct_brand_id(cars, brands):
    for car in cars:
       car.id_brand = find_new_brand_id(car.id_brand, brands)
    for brand in brands:
        del brand.old_id