from db_connection import db
from datetime import datetime


collection = db["seed_events"]
alerts_collection = db["alerts_log"]

TEMP_MAX = 40
HUMIDITY_MIN = 15
RAINFALL_MAX = 120
WIND_MAX = 80

eventos = collection.find()

print("\n ALERTA DETECTADA:\n")

for evento in eventos:
    alertas = []

    if evento ["temperature_c"] > TEMP_MAX:
        alertas.append("Temperatura extrema")
    if evento ["humidity_percent"] < HUMIDITY_MIN:
        alertas.append("Humedad Crítica")
    if evento ["rainfall_mm"] > RAINFALL_MAX and evento["wind_speed_kmh"] > WIND_MAX:
        alertas.append("Posible DANA(tormenta grave)")
    if evento ["hail_detected"]:
        alertas.append("Granizo Detectado")
    if evento ["flood_risk_level"] in ["high", "extreme"]:
        alertas.append("Riesgo de inundación")
    if evento ["animal_alert"]:
        alertas.append("Riesgo para animales")


    if alertas:
        print(f"Evento en {evento['location']} - {evento['event_type']}")
        for a in alertas: 
            print(f"  - {a}")
        print("---")


        alert_doc = {
            "timestamp" : datetime.utcnow().isoformat(),
            "location" : evento["location"],
            "event_type" : evento["event_type"],
            "detected_alerts" : alertas,
            "original_id" : str(evento["_id"]),
        }
        alerts_collection.insert_one(alert_doc)

