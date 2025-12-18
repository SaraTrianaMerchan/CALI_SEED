# 🚀 Guía de Despliegue en Vercel

Esta guía te ayudará a desplegar CALI + SEED en Vercel.

---

## 📋 Pre-requisitos

1. Cuenta en [Vercel](https://vercel.com)
2. Repositorio Git (GitHub, GitLab, o Bitbucket)
3. MongoDB Atlas configurado
4. Código subido al repositorio

---

## 🔧 Configuración Paso a Paso

### 1. Preparar el Repositorio

Asegúrate de que tu repositorio contenga estos archivos:

```
CALI_SEED/
├── api/
│   └── index.py          # Backend serverless
├── frontend/
│   ├── index.html        # Frontend
│   ├── style.css
│   └── app.js
├── vercel.json           # Configuración de Vercel
├── requirements.txt      # Dependencias Python
├── db_connection.py      # Conexión MongoDB
└── .gitignore
```

### 2. Conectar Vercel con tu Repositorio

1. Ve a [vercel.com](https://vercel.com)
2. Haz clic en **"Add New Project"**
3. Selecciona tu repositorio de GitHub
4. Importa el proyecto

### 3. Configurar Variables de Entorno

En la configuración del proyecto en Vercel:

1. Ve a **Settings** → **Environment Variables**
2. Agrega la siguiente variable:

```
Name: MONGO_URL
Value: mongodb+srv://usuario:password@cluster.mongodb.net/cali_db
```

**IMPORTANTE**: Reemplaza con tu cadena de conexión real de MongoDB Atlas.

### 4. Configurar el Proyecto

Vercel debería detectar automáticamente la configuración desde `vercel.json`.

Si no lo hace, configura manualmente:

- **Framework Preset**: `Other`
- **Root Directory**: `./` (raíz del proyecto)
- **Build Command**: (dejar vacío)
- **Output Directory**: `frontend`

### 5. Desplegar

1. Haz clic en **"Deploy"**
2. Espera a que termine el despliegue (2-3 minutos)
3. Vercel te dará una URL como: `https://tu-proyecto.vercel.app`

---

## 🔍 Verificar el Despliegue

### Probar el Backend

Abre en tu navegador:
```
https://tu-proyecto.vercel.app/api
```

Deberías ver:
```json
{
  "message": "CALI + SEED API",
  "version": "1.0",
  "status": "online",
  "endpoints": [...]
}
```

### Probar el Frontend

Abre:
```
https://tu-proyecto.vercel.app
```

Deberías ver el dashboard de CALI + SEED.

---

## 🐛 Solución de Problemas

### Error: 404 NOT_FOUND

**Causa**: Vercel no encuentra los archivos.

**Solución**:
1. Verifica que `vercel.json` esté en la raíz del proyecto
2. Asegúrate de que la carpeta `frontend/` exista
3. Redespliega el proyecto

### Error: Database not available

**Causa**: MongoDB no está conectado.

**Solución**:
1. Verifica que la variable `MONGO_URL` esté configurada en Vercel
2. Asegúrate de que tu IP esté en la whitelist de MongoDB Atlas (o permite todas las IPs: `0.0.0.0/0`)
3. Verifica que la cadena de conexión sea correcta

### Error: 500 Internal Server Error

**Causa**: Error en el backend.

**Solución**:
1. Ve a **Deployments** → selecciona el último despliegue
2. Haz clic en **"View Function Logs"**
3. Revisa los errores en los logs
4. Verifica que todas las dependencias estén en `requirements.txt`

### Error: CORS

**Causa**: Problemas de origen cruzado.

**Solución**:
- El backend ya tiene CORS configurado con `Flask-CORS`
- Si persiste, verifica que el frontend esté haciendo peticiones a `/api` y no a otro dominio

---

## 🔄 Actualizar el Despliegue

Cada vez que hagas un `git push` a tu rama principal, Vercel automáticamente:
1. Detectará los cambios
2. Reconstruirá el proyecto
3. Desplegará la nueva versión

Para desplegar manualmente:
1. Ve a tu proyecto en Vercel
2. Haz clic en **"Redeploy"**

---

## 📊 Monitoreo

Vercel proporciona:
- **Analytics**: Tráfico y rendimiento
- **Logs**: Errores y ejecuciones de funciones
- **Deployments**: Historial de despliegues

Accede a ellos desde el dashboard del proyecto.

---

## 🌐 Dominio Personalizado (Opcional)

1. Ve a **Settings** → **Domains**
2. Agrega tu dominio personalizado
3. Configura los registros DNS según las instrucciones
4. Espera la propagación (24-48 horas)

---

## 💡 Tips Adicionales

1. **Rama de Producción**: Configura `main` o `master` como rama de producción
2. **Preview Deployments**: Cada rama tendrá su propio preview deployment
3. **Rollback**: Puedes volver a versiones anteriores fácilmente
4. **Límites**: Plan gratuito tiene límites de uso (100GB bandwidth, 100 hours serverless)

---

## 📞 Soporte

Si tienes problemas:
1. Revisa la [documentación de Vercel](https://vercel.com/docs)
2. Revisa los logs del deployment
3. Verifica la configuración de MongoDB Atlas

---

## ✅ Checklist de Despliegue

- [ ] Repositorio conectado a Vercel
- [ ] Variable `MONGO_URL` configurada
- [ ] Archivos `vercel.json` y `requirements.txt` presentes
- [ ] MongoDB Atlas permite conexiones de cualquier IP (0.0.0.0/0)
- [ ] Datos insertados en la base de datos (ejecutar `seed_data.py` y `detect.py`)
- [ ] Primer despliegue completado
- [ ] API responde correctamente en `/api`
- [ ] Frontend carga correctamente en `/`
- [ ] Dashboard muestra datos

---

**¡Tu aplicación CALI + SEED está lista en la nube! 🌱☁️**
