from flask import Flask, render_template

apps = Flask(__name__)

@apps.route("/todo")
def todo():
    return render_template("todo.html")