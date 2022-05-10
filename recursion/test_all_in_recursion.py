import unittest
from recursion.numbers_sum import numbers_sum
from recursion.count import count
from recursion.mx import mx
from recursion.greatest_common_divisor import gcd


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
        with self.subTest(msg='Test elements of float type'):
            with self.assertRaises(ValueError):
                numbers_sum([3.14, 9.99])

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

    def test_gcd(self):
        """Test gcd function.

        Write a recursive function for quickly finding the GCD of two integers.
        Use the Euclidean Algorithm as a basis.
        """
        with self.subTest(msg='Test base case'):
            self.assertEqual(gcd(0, 37), 37)
            self.assertEqual(gcd(12, 0), 12)
        with self.subTest(msg='Test correct values'):
            self.assertEqual(gcd(270, 192), 6)
            self.assertEqual(gcd(192, 270), 6)
        with self.subTest(msg='Test GCD equal to 1'):
            self.assertEqual(gcd(13, 7), 1)
            self.assertEqual(gcd(True, False), 1)
        with self.subTest(msg='Test incorrect input'):
            with self.assertRaises(ValueError):
                gcd(3.14, 8)
            with self.assertRaises(ValueError):
                gcd('abc', None)


if __name__ == '__main__':
    unittest.main()
