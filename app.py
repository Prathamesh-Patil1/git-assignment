from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# Path to the data.json file
DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")

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

if __name__ == "__main__":
    app.run(debug=True)

#ppatil2004
