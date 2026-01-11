from Database.Mapper import get_all, insert, get_by_id, delete, update
from Objects.Customer import Customer


class CustomerDAO:

    @staticmethod
    def get_all():
        return get_all(Customer)

    @staticmethod
    def get_by_id(id_customer):
        return get_by_id(data_class=Customer, id_record=id_customer)

    @staticmethod
    def insert(customer):
        customer.id_customer = insert(customer)

    @staticmethod
    def delete(customer):
        return delete(customer)

    @staticmethod
    def update(customer):
        return update(customer)
