from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from config.config import FORCE_SUBSCRIBE_CHANNEL

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the File Store Bot!')

def download_file(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Please provide the link to download.')

def force_subscribe(update: Update, context: CallbackContext) -> None:
    user_id = update.message.chat.id
    chat_id = FORCE_SUBSCRIBE_CHANNEL
    update.message.reply_text(f"Please join {chat_id} to access the bot.")
