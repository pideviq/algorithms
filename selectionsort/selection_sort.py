SORT_ORDER_TO_EXTREME_TYPE_MAP = {
    'asc': 'low',
    'desc': 'high',
}


def selection_sort(array: list, order: str = 'asc') -> list:
    """Sort the array using Selection Sort algorithm"""
    sorted_array = []
    order = order.lower()
    for i in range(len(array)):
        try:
            index = find_extreme(array, SORT_ORDER_TO_EXTREME_TYPE_MAP[order])
        except KeyError:
            legal_order_values = ', '.join(SORT_ORDER_TO_EXTREME_TYPE_MAP.keys())
            raise TypeError(f'argument "order" must be in ({legal_order_values})')
        else:
            sorted_array.append(array.pop(index))
    return sorted_array


def find_extreme(array: list, _type: str = 'low') -> int:
    """Return the index of the extreme element in the array"""
    # Set initial values
    if len(array):
        index = 0
        extreme = array[index]
    else:
        raise IndexError('array must not be empty')
    # Check _type value
    if _type not in SORT_ORDER_TO_EXTREME_TYPE_MAP.values():
        legal_type_values = ', '.join(SORT_ORDER_TO_EXTREME_TYPE_MAP.values())
        raise TypeError(f'argument "_type" must be in ({legal_type_values})')
    # Find extreme
    for key, value in enumerate(array[1:], 1):
        if (_type == 'low' and value < extreme)\
                or (_type == 'high' and value > extreme):
            index, extreme = key, value
    return index
