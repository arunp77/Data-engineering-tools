### What is `doctest`?

`doctest` is a module included in Python’s standard library that allows you to embed tests directly in your docstrings. When you run `doctest`, it extracts these tests, runs them, and checks whether the output matches the expected results as documented.

### Why Use `doctest`?

- **Documentation**: `doctest` makes sure that your documentation is up-to-date and that the examples you provide actually work. This is especially useful for libraries and APIs, where users rely heavily on examples.
- **Simplicity**: Since tests are embedded in docstrings, there’s no need to write separate test cases or methods. The syntax is simple and straightforward.
- **Ease of Use**: `doctest` can be used alongside other testing frameworks like `unittest` or `pytest` without any issues.

**Comments/docstrings have a couple of drawbacks:**
- They’re ignored by the interpreter or compiler, which makes them unreachable at runtime.
- They often get outdated when the code evolves and the comments remain untouched.

### How `doctest` Works

The doctest module is a lightweight testing framework that provides quick and straightforward test automation. It can read the test cases from your project’s documentation and your code’s docstrings. This framework is shipped with the Python interpreter and adheres to the batteries-included philosophy.

`doctest` parses the docstrings of your functions, methods, classes, and modules, looking for pieces of text that look like interactive Python sessions. It then executes these sessions and compares the results against the expected output.

You can use doctest from either your code or your command line. To find and run your test cases, doctest follows a few steps:

- Searches for text that looks like Python interactive sessions in your documentation and docstrings
- Parses those pieces of text to distinguish between executable code and expected results
- Runs the executable code like regular Python code
- Compares the execution result with the expected result

The doctest framework searches for test cases in your documentation and the docstrings of packages, modules, functions, classes, and methods. It doesn’t search for test cases in any objects that you import.

In general, doctest interprets as executable Python code all those lines of text that start with the primary (`>>>`) or secondary (`...`) REPL prompts. The lines immediately after either prompt are understood as the code’s expected output or result.

### What doctest Is Useful For?

- Writing quick and effective test cases to check your code as you write it
- Running acceptance, regression, and integration test cases on your projects, packages, and modules
- Checking if your docstrings are up-to-date and in sync with the target code
- Verifying if your projects’ documentation is up-to-date
- Writing hands-on tutorials for your projects, packages, and modules
- Illustrating how to use your projects’ APIs and what the expected input and output must be

Having doctest tests in your documentation and docstrings is an excellent way for your clients or teammates to run those tests when evaluating the features, specifications, and quality of your code.

### Writing Your Own doctest Tests in Python
Now that you know what doctest is and what you can use it for, you’ll learn how to use doctest to test your code. No particular setup is required because doctest is part of the Python standard library. You can use it in your Python code without installing any additional packages.

#### Creating doctest Tests for Checking Returned and Printed Values

The first and probably most common use case of code testing is checking the return value of functions, methods, and other callables. You can do this with doctest tests. For example, say you have a function called `add()` that takes two numbers as arguments and returns their arithmetic sum:

```python 
# calculations.py

def add(a, b):
    return float(a + b)
```
This function adds two numbers together. Documenting your code is a good practice, so you can add a docstring to this function. Your docstring can look something like this:

```python 
# calculations.py

def add(a, b):
    """Compute and return the sum of two numbers.

    Usage examples:
    >>> add(4.0, 2.0)
    6.0
    >>> add(4, 2)
    6.0
    """
    return float(a + b)
```
This docstring includes two examples of how to use `add()`. Each example consists of an initial line that starts with Python’s primary interactive prompt, `>>>`. This line includes a call to `add()` with two numeric arguments. Then the example has a second line that contains the expected output, which matches the function’s expected return value.

In both examples, the expected output is a floating-point number, which is required because the function always returns this type of number.

You can run these tests with doctest. Go ahead and run the following command:

```bash 
python -m doctest calculations.py
```

### Running `doctest`

Here’s a basic example to illustrate how `doctest` works:

```python
def add(a, b):
    """
    Adds two numbers together.

    Example:
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b
```

In the example above, doctest will run the code snippets in the docstring when you run the test, checking if `add(2, 3)` indeed returns 5, and `add(-1, 1)` returns 0. This approach ensures that anyone reading your documentation can trust that the examples are accurate and reflective of the actual behavior of the code.

### How to use?
You can run `doctest` in several ways:

1. **From the Command Line**: You can run `doctest` on a module directly from the command line using the `-m` flag.

   ```bash
   python -m doctest your_module.py
   ```

   This will execute all the `doctest`s in the module and report any failures.

