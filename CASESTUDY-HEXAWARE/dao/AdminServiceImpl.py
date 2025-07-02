import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util.DBConnUtil import DBConnUtil
from entity.Admin import Admin
from mysql.connector import Error

class AdminServiceImpl:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def get_admin_by_username(self, username):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Admin WHERE Username = %s", (username,))
        row = cursor.fetchone()
        return Admin(*row) if row else None

    def register_admin(self, admin):
        cursor = self.conn.cursor()
        sql = """INSERT INTO Admin (FirstName, LastName, Email, PhoneNumber, Username, PasswordHash, RoleID)
                 VALUES (%s, %s, %s, %s, %s, SHA2(%s, 256), %s)"""
        cursor.execute(sql, (admin.first_name, admin.last_name, admin.email, admin.phone,
                             admin.username, admin.password_hash, admin.role_id))
        self.conn.commit()
