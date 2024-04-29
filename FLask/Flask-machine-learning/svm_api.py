from flask import Flask, request, jsonify, json
from sklearn.svm import SVC
import pickle
import numpy as np
import pandas as pd
import uvicorn
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


# Access the environment variables
FLASK_APP = os.getenv("FLASK_APP")
FLASK_ENV = os.getenv("FLASK_ENV")

# Loading the model
svm = pickle.load(open("svm_titanic.pkl", "rb"))

app = Flask(__name__)

@app.route("/predict", methods=["GET"])
def predict():
    features = []
    data = request.get_json(force=True)
    features.append(data["pclass"])
    features.append(data["sex"])
    features.append(data["age"])
    features.append(data["fare"])
    features.append(data["embarked"])
    features.append(data["single"])
    features.append(data["famillySize"][0])
    features.append(data["famillySize"][1])
    features.append(data["famillySize"][2])
    features.append(data["title"])

    to_predict = np.array([features]) # the features vector
    prediction = svm.predict(to_predict)[0]

    if prediction==0:
        result = {"Prediction" : "Survived"}
    else:
        result = {"Prediction" : "Did not survive"}

    return jsonify(result)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2222, debug=True)