# 🌦️ Configuración de la API de Clima

Esta guía te ayudará a configurar la integración con OpenWeatherMap para obtener datos del clima en tiempo real.

---

## 📋 Paso 1: Obtener API Key de OpenWeatherMap

### 1.1 Crear Cuenta
1. Ve a [https://openweathermap.org/](https://openweathermap.org/)
2. Haz clic en **Sign Up** (esquina superior derecha)
3. Completa el registro con tu email
4. Verifica tu email

### 1.2 Obtener tu API Key
1. Inicia sesión en OpenWeatherMap
2. Ve a tu perfil → **My API keys**
3. Copia el **Default API key** (o crea una nueva)

**IMPORTANTE**: La API key puede tardar hasta 2 horas en activarse (usualmente es instantáneo).

---

## 🔧 Paso 2: Configurar Variables de Entorno

### Para Desarrollo Local

Agrega la API key al archivo `.env`:

```bash
# Agregar al archivo .env
OPENWEATHER_API_KEY=tu_api_key_aqui
```

### Para Vercel (Producción)

1. Ve al Dashboard de Vercel
2. Selecciona tu proyecto **cali-seed**
3. Ve a **Settings** → **Environment Variables**
4. Agrega una nueva variable:
   - **Name**: `OPENWEATHER_API_KEY`
   - **Value**: Tu API key de OpenWeatherMap
   - **Environment**: Production, Preview, Development (todas)
5. Haz clic en **Save**
6. **Redespliega** el proyecto (Deployments → Redeploy)

---

## ✅ Paso 3: Verificar la Integración

### Probar Localmente

```bash
# Ejecutar el backend
python3 app.py

# En otro terminal, probar el endpoint
curl http://localhost:5000/api/weather

# O para una ubicación específica
curl http://localhost:5000/api/weather/Zaragoza
```

**Respuesta esperada:**
```json
{
  "success": true,
  "data": {
    "location": "Zaragoza",
    "temperature_c": 15.3,
    "humidity_percent": 65,
    "wind_speed_kmh": 12.5,
    ...
  }
}
```

### Probar en Producción (Vercel)

```bash
curl https://tu-app.vercel.app/api/weather
```

---

## 🌐 Usar la Interfaz Web

1. Abre tu aplicación (local o Vercel)
2. Haz clic en la pestaña **"Clima en Tiempo Real"**
3. Deberías ver 3 tarjetas con el clima actual de:
   - Zaragoza
   - Huesca
   - Teruel

Cada tarjeta muestra:
- 🌡️ Temperatura actual y sensación térmica
- 💧 Humedad
- 💨 Velocidad del viento
- ☁️ Porcentaje de nubes
- 🌧️ Precipitación (si hay)
- 👁️ Visibilidad
- 🌡️ Presión atmosférica
- ⚠️ Alertas automáticas (si se detectan condiciones extremas)

---

## 🚨 Detección de Alertas Automáticas

El sistema detecta automáticamente:

- ⚠️ **Temperatura alta** (>35°C) - Riesgo de ola de calor
- ⚠️ **Temperatura bajo cero** (<0°C) - Riesgo de heladas
- ⚠️ **Humedad muy baja** (<20%) - Riesgo de incendios
- ⚠️ **Vientos fuertes** (>70 km/h) - Posible tormenta
- ⚠️ **Lluvia intensa** (>20mm) - Riesgo de inundación

---

## 📊 Endpoints Disponibles

### GET `/api/weather`
Obtiene el clima actual de todas las ubicaciones (Zaragoza, Huesca, Teruel).

**Respuesta:**
```json
{
  "success": true,
  "count": 3,
  "data": [
    {
      "location": "Zaragoza",
      "temperature_c": 15.3,
      "humidity_percent": 65,
      "wind_speed_kmh": 12.5,
      "weather_description": "nubes dispersas",
      "alerts": ["Alerta si hay"]
    },
    ...
  ]
}
```

### GET `/api/weather/<location>`
Obtiene el clima de una ubicación específica.

**Ejemplo:**
```bash
GET /api/weather/Zaragoza
GET /api/weather/Huesca
GET /api/weather/Teruel
```

---

## 🐛 Solución de Problemas

### Error: "OPENWEATHER_API_KEY not configured"

**Causa**: La variable de entorno no está configurada.

**Solución**:
1. Verifica que agregaste la variable en `.env` (local) o en Vercel (producción)
2. Reinicia el servidor (local) o redespliega (Vercel)

### Error: "API request failed" o "401 Unauthorized"

**Causa**: API key inválida o no activada.

**Solución**:
1. Verifica que copiaste correctamente la API key
2. Espera 2 horas si acabas de crear la cuenta
3. Verifica que tu cuenta de OpenWeatherMap esté activa

### Error: "Location not supported"

**Causa**: La ubicación no está en la lista predefinida.

**Solución**: Solo están disponibles Zaragoza, Huesca y Teruel. Para agregar más ubicaciones, edita `weather_api.py`:

```python
LOCATIONS = {
    'Zaragoza': {'lat': 41.6488, 'lon': -0.8891},
    'Huesca': {'lat': 42.1401, 'lon': -0.4080},
    'Teruel': {'lat': 40.3456, 'lon': -1.1065},
    'TuCiudad': {'lat': XX.XXXX, 'lon': X.XXXX}  # Agregar aquí
}
```

---

## 💡 Plan Gratuito de OpenWeatherMap

El plan gratuito incluye:
- ✅ 1,000 llamadas por día
- ✅ Datos actuales del clima
- ✅ Sin costo
- ✅ Suficiente para desarrollo y uso moderado

**Límite de llamadas**: Con 1,000 llamadas/día y actualizaciones cada 30 segundos, puedes tener la app corriendo continuamente.

---

## 🔄 Actualización Automática

El frontend actualiza automáticamente los datos cada **30 segundos** cuando estás en la pestaña de "Clima en Tiempo Real".

También puedes hacer clic en el botón **🔄 Actualizar** para refrescar manualmente.

---

## 🌍 Alternativa: AEMET (API Española)

Si prefieres usar la **AEMET** (Agencia Estatal de Meteorología de España):

1. Solicita API key en: [https://opendata.aemet.es/centrodedescargas/inicio](https://opendata.aemet.es/centrodedescargas/inicio)
2. Modifica `weather_api.py` para usar AEMET en lugar de OpenWeatherMap
3. AEMET es gratuita y oficial de España

**Ventajas de AEMET**:
- Datos oficiales de España
- Gratuita
- Más precisa para territorio español

**Desventajas**:
- API más compleja de usar
- Requiere múltiples llamadas
- Documentación en español solamente

---

## 📝 Archivos Relacionados

- `weather_api.py` - Lógica de integración con OpenWeatherMap
- `api/index.py` - Endpoints del API (líneas 197-254)
- `public/app.js` - Frontend (funciones `loadWeather`, `createWeatherCard`)
- `public/index.html` - Pestaña de clima (línea 55-62)
- `public/style.css` - Estilos de tarjetas del clima

---

**¡Disfruta del clima en tiempo real en CALI + SEED! 🌱🌤️**
