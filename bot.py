import os
from flask import Flask, request
from telegram import Bot

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")  # ID nhóm/kênh Telegram nhận thông báo

bot = Bot(token=TOKEN)
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot đang chạy..."

@app.route("/notify", methods=["POST"])
def notify():
    data = request.json
    if not data:
        return {"status": "fail", "message": "No JSON received"}, 400

    days = data.get("days")
    amount = data.get("amount")
    coin = data.get("coin")

    msg = (
        f"🔔 Khách vừa mã hóa ghi chú:\n"
        f"📅 Số ngày khóa: {days} ngày\n"
        f"💰 Số tiền cần thanh toán: {amount} USDT\n"
        f"💱 Cặp coin: {coin}"
    )
    bot.send_message(chat_id=CHAT_ID, text=msg)
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(debug=True)
