def gcd(a: int, b: int) -> int:
    """Find the Greatest Common Divisor of two integers.

    Based on the Euclidean Algorithm.
    """
    # Filter incorrect input
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError('a and b must be integers')
    # Base case
    if a == 0:
        return b
    if b == 0:
        return a
    # Recursive case
    a, b = max(a, b), min(a, b)
    remainder = a % b
    return gcd(b, remainder)
