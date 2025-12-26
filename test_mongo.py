from pymongo import MongoClient
import os

uri = (
    "mongodb+srv://Neeraj_gup:Neeraj123"
    "@cluster0.sq72tld.mongodb.net/network_security"
    "?retryWrites=true&w=majority&authSource=admin"
)

try:
    client = MongoClient(uri)
    client.admin.command("ping")
    print("✅ MongoDB connected successfully")
except Exception as e:
    print("❌ Error:", e)
