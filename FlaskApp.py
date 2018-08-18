from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/profile")
def profile():
    return "Hello this is your profile!"