from pathlib import Path

from Conversion.Convertor import convert_csv_to_data_objects, store_old_id, correct_brand_id, \
    convert_csv_to_data_objects_if_exist
from DAO.BrandDAO import BrandDAO
from DAO.CarDAO import CarDAO
from DAO.CustomerDAO import CustomerDAO
from Database import DB
from Database.Config import find_file
from Objects.Brand import Brand
from Objects.Car import Car
from Objects.Customer import Customer

customer_csv = find_file("customer.csv")
brand_csv = find_file("brand.csv")
car_csv = find_file("car.csv")

def insert_customers_using_csv():
    customers = convert_csv_to_data_objects_if_exist(customer_csv, Customer)
    try:
        CustomerDAO.insert_all(customers)
    finally:
        pass # CustomerDAO.delete_all(customers)


def insert_cars_using_csv():
    brands = convert_csv_to_data_objects_if_exist(brand_csv, Brand)

    store_old_id(brands)

    try:
        BrandDAO.insert_all(brands)
        insert_cars_using_csv_only(brands)
    finally:
        pass # BrandDAO.delete_all(brands)


def insert_cars_using_csv_only(brands):
    cars = convert_csv_to_data_objects_if_exist(car_csv, Car)
    try:
        correct_brand_id(cars, brands)
        CarDAO.insert_all(cars)
    finally:
        pass # CarDAO.delete_all(cars)

def import_all() -> None:
    DB.global_connection = DB.LongConnection()
    try:
        insert_customers_using_csv()
        insert_cars_using_csv()
    except Exception as e:
        DB.global_connection.really_rollback()
        raise RuntimeError(f"Chyba transakce': {str(e)}") from e
    else:
        DB.global_connection.really_commit()
    finally:
        DB.global_connection.really_close()
        DB.global_connection = None

def print_file_info(file_path):
    print(f"Expected path: {file_path}")
    print(f"Exists: {Path(file_path).resolve().exists()}")

def main() -> None:
    print("=== Import cars, brands and customers if exist in one transaction ===\n")
    print("Expected input: 0 - 3 files in root\n")
    print("Examples: see CSV files Test\\TestData\n")
    print_file_info(customer_csv)
    print_file_info(brand_csv)
    print_file_info(car_csv)
    try:
        import_all()
    except Exception as e:
        print(f"\nERROR: {e}\n")


if __name__ == "__main__":
    main()
