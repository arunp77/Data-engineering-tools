import random

def random_integer(low, high):
    """
    Generate a random integer within a specified range.

    Parameters:
    low (int): The lower bound of the range (inclusive).
    high (int): The upper bound of the range (inclusive).

    Returns:
    int: A random integer between low and high, inclusive.

    Examples:
    >>> random_integer(1, 10)
    7
    >>> random_integer(-5, 5)
    -3
    """
    return random.randint(low, high)

def random_float(low, high):
    """
    Generate a random float within a specified range.

    Parameters:
    low (float): The lower bound of the range.
    high (float): The upper bound of the range.

    Returns:
    float: A random float between low and high.

    Examples:
    >>> random_float(1.0, 10.0)
    7.334567
    >>> random_float(-5.0, 5.0)
    -2.6457
    """
    return random.uniform(low, high)
