from flask import Flask, render_template, request, abort 
import os
from werkzeug.exceptions import NotFound, BadRequest, Unauthorized
import numpy.random as ran

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(current_directory))
user = {
    '123': {'name': 'John', 'age': 30},
    '456': {'name': 'Alice', 'age': 25},
    # Add more users as needed
}


@app.route("/")
def hello_arun():
    return "Hello Arun !"

@app.route('/hello', methods=['GET']) # curl -X GET 'http://localhost:5000/hello?name=Arun'
def hello():
    name = request.args.get('name')
    return f'Hello, {name}!'

@app.route("/hello/<name>")  # curl -X GET http://localhost:5000/hello/Arun
def hello_name(name):
    return f"Hello {name}!"
# Do not consider this line </name>   

@app.route("/hello_post", methods=["POST"]) # curl -X POST -H "Content-Type: application/json" -d '{"name": "Arun"}' http://localhost:5000/hello_post
def hello_post():
    data = request.get_json()
    return f"Hello {data['name']}!"

# Example-1: Error handling
# @app.route("/age/<int:age>")
# def age(age):
#     return f"Hello, I am {age} years old."
# For error handling.
# #@app.errorhandler(NotFound)
# def handler_error404(err):
#     return "You have encountered an error of 404",404
# # after removing the decorator, use below line aling with the functuon defined above.
# app.register_error_handler(404,handler_error404)


# Example-2: error handling (now we dont need to add the errorhandler.)
# @app.route("/age/<val>")
# def age(val):
#     try:
#         return f"Hello, I am {int(val)} years old"
#     except ValueError:
#         return "You did not enter an integer",400
# # Do not consider this line </val>    

# Example-3: error handling (again we dont need to add the errorhandler.)
# @app.route("/age/<val>")
# def age(val):
#     try:
#         return "Hello, I am {} years old".format(int(val))
#     except ValueError:
#         raise BadRequest("You did not enter an integer")
# # Do not consider this line </val>   

# Example-4: error handling with the description.
@app.route("/age/<val>")
def age(val):        
    try:
        return f"Hello, I am {int(val)} years old."
    except ValueError:
        abort(400,description="You did not enter an integer")
# Do not consider this line </val>  

# Example-5: error handling 
# Create a route "/random" that will return a random number between 0 and an integer end, but access is restricted to the user who will send by POST "name": "Daniel", but also the value of end. So you have to send the HTTP exception for bad authentication but also the exception for an incorrect value for end.
@app.route("/random", methods=["POST"])
def random():
    data = request.get_json()
    if data["name"] == "Daniel":
        try: 
            return f"Your lucky number is {ran.randint(0, int(data['end']) + 1)}.\n"
        except ValueError:
            raise BadRequest("You did not enter an integer")
    else:
        raise Unauthorized("The user is not Daniel")


@app.route("/users/<id>") # curl -X GET http://localhost:5000/users/123
def get_user(id):
    return user[id]

@app.route("/add",methods=["PUT"])
def add_user():
    data = request.get_json()
    user[str(len(user))]=data
    return "User {} has been added to the database.".format(len(user)-1)

@app.route("/update/<id>",methods=["POST"])
def update_user(id):
    if id in user:
        user[id] = request.get_json()
        return "User {} has been modified".format(id)
    return "User {} is missing from the database".format(id) 

@app.route("/delete/<id>",methods=["DELETE"])
def delete_user(id):
    if id in user:
        del user[id]
        return "User {} has been deleted".format(id)
    return "The user {} is absent from the database".format(id)


# Route for division operation
@app.route('/divide/<int:num1>/<int:num2>')             # http://localhost:5000/divide/24/21 ==> The result of 24 divided by 21 is 1.1428571428571428
def divide(num1, num2):
    result = num1 / num2
    return f"The result of {num1} divided by {num2} is {result}"


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)