# MongoDB कनेक्शनसाठी साधा कोड

import pymongo
from pymongo import MongoClient
import os

client = MongoClient(os.environ['MONGODB_URI'])  # MongoDB URI पर्यावरणातून घेणे
db = client['file_store_db']  # तुमच्या डेटाबेसचे नाव
collection = db['files']  # कलेक्शन नाव

def save_file(file_data):
    collection.insert_one(file_data)

def get_file(file_id):
    return collection.find_one({"_id": file_id})
