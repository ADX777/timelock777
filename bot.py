import os
import requests
from flask import Flask

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

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

# Test gửi tin nhắn mỗi khi khởi động lại bot
if __name__ == "__main__":
    send_message("🚀 Bot Telegram đã hoạt động trên Railway!")
    app.run(host="0.0.0.0", port=8080)
