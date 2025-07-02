import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from util.DBConnUtil import DBConnUtil
from entity.Reservation import Reservation
from mysql.connector import Error

class ReservationServiceImpl:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()

    def get_reservation_by_id(self, reservation_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Reservation WHERE ReservationID = %s", (reservation_id,))
        row = cursor.fetchone()
        return Reservation(*row) if row else None

    def get_reservations_by_customer_id(self, customer_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Reservation WHERE CustomerID = %s", (customer_id,))
        return [Reservation(*row) for row in cursor.fetchall()]

    def create_reservation(self, reservation):
        cursor = self.conn.cursor()
        sql = """INSERT INTO Reservation (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status)
                 VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (reservation.customer_id, reservation.vehicle_id,
                             reservation.start_date, reservation.end_date,
                             reservation.total_cost, reservation.status))
        self.conn.commit()

    def update_reservation(self, reservation):
        cursor = self.conn.cursor()
        sql = """UPDATE Reservation SET StartDate=%s, EndDate=%s, TotalCost=%s, Status=%s
                 WHERE ReservationID=%s"""
        cursor.execute(sql, (reservation.start_date, reservation.end_date,
                             reservation.total_cost, reservation.status,
                             reservation.reservation_id))
        self.conn.commit()

    def cancel_reservation(self, reservation_id):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE Reservation SET Status='Cancelled' WHERE ReservationID = %s", (reservation_id,))
        self.conn.commit()
