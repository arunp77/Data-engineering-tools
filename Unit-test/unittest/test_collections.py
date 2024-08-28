import unittest

"""_summary_
    In this example, you have several toy tests. The first test compares a tuple with a string using the .assertSequenceEqual() method because they’re both sequences. 
    The test passes because both sequences contain the same set of characters. Note that you can’t perform this test with the .assertEqual() method, so this is a real 
    specialized use case.

    Next, you write similar tests to compare string, list, tuple, dictionary, and set objects. It’s important to highlight that the .assertDictEqual() and 
    .assertSetEqual() methods compare their target objects using the same rules for regular comparisons between dictionaries and sets. They compare the 
    items without considering their order in the collection.
"""

class TestCollections(unittest.TestCase):
    def test_sequence_objects(self):
        a = ("H", "e", "l", "l", "o")
        b = "Hello"
        self.assertSequenceEqual(a, b)

    def test_string_objects(self):
        a = "Hello"
        b = "Hello"
        self. assertMultiLineEqual(a, b)

    def test_list_objects(self):
        a = [1, 2, 3, 4, 5]
        b = [1, 2, 3, 4, 5]
        self.assertListEqual(a, b)

    def test_tuple_objects(self):
        a = ("Jane", 25, "New York")
        b = ("Jane", 25, "New York")
        self.assertTupleEqual(a, b)

    def test_dictionary_objects(self):
        a = {"framework": "unittest", "language": "Python"}
        b = {"language": "Python", "framework": "unittest"}
        self.assertDictEqual(a, b)

    def test_set_objects(self):
        a = {1, 2, 4, 3, 5}
        b = {1, 5, 3, 4, 2}
        self.assertSetEqual(a, b)

if __name__ == "__main__":
    unittest.main(verbosity=2)