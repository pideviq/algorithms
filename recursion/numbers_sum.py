def numbers_sum(array: list) -> int:
    """Add up all the numbers in the array and return the total."""
    try:
        first = int(array[0])
    except IndexError:
        raise IndexError('array is empty')
    except ValueError:
        raise ValueError('array should consist of integers only')
    else:
        if len(array) > 1:
            # Recursive case
            return first + numbers_sum(array[1:])
        # Base case
        return first
