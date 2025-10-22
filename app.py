from flask import Flask
from instabot import Bot

app = Flask(__name__)

# ----------------- HARDCODED CONFIG -----------------
INSTAGRAM_USERNAME = "mk_test_xx_1"
INSTAGRAM_PASSWORD = "mahabbat@2008"
TARGET_USER = "mk__mahabbat"
# ----------------------------------------------------

@app.route('/')
def home():
    return "✅ Instabot Web Service is running!"

@app.route('/follow')
def follow_user():
    try:
        bot = Bot()  # Create bot inside route to prevent startup crash
        bot.login(username=INSTAGRAM_USERNAME, password=INSTAGRAM_PASSWORD)
        bot.follow(TARGET_USER)
        bot.logout()
        return f"🎯 Followed user: {TARGET_USER}"
    except Exception as e:
        return f"❌ Error: {e}"

if __name__ == "__main__":
    app.run()  # No host, no port specified
