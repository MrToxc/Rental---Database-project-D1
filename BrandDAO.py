import database
from Brand import Brand


class BrandDAO:

    TABLE_NAME = "brand"

    @staticmethod
    def get_all():
        return database.get_all_as_objects(BrandDAO.TABLE_NAME, Brand)

    @staticmethod
    def get_by_id(id_brand):
        return database.get_by_id_as_object(BrandDAO.TABLE_NAME, id_brand, Brand)

    @staticmethod
    def insert(brand):
        brand.id_brand = database.insert(BrandDAO.TABLE_NAME, brand)

    @staticmethod
    def delete(id_brand):
        return database.delete(BrandDAO.TABLE_NAME, id_brand)

    @staticmethod
    def update(brand):
        return database.update(BrandDAO.TABLE_NAME, brand)
