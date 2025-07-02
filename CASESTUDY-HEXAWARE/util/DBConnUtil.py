import mysql.connector
from mysql.connector import Error
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from util.DBPropertyUtil import DBPropertyUtil



class DBConnUtil:
    @staticmethod
    def get_connection():
        try:
            db_config = DBPropertyUtil.load_db_properties()
            connection = mysql.connector.connect(
                host=db_config['host'],
                database=db_config['database'],
                user=db_config['user'],
                password=db_config['password']
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print("Error connecting to MySQL:", e)
            return None
