# mathlib/algebra.py

import math

def solve_linear(a, b):
    """
    Solve a linear equation of the form ax + b = 0.

    Parameters:
    a (float): Coefficient of x.
    b (float): Constant term.

    Returns:
    float: The solution for x.

    Raises:
    ValueError: If `a` is 0, indicating no solution exists.

    Examples:
    >>> solve_linear(2, -4)
    2.0
    >>> solve_linear(0, 5)
    Traceback (most recent call last):
        ...
    ValueError: No solution exists.
    """
    if a == 0:
        raise ValueError("No solution exists.")
    return -b / a

def solve_quadratic(a, b, c):
    """
    Solve a quadratic equation of the form ax^2 + bx + c = 0.

    Parameters:
    a (float): Coefficient of x^2.
    b (float): Coefficient of x.
    c (float): Constant term.

    Returns:
    tuple or None: A tuple containing the real roots of the equation. If no real roots exist, returns None.
                    If there is exactly one real root, it is returned as (root, root).

    Examples:
    >>> solve_quadratic(1, -3, 2)
    (2.0, 1.0)
    >>> solve_quadratic(1, 2, 5)
    None
    >>> solve_quadratic(1, 2, 1)
    (-1.0, -1.0)
    """
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return (root, root)
    else:
        return None  # No real roots
