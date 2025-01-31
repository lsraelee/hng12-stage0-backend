from flask import Flask, Response
from flask_cors import CORS
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    
    current_datetime = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    response_data = {
        "email": "ayomikunadewemimo@gmail.com", 
        "current_datetime": current_datetime, 
        "github_url": "https://github.com/lsraelee/hng12-stage0-backend.git"
    }
    # Serialize JSON while preserving order
    response_json = json.dumps(response_data, indent=4)
    # Return response with status 200
    return Response(response_json, status=200, content_type="application/json")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
