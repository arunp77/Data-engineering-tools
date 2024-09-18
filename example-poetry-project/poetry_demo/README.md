
# Poetry python demo
- Install poetry using:
  ```
  poetry install
  ```

- When run following commnad:
    ```
    poetry new poetry-demo
    ```
    It will create a new directory named `poetry-demo` with a basic `pyproject.toml` and follwoing is the project directory structure:

    ```
    poetry-demo
    ├── pyproject.toml
    ├── README.md
    ├── src
    │   └── poetry_demo
    │       └── __init__.py
    └── tests
        └── __init__.py
    ```

- If you want to use a src folder, you can use the `--src` option:
  - use it if you have allready followed the above step
    ```
    poetry new poetry-demo --src 
    ```
  - and If you have not yet followed the steps, then you can use following command to start from scratch
    ``` 
    poetry new --src poetry_demo
    ```


# Reference
- [Poetry Documentation](https://python-poetry.org/docs/) 
- https://python-poetry.org/docs/cli/