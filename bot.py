import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")  # Ví dụ: -1001234567890

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    try:
        r = requests.post(url, json=payload)
        if r.status_code == 200:
            print("✅ Message sent successfully!")
        else:
            print(f"❌ Failed to send message: {r.text}")
    except Exception as e:
        print(f"⚠️ Exception: {e}")

@app.route("/")
def home():
    return "🤖 Bot is running."

@app.route("/notify", methods=["POST"])
def notify():
    data = request.json
    duration = data.get("duration")
    amount = data.get("amount")
    coin = data.get("coin")

    message = f"🔐 KHÁCH VỪA YÊU CẦU MÃ HÓA:\n⏳ Thời gian khóa: {duration}\n💰 Số USDT: {amount}\n🪙 Cặp coin: {coin}"
    send_message(message)
    return jsonify({"status": "ok"})

# ❗ Đặt bên ngoài if để Railway luôn chạy được dòng này
send_message("🚀 Bot Telegram đã hoạt động trên Railway!")

# 👇 Đoạn này chỉ chạy khi bạn test local (python bot.py)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
