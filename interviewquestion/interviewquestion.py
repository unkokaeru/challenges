"""interviewquestion: Find the first unique character in a string."""

from string import ascii_letters


def find_first_unique_character(string: str, accepted_characters: list[str]) -> str:
    """
    Finds the first unique character within a string.

    Parameters
    ----------
    string : str
        The string to test.
    accepted_characters : list[str]
        The possible characters to count.

    Returns
    -------
    str
        The first unique character in the given string.

    Examples
    --------
    >>> print(find_first_unique_character("aadvark"))
    "d"

    >>> print(find_first_unique_character("primark"))
    "p"

    >>> print(find_first_unique_character(""))
    ""

    >>> print(find_first_unique_character("google"))
    "l"

    Raises
    ------
    ValueError
        If no unique characters are found.

    Notes
    -----
    Loops through each character in the string, appending each
    new character into a dictionary as a key, with an initial
    value of 1. Each time the loop repeats a character, it adds
    1 to this value. At the end, it checks to find the first
    character in the dictionary with a value of 1 - utilising
    the ordered nature of dictionaries in Python 3.7.

    Can easily be changed to find the first character with N
    occurences.
    """
    character_counts: dict[str, int] = {}

    if string == "":
        return ""

    for character in string:
        if character in accepted_characters:
            if character in character_counts:
                character_counts[character] += 1
            else:
                character_counts[character] = 1

    for character_count in character_counts:
        count = character_counts[character_count]

        if count == 1:
            return character_count

    raise ValueError("No unique characters found.")


def test_find_first_unique_character() -> None:
    """Test the find_first_unique_character function."""
    assert find_first_unique_character("aadvark", list(ascii_letters)) == "d"
    assert find_first_unique_character("primark", list(ascii_letters)) == "p"
    assert find_first_unique_character("", list(ascii_letters)) == ""
    assert find_first_unique_character("google", list(ascii_letters)) == "l"


if __name__ == "__main__":
    test_find_first_unique_character()
    print("All tests passed!")
