from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# ==========================
# TOKEN DO BOT
# ==========================
TOKEN = "8944693063:AAEodDqJqcqCvB7NJr17Kte-Jh38Lp3Y43g"


# ==========================
# COMANDO /start
# ==========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! 👋\n\n"
        "Bem-vindo ao Gestor Pessoal.\n\n"
        "Em breve vou controlar suas receitas, despesas e muito mais."
    )


# ==========================
# FUNÇÃO PRINCIPAL
# ==========================
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ Gestor Pessoal iniciado!")

    app.run_polling()


# ==========================
# INICIAR BOT
# ==========================
if __name__ == "__main__":
    main()
