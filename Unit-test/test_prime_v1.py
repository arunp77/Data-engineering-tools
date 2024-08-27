import unittest

from prime_v1 import is_prime

""""
In this example, you have a TestIsPrime class with two methods. The first method tests is_prime() with 
a prime number, which must result in True, so you use .assertTrue() for the check. The second method 
tests is_prime() with a non-prime number, which must result in False, and you use .assertFalse() in this case.
"""


class TestIsPrime(unittest.TestCase):
    def test_prime_number(self):
        self.assertTrue(is_prime(17))

    def test_non_prime_number(self):
        self.assertFalse(is_prime(10))

if __name__ == "__main__":
    unittest.main(verbosity=2)