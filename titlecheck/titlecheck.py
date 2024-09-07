"""titlecheck.py: A module for checking if a string is a title."""


def is_title(string_to_check: str) -> bool:
    """
    Check if a string is formatted as a title,
    such that every word of the string starts
    with a letter in upper case.

    Parameters
    ----------
    string_to_check: str
        The string to be checked.

    Returns
    -------
    bool
        True if the string is a title, False otherwise.

    Examples
    --------
    >>> is_title("A Mind Boggling Achievement")
    True

    >>> is_title("A Simple C++ Program!")
    True

    >>> is_title("Water is transparent")
    False

    Notes
    -----
    Loops through each character of the string and
    checks if the character is the first letter of
    a word. If it is, then it checks if the letter
    is in upper case. If not, then the function
    returns False.
    The loop continues until either the end of the
    string, or a False is returned. If the loop
    completes without returning False, then the
    function returns True.
    """

    def is_letter(char: str) -> bool:
        """
        Check if a character is a letter.

        Parameters
        ----------
        char : str
            The character to be checked.

        Returns
        -------
        bool
            True if the character is a letter, False otherwise.

        Examples
        --------
        >>> is_letter("a")
        True

        >>> is_letter("1")
        False
        """
        return char.isalpha()

    def is_uppercase(char: str) -> bool:
        """
        Check if a character is in upper case.

        Parameters
        ----------
        char : str
            The character to be checked.

        Returns
        -------
        bool
            True if the character is in upper case, False otherwise.

        Examples
        --------
        >>> is_uppercase("A")
        True

        >>> is_uppercase("a")
        False
        """
        return char == char.upper()

    for i, char in enumerate(string_to_check):
        if i == 0:
            if is_letter(char) and not is_uppercase(char):
                return False
        elif char == " ":
            if is_letter(string_to_check[i + 1]) and not is_uppercase(
                string_to_check[i + 1]
            ):
                return False

    return True


def test_is_title() -> None:
    """Test the is_title function."""
    assert is_title("A Mind Boggling Achievement")
    assert is_title("A Simple C++ Program!")
    assert not is_title("Water is transparent")


if __name__ == "__main__":
    test_is_title()
    print("All tests passed!")
