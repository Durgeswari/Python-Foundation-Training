import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util.DBConnUtil import DBConnUtil
from entity.Address import Address
from mysql.connector import Error

class AddressServiceImpl:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def get_addresses_by_customer_id(self, customer_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Address WHERE CustomerID = %s", (customer_id,))
        print("CustomerID:",customer_id)
        rows = cursor.fetchall()
        return [Address(*row) for row in rows]

    def add_address(self, address):
        cursor = self.conn.cursor()
        sql = """INSERT INTO Address (CustomerID, Street, City, State, ZIP, AddressType)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (address.customer_id, address.street, address.city,
                             address.state, address.zip_code, address.address_type))
        self.conn.commit()
