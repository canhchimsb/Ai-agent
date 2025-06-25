
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong from Render/GitHub"})

@app.route("/message", methods=["POST"])
def message():
    data = request.json
    return jsonify({"reply": f"Received: {data}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
