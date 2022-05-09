import unittest
from recursion.numbers_sum import numbers_sum


class TestRecursion(unittest.TestCase):
    """Test all files in recursion folder."""

    def test_numbers_sum(self):
        """Test numbers_sum function.

        You're given an array of numbers.
        You have to add up all the numbers and return the total.
        You should do this with a recursive function.
        """
        with self.subTest(msg='Test empty list'):
            with self.assertRaises(IndexError):
                numbers_sum([])
        arrays = [
            [11],
            [3, 56, -7, 9],
        ]
        for array in arrays:
            with self.subTest(msg='Correct input', array=array):
                self.assertEqual(numbers_sum(array), sum(array))
        with self.subTest(msg='Non-int elements in the list'):
            with self.assertRaises(ValueError):
                numbers_sum([34, '6x', -9, 'a'])


if __name__ == '__main__':
    unittest.main()
