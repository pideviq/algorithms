from typing import List


def mx(array: List[int]) -> int:
    """Find the maximum number in a list."""
    try:
        first = array[0]
    except IndexError:
        raise IndexError('array is empty')
    else:
        if not isinstance(first, int):
            raise ValueError('array should consist of integers only')
        if rest := array[1:]:
            # Recursive case
            max_in_rest = mx(rest)
            return first if first > max_in_rest else max_in_rest
        else:
            # Base case
            return first
