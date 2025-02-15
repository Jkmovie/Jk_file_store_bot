import database  # MongoDB database functions import करा

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

    # MongoDB मध्ये फाईल डेटा सेव करा
    database.save_file(uploaded_file.get('id'), update.message.document.file_name, update.message.chat_id)

    os.remove(file_path)
    
    await update.message.reply_text(f"File Uploaded Successfully! Google Drive ID: {uploaded_file.get('id')}")

async def get_file(update: Update, context: CallbackContext) -> None:
    if not context.args:
        await update.message.reply_text("कृपया फाईलचे नाव टाका.")
        return

    file_name = " ".join(context.args)
    file_data = database.get_file(file_name)

    if file_data:
        await update.message.reply_text(f"File Found! Google Drive ID: {file_data['file_id']}")
    else:
        await update.message.reply_text("ही फाईल सापडली नाही.")

app.add_handler(CommandHandler("getfile", get_file))
