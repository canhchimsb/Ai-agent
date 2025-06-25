# main_agent.py

# --- PHẦN KIỂM TRA MẠNG ---
import requests

def check_nodes():
    node_urls = {
        "HuggingFace": "https://canhchimhoabinhsb--ai-agent.hf.space/api/ping",
        "Replit": "https://aiagent.canhchimhoabin1.repl.co/api/ping",
        "Render": "https://ai-agent-eld4.onrender.com/api/ping",
        "Colab": "http://localhost:7860/api/ping"  # Update lại nếu Colab dùng IP công khai
    }

    print("🛰️  Checking node connectivity...\n")
    for name, url in node_urls.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"✅ {name} is online! Response: {response.json()}")
            else:
                print(f"⚠️ {name} responded with status code {response.status_code}")
        except Exception as e:
            print(f"❌ Cannot connect to {name}: {e}")

# --- GỌI HÀM KIỂM TRA TRƯỚC KHI CHẠY AGENT ---
check_nodes()

# --- PHẦN CHÍNH CỦA AI AGENT BÊN DƯỚI ---
# ... (giữ nguyên phần agent hiện tại của bạn)
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
