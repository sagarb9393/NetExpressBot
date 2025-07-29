from flask import Flask
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

app = Flask(__name__)

# Telegram bot token from environment variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to NetExpress Cyber Cafe! Type 'pf' to get WhatsApp help.")

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if "pf" in text:
        update.message.reply_text("For PF withdrawal help, message us on WhatsApp: https://wa.me/7972485628")

def run_telegram_bot():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(MessageHandler(None, handle_message))
    updater.start_polling()

@app.route('/')
def home():
    return "NetExpress Bot is Live!"

if __name__ == "__main__":
    run_telegram_bot()
    app.run(host="0.0.0.0", port=10000)
