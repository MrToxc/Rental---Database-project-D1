from DAO.BrandDAO import BrandDAO
from Database.Mapper import get_all, insert, get_by_id, delete, update
from Objects.Car import Car


class CarDAO:

    @staticmethod
    def get_all():
        return get_all(Car)

    @staticmethod
    def get_by_id(id_car):
        return get_by_id(data_class=Car, id_record=id_car)

    @staticmethod
    def insert(car):
        car.id_car = insert(car)

    @staticmethod
    def delete(car):
        return delete(car)

    @staticmethod
    def update(car):
        return update(car)

    @staticmethod
    def get_brand(car):
        return BrandDAO.get_by_id(id_brand=car.id_brand)
