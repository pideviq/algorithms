import unittest
import json
import os
from binarysearch.binary_search import binary_search, binary_search_recursive


class TestBinarySearch(unittest.TestCase):
    """Test Binary Search algorithm."""

    def setUp(self) -> None:
        """Load test data."""
        data_file_full_path = os.path.join(os.path.dirname(__file__),
                                           'data.json')
        with open(data_file_full_path) as test_cases_file:
            self.test_cases = json.load(test_cases_file)
        return None

    def test_search(self):
        """Test correct values."""
        for case in self.test_cases.values():
            with self.subTest(case=case):
                values, search = case['values'], case['search']
                answer = values.index(search)
                self.assertEqual(binary_search(values[:], search), answer)
                self.assertEqual(binary_search_recursive(values[:], search),
                                 answer)

    def test_none(self):
        """Test value out of list."""
        values = [3, 7, 12]
        search = 1
        self.assertIsNone(binary_search(values, search))
        self.assertIsNone(binary_search_recursive(values, search))

    def test_empty_list(self):
        """Test empty list on input."""
        values = []
        search = 1
        self.assertIsNone(binary_search(values, search))
        self.assertIsNone(binary_search_recursive(values, search))


if __name__ == '__main__':
    unittest.main()
