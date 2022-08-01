# Driver Code.
from charging import *
import unittest

class chargingTest(unittest.TestCase):
    def test_range_and_count(self):
        self.assertEqual(charging_measurement([4, 5]), ['4 - 5, 2'])

if __name__ == '__main__':
      unittest.main()
