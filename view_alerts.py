# === view_alerts.py ===
# Displays stored alerts from MongoDB in a human-readable format
# Connects to the alerts_log collection


from db_connection import db
from pprint import pprint 

collection = db["alerts_log"]

print("\nRegistered Environmental Alerts:\n")

alertas = collection.find()

for alerta in alertas: 
    print(f"Timestamp: {alerta['timestamp']}")
    print(f"Location: {alerta['location']}")
    print(f"Event Type: {alerta['event_type']}")
    print("Detected Alerts: ")
    for a in alerta ["detected_alerts"]:
        print(f"   - {a}")
    print("Mongo ID:", alerta["original_id"])
    print("---\n")

