import unittest
from recursion.numbers_sum import numbers_sum
from recursion.count import count


class TestRecursion(unittest.TestCase):
    """Test all files in recursion folder."""

    def setUp(self) -> None:
        self.arrays = [
            [11],
            [3, 56, -7, 9],
        ]

    def test_numbers_sum(self):
        """Test numbers_sum function.

        You're given an array of numbers.
        You have to add up all the numbers and return the total.
        You should do this with a recursive function.
        """
        with self.subTest(msg='Test empty list'):
            with self.assertRaises(IndexError):
                numbers_sum([])
        for array in self.arrays:
            with self.subTest(msg='Correct input', array=array):
                self.assertEqual(numbers_sum(array), sum(array))
        with self.subTest(msg='Non-int elements in the list'):
            with self.assertRaises(ValueError):
                numbers_sum([34, '6x', -9, 'a'])

    def test_cont(self):
        """Test count function.

        Write a recursive function to count the number of items in a list.
        """
        with self.subTest(msg='Test empty list'):
            self.assertEqual(count([]), 0)
        for array in self.arrays:
            with self.subTest(msg='Correct input', array=array):
                self.assertEqual(count(array), len(array))
        mix = [12, 3.14, '', 'abc', '45d', None, False]
        with self.subTest(
                msg='List with elements of different types', mix=mix):
            self.assertEqual(count(mix), len(mix))


if __name__ == '__main__':
    unittest.main()
