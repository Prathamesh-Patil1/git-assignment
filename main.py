from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://patilprathamesh9777:ppatil2004@cluster0.pxm87ul.mongodb.net/test_db?retryWrites=true&w=majority&appName=Cluster0")
db = client["test_db"]
collection = db["test_data"]

# Form route
@app.route("/", methods=["GET", "POST"])
def form():
    error = None
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        try:
            collection.insert_one({"name": name, "age": age})
            return redirect(url_for("success"))
        except Exception as e:
            error = str(e)
    return render_template("form.html", error=error)

# Success page
@app.route("/success")
def success():
    return "Data submitted successfully"

if __name__ == "__main__":
    app.run(debug=True)
