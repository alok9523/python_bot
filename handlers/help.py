# handlers/help.py
from telegram import Update
from telegram.ext import CallbackContext

async def help_command(update: Update, context: CallbackContext) -> None:
    """Send a help message to the user."""
    await update.message.reply_text("Here are the available commands:\n/start - Start the bot\n/help - Get help")