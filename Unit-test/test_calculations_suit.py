import unittest

from calculations import (
    add,
    divide,
    mean,
    median,
    mode,
    multiply,
    subtract,
)

class TestArithmeticOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-1, 1), -1)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

class TestStatisticalOperations(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4, 5, 6]), 3.5)

    def test_median_odd(self):
        self.assertEqual(median([1, 3, 3, 6, 7, 8, 9]), 6)

    def test_median_even(self):
        self.assertEqual(median([1, 2, 3, 4, 5, 6, 8, 9]), 4.5)

    def test_median_unsorted(self):
        self.assertEqual(median([7, 1, 3, 3, 2, 6]), 3)

    def test_mode_single(self):
        self.assertEqual(mode([1, 2, 2, 3, 4, 4, 4, 5]), [4])

    def test_mode_multiple(self):
        self.assertEqual(set(mode([1, 1, 2, 3, 4, 4, 5, 5])), {1, 4, 5})

#============================================================
""" 
# First method
In the make_suite() function, you create a list of all tests from the TestArithmeticOperations test case. 

Then, you create and return a test suite using the TestSuite() constructor with the list of tests as an argument.
"""

## Uncomment this one and comment the both the two below to run this one using python test_calculations_suit.py
# def make_suite():
#     arithmetic_tests = [
#         TestArithmeticOperations("test_add"),
#         TestArithmeticOperations("test_subtract"),
#         TestArithmeticOperations("test_multiply"),
#         TestArithmeticOperations("test_divide"),
#     ]
#     return unittest.TestSuite(tests=arithmetic_tests)

# if __name__ == "__main__":
#     suite = make_suite()
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)

#============================================================
""" 
# Second method
This new version of make_suite() works like the previous section. Instead of using the class constructor to 
build the test suite, you use the .addTest() method. This approach can be useful when you have an existing test 
suite, and you need to add more tests to it.
"""
## Uncomment this one and comment the above one and below one tests to run this one using python test_calculations_suit.py
# def make_suite():
#     arithmetic_suite = unittest.TestSuite()
#     arithmetic_suite.addTest(TestArithmeticOperations("test_add"))
#     arithmetic_suite.addTest(TestArithmeticOperations("test_subtract"))
#     arithmetic_suite.addTest(TestArithmeticOperations("test_multiply"))
#     arithmetic_suite.addTest(TestArithmeticOperations("test_divide"))
#     return arithmetic_suite

# if __name__ == "__main__":
#     suite = make_suite()
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)
#============================================================   

#============================================================
""" 
# Third method
The TestSuite class also has a .addTests() method that you can use to add several tests in one go. 
This method takes an iterable of test cases, test suites, or a combination of them. Consider the 
following example that creates a test suite with the statistical tests:
"""
## uncomment for this suit and comment the two above
# def make_suite():
#     statistical_tests = [
#         TestStatisticalOperations("test_mean"),
#         TestStatisticalOperations("test_median_odd"),
#         TestStatisticalOperations("test_median_even"),
#         TestStatisticalOperations("test_median_unsorted"),
#         TestStatisticalOperations("test_mode_single"),
#         TestStatisticalOperations("test_mode_multiple"),
#     ]
#     statistical_suite = unittest.TestSuite()
#     statistical_suite.addTests(statistical_tests)

#     return statistical_suite

# if __name__ == "__main__":
#     suite = make_suite()
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)
    
##==================================================================================================
##====================combined suit ========================================
# uncomment this one if you want to test the combined unittest for the arthemtic and statsitical tests
# def make_suite():
#     # Create a suite for arithmetic tests
#     arithmetic_tests = [
#         TestArithmeticOperations("test_add"),
#         TestArithmeticOperations("test_subtract"),
#         TestArithmeticOperations("test_multiply"),
#         TestArithmeticOperations("test_divide"),
#     ]

#     # Create a suite for statistical tests
#     statistical_tests = [
#         TestStatisticalOperations("test_mean"),
#         TestStatisticalOperations("test_median_odd"),
#         TestStatisticalOperations("test_median_even"),
#         TestStatisticalOperations("test_median_unsorted"),
#         TestStatisticalOperations("test_mode_single"),
#         TestStatisticalOperations("test_mode_multiple"),
#     ]

#     # Combine both suites into one
#     combined_suite = unittest.TestSuite()
#     combined_suite.addTests(arithmetic_tests)
#     combined_suite.addTests(statistical_tests)

#     return combined_suite

# if __name__ == "__main__":
#     suite = make_suite()
#     runner = unittest.TextTestRunner(verbosity=2)
#     runner.run(suite)

##========================Creating Suites With the load_tests() Function ======================================
## uncomment it if you want to run the test using the load_tests
def load_tests(loader, standard_tests, pattern):
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestArithmeticOperations))
    suite.addTests(loader.loadTestsFromTestCase(TestStatisticalOperations))
    return suite

if __name__ == "__main__":
    unittest.main()