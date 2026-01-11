import database
from Objects.Customer import Customer

class CustomerDAO:

    @staticmethod
    def get_all():
        return database.get_all_as_objects(Customer)

    @staticmethod
    def get_by_id(id_customer):
        return database.get_by_id_as_object(data_class=Customer, id_record=id_customer)

    @staticmethod
    def insert(customer):
        customer.id_customer = database.insert(customer)

    @staticmethod
    def delete(customer):
        return database.delete(customer)

    @staticmethod
    def update(customer):
        return database.update(customer)
