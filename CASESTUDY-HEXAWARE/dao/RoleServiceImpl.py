from util.DBConnUtil import DBConnUtil
from entity.Role import Role
from mysql.connector import Error

class RoleServiceImpl:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def get_all_roles(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Role")
        rows = cursor.fetchall()
        return [Role(*row) for row in rows]

    def get_role_by_id(self, role_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Role WHERE RoleID = %s", (role_id,))
        row = cursor.fetchone()
        return Role(*row) if row else None
