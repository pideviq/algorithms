from typing import List


def quicksort(array: List[int]) -> list:
    """Sort elements in array in ascending order.

    Quicksort algorithm demonstration.
    Is useless with big datasets because of recursion depth limit.
    """
    # Base case
    if len(array) < 2:
        return array
    # Recursive case
    pivot = array[0]
    less = []
    greater = []
    for i in array[1:]:
        if not isinstance(i, int):
            raise ValueError('array should consist of integers only')
        if i > pivot:
            greater.append(i)
        else:
            less.append(i)
    return quicksort(less) + [pivot] + quicksort(greater)
