def add(a, b):
    """Compute and return the sum of two numbers.

    Usage examples:
    >>> add(4.0, 2.0)
    6.0
    >>> add(4, 2)
    6.0
    """
    return float(a + b)


# ## This is added for testing the error handling section. 
# ## 8. Writing doctest Tests for Catching Exceptions
# def divide(a, b):
#     return float(a / b)


# Now handling the error can be done in devide function using folloiwng:

def divide(a, b):
    """Compute and return the quotient of two numbers.

    Usage examples:
    >>> divide(84, 2)
    42.0
    >>> divide(15, 3)
    5.0
    >>> divide(42, -2)
    -21.0

    >>> divide(42, 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    """
    return float(a / b)