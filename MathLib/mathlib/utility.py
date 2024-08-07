import math

def factorial(n):
    """
    Compute the factorial of a non-negative integer.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be computed.

    Returns:
    int: The factorial of the input integer.

    Raises:
    ValueError: If n is a negative integer.

    Examples:
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    return math.factorial(n)

def gcd(a, b):
    """
    Compute the greatest common divisor (GCD) of two integers.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The greatest common divisor of a and b.

    Examples:
    >>> gcd(48, 18)
    6
    >>> gcd(101, 10)
    1
    """
    return math.gcd(a, b)

def lcm(a, b):
    """
    Compute the least common multiple (LCM) of two integers.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The least common multiple of a and b.

    Examples:
    >>> lcm(4, 5)
    20
    >>> lcm(21, 6)
    42
    """
    return abs(a * b) // gcd(a, b)
