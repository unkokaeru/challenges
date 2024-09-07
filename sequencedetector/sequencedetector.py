"sequencedetector: A module to detect a sequence in a list of numbers." ""

from typing import Literal

SEQUENCE_TYPE = Literal["arithmetic", "geometric", "random"]


def find_sequence_type(sequence: list[float]) -> tuple[SEQUENCE_TYPE, float | None]:
    """
    Detect the type of sequence in a list of numbers.

    Parameters
    ----------
    sequence : list[float]
        The list of numbers to be checked.

    Returns
    -------
    tuple[SEQUENCE_TYPE, float | None]
        A tuple containing the type of sequence and the common difference/ratio.
        If the sequence is random, the second element is None.

    Raises
    ------
    ValueError
        If the length of the sequence is less than 3.

    Examples
    --------
    >>> find_sequence_type([1, 2, 3, 4, 5])
    ('arithmetic', 1)

    >>> find_sequence_type([1, 2, 4, 8, 16])
    ('geometric', 2)

    >>> find_sequence_type([1, 2, 4, 3, 5])
    ('random', None)
    """
    if len(sequence) < 3:
        raise ValueError("The sequence must have at least 3 elements.")

    differences = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
    ratios = [sequence[i + 1] / sequence[i] for i in range(len(sequence) - 1)]

    if all(diff == differences[0] for diff in differences):
        common_difference = differences[0]
        return ("arithmetic", common_difference)
    elif all(ratio == ratios[0] for ratio in ratios):
        common_ratio = ratios[0]
        return ("geometric", common_ratio)
    else:
        return ("random", None)


def predict_sequence(sequence: list[float], term_number: int) -> float | None:
    """
    Predict the nth number in a sequence.

    Parameters
    ----------
    sequence : list[float]
        The list of numbers to be checked.
    term_number : int
        The term number to be predicted.

    Returns
    -------
    float | None
        The nth number in the sequence if it can be predicted, None otherwise.

    Examples
    --------
    >>> predict_sequence([1, 2, 3, 4, 5], 6)
    6

    >>> predict_sequence([1, 2, 4, 8, 16], 6)
    32

    >>> predict_sequence([1, 2, 4, 3, 5], 6)
    None
    """
    sequence_type, common_relationship = find_sequence_type(sequence)

    if common_relationship is None:
        return None

    if sequence_type == "arithmetic":
        first_term = sequence[0]
        return first_term + (term_number - 1) * common_relationship
    elif sequence_type == "geometric":
        first_term = sequence[0]
        return first_term * common_relationship ** (term_number - 1)
    else:
        return None


def test_find_sequence_type() -> None:
    """Test the find_sequence_type function."""
    assert find_sequence_type([1, 2, 3, 4, 5]) == ("arithmetic", 1)
    assert find_sequence_type([1, 2, 4, 8, 16]) == ("geometric", 2)
    assert find_sequence_type([1, 2, 4, 3, 5]) == ("random", None)

    assert predict_sequence([1, 2, 3, 4, 5], 6) == 6
    assert predict_sequence([1, 2, 4, 8, 16], 6) == 32
    assert predict_sequence([1, 2, 4, 3, 5], 6) is None


if __name__ == "__main__":
    test_find_sequence_type()
    print("All tests passed!")
