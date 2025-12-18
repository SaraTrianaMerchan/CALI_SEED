# === db_connection.py ===
# Connects to MongoDB Atlas using pymongo
# Requires a connection string (Mongo URL) stores securely

import os
from pymongo import MongoClient
from dotenv import load_dotenv
from pymongo.errors import ConnectionFailure


load_dotenv()


MONGO_URL = os.getenv("MONGO_URL")

try:

    client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)
    client.admin.command("ping")
    db = client["cali_db"]
    print("Mongo conectado")

except ConnectionFailure as e:
    print(" Error al conectar a MongoDB")
    print(e)
