# 🌱 CALI + SEED - Guía de Configuración Frontend + Backend

Esta guía te ayudará a configurar y ejecutar el sistema completo de CALI + SEED con frontend y backend.

---

## 📋 Requisitos Previos

- Python 3.8+
- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- MongoDB Atlas configurado (o conexión a MongoDB)
- Variables de entorno configuradas

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone <tu-repositorio>
cd CALI_SEED
```

### 2. Crear entorno virtual

```bash
python3 -m venv myenv
source myenv/bin/activate  # En Windows: myenv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r recursos.txt
```

### 4. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```bash
MONGO_URL=mongodb+srv://usuario:password@cluster.mongodb.net/
```

---

## 🗄️ Configurar Base de Datos

### 1. Insertar datos de prueba

```bash
python3 seed_data.py
```

### 2. Ejecutar detección de alertas

```bash
python3 detect.py
```

### 3. Verificar datos (opcional)

```bash
python3 view_alerts.py
```

---

## ⚙️ Ejecutar el Backend API

En una terminal, ejecuta:

```bash
python3 app.py
```

Deberías ver:

```
🌱 CALI + SEED API Server Starting...
📍 Endpoints available at http://localhost:5000
📊 Access API documentation at http://localhost:5000/
```

**Endpoints disponibles:**
- `GET /` - Información de la API
- `GET /api/events` - Obtener eventos ambientales
- `GET /api/alerts` - Obtener alertas detectadas
- `GET /api/stats` - Obtener estadísticas
- `GET /api/locations` - Obtener ubicaciones

---

## 🌐 Ejecutar el Frontend

### Opción 1: Servidor web simple con Python

En otra terminal (mantén el backend corriendo):

```bash
cd frontend
python3 -m http.server 8000
```

Abre tu navegador en: **http://localhost:8000**

### Opción 2: Abrir directamente el archivo HTML

Simplemente abre el archivo `frontend/index.html` en tu navegador.

---

## 📊 Uso de la Interfaz

### Dashboard
- Visualiza estadísticas generales del sistema
- Gráficos de eventos y alertas por ubicación
- Actualización automática cada 30 segundos

### Eventos
- Lista completa de eventos ambientales
- Filtros por ubicación y tipo de evento
- Detalles de temperatura, humedad, lluvia, viento, etc.

### Alertas
- Alertas críticas detectadas por el sistema
- Filtro por ubicación
- Detalles de cada tipo de alerta

---

## 🔧 Solución de Problemas

### Error: "No se puede conectar al backend"

1. Verifica que el backend esté corriendo en `http://localhost:5000`
2. Revisa que no haya errores en la terminal del backend
3. Verifica la configuración de CORS en `app.py`

### Error: "No hay datos disponibles"

1. Asegúrate de haber ejecutado `seed_data.py` primero
2. Ejecuta `detect.py` para generar alertas
3. Verifica la conexión a MongoDB en el archivo `.env`

### Error: "MONGO_URL no encontrado"

1. Crea el archivo `.env` en la raíz del proyecto
2. Agrega tu cadena de conexión de MongoDB Atlas
3. Reinicia el backend

---

## 🏗️ Estructura del Proyecto

```
CALI_SEED/
├── app.py                  # Backend API Flask
├── db_connection.py        # Conexión a MongoDB
├── seed_data.py           # Insertar datos de prueba
├── detect.py              # Detectar alertas
├── view_alerts.py         # Ver alertas en consola
├── visualize_data.py      # Visualización de datos
├── recursos.txt           # Dependencias Python
├── .env                   # Variables de entorno
├── SETUP_FRONTEND.md      # Esta guía
└── frontend/
    ├── index.html         # Interfaz principal
    ├── style.css          # Estilos
    └── app.js             # Lógica del frontend
```

---

## 🎯 Próximos Pasos

1. **Mejorar la interfaz**: Agregar más visualizaciones y gráficos
2. **Autenticación**: Implementar login y roles de usuario
3. **Tiempo real**: Integrar WebSockets para actualizaciones en vivo
4. **Predicciones**: Agregar modelos ML para predicción de eventos
5. **Notificaciones**: Sistema de alertas por email/SMS
6. **Dashboard avanzado**: Mapas interactivos de ubicaciones

---

## 👥 Autor

Desarrollado con 💚 por **Sara Triana Merchán**

- LinkedIn: [Sara Triana Merchán](https://www.linkedin.com/in/sara-triana-merchan)
- GitHub: [SaraTrianaMerchan](https://github.com/SaraTrianaMerchan)
- Devpost: [saratrianamerchan](https://devpost.com/saratrianamerchan)

---

## 📄 Licencia

Este proyecto está desarrollado para apoyar a las comunidades rurales en la detección temprana de eventos ambientales extremos.

---

**¡Disfruta usando CALI + SEED! 🌱**
