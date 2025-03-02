from telegram import Update
from telegram.ext import CallbackContext
from handlers.gpt_handler import generate_ai_response

async def chat(update: Update, context: CallbackContext) -> None:
    """Handles AI-powered chat using OpenRouter API."""
    user_message = update.message.text
    ai_response = generate_ai_response(user_message)
    await update.message.reply_text(ai_response)