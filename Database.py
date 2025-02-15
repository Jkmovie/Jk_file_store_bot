from pymongo import MongoClient
import config

client = MongoClient(config.MONGO_URI)
db = client["FileStoreBot"]
files_collection = db["files"]

def save_file(file_id, file_name, user_id):
    file_data = {"file_id": file_id, "file_name": file_name, "user_id": user_id}
    files_collection.insert_one(file_data)

def get_file(file_name):
    return files_collection.find_one({"file_name": file_name})
