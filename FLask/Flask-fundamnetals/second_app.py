from flask import Flask, render_template, request
import os

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
    return "Hello {}".format(name)
# Do not consider this line </name>   

@app.route("/hello_post", methods=["POST"]) # curl -X POST -H "Content-Type: application/json" -d '{"name": "Arun"}' http://localhost:5000/hello_post
def hello_post():
    data = request.get_json()
    return f"Hello {data['name']}!"

@app.route("/age/<int:age>")
def hello_age(age):
    return "Hello, I am {} years old".format(age)


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





if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)