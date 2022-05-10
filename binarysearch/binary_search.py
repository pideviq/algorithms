from __future__ import annotations
from typing import List

# NOTE: for Python 3.9 import of annotations is not required
__version__ = '3.8'


def binary_search(values: List[int], search) -> int | None:
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


def binary_search_recursive(values: List[int], search) -> int | None:
    """Search an element in an array using Binary Search algorithm.

    Divide-and-Conquer Edition.
    """
    # Base case
    if not values:
        return None
    # Recursive case
    high = len(values) - 1
    middle = high // 2
    guess = values[middle]
    if guess == search:
        return middle
    elif guess > search:
        return binary_search_recursive(values[:middle], search)
    else:
        new_low = middle + 1
        index = binary_search_recursive(values[new_low:], search)
        return None if index is None else new_low + index
