from flask import Flask, jsonify, request
import json
import os
from pymongo import MongoClient

app = Flask(__name__)

# Path to the data.json file
DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["todo_items"]

# Home route
@app.route("/")
def home():
    return "✅ Flask is running! Go to /api to see the data."

# API route
@app.route("/api", methods=["GET"])
def get_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# NEW ROUTE FOR TASK 3
@app.route("/submittodoitem", methods=["POST"])
def submit_todo():

    itemName = request.form.get("itemName")
    itemDescription = request.form.get("itemDescription")

    todo_item = {
        "itemName": itemName,
        "itemDescription": itemDescription
    }

    collection.insert_one(todo_item)

    return jsonify({"message": "Todo item saved successfully"})


if __name__ == "__main__":
    app.run(debug=True)
