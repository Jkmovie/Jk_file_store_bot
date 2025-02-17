import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from config.config import BOT_TOKEN, MONGO_URI
import pymongo
from bot.handlers import start, download_file, force_subscribe

# MongoDB Configuration
client = pymongo.MongoClient(MONGO_URI)
db = client["file_store_db"]

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Start the bot."""
    updater = Updater(BOT_TOKEN)

    # Add handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("download", download_file))
    dispatcher.add_handler(CommandHandler("force_subscribe", force_subscribe))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
