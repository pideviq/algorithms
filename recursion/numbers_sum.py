def numbers_sum(array: list) -> int:
    """Add up all the numbers in the array and return the total."""
    try:
        first = array[0]
    except IndexError:
        raise IndexError('array is empty')
    else:
        if not isinstance(first, int):
            raise ValueError('array should consist of integers only')
        if len(array) > 1:
            # Recursive case
            return first + numbers_sum(array[1:])
        # Base case
        return first
