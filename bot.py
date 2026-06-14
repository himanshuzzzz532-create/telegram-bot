from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("7981769218:AAG5fa7optt5JgxdwdQqmUSuaJJcIjqwLLs")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot Online ✅")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
