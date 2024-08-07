import math

def complex_addition(c1, c2):
    """
    Add two complex numbers.

    Parameters:
    c1 (complex): The first complex number.
    c2 (complex): The second complex number.

    Returns:
    complex: The result of adding c1 and c2.

    Examples:
    >>> complex_addition(1 + 2j, 3 + 4j)
    (4+6j)
    """
    return c1 + c2

def complex_subtraction(c1, c2):
    """
    Subtract one complex number from another.

    Parameters:
    c1 (complex): The complex number to subtract from.
    c2 (complex): The complex number to subtract.

    Returns:
    complex: The result of subtracting c2 from c1.

    Examples:
    >>> complex_subtraction(5 + 6j, 3 + 2j)
    (2+4j)
    """
    return c1 - c2

def complex_multiplication(c1, c2):
    """
    Multiply two complex numbers.

    Parameters:
    c1 (complex): The first complex number.
    c2 (complex): The second complex number.

    Returns:
    complex: The result of multiplying c1 and c2.

    Examples:
    >>> complex_multiplication(1 + 2j, 3 + 4j)
    (-5+10j)
    """
    return c1 * c2

def complex_division(c1, c2):
    """
    Divide one complex number by another.

    Parameters:
    c1 (complex): The complex number to be divided.
    c2 (complex): The complex number to divide by.

    Returns:
    complex: The result of dividing c1 by c2.

    Examples:
    >>> complex_division(1 + 2j, 3 + 4j)
    (0.44+0.08j)
    """
    return c1 / c2

def complex_magnitude(c):
    """
    Compute the magnitude (or absolute value) of a complex number.

    Parameters:
    c (complex): The complex number.

    Returns:
    float: The magnitude of the complex number.

    Examples:
    >>> complex_magnitude(3 + 4j)
    5.0
    """
    return abs(c)

def complex_phase(c):
    """
    Compute the phase (or argument) of a complex number.

    Parameters:
    c (complex): The complex number.

    Returns:
    float: The phase of the complex number in radians.

    Examples:
    >>> complex_phase(1 + 1j)
    0.7853981633974483
    """
    return math.phase(c)
