"""smilecounter.py: A simple ascii smiley counter."""


def count_smileys(smileys: list[str]) -> int:
    """
    Count the number of valid smileys in a list of strings.

    Parameters
    ----------
    smileys : list[str]
        A list of strings containing smileys.

    Returns
    -------
    int
        The number of valid smileys in the list of strings.

    Examples
    --------
    >>> count_smileys([":)", ";(", ";}", ":-D"])
    2

    >>> count_smileys([";D", ":-(", ":-)", ";~)"])
    3

    >>> count_smileys([";]", ":[", ";*", ":$", ";-D"])
    1
    """
    valid_smileys = 0

    if not smileys:
        return valid_smileys

    for smiley in smileys:
        if len(smiley) == 2:  # Without nose
            if smiley[0] in [":", ";"] and smiley[1] in [")", "D"]:
                valid_smileys += 1
        elif len(smiley) == 3:  # With nose
            if (
                smiley[0] in [":", ";"]
                and smiley[1] in ["-", "~"]
                and smiley[2] in [")", "D"]
            ):
                valid_smileys += 1

    return valid_smileys


def test_count_smileys() -> None:
    """Test the count_smileys function."""
    assert count_smileys([":)", ";(", ";}", ":-D"]) == 2
    assert count_smileys([";D", ":-(", ":-)", ";~)"]) == 3
    assert count_smileys([";]", ":[", ";*", ":$", ";-D"]) == 1


if __name__ == "__main__":
    test_count_smileys()
    print("All tests passed!")
