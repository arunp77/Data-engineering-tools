import unittest

""" 
This class inherits from TestCase. So, it provides all the assert methods you’ve seen so far. 
In addition, you extend the functionality of TestCase with a new assert method called .assertAllIntegers(), 
which takes a list of values and checks whether all the values are integer numbers.
"""

class CustomTestCase(unittest.TestCase):
    def assertAllIntegers(self, values):
        for value in values:
            self.assertIsInstance(
                value,
                int,
            )

class TestIntegerList(CustomTestCase):
    def test_values_are_integers(self):
        integers_list = [1, 2, 3, 4, 5]
        self.assertAllIntegers(integers_list)

if __name__ == "__main__":
    unittest.main()