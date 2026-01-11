from Database.Mapper import get_all, insert, get_by_id, delete, update
from Objects.Brand import Brand


class BrandDAO:

    @staticmethod
    def get_all():
        return get_all(Brand)

    @staticmethod
    def get_by_id(id_brand):
        return get_by_id(data_class=Brand, id_record=id_brand)

    @staticmethod
    def insert(brand):
        brand.id_brand = insert(brand)

    @staticmethod
    def delete(brand):
        return delete(brand)

    @staticmethod
    def update(brand):
        return update(brand)
