from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Token do bot
TOKEN = "7993006451:AAHf6b2CIM3XZ8gTvMxU-oAQvITBEOfxS1k"

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.message.from_user.first_name
    await update.message.reply_text(
        f"👋 Olá, {user_first_name}! Bem-vindo ao sistema da Oficina!"
    )

# Inicialização do bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot está rodando...")
    app.run_polling()
