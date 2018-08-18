from flask import Flask, render_template
import os 
app = Flask(__name__)

dir_path = os.path.dirname(os.path.realpath(__file__))

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/profile")
def profile():
    return render_template('Buttons.html')