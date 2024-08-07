import math

def sin(x):
    """
    Compute the sine of an angle.

    Parameters:
    x (float): The angle in radians.

    Returns:
    float: The sine of the angle.

    Examples:
    >>> sin(math.pi / 2)
    1.0
    >>> sin(0)
    0.0
    """
    return math.sin(x)

def cos(x):
    """
    Compute the cosine of an angle.

    Parameters:
    x (float): The angle in radians.

    Returns:
    float: The cosine of the angle.

    Examples:
    >>> cos(math.pi)
    -1.0
    >>> cos(0)
    1.0
    """
    return math.cos(x)

def tan(x):
    """
    Compute the tangent of an angle.

    Parameters:
    x (float): The angle in radians.

    Returns:
    float: The tangent of the angle.

    Examples:
    >>> tan(math.pi / 4)
    0.9999999999999999
    >>> tan(0)
    0.0
    """
    return math.tan(x)

def arcsin(x):
    """
    Compute the arc sine of a value.

    Parameters:
    x (float): The value for which to compute the arc sine. Must be in the range [-1, 1].

    Returns:
    float: The arc sine of the value in radians.

    Raises:
    ValueError: If x is not in the range [-1, 1].

    Examples:
    >>> arcsin(1)
    1.5707963267948966
    >>> arcsin(0)
    0.0
    """
    if x < -1 or x > 1:
        raise ValueError("Input must be in the range [-1, 1].")
    return math.asin(x)

def arccos(x):
    """
    Compute the arc cosine of a value.

    Parameters:
    x (float): The value for which to compute the arc cosine. Must be in the range [-1, 1].

    Returns:
    float: The arc cosine of the value in radians.

    Raises:
    ValueError: If x is not in the range [-1, 1].

    Examples:
    >>> arccos(1)
    0.0
    >>> arccos(0)
    1.5707963267948966
    """
    if x < -1 or x > 1:
        raise ValueError("Input must be in the range [-1, 1].")
    return math.acos(x)

def arctan(x):
    """
    Compute the arc tangent of a value.

    Parameters:
    x (float): The value for which to compute the arc tangent.

    Returns:
    float: The arc tangent of the value in radians.

    Examples:
    >>> arctan(1)
    0.7853981633974483
    >>> arctan(0)
    0.0
    """
    return math.atan(x)
