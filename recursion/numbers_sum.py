from typing import List


def numbers_sum(array: List[int]) -> int:
    """Add up all the numbers in the array and return the total.

    Return 0 if empty array given.
    """
    # Base case
    if not array:
        return 0
    # Recursive case
    first = array[0]
    if not isinstance(first, int):
        raise ValueError('array should consist of integers only')
    return first + numbers_sum(array[1:])
