# mathlib/algebra.py

def solve_linear(a, b):
    if a == 0:
        raise ValueError("No solution exists.")
    return -b / a
