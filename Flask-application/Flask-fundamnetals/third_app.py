from flask import make_response 
from flask import Flask, render_template, request, abort 
import os

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(current_directory))

@app.route("/test")
def test():
    return make_response("You did not enter an integer",400)    


@app.route("/header",methods=["POST"])
def hd():
    header = dict(request.headers)
    data = request.get_json()
    for key,value in data.items():
        header[key]=value        
    return make_response("<H1>It's all good</H1>",200,data)


@app.route("/age/<val>")
def hello(val):        
    try:
        return "Hello, I am {} years old".format(int(val))
    except ValueError:
        abort(400,description="You did not enter an integer")
# Do not consider this line </val>    


@app.route("/birth",methods=["POST"])
def intro():
    data = request.get_json()
    header = dict()
    try:
        int(data["birth_year"])
        return f"{data['name']} was born in {data['birth_year']}"
    except ValueError:
        header["status_code"]=400
        for key,value in data.items():
            header[key]=value
        return make_response("{} is not an number".format(header["birth_year"]),400,header)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)