import unittest
import os
import json
from selectionsort.selection_sort import selection_sort, find_extreme


class TestSelectionSort(unittest.TestCase):
    """Test Selection Sort algorithm."""

    def setUp(self) -> None:
        """Load test data."""
        data_file_full_path = os.path.join(os.path.dirname(__file__), 'data.json')
        with open(data_file_full_path) as test_cases_file:
            self.test_cases = json.load(test_cases_file)
        return None

    def test_find_extreme_illegal_type_value(self):
        """Test illegal value for the '_type' argument."""
        values = [1, 4, 2]
        _type = 'illegal'
        self.assertRaises(TypeError, find_extreme, values, _type)

    def test_find_extreme_empty_array_on_input(self):
        """Test empty array given for the find_extreme function."""
        values = []
        self.assertRaises(IndexError, find_extreme, values)

    def test_find_extreme(self):
        """Test find_extreme function with correct values."""
        values = [2, 143, 1, 9]
        extremes = {
            'low': 2,
            'high': 1,
        }
        for _type, index in extremes.items():
            with self.subTest(_type=_type):
                self.assertEqual(find_extreme(values, _type), index)

    def test_selection_sort_illegal_order_value(self):
        """Test illegal value for the 'order' argument."""
        values = [1, 4, 2]
        order = 'illegal'
        self.assertRaises(TypeError, selection_sort, values, order)

    def test_selection_sort(self):
        """Test correct values."""
        for case in self.test_cases.values():
            with self.subTest(case=case):
                _input, order, output = case['input'], case['order'], case['output']
                self.assertEqual(selection_sort(_input, order=order), output)


if __name__ == '__main__':
    unittest.main()
