from charging import *
import unittest

class chargingTest(unittest.TestCase):
    def test_range_and_count(self):
        self.assertEqual(charging_measurement([4, 5]), ['4 - 5, 2'])
        self.assertEqual(charging_measurement([3, 3, 5, 4, 10, 11, 12]), ['3 - 5, 4', '10 - 12, 3'])

if __name__ == '__main__':
      unittest.main()