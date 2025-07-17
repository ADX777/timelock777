import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Lấy token bot và ID kênh từ biến môi trường Railway
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")  # VD: -1001234567890

# Hàm gửi tin nhắn đến Telegram
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

# Route chính để kiểm tra bot sống
@app.route("/")
def home():
    return "🤖 Bot is running."

# Route nhận yêu cầu từ web để gửi tin nhắn
@app.route("/notify", methods=["POST"])
def notify():
    data = request.json
    duration = data.get("duration")
    amount = data.get("amount")
    coin = data.get("coin")

    message = f"🔐 KHÁCH VỪA YÊU CẦU MÃ HÓA:\n⏳ Thời gian khóa: {duration}\n💰 Số USDT: {amount}\n🪙 Cặp coin: {coin}"
    send_message(message)
    return jsonify({"status": "ok"})

# Gửi thông báo khi bot khởi động (chỉ chạy khi chạy local hoặc Railway dùng kiểu CMD)
if __name__ == "__main__":
    send_message("🚀 Bot Telegram đã hoạt động trên Railway!")
    app.run(host="0.0.0.0", port=8080)
