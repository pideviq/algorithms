from __future__ import annotations

# NOTE: for Python 3.9 import is not required
__version__ = '3.8'


def binary_search(values: list, search) -> int | None:
    """Search an element in an array using Binary Search algorithm."""
    low = 0
    high = len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        guess = values[middle]
        if guess == search:
            return middle
        if search > guess:
            low = middle + 1
        else:
            high = middle - 1
    return None
