# DataVista

**DataVista** is a modern Tkinter application designed for complex data analytics, providing a user-friendly interface to visualize, manipulate, and analyze datasets.

## Features

- Modern UI design with customizable themes
- Reusable components for quick development
- Responsive layout adaptable to various screen sizes

## Requirements

- Python 3.x
- Tkinter (included with standard Python installation)


## Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/arunp77/Data-engineering-tools.git
   ```
   next go to the tinker project directory:
   ```bash
   cd Python-ui/Tinker-project
   ```
2. Install Poetry if you haven't already. Follow the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

3. Create a virtual environment and install dependencies:

   - Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
    - Install required packages:
    ```bash
    poetry install
    ```
    or just install the `tkinter` using (for more details on the tkinter library, please check the [official documentation](https://docs.python.org/3/library/tkinter.html)): 
    ```bash
    pip install tk
    ```

## Usage

To run the application, execute the following command in your terminal:
```bash
python src/main.py
```

or 

```bash
poetry run python src/main.py
```

## Project Structure

```
datavista/
├── src/
│   ├── __init__.py
│   ├── main.py            # Main application file
│   └── ui/
│       ├── main_window.py  # Main window class
│       └── custom_widgets.py # Custom widgets
├── tests/
├── pyproject.toml
└── README.md
```

## Contributing

Feel free to contribute to this project! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, feel free to reach out to [arunp77@gmail.com](mailto:arunp77@gmail.com).
