# MathLib: A Simple Python Library for Basic Mathematical Operations

MathLib is a simple Python library for basic mathematical operations, including arithmetic and algebraic functions. It's designed to be easy to use and extendable for more advanced mathematical operations.

## Features

- **Arithmetic Operations**: Addition, subtraction, multiplication, and division.
- **Algebraic Operations**: Solving simple linear equations.

## Important steps

### Step 1: Set Up the Project Structure

First, set up your directory structure:

```
mathlib/
├── mathlib/
│   ├── __init__.py
│   ├── arithmetic.py
│   ├── algebra.py
├── tests/
│   ├── test_arithmetic.py
│   ├── test_algebra.py
├── setup.py
├── README.md
└── LICENSE
```

### Step 2: Write the Package Code

#### `mathlib/__init__.py`
This file makes the `mathlib` directory a package.

```python
# mathlib/__init__.py

from .arithmetic import add, subtract, multiply, divide
from .algebra import solve_linear

__all__ = ['add', 'subtract', 'multiply', 'divide', 'solve_linear']
```

#### `mathlib/arithmetic.py`
This module will contain basic arithmetic functions.

```python
# mathlib/arithmetic.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
```

#### `mathlib/algebra.py`
This module will contain algebraic functions.

```python
# mathlib/algebra.py

def solve_linear(a, b):
    if a == 0:
        raise ValueError("No solution exists.")
    return -b / a
```

### Step 3: Write Tests

Create some basic tests for your package.

#### `tests/test_arithmetic.py`

```python
# tests/test_arithmetic.py

import pytest
from mathlib.arithmetic import add, subtract, multiply, divide

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(2, 1) == 1

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 2) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
```

#### `tests/test_algebra.py`

```python
# tests/test_algebra.py

import pytest
from mathlib.algebra import solve_linear

def test_solve_linear():
    assert solve_linear(2, -4) == 2

def test_solve_linear_no_solution():
    with pytest.raises(ValueError):
        solve_linear(0, 4)
```

### Step 4: Set Up the Package Metadata

#### `setup.py`

```python
# setup.py

from setuptools import setup, find_packages

setup(
    name='mathlib',
    version='0.1',
    packages=find_packages(),
    description='A simple math library with basic operations',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Arun Kumar Pandey',
    author_email='arunp77@gmail.com',
    url='https://github.com/arunp77/Data-engineering-tools/matlib',
    license='MIT',
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

```
This `setup.py` file is used to install the package using pip. It includes metadata such as

### Arithmetic Operations

```python
from mathlib import add, subtract, multiply, divide

# Addition
result = add(2, 3)
print(result)  # Output: 5

# Subtraction
result = subtract(5, 2)
print(result)  # Output: 3

# Multiplication
result = multiply(3, 4)
print(result)  # Output: 12

# Division
result = divide(10, 2)
print(result)  # Output: 5.0
```

### Algebraic Operations

```python
from mathlib import solve_linear

# Solve a linear equation ax + b = 0
# Example: 2x + 4 = 0
solution = solve_linear(2, 4)
print(solution)  # Output: -2.0
```

## Testing

To run the tests for this project, use `pytest`:

```bash
pytest tests/
```

This will run the test suite located in the `tests` directory, ensuring that all functions work as expected.

---------

## Installation
- **Step-1: Install the Package Locally**

    You can install MathLib directly from the source code:

    ```bash
    git clone https://github.com/arunp77/Data-engineering-tools.git
    ```
    Navigate to the root directory of your project (where setup.py is located) 
    ```bash
    cd /Data-engineering-tools/mathlib
    ```
    and then run:
    ```bash
    pip install -e . -v
    ```
    The `-e` flag stands for "editable," which means any changes you make to the code will immediately be reflected without needing to reinstall the package. Here `-v` will give you more detailed output about what is happening during the installation process.

    ![alt text](image.png)

    We can alsi install it using:

    ```bash
    pip install mathlib
    ```
    ![alt text](image-1.png)

- **Step 2: Verify Installation**
  
  After running the installation, you can verify that the package was installed by running:

    ```bash
    pip show mathlib
    ```
    This should display information about the mathlib package, such as the version and location.

    > **Verify Import in Python Shell:**
    > Try importing mathlib directly in the Python shell to ensure it is correctly recognized:
    > ```bash
    > >>> import mathlib
    >
    > >>> mathlib
    > ```
> We can also install mathlib, directly using `setup.py` file, using:
> ```bash
> python setup.py install --verbose
> ```
> This will give you more detailed output about what is happening during the installation process.
>
> If you're using `pip install`, you can add the `-v` option for verbose output:


- **Step 3: Run the Tests**
  Once the package is installed, you should run the tests to ensure everything is working as expected.

  Navigate to the root directory of your project and run:
  ```bash
    pytest tests/
  ```
  This will execute the tests defined in `tests/test_arithmetic.py` and `tests/test_algebra.py`. If all the tests pass, it indicates that your package is functioning correctly.

## Contributing

Contributions are welcome! If you'd like to improve MathLib, please fork the repository and create a pull request with your changes. Make sure to update the tests as needed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, feel free to reach out at [arunp77@gmail.com](mailto:arunp77@gmail.com).
