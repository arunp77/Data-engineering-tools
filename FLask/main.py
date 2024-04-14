from flask import Flask, render_template, url_for, flash, redirect
from dotenv import load_dotenv
import os

from forms import RegristrationForm, LoginForm

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

posts = [
    {
        'author' : 'Author 1',
        'title' : 'Blog Post 1', 
        'content' : 'First post content',
        'date_posted' : 'April, 4, 2024'
    },
    {
        'author' : 'Author 2',
        'title' : 'Blog Post 2', 
        'content' : 'Second post content',
        'date_posted' : 'April, 5, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegristrationForm()
    if form.validate_on_submit():
        user = form.username.data
        flash(f"Account created for {user}!", "success")
        return redirect(url_for("home"))
    return render_template('register.html', title='Register', form=form)

# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     return render_template('login.html', title='Login', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'Your email' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)




if __name__ == '__main__':
    app.run(debug=True)




















if __name__ == '__main__':
    """
    This code block will only execute if the script is run directly
    It won't execute if the script is imported as a module
    You can put your main program logic here. With this, to run this script, we need to use 
    
    python main.py
    
    instead of `flask run`
    
    In the case of 'flask run' command is used to start the Flask development server. 
    However, when using the 'flask run' command, the 'if __name__ == '__main__':' block 
    is not necessary in the script. Instead of directly calling 'app.run()', we simply define
    our Flask application instance ('app'), and then use the flask run command in our terminal 
    to start the server.
    """
    app.run(debug=True)
