import sys
import os
import random
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from dao.VehicleServiceImpl import VehicleServiceImpl
from entity.Vehicle import Vehicle

class TestVehicleAddUpdate(unittest.TestCase):

    def setUp(self):
        self.service = VehicleServiceImpl()
        self.test_reg_number = "TN78TEST" + str(random.randint(1000, 9999))

    def tearDown(self):
        cursor = self.service.conn.cursor()
        cursor.execute("DELETE FROM Vehicle WHERE RegistrationNumber = %s", (self.test_reg_number,))
        self.service.conn.commit()

    def test_add_new_vehicle(self):
        """Test 3: Add a new vehicle"""
        vehicle = Vehicle(
            vehicle_id=None,
            model="Fronx",
            make="Maruti",
            year=2024,
            color="Maroon",
            registration_number=self.test_reg_number,
            daily_rate=1350.0,
            availability=True
        )
        result = self.service.add_vehicle(vehicle)
        self.assertTrue(result)

    def test_update_vehicle_details(self):
        """Test 4: Update color of an existing vehicle"""
        vehicle = Vehicle(
            vehicle_id=None,
            model="Fronx",
            make="Maruti",
            year=2024,
            color="Red",
            registration_number=self.test_reg_number,
            daily_rate=1350.0,
            availability=True
        )
        added = self.service.add_vehicle(vehicle)
        self.assertTrue(added)
        vehicle = self.service.get_vehicle_by_registration_number(self.test_reg_number)
        self.assertIsNotNone(vehicle)
        vehicle.color = "Matte Black"
        updated = self.service.update_vehicle(vehicle)
        self.assertTrue(updated)

if __name__ == '__main__':
    unittest.main()
