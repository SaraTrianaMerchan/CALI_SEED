from datetime import datetime
import random
from db_connection import db

collection = db["seed_events"]

locations = ["Zaragoza", "Huesca", "Teruel"]
event_types = ["flood_warning", "hailstrom", "heatwave", "wildfire_risk", "storm_anomaly"]

def generate_event():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "location": random.choice(locations),
        "event_type": random.choice(event_types),
        "soil_moisture": round(random.uniform(3, 90), 2),
        "temperature_c": round(random.uniform(-5, 45), 1),
        "humidity_percent": round(random.uniform(10, 100), 1),
        "rainfall_mm": round(random.uniform(0, 200), 1),
        "wind_speed_kmh": round(random.uniform(0, 130), 1),
        "hail_detected": random.choice([True, False]),
        "flood_risk_level": random.choice(["low", "moderate", "high", "extreme"]),
        "animal_alert": random.choice([True, False]),
        "alert_triggered": False
    }

documents = [generate_event() for _ in range(10)]
result = collection.insert_many(documents)
print(f"Insertados {len(result.inserted_ids)} eventos.")

