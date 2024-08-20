from flask import Flask, request
from pydantic import BaseModel
from flask_pydantic import validate
from werkzeug.exceptions import NotFound

class Query(BaseModel):
    name:str
    age:int
    
class Player(BaseModel):
    name:str
    position:str
    team:str
    birth_year:int

app = Flask(__name__)

@app.route("/intro")
@validate()
def intro(query:Query):
    return f"Hello, my name is {query.name} and I am {query.age} years old"

@app.route("/info")
@validate()
def info(query:Player):
    return query.dict()

@app.route("/info_post",methods=["POST"])
@validate()
def info_post(body:Player):
    return body.dict()

@app.route("/head")
def head():
    if request.headers.get("username"):
        return "Hello {}".format(request.headers.get("username"))
    elif request.headers.get("enterprise"):
        return "Hello {}".format(request.headers.get("enterprise"))
    else:
        return "Hello World !"

@app.route("/hello")
def hello():
  return "Hello World"

# @app.errorhandler(NotFound)
# def handler_error404(err):
#   return "You have encountered an error of 404",404


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)