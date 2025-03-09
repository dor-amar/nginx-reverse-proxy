from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "Hello From Flask INT api application"

@app.route("/api/projects", methods=["GET"])
def get_projects():
    with open("projects.json", "r") as f:
        projects = json.load(f)
    return jsonify(projects)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)