import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Telegram Bot Token
GDRIVE_FOLDER_ID = os.getenv("GDRIVE_FOLDER_ID")  # Google Drive Folder ID
CREDENTIALS_FILE = "credentials.json"  # Google API Credentials
MONGO_URI = os.getenv("MONGO_URI")  # MongoDB Connection String
