import sys
import os
import unittest
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dao.CustomerServiceImpl import CustomerServiceImpl
from entity.Customer import Customer

class TestCustomerService(unittest.TestCase):
    
    def setUp(self):
        self.service = CustomerServiceImpl()

    def test_invalid_customer_authentication(self):
        customer = self.service.get_customer_by_username("wrong_user")
        self.assertIsNone(customer)

    def test_update_customer_information(self):
        customer = self.service.get_customer_by_username("durga_m")
        self.assertIsNotNone(customer) 

        print("\nCustomer ID:", customer.customer_id)
        print("Old Phone:", customer.phone)
        print("PasswordHash:", customer.password_hash)
        customer.phone = f"99999{random.randint(10000, 99999)}"
        if not customer.password_hash:
            customer.password_hash = "dummyhash123"

        result = self.service.update_customer(customer)
        self.assertTrue(result)  
if __name__ == '__main__':
    unittest.main()
