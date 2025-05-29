

import os
from pymongo import MongoClient


MONGO_URL = "mongodb+srv://SaraTrianaMerchan:bhLwr7Qx6OUvUZF2@cali-node.cmmdoz5.mongodb.net/?retryWrites=true&w=majority&appName=CALI-Node"

client = MongoClient(MONGO_URL)


db = client["cali_db"]
     
