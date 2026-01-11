import database
from Objects.Brand import Brand

class BrandDAO:

    @staticmethod
    def get_all():
        return database.get_all_as_objects(Brand)

    @staticmethod
    def get_by_id(id_brand):
        return database.get_by_id_as_object(data_class=Brand, id_record=id_brand)

    @staticmethod
    def insert(brand):
        brand.id_brand = database.insert(brand)

    @staticmethod
    def delete(brand):
        return database.delete(brand)

    @staticmethod
    def update(brand):
        return database.update(brand)
