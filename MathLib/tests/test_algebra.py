# tests/test_algebra.py

import pytest
from mathlib.algebra import solve_linear

def test_solve_linear():
    assert solve_linear(2, -4) == 2

def test_solve_linear_no_solution():
    with pytest.raises(ValueError):
        solve_linear(0, 4)
