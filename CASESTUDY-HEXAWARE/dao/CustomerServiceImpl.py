import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.DBConnUtil import DBConnUtil
from entity.Customer import Customer
from mysql.connector import Error

class CustomerServiceImpl:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def get_customer_by_username(self, username):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Customer WHERE Username = %s", (username,))
            row = cursor.fetchone()
            return Customer(*row) if row else None
        except Error as e:
            print("Error:", e)

    def register_customer(self, customer):
        try:
            cursor = self.conn.cursor()
            sql = """INSERT INTO Customer (FirstName, LastName, Email, PhoneNumber, Username, PasswordHash)
                     VALUES (%s, %s, %s, %s, %s, SHA2(%s, 256))"""
            cursor.execute(sql, (customer.first_name, customer.last_name, customer.email,
                                 customer.phone, customer.username, customer.password_hash))
            self.conn.commit()
        except Error as e:
            print("Error:", e)

    def get_all_customers(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Customer")
            rows = cursor.fetchall()
            return [Customer(*row) for row in rows]
        except Error as e:
            print("Error:", e)
            return []
    
    def update_customer(self, customer):
        try:
            cursor = self.conn.cursor()
            sql = """
            UPDATE Customer
            SET FirstName=%s,
                LastName=%s,
                Email=%s,
                PhoneNumber=%s,
                Username=%s
            WHERE CustomerID=%s
            """
            cursor.execute(sql, (customer.first_name, customer.last_name, customer.email,
                             customer.phone, customer.username, customer.customer_id))
            self.conn.commit()
            return cursor.rowcount > 0
        except Error as e:
            print("Error updating customer:", e)
            return False
