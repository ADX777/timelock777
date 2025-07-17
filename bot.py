import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Lấy biến môi trường
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# Hàm gửi tin nhắn đến Telegram
def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": text,
        "parse_mode": "HTML"
    }

    print("📤 Đang gửi tin nhắn Telegram...")
    print(f"➡️ Payload: {payload}")
    try:
        r = requests.post(url, json=payload)
        print(f"✅ Trạng thái: {r.status_code}")
        print(f"📩 Phản hồi: {r.text}")
    except Exception as e:
        print(f"❌ Exception: {e}")

# Trang chủ để test
@app.route("/")
def home():
    return "🤖 Bot is running."

# API nhận dữ liệu từ web rồi gửi tin nhắn
@app.route("/notify", methods=["POST"])
def notify():
    data = request.json
    duration = data.get("duration")
    amount = data.get("amount")
    coin = data.get("coin")

    message = f"🔐 KHÁCH VỪA YÊU CẦU MÃ HÓA:\n⏳ Thời gian khóa: {duration}\n💰 Số USDT: {amount}\n🪙 Cặp coin: {coin}"
    send_message(message)
    return jsonify({"status": "ok"})

# Khi Railway khởi động, hàm này sẽ chạy khi có request đầu tiên
@app.before_first_request
def startup():
    send_message("🚀 Bot Telegram đã hoạt động trên Railway!")

# Chỉ dùng khi chạy local
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
