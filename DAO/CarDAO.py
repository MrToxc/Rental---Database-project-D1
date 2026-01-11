import database
from BrandDAO import BrandDAO
from Objects.Car import Car

class CarDAO:

    @staticmethod
    def get_all():
        return database.get_all_as_objects(Car)

    @staticmethod
    def get_by_id(id_car):
        return database.get_by_id_as_object(data_class=Car, id_record=id_car)

    @staticmethod
    def insert(car):
        car.id_car = database.insert(car)

    @staticmethod
    def delete(car):
        return database.delete(car)

    @staticmethod
    def update(car):
        return database.update(car)

    @staticmethod
    def get_brand(car):
        return BrandDAO.get_by_id(id_brand=car.id_brand)
