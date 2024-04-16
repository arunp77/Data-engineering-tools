from flask import Flask, render_template 
import os

# Get the current directory
current_directory = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(current_directory))


header = ["Name", "Duty"]
data = [
    ["Daniel", "Support"],
    ["Diane", "Career Management"],
    ["Donna", "Life of the program"]
]

@app.route("/")
def table():
    return render_template("table.html",headings=header,data=data)

@app.route("/Arun")
def hello_daniel():
  return "Hello Arun !"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)