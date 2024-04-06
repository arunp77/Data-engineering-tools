# Getting Started with Flask: A Comprehensive Tutorial

Flask is a famous Python framework for building web applications. Released in 2011, Flask has established itself as a reference for creating an API on Python. It stands out from Django, another famous framework used in Python, because of its lightness. Indeed, Flask is considered as a micro framework, you do not have to define the databases to use or the formatting. However with Flask, you create the core of your web application, then according to your need you add different services. That's why, in a few lines, we can easily display a Hello World on a web page without using an HTML file.

In this repo, we'll cover the basics of Flask and guide through creating the first web application.

## Prerequisites

Before getting started with Flask, ensure that you have Python installed on your system. You can download and install Python from the official Python website (https://www.python.org/).

## Installing Flask

You can install Flask using `pip`, the Python package manager. Open your terminal or command prompt and run the following command:

```bash
pip install Flask
```

This will install Flask and its dependencies on your system.

## Creating a Flask Application

Let's create a simple Flask application to get started. Create a new directory for your project and navigate into it. Then, create a new Python script (e.g., `app.py`) and open it in your preferred text editor.

```python
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route
@app.route('/')
def hello():
    return 'Hello, Flask!'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

Save the file and return to your terminal. Navigate to the directory where your `app.py` script is located and run the following command to start the Flask development server:

```bash
python app.py
```

You should see output indicating that the server is running. Open your web browser and navigate to `http://localhost:5000/`. You should see the message "Hello, Flask!" displayed in your browser.

## Understanding Routes

In the Flask application we just created, we defined a route using the `@app.route()` decorator. Routes define URL patterns and the functions that should be called when those URLs are accessed. In our example, the `/` route corresponds to the root URL of the application.

```python
@app.route('/')
def hello():
    return 'Hello, Flask!'
```

## Serving HTML Templates

Flask allows us to serve HTML templates to render dynamic content in our web applications. Let's modify our `app.py` script to render an HTML template instead of returning a plain text response.

First, create a directory named `templates` in your project directory. This is where Flask will look for HTML templates by default.

Create a new HTML file named `index.html` in the `templates` directory:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App</title>
</head>
<body>
    <h1>Hello, Flask!</h1>
</body>
</html>
```

Now, modify your `app.py` script to render this HTML template:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

Run your Flask application again using `python app.py` and navigate to `http://localhost:5000/` in your web browser. You should see the "Hello, Flask!" message rendered using the HTML template.

## Handling Form Submissions

Flask allows us to handle form submissions from web pages. Let's create a simple form in our HTML template and modify our Flask application to process the form data.

Modify the `index.html` file to include a form:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App</title>
</head>
<body>
    <h1>Hello, Flask!</h1>
    <form action="/submit" method="post">
        <input type="text" name="name" placeholder="Enter your name">
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

Now, modify your `app.py` script to handle the form submission:

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)
```

Now, when you enter your name in the form and submit it, Flask will process the form data and display a personalized greeting message.

## Conclusion

Congratulations! You've now learned the basics of Flask and how to create a simple web application using this powerful framework. There's much more to explore with Flask, including handling database interactions, user authentication, and building RESTful APIs. Check out the Flask documentation for more information and advanced topics.

## Further Reading

- Flask Documentation: https://flask.palletsprojects.com/
- Flask Tutorial: https://flask.palletsprojects.com/en/2.0.x/tutorial/

---
## Let's get connected:
- You can connect with me on Linkedin at: [https://linkedin.com/in/arunp77](https://linkedin.com/in/arunp77)
- You can follow me on Twitter at: [https://twitter.com/arunp77_](https://twitter.com/arunp77_)