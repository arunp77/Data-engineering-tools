# mathlib/__init__.py

from .arithmetic import add, subtract, multiply, divide, power, sqrt
from .algebra import solve_linear, solve_quadratic
from .trigonometry import sin, cos, tan, arcsin, arccos, arctan
from .statistics import mean, median, mode, variance, standard_deviation
from .matrix_operations import matrix_addition, matrix_multiplication, matrix_determinant, matrix_inverse
from .complex_numbers import complex_addition, complex_subtraction, complex_multiplication, complex_division, complex_magnitude, complex_phase
from .random_utils import random_integer, random_float
from .utility import factorial, gcd, lcm

__all__ = [
    'add', 'subtract', 'multiply', 'divide', 'power', 'sqrt',
    'solve_linear', 'solve_quadratic',
    'sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan',
    'mean', 'median', 'mode', 'variance', 'standard_deviation',
    'matrix_addition', 'matrix_multiplication', 'matrix_determinant', 'matrix_inverse',
    'complex_addition', 'complex_subtraction', 'complex_multiplication', 'complex_division', 'complex_magnitude', 'complex_phase',
    'random_integer', 'random_float',
    'factorial', 'gcd', 'lcm'
]
