import unittest

from even import is_even

class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        self.assertEqual(is_even(2), True)

    def test_odd_number(self):
        self.assertEqual(is_even(3), False)

    def test_negative_even_number(self):
        self.assertEqual(is_even(-2), True)

    def test_negative_odd_number(self):
        self.assertEqual(is_even(-4), False)

if __name__ == "__main__":
    unittest.main(verbosity=2)