import unittest
from src.vehicle import Vehicle


class VehicleTest(unittest.TestCase):
    def test_InitVelocity(self):
        self.assertAlmostEqual(Vehicle(1).v, 1)

        self.assertAlmostEqual(Vehicle(5).v, 5)

        self.assertAlmostEqual(Vehicle(9).v, 9)
