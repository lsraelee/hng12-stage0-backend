from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
from collections import OrderedDict

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    response = OrderedDict([
        ("email", "ayomikunadewemimo@gmail.com"),
        ("current_datetime", datetime.utcnow().isoformat()),
        ("github_url", "https://github.com/lsraelee/hng12-stage0-backend.git")
    ])
    
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)