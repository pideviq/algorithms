def count(items: list) -> int:
    """Count the number of items in a list."""
    try:
        items[0]
    except IndexError:
        # Base case
        return 0
    else:
        # Recursive case
        return 1 + count(items[1:])
