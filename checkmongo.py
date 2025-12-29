import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

print("Mongo URL:", os.getenv("MONGO_DB_URL"))

client = pymongo.MongoClient(os.getenv("MONGO_DB_URL"))
collection = client["network_security"]["phishing_data"]

print("Total documents in collection:", collection.count_documents({}))
