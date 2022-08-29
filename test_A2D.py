from A2D_converter import *
import unittest

class chargingTest(unittest.TestCase):
    def test_range_and_count(self):
        self.assertEqual(A2D_Converter([1,1,1,1,1,1,1,1,1,1,1,0]), 10)
        self.assertEqual(A2D_Converter([1,1,1,1,1,1,1,1,1,1,1,1]), "Error!!!")

        self.assertEqual(A2D_Converter([0,0,0,0,0,0,0,0,0,0]), -15)
        self.assertEqual(A2D_Converter([0,1,1,1,1,1,1,1,1,1]), 0)
        self.assertEqual(A2D_Converter([1,1,1,1,1,1,1,1,1,1]), 15)

        self.assertEqual(A2D_Converter([1,1,1,1,1,1,1,1,1,1,1]), "Invalid Input!")
        self.assertEqual(A2D_Converter([1,1,1,1,1,1,1]), "Invalid Input!")


if __name__ == '__main__':
      unittest.main()