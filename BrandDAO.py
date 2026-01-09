import database
from Brand import Brand


class BrandDAO:

    TABLE_NAME = "brand"

    @staticmethod
    def get_all():
        brands = []
        with database.get_db_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT id_brand, name, category FROM brand")
            for row in cursor.fetchall():
                brands.append(Brand(row.name, row.category, row.id_brand))
        return brands

    @staticmethod
    def insert(brand):
        brand.id_brand = database.insert(BrandDAO.TABLE_NAME, brand)

    @staticmethod
    def delete(id_brand):
        return database.delete(BrandDAO.TABLE_NAME, id_brand)

    @staticmethod
    def update(brand):
        return database.update(BrandDAO.TABLE_NAME, brand)
