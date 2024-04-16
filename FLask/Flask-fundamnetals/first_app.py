from flask import Flask
from pydantic import BaseModel
from flask_pydantic import validate

class Query(BaseModel):
    name:str
    age:int

app = Flask(__name__)

@app.route("/intro")
@validate()
def intro(query:Query):
    return f"Hello, my name is {query.name} and I am {query.age} years old"



if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)