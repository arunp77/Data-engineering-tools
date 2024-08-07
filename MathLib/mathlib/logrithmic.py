import math

def exp(x):
    """
    Compute the exponential of a number.

    Parameters:
    x (float): The exponent to which e (Euler's number) is raised.

    Returns:
    float: The value of e raised to the power of x.

    Examples:
    >>> exp(1)
    2.718281828459045
    >>> exp(0)
    1.0
    """
    return math.exp(x)

def log(x, base=math.e):
    """
    Compute the logarithm of a number with a specified base.

    Parameters:
    x (float): The number for which to compute the logarithm.
    base (float): The base of the logarithm (default is e for natural log).

    Returns:
    float: The logarithm of x with the specified base.

    Raises:
    ValueError: If x is less than or equal to 0, or if base is less than or equal to 0 or equal to 1.

    Examples:
    >>> log(10, 10)
    1.0
    >>> log(100, 10)
    2.0
    >>> log(2)
    0.6931471805599453
    """
    if x <= 0 or base <= 0 or base == 1:
        raise ValueError("Invalid input for logarithm.")
    return math.log(x, base)

def log10(x):
    """
    Compute the base-10 logarithm of a number.

    Parameters:
    x (float): The number for which to compute the logarithm.

    Returns:
    float: The base-10 logarithm of x.

    Raises:
    ValueError: If x is less than or equal to 0.

    Examples:
    >>> log10(100)
    2.0
    >>> log10(1)
    0.0
    """
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    return math.log10(x)

def log2(x):
    """
    Compute the base-2 logarithm of a number.

    Parameters:
    x (float): The number for which to compute the logarithm.

    Returns:
    float: The base-2 logarithm of x.

    Raises:
    ValueError: If x is less than or equal to 0.

    Examples:
    >>> log2(8)
    3.0
    >>> log2(1)
    0.0
    """
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    return math.log2(x)
