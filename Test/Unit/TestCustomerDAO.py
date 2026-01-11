import unittest
from DAO.CustomerDAO import CustomerDAO
from Objects.Customer import Customer


class TestCustomerDAO(unittest.TestCase):

    def test_insert_update_delete_find(self):
        customer = Customer("Jana", "Nováková", "jana.novakova@email.cz")
        CustomerDAO.insert(customer)
        try:
            self.assertTrue(customer.id_customer is not None and customer.id_customer >= 0)
            customers = CustomerDAO.get_all()
            self.assertTrue(customer in customers)
            customer.surname = "Vdaná"
            CustomerDAO.update(customer)
            self.assertTrue(customer in CustomerDAO.get_all())
            self.assertTrue(customer == CustomerDAO.get_by_id(customer.id_customer))
        finally:
            CustomerDAO.delete(customer)
        self.assertTrue(customer not in customers)
        customer.name = "Vdaná podruhé"
        self.assertFalse(customer in CustomerDAO.get_all())





if __name__ == '__main__':
    unittest.main()