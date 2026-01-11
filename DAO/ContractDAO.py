from DAO.CustomerDAO import CustomerDAO
from Database.Mapper import get_all, insert, get_by_id, delete, update
from Objects.Contract import Contract


class ContractDAO:

    @staticmethod
    def get_all():
        return get_all(Contract)

    @staticmethod
    def get_by_id(id_contract):
        return get_by_id(data_class=Contract, id_record=id_contract)

    @staticmethod
    def insert(contract):
        contract.id_contract = insert(contract)

    @staticmethod
    def delete(contract):
        return delete(contract)

    @staticmethod
    def update(contract):
        return update(contract)

    @staticmethod
    def get_customer(contract):
        return CustomerDAO.get_by_id(contract.id_customer)

