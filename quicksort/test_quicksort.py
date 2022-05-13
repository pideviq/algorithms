import unittest
import os
import sys
import json
from quicksort.quicksort import quicksort


class MyTestCase(unittest.TestCase):
    """Test Quicksort algorithm."""

    def setUp(self) -> None:
        """Load test data."""
        data_file_full_path = os.path.join(os.path.dirname(__file__), 'data.json')
        with open(data_file_full_path) as test_cases_file:
            self.test_cases = json.load(test_cases_file)
        return None

    def test_base_case(self):
        """Test base case."""
        self.assertEqual(quicksort([]), [])
        self.assertEqual(quicksort([3]), [3])

    def test_recursive_case(self):
        """Test recursive case."""
        for case in self.test_cases.values():
            with self.subTest(case=case):
                self.assertEqual(quicksort(case['input']), case['output'])

    def test_incorrect_input(self):
        """Test handling illegal values on input."""
        bad_input = [
            [3, 'abc', 9],
            [3, 9, None],
            [3, 7.0, 9],
        ]
        for case in bad_input:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    quicksort(case)

    def test_recursion_depth_limit(self):
        """Test the limit of recursion."""
        max_recursion_depth = sys.getrecursionlimit()
        with self.assertRaises(RecursionError):
            quicksort(list(range(max_recursion_depth+1)))


if __name__ == '__main__':
    unittest.main()
