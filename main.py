from flask import Flask
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os
import threading

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Telegram Bot Handlers
def start(update: Update, context: CallbackContext):
    update.message.reply_text("🙏 Welcome to NetExpress Cyber Cafe!\nType 'pf' to get WhatsApp support.")

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if "pf" in text:
        update.message.reply_text("📲 For PF withdrawal help, message us on WhatsApp: https://wa.me/7972485628")
    else:
        update.message.reply_text("❓ Type 'pf' to get WhatsApp support.")

def run_bot():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

@app.route('/')
def index():
    return "✅ NetExpress Bot is running."

if __name__ == '__main__':
    # Run Telegram bot in a thread
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=10000)
