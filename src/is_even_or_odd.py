def is_even_or_odd(number):
    """
    Determines if a number is even or odd.
    :param number: int
    :return: "even" if number is even, "odd" if number is odd
    """
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    return "even" if number % 2 == 0 else "odd"