from flask import Flask 

'''
It creates an instance of the Flask class, which will be the WSGI (Web Server Gateway interface) application.
'''

### WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my website!"


@app.route("/index")
def index():
    return "Welcome to my index page of my website!"


if __name__=="__main__":
    app.run(debug=True)