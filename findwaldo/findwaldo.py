"""findwaldo.py: A simple prototype to find a unique character in a grid of characters."""


def find_unique(grid: list[list[str]]) -> tuple[int, int] | None:
    """
    Find the unique character in a grid.

    Parameters
    ----------
    grid : list[list[str]]
        The grid of characters to be checked.

    Returns
    -------
    tuple[int, int] | None
        The coordinates of the unique character in the grid,
        or None if no unique character is found.

    Examples
    --------
    >>> find_unique([
            ["A", "A", "A"],
            ["A", "A", "A"],
            ["A", "B", "A"]
        ])
    (3, 2)

    >>> find_unique([
            ["c", "c", "c", "c"],
            ["c", "c", "c", "d"]
        ])
    (2, 4)

    >>> find_unique([
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"],
            ["P", "O", "O", "O"],
            ["O", "O", "O", "O"]
        ])
    (5, 1)
    """
    # Ensure the grid is at least 2x3
    if len(grid) < 2 or len(grid[0]) < 3:
        return None

    # Select the list which isn't full of the same character
    unique_lists = [row for row in grid if len(set(row)) > 1]
    if len(unique_lists) != 1:
        return None
    else:
        unique_list = unique_lists[0]

    # Find the unique character in the list
    list_chars = list(set(unique_list))

    if unique_list.count(list_chars[0]) == 1:
        unique_char = list_chars[0]
    else:
        unique_char = list_chars[1]

    # Find the coordinates of the unique character
    row_index = grid.index(unique_list) + 1
    col_index = unique_list.index(unique_char) + 1

    return (row_index, col_index)


def test_find_unique() -> None:
    """Test the find_unique function."""
    assert find_unique(
        [
            ["A", "A", "A"],
            ["A", "A", "A"],
            ["A", "B", "A"],
        ]
    ) == (3, 2)

    assert find_unique(
        [
            ["c", "c", "c", "c"],
            ["c", "c", "c", "d"],
        ]
    ) == (2, 4)

    assert find_unique(
        [
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"],
            ["O", "O", "O", "O"],
            ["P", "O", "O", "O"],
            ["O", "O", "O", "O"],
        ]
    ) == (5, 1)

    assert (
        find_unique(
            [
                ["A", "A", "A"],
                ["A", "A", "A"],
                ["A", "A", "A"],
            ]
        )
        is None
    )


if __name__ == "__main__":
    test_find_unique()
    print("All tests passed!")
