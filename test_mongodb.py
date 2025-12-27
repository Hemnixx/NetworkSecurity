import os
from dotenv import load_dotenv
import pymongo
import certifi

load_dotenv()

print("URL:", os.getenv("MONGO_DB_URL"))

client = pymongo.MongoClient(
    os.getenv("MONGO_DB_URL"),
    tlsCAFile=certifi.where()
)

print("Databases:", client.list_database_names())

db = client["network_security"]
print("Collections:", db.list_collection_names())

