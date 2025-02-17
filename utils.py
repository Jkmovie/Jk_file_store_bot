import pymongo

# MongoDB Setup
def connect_to_mongo():
    client = pymongo.MongoClient("your_mongo_uri_here")
    return client["file_store_db"]

def save_file_to_db(file_info):
    db = connect_to_mongo()
    db.files.insert_one(file_info)

def get_file_from_db(file_id):
    db = connect_to_mongo()
    return db.files.find_one({"file_id": file_id})
