"""lettersort.py: A module to sort a list of strings in ascending alphabetical order."""


def sort_by_letter(letter_array: list[str]) -> list[str]:
    """
    Sort a list of strings in ascending alphabetical order.

    Parameters
    ----------
    letter_array : list[str]
        The list of strings to be sorted.

    Returns
    -------
    list[str]
        The sorted list of strings.

    Raises
    ------
    TypeError
        If the input is not a list of strings.

    Examples
    --------
    >>> sort_by_letter(["932c", "832u32", "2344b"])
    ["2344b", "932c", "832u32"]

    >>> sort_by_letter(["99a", "78b", "c2345", "11d"])
    ["99a", "78b", "c2345", "11d"]

    >>> sort_by_letter(["572z", "5y5", "304q2"])
    ["304q2", "5y5", "572z"]

    >>> sort_by_letter([])
    []

    Notes
    -----
    The function is based on the following assumptions...
    1. Each string will only have one (lowercase) letter.
    2. If given an empty list, return an empty list.
    """
    # Check the input type
    if not all(isinstance(letter, str) for letter in letter_array):
        raise TypeError("The input must be a list of strings.")

    # Check if the list is empty
    if len(letter_array) == 0:
        return []

    # Main logic
    letter_dictionary = {}

    for string in letter_array:
        letter = [char for char in string if char.isalpha()][0]
        letter_dictionary[letter] = string

    sorted_letters = sorted(letter_dictionary.keys())

    return [letter_dictionary[letter] for letter in sorted_letters]


def test_sort_by_letter() -> None:
    """Test the sort_by_letter function."""
    assert sort_by_letter(["932c", "832u32", "2344b"]) == ["2344b", "932c", "832u32"]
    assert sort_by_letter(["99a", "78b", "c2345", "11d"]) == [
        "99a",
        "78b",
        "c2345",
        "11d",
    ]
    assert sort_by_letter(["572z", "5y5", "304q2"]) == ["304q2", "5y5", "572z"]
    assert sort_by_letter([]) == []


if __name__ == "__main__":
    test_sort_by_letter()
    print("All tests passed!")
