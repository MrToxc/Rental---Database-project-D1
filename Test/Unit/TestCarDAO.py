import unittest

from Objects.Brand import Brand
from DAO.BrandDAO import BrandDAO
from DAO.CarDAO import CarDAO
from Objects.Car import Car


class TestCarDAO(unittest.TestCase):

    def test_insert_update_delete_find(self):
        brand = Brand("Skoda", "Economy")
        BrandDAO.insert(brand)
        try:
            self.car_test(brand)
        finally:
            BrandDAO.delete(brand)

    def car_test(self, brand: Brand):
        car = Car("88B4PO", "model", 100, False, brand.id_brand)
        CarDAO.insert(car)
        try:
            self.assertTrue(car.id_car is not None and car.id_car >= 0)
            cars = CarDAO.get_all()
            self.assertTrue(car in cars)
            car.model = "model 2"
            CarDAO.update(car)
            self.assertTrue(car in CarDAO.get_all())
            self.assertTrue(car == CarDAO.get_by_id(car.id_car))
            self.assertTrue(car.id_brand == brand.id_brand)
            self.assertTrue(CarDAO.get_brand(car) == brand)
        finally:
            CarDAO.delete(car)
        self.assertTrue(car not in cars)
        car.model = "model 3"
        self.assertFalse(car in CarDAO.get_all())


if __name__ == '__main__':
    unittest.main()