from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Your bot is alive on Python 3.13 🎉")

def main():
    token = os.getenv("BOT_TOKEN")  # set this in Render Dashboard (Environment Variables)
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
