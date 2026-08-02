import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! 👋\n\n"
        "Sou seu assessor financeiro.\n\n"
        "Em breve vou ajudar você a controlar receitas, despesas e metas."
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()
