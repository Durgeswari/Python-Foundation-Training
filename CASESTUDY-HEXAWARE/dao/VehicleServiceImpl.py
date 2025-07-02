import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util.DBConnUtil import DBConnUtil
from entity.Vehicle import Vehicle
from mysql.connector import Error

class VehicleServiceImpl:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def get_all_vehicles(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Vehicle")
        return [Vehicle(*row) for row in cursor.fetchall()]

    def get_available_vehicles(self, start_date, end_date):
        cursor = self.conn.cursor()
        query = """
        SELECT * FROM vehicle v
        WHERE v.vehicleid NOT IN (
        SELECT r.vehicleid FROM reservation r
        WHERE NOT (
            r.enddate < %s OR r.startdate > %s
        )
        )
        """
        print("Checking available vehicles from", start_date, "to", end_date)

        cursor.execute(query, (start_date, end_date))
        rows = cursor.fetchall()
        return [Vehicle(*row) for row in rows]



    def get_vehicle_by_id(self, vehicle_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Vehicle WHERE VehicleID = %s", (vehicle_id,))
        row = cursor.fetchone()
        return Vehicle(*row) if row else None


    def add_vehicle(self, vehicle):
        try:
            cursor = self.conn.cursor()
            sql = """INSERT INTO Vehicle (Model, Make, Year, Color, RegistrationNumber, DailyRate, Availability)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (vehicle.model, vehicle.make, vehicle.year, vehicle.color,
                             vehicle.registration_number, vehicle.daily_rate, vehicle.availability))
            self.conn.commit()
            return cursor.rowcount > 0 
        except Error as e:
            print("Error inserting vehicle:", e)
            return False


    def update_vehicle(self, vehicle):
        try:
            cursor = self.conn.cursor()
            sql = """UPDATE Vehicle SET Model=%s, Make=%s, Year=%s, Color=%s,
                    RegistrationNumber=%s, DailyRate=%s, Availability=%s WHERE VehicleID=%s"""
            cursor.execute(sql, (vehicle.model, vehicle.make, vehicle.year, vehicle.color,
                                vehicle.registration_number, vehicle.daily_rate, vehicle.availability,
                                vehicle.vehicle_id))
            self.conn.commit()
            return cursor.rowcount > 0  
        except Error as e:
            print("Error updating vehicle:", e)
            return False
        
    def get_vehicle_by_registration_number(self, reg_number):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Vehicle WHERE RegistrationNumber = %s", (reg_number,))
        row = cursor.fetchone()
        return Vehicle(*row) if row else None


    def delete_vehicle(self, vehicle_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM Vehicle WHERE VehicleID = %s", (vehicle_id,))
        self.conn.commit()
