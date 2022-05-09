import unittest
from recursion.numbers_sum import numbers_sum
from recursion.count import count
from recursion.mx import mx


class TestRecursion(unittest.TestCase):
    """Test all files in recursion folder."""

    def setUp(self) -> None:
        self.arrays = [
            [11],
            [3, 56, -7, 9],
        ]
        self.mix = [12, 3.14, '', 'abc', '45d', None, False]

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
        with self.subTest(
                msg='List with elements of different types', mix=self.mix):
            self.assertEqual(count(self.mix), len(self.mix))

    def test_mx(self):
        """Test mx function.

        Write a recursive function to find the maximum number in a list.
        """
        with self.subTest(msg='Test empty list'):
            with self.assertRaises(IndexError):
                mx([])
        for array in self.arrays:
            with self.subTest(msg='Test correct input', array=array):
                self.assertEqual(mx(array), max(array))
        with self.subTest(
                msg='List with elements of different types'):
            with self.assertRaises(ValueError):
                mx(self.mix)


if __name__ == '__main__':
    unittest.main()
