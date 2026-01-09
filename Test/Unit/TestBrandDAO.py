import unittest
from BrandDAO import BrandDAO
from Brand import Brand


class TestBrandDAO(unittest.TestCase):
    def test_insert_update_delete_find(self):
        brand = Brand("BMW", "Standard")
        BrandDAO.insert(brand)
        try:
            self.assertTrue(brand.id_brand is not None and brand.id_brand >= 0)
            brands = BrandDAO.get_all()
            self.assertTrue(brand in brands)
            brand.name = "Mercedes"
            brand.category = "Luxury"
            BrandDAO.update(brand)
            self.assertTrue(brand in BrandDAO.get_all())
        finally:
            BrandDAO.delete(brand.id_brand)
        self.assertTrue(brand not in brands)
        brand.name = "Toyota"
        self.assertFalse(brand in BrandDAO.get_all())










if __name__ == '__main__':
    unittest.main()