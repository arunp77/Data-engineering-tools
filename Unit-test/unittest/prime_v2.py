from math import sqrt

"""_summary_
In this updated version of is_prime(), you have two conditional statements. The first conditional ensures that 
the input number is an integer. If that’s not the case, then your code raises a TypeError with an appropriate error message.

The second conditional checks for input numbers greater than 2. If the input number is 1 or lower, then you raise a ValueError. 
The rest of the code is similar to what you’ve already seen.
"""

def is_prime(number):
    if not isinstance(number, int):
        raise TypeError(
            f"integer number expected, got {type(number).__name__}"
        )
    if number < 2:
        raise ValueError(f"integer above 1 expected, got {number}")
    for candidate in range(2, int(sqrt(number)) + 1):
        if number % candidate == 0:
            return False
    return True