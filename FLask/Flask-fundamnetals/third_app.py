from flask import make_response 
from flask import Flask, render_template, request, abort 
import os

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(current_directory))

@app.route("/test")
def test():
    return make_response("I use the function 'make_response'.")    


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)