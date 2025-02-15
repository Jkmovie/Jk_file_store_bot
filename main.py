import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials
import config

# लॉगिंग सेटअप
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Google Drive Authentication
def authenticate_drive():
    creds = Credentials.from_service_account_file(config.CREDENTIALS_FILE, scopes=["https://www.googleapis.com/auth/drive"])
    return build('drive', 'v3', credentials=creds)

drive_service = authenticate_drive()

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Hello! मी File Store Bot आहे. तुमचे फायली Google Drive वर सेव करू शकतो.")

async def upload_file(update: Update, context: CallbackContext) -> None:
    if not update.message.document:
        await update.message.reply_text("कृपया एक फाइल पाठवा.")
        return
    
    file = await update.message.document.get_file()
    file_path = f"downloads/{update.message.document.file_name}"
    
    await file.download_to_drive(file_path)

    # Google Drive वर अपलोड करा
    file_metadata = {'name': update.message.document.file_name, 'parents': [config.GDRIVE_FOLDER_ID]}
    media = MediaFileUpload(file_path, resumable=True)
    uploaded_file = drive_service.files().create(body=file_metadata, media_body=media, fields="id").execute()

    os.remove(file_path)
    
    await update.message.reply_text(f"File Uploaded Successfully! Google Drive ID: {uploaded_file.get('id')}")

def main():
    app = Application.builder().token(config.BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Document.ALL, upload_file))
    
    app.run_polling()

if __name__ == "__main__":
    main()