2. **Programmatically**: You can also include `doctest` in your scripts, which is useful if you want to run tests when the module is executed.

   ```python
   if __name__ == "__main__":
       import doctest
       doctest.testmod()
   ```

   The `doctest.testmod()` function will find and run all the tests in the current module.

3. **Integration with `unittest` or `pytest`**: You can run `doctest` tests using `unittest` or `pytest` to include them in a larger test suite.

   With `unittest`, you can create a test suite that includes `doctest`:

   ```python
   import unittest
   import doctest

   def load_tests(loader, tests, ignore):
       tests.addTests(doctest.DocTestSuite(your_module))
       return tests

   if __name__ == "__main__":
       unittest.main()
   ```

   With `pytest`, `doctest` tests are automatically discovered and run if you use the `--doctest-modules` flag:

   ```bash
   pytest --doctest-modules
   ```

### Writing `doctest`s

When writing `doctest`s, you need to follow the format of a Python interactive shell session. Here are a few things to keep in mind:

1. **Prompt and Output**: The examples must start with the Python prompt (`>>>` for single-line statements or `...` for continuation lines). The expected output follows on the next line(s).

   ```python
   def multiply(a, b):
       """
       Multiplies two numbers.

       >>> multiply(2, 3)
       6
       >>> multiply(0, 10)
       0
       """
       return a * b
   ```

2. **Whitespace and Exact Match**: `doctest` checks for an exact match between the actual output and the expected output. This means that even minor differences in whitespace or formatting can cause a test to fail.

   ```python
   def greet(name):
       """
       Greets a person.

       >>> greet("Alice")
       'Hello, Alice!'
       """
       return f"Hello, {name}!"
   ```

   Here, the output is a string, so it must match exactly, including quotes and punctuation.

3. **Handling Exceptions**: You can also test that exceptions are raised as expected.

   ```python
   def divide(a, b):
       """
       Divides two numbers.

       >>> divide(10, 2)
       5.0
       >>> divide(10, 0)
       Traceback (most recent call last):
           ...
       ZeroDivisionError: division by zero
       """
       return a / b
   ```

4. **Ignoring Unimportant Details**: If you want to ignore certain parts of the output (like memory addresses), you can use the `...` wildcard.

   ```python
   def create_list(size):
       """
       Creates a list of the specified size.

       >>> create_list(3)  # doctest: +ELLIPSIS
       [0, 1, 2, ...]
       """
       return list(range(size)) + [None]
   ```

### Advanced Usage of `doctest`

1. **Options**: You can use various `doctest` options to modify how tests are evaluated. For example, you can use `+IGNORE_EXCEPTION_DETAIL` to ignore details in exception output.

2. **DocFileSuite**: `doctest` can also be used to test entire files of documentation. This is useful if you have examples in your README or other documentation files.

   ```python
   import doctest

   def load_tests(loader, tests, ignore):
       tests.addTests(doctest.DocFileSuite("README.txt"))
       return tests
   ```

3. **Testing Multiple Modules**: You can use `doctest.testmod()` on specific modules if you need to run tests across multiple files.

   ```python
   import doctest
   import mymodule1, mymodule2

   doctest.testmod(mymodule1)
   doctest.testmod(mymodule2)
   ```

### When to Use `doctest`?

- **Simple Functions**: `doctest` is ideal for simple functions where the expected output can be easily represented as text.
- **Documentation Accuracy**: If you want to ensure that the examples in your documentation remain accurate, `doctest` is a great choice.
- **Lightweight Testing**: When you don’t need the full power of `unittest` or `pytest` and want a lightweight solution, `doctest` is sufficient.

### Limitations of `doctest`

- **Limited Scope**: `doctest` is not well-suited for complex testing scenarios, such as those involving setup/teardown operations, mocking, or extensive data manipulation.
- **Exact Output Matching**: Because `doctest` requires exact matching of output, even small differences in formatting can cause tests to fail, which can be cumbersome to manage.
- **Not Ideal for TDD**: Unlike `unittest` or `pytest`, `doctest` is not designed for test-driven development (TDD) as it’s more focused on validating examples rather than driving the design of the code.

### Conclusion

`doctest` is a powerful tool for keeping your documentation accurate and ensuring that the examples you provide are correct. It’s easy to use, integrates well with other testing frameworks, and is especially useful for small functions and libraries. However, for more complex testing needs, `unittest` or `pytest` might be more appropriate.