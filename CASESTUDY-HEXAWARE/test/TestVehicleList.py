import unittest
import sys
import os
from datetime import date, timedelta


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dao.VehicleServiceImpl import VehicleServiceImpl

class TestVehicleList(unittest.TestCase):
    def setUp(self):
        self.service = VehicleServiceImpl()

    def test_get_available_vehicles(self):
        start_date = str(date.today() + timedelta(days=1))
        end_date = str(date.today() + timedelta(days=3))

        vehicles = self.service.get_available_vehicles(start_date, end_date)
        self.assertIsInstance(vehicles, list)
        self.assertGreater(len(vehicles), 0)
    def test_get_all_vehicles(self):
        vehicles = self.service.get_all_vehicles()
        self.assertIsInstance(vehicles, list)
        self.assertGreater(len(vehicles), 0)
if __name__ == '__main__':
    unittest.main()
