# 🚀 QUICK START - CALI + SEED

Guía rápida para ejecutar el proyecto completo en **3 pasos**.

---

## ⚡ Inicio Rápido

### 1️⃣ Instalar Dependencias

```bash
# Crear y activar entorno virtual
python3 -m venv myenv
source myenv/bin/activate

# Instalar dependencias
pip install -r recursos.txt
```

### 2️⃣ Configurar Base de Datos

```bash
# Crear archivo .env con tu conexión MongoDB
echo "MONGO_URL=tu_conexion_mongodb_atlas" > .env

# Insertar datos de prueba
python3 seed_data.py

# Detectar alertas
python3 detect.py
```

### 3️⃣ Ejecutar el Sistema

**Terminal 1 - Backend:**
```bash
python3 app.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
python3 -m http.server 8000
```

**🌐 Abre tu navegador en:** http://localhost:8000

---

## 📊 Lo que verás

### Dashboard
- Estadísticas generales
- Gráficos por ubicación
- Actualización automática

### Eventos
- Lista de eventos ambientales
- Filtros por ubicación y tipo
- Datos de sensores (temperatura, humedad, etc.)

### Alertas
- Alertas críticas detectadas
- Detalles de cada alerta
- Filtro por ubicación

---

## 🔧 Endpoints del API

El backend expone estos endpoints en `http://localhost:5000`:

- `GET /` - Info de la API
- `GET /api/events` - Eventos ambientales
- `GET /api/alerts` - Alertas detectadas
- `GET /api/stats` - Estadísticas
- `GET /api/locations` - Ubicaciones disponibles

**Ejemplo de uso:**
```bash
curl http://localhost:5000/api/stats
```

---

## 💡 Tips

1. **Datos de prueba**: Ejecuta `seed_data.py` para generar nuevos eventos
2. **Actualizar alertas**: Ejecuta `detect.py` después de insertar nuevos datos
3. **Ver en consola**: Usa `view_alerts.py` para ver alertas en terminal
4. **Auto-refresh**: El frontend se actualiza cada 30 segundos

---

## 🐛 Problemas Comunes

**"Connection refused"**
→ Asegúrate de que el backend esté corriendo en el puerto 5000

**"No data available"**
→ Ejecuta `seed_data.py` y `detect.py` primero

**"MONGO_URL not found"**
→ Crea el archivo `.env` con tu cadena de conexión

---

## 📖 Más Información

- **Setup completo**: Ver `SETUP_FRONTEND.md`
- **Documentación**: Ver `README.md`

---

**¡Listo! Ya tienes CALI + SEED funcionando 🌱**
