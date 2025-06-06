# === visualize_data.py ===
# Visualiza eventos ambientales almacenados en MongoDB Atlas usando pandas y matplotlib

import pandas as pd
import matplotlib.pyplot as plt
from db_connection import db

# Leer datos de MongoDB
collection = db["seed_events"]
data = list(collection.find())

# Convertir a DataFrame
df = pd.DataFrame(data)

# Asegurar que haya datos
if df.empty:
    print("❌ No hay datos en la colección.")
    exit()

# Convertir la columna timestamp a formato datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Ordenar cronológicamente por si acaso
df = df.sort_values("timestamp")

# Gráfico 1: Temperatura a lo largo del tiempo
plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["temperature_c"], marker="o", linestyle="-", color="crimson", label="Temperatura (°C)")
plt.title("🌡️ Evolución de la Temperatura")
plt.xlabel("Tiempo")
plt.ylabel("Temperatura (°C)")
plt.grid(True)
plt.legend()
plt.tight_layout()
#plt.show()
plt.savefig("grafica_temperatura.png")