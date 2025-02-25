# "flask run" to run and right click link in terminal. Don't deploy on test server more than a few times per minute. Otherwise it won't load
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", placeholder="name")


@app.route("/greet")
def greet():
    name = request.args.get("name", "world")
    return render_template("greet.html", name=name)