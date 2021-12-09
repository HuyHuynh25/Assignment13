########################################################################
 ##
 ## CS 101 Lab
 ## Program 13
 ## Name: Huynh Gia Huy-Jim Huynh
 ## Email: hghydv@umsystem.edu
 ##
 ## PROBLEM : Create write a program to use the turtle 
 ## module to draw on the screen a little
 ##      Step 1:  Start
 ##      Step 2:  Import math
 ##      Step 3:  Import unittest
 ##      Step 4:  Import Grade(you will create equation from other file)
 ##      Step 5:  Define class Grade_Test(unittest.TestCase)
 ##      Step 6:  Define function test_total_returns_total_of_list(self)
 ##      Step 7:  Define function test_total_returns_0(self)
 ##      Step 8:  Define function test_average_two(self)
 ##      Step 9:  Define function test_average_returns_nan(self)
 ##      Step 10: Define function test_median_returns_one(self)
 ##      Step 11: Define function test_median_returns_two(self)
 ##      Step 12: Define function test_median_raise_error(self)
 ##      Step 13: Make an if __name__ == "__main__"
 ##      Step 14: Call unittest.main()
 ##      Step 15: End
 ##ERROR HANDLING
 ##      N/A
 ##
 ## OTHER COMMENTS:
 ##      Any special comments
 ##
 ########################################################################
import math
import unittest
import Grade
class Grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = Grade.total([1, 10, 22])
        self.assertEqual(result, 33, "The total function should return 33")
    def test_total_returns_0(self):
        result = Grade.total([])
        self.assertEqual(result, 0, "The total function should return 0")
    def test_average_one(self):
        result = Grade.average([2, 5, 9])
        self.assertAlmostEqual(result, 5.33333, 5, "The average should return 5.33333")
    def test_average_two(self):
        result = Grade.average([2, 15, 22, 9])
        self.assertAlmostEqual(result, 12.0000, 4, "The average should return 12")
    def test_average_returns_nan(self):
        result = Grade.average([])
        self.assertIs(result, math.nan, "The average should return nan")
    def test_median_returns_one(self):
        result = Grade.median([2, 5, 1])
        self.assertEqual(result, 2, "The median should return 2")
    def test_median_returns_two(self):
        result = Grade.median([5, 2, 1, 3])
        self.assertAlmostEqual(result, 2.5, 1, "The median should return 2.5")
    def test_median_raise_error(self):
        with self.assertRaises(ValueError):
            result = Grade.median([])
            return result
if __name__ == "__main__":
    unittest.main()
