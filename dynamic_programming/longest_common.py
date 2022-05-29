def substring(string_a: str, string_b: str) -> int:
    """Return the length of the longest common substring of two strings.

    Arguments:
        string_a -- arbitrary string
        string_b -- arbitrary string
    """
    grid = [[0 for _ in string_a] for _ in string_b]
    for row, letter_b in enumerate(string_b):
        for col, letter_a in enumerate(string_a):
            if letter_a == letter_b:
                top_left_neighbor = grid[row - 1][col - 1]\
                    if row > 0 and col > 0 else 0
                grid[row][col] = top_left_neighbor + 1
    return max(max(grid, key=max))


def subsequence(string_a: str, string_b: str) -> int:
    """Return the length of the longest common subsequence of two strings.

    Arguments:
        string_a -- arbitrary string
        string_b -- arbitrary string
    """
    grid = [[0 for _ in string_a] for _ in string_b]
    for row, letter_b in enumerate(string_b):
        for col, letter_a in enumerate(string_a):
            if letter_a == letter_b:
                top_left_neighbor = grid[row - 1][col - 1]\
                    if row > 0 and col > 0 else 0
                grid[row][col] = top_left_neighbor + 1
            else:
                left_neighbor = grid[row][col - 1] if col > 0 else 0
                top_neighbor = grid[row - 1][col] if row > 0 else 0
                grid[row][col] = max(left_neighbor, top_neighbor)
    return grid[len(string_b) - 1][len(string_a) - 1]
