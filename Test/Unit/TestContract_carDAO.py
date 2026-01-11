import unittest

from DAO.BrandDAO import BrandDAO
from DAO.CarDAO import CarDAO
from DAO.ContractDAO import ContractDAO
from DAO.Contract_carDAO import Contract_carDAO
from DAO.CustomerDAO import CustomerDAO
from Objects.Brand import Brand
from Objects.Car import Car
from Objects.Contract import Contract
from Objects.Contract_car import Contract_car
from Objects.Customer import Customer

class TestContract_carDAO(unittest.TestCase):

    def test_insert_update_delete_find(self):
        customer = Customer("Jan", "Novak", "janovak@seznam.cz")
        CustomerDAO.insert(customer)
        try:
            self.contract_test(customer)
        finally:
            CustomerDAO.delete(customer)

    def contract_test(self, customer: Customer):
        contract = Contract(1000.0, customer.id_customer)
        ContractDAO.insert(contract)
        try:
            self.brand_test(contract)
        finally:
            ContractDAO.delete(contract)

    def brand_test(self, contract: Contract):
        brand = Brand("Skoda", "Economy")
        BrandDAO.insert(brand)
        try:
            self.car_test(brand, contract)
        finally:
            BrandDAO.delete(brand)

    def car_test(self, brand: Brand, contract: Contract):
        car = Car("88B4PO", "model", 100, False, brand.id_brand)
        CarDAO.insert(car)
        try:
            self.contract_car_test(car, contract)
        finally:
            CarDAO.delete(car)

    def contract_car_test(self, car: Car, contract: Contract):
        contract_car = Contract_car(id_contract=contract.id_contract, id_car=car.id_car)
        Contract_carDAO.insert(contract_car)
        try:
            contract_cars = Contract_carDAO.get_all()
            self.assertTrue(contract_car in contract_cars)
        finally:
            Contract_carDAO.delete(contract_car)
        contract_cars = Contract_carDAO.get_all()
        self.assertTrue(contract_car not in contract_cars)


if __name__ == '__main__':
    unittest.main()