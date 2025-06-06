# === db_connection.py ===
# Connects to MongoDB Atlas using pymongo
# Requires a connection string (Mongo URL) stores securely

import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()



MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(MONGO_URL)


db = client["cali_db"]
     
