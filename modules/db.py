from pymongo import MongoClient
import os

# MongoDB connection
MONGO_URI = "mongodb+srv://db_user:N4CUI3hTSaIXIEMA@cluster0.gct52mp.mongodb.net/SkillGapAnalyzer"
client = MongoClient(MONGO_URI)

# Explicit DB + Collection
db = client["SkillGapAnalyzer"]
collection = db["resumes_data"]

def save_result(data):
    """
    Stores analysis result in MongoDB
    """
    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary")

    collection.insert_one(data)
    print("Result saved to MongoDB")