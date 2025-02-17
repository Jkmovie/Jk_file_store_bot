from pymongo import MongoClient

# तुमचा MongoDB URI येथे ठेवा
MONGO_URI = "mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client["your_database"]  # डेटाबेसचे नाव बदला
collection = db["your_collection"]  # कलेक्शनचे नाव बदला

def insert_data(data):
    """MongoDB मध्ये डेटा घालण्यासाठी फंक्शन"""
    collection.insert_one(data)
    return "Data inserted successfully"

def get_data(query):
    """MongoDB मधून डेटा मिळवण्यासाठी फंक्शन"""
    return collection.find_one(query)
