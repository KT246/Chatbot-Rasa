from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # 🔥 Cho phép tất cả nguồn truy cập (fix lỗi CORS)

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    response = requests.post(RASA_URL, json=data)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(port=8001)
