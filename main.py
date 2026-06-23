from flask import Flask, request, send_from_directory
import requests

app = Flask(__name__)

BOT_TOKEN = "8733907884:AAGfVYq8b82kNunAiXTMSnbF2d8J0h3YXFE"
CHAT_ID = "8478208834"

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    name = data["name"]
    phone = data["phone"]

    text = f"📥 فرم جدید\n\n👤 نام: {name}\n📞 شماره: {phone}"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text
    })

    return {"status": "ok"}

app.run(host="0.0.0.0", port=5000)