from flask import Flask 

'''
It creates an instance of the Flask class, which will be the WSGI (Web Server Gateway interface) application.
'''

### WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to my website</h1></html>"


@app.route("/index")
def index():
    return "Welcome to my index page of my website!"


if __name__=="__main__":
    app.run(debug=True)