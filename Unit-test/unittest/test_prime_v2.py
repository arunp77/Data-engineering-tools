import unittest

from prime_v2 import is_prime

""" 
The first two tests are familiar. They cover the primary use case of your is_prime() function. 
The third and fourth tests check for those cases where the function gets an argument of an 
incorrect type. These tests specifically check for floating-point numbers and strings.

The fifth test checks for those situations where the input is 0 or 1. In those cases, the 
function must raise a ValueError, so that’s what the assertions catch. Finally, the sixth 
test checks for negative numbers, which must also raise a ValueError. You can run the test 
from your command line to check how they work.
"""

class TestIsPrime(unittest.TestCase):
    def test_prime_number(self):
        self.assertTrue(is_prime(17))

    def test_non_prime_number(self):
        self.assertFalse(is_prime(10))

    def test_invalid_type_float(self):
        with self.assertRaises(TypeError):
            is_prime(4.5)

    def test_invalid_type_str(self):
        with self.assertRaises(TypeError):
            is_prime("5")

    def test_zero_and_one(self):
        with self.assertRaises(ValueError):
            is_prime(0)
        with self.assertRaises(ValueError):
            is_prime(1)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            is_prime(-1)

if __name__ == "__main__":
    unittest.main(verbosity=2)