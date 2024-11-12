from flask import Flask, redirect, render_template, request
from counter import Counter

app = Flask(__name__)
cnt = Counter()

# snarky comment

@app.route("/")
def index():
    return render_template("index.html", value=cnt.value)

@app.route("/increase", methods=["POST"])
def increase():
    cnt.increase()
    return redirect("/")

@app.route("/increment", methods=["POST"])
def increment():
    value = int(request.form["value"])
    cnt.increment(value)
    return redirect("/")

@app.route("/set_value", methods=["POST"])
def set_value():
    value = int(request.form["set_value"])
    cnt.set_value(value)
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    cnt.reset()
    return redirect("/")
