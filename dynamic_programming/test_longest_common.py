import unittest
from dynamic_programming.longest_common import substring, subsequence


class TestLongestCommonSubstring(unittest.TestCase):
    """Test work of substring function."""

    def setUp(self) -> None:
        self.substring_cases = [
            {
                'input': ('hish',
                          'fish'),
                'output': 3,
            },
            {
                'input': ('vista',
                          'fish'),
                'output': 2,
            },
            {
                'input': ('blue',
                          'clues'),
                'output': 3,
            },
            {
                'input': ('apple',
                          'duck'),
                'output': 0,
            },
            {
                'input': ('text with spaces',
                          'another string'),
                'output': 2,
            },
        ]
        self.subsequence_cases = [
            {
                'input': ('fosh',
                          'fort'),
                'output': 2,
            },
            {
                'input': ('fosh',
                          'fish'),
                'output': 3,
            },
            {
                'input': ('apple',
                          'duck'),
                'output': 0,
            },
            {
                'input': ('text with spaces',
                          'another string'),
                'output': 4,
            },
        ]

    def test_substring(self):
        """Test the longest common substring algorithm."""
        for case in self.substring_cases:
            with self.subTest(strings=case['input'], answer=case['output']):
                self.assertEqual(case['output'], substring(*case['input']))

    def test_subsequence(self):
        """Test the longest common subsequence algorithm."""
        for case in self.subsequence_cases:
            with self.subTest(strings=case['input'], answer=case['output']):
                self.assertEqual(case['output'], subsequence(*case['input']))


if __name__ == '__main__':
    unittest.main()
