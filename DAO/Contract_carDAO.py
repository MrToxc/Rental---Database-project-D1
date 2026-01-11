from Database.MnMapper import get_all, insert, delete
from Objects.Contract_car import Contract_car


class Contract_carDAO:

    @staticmethod
    def get_all():
        return get_all(Contract_car)

    @staticmethod
    def insert(contract_car):
        insert(contract_car)

    @staticmethod
    def delete(contract_car):
        return delete(contract_car)
