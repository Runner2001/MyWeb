from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def index():
    name = ["runner", "runner1", "runner2"]
    return render_template("Flask7.html", name = name)
