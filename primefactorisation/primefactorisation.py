"""primefactorisation.py: A module to find the prime factors of a number."""


def find_prime_factors(number: int) -> list[int]:
    """
    Find the prime factors of a number.

    Parameters
    ----------
    number : int
        The number for which prime factors are to be found.

    Returns
    -------
    list[int]
        A list of prime factors of the given number.

    Raises
    ------
    ValueError
        If the number is less than 2.

    Examples
    --------
    >>> find_prime_factors(12)
    [2, 2, 3]

    >>> find_prime_factors(56)
    [2, 2, 2, 7]

    >>> find_prime_factors(29)
    [29]
    """
    if number < 2:
        raise ValueError("The number must be greater than or equal to 2.")

    prime_factors = []
    divisor = 2

    while number != 1:
        if number % divisor == 0:
            prime_factors.append(divisor)
            number //= divisor
        else:
            divisor += 1

    return prime_factors


def test_find_prime_factors() -> None:
    """Run the tests for the find_prime_factors function."""
    assert find_prime_factors(12) == [2, 2, 3]
    assert find_prime_factors(56) == [2, 2, 2, 7]
    assert find_prime_factors(29) == [29]


if __name__ == "__main__":
    test_find_prime_factors()
    print("All tests passed!")
