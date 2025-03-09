from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    api_url = "http://localhost:5001/api/projects"
    response = requests.get(api_url)
    projects = response.json() if response.status_code == 200 else []
    return render_template("index.html", projects=projects)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)