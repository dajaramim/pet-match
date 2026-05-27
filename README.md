# Pet Match

Plataforma de cruza responsable de mascotas. Backend Django con API REST + Frontend Flutter Web/Mobile.

## Estructura del proyecto

```
pet-match/
├── petmatch/              # Configuración Django
├── movies/                # App principal (models, views, API)
│   ├── models.py          # Modelos Breeds y Pets
│   ├── views.py           # Vistas web (templates)
│   ├── api_views.py       # API REST endpoints
│   ├── api_urls.py        # Rutas de la API
│   └── serializers.py     # Serializers DRF
├── flutter_app/           # App Flutter (mobile + web)
│   ├── lib/
│   │   ├── main.dart      # UI principal
│   │   └── api_service.dart # Conexión con la API
│   └── build/web/         # Build web para Vercel
├── templates/             # Templates Django
├── vercel.json            # Config deploy Vercel
└── requirements.txt       # Dependencias Python
```

## Requisitos

- Python 3.10+
- Flutter SDK 3.11+ (para desarrollo mobile)
- pip

## Instalación y ejecución local

### 1. Backend Django

```bash
# Clonar el repositorio
git clone https://github.com/dajaramim/pet-match.git
cd pet-match

# Crear y activar ambiente virtual
python3 -m venv env
source env/bin/activate        # macOS/Linux
# env\Scripts\activate         # Windows

# Instalar dependencias
pip install -r requirements.txt

# Crear base de datos y migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# (Opcional) Cargar datos de prueba
python load_test_data.py

# Iniciar servidor
python manage.py runserver 0.0.0.0:8000
```

El backend queda disponible en:
- Web: http://localhost:8000
- API: http://localhost:8000/api/
- Admin: http://localhost:8000/admin

### 2. Flutter App (mobile)

```bash
cd flutter_app

# Instalar dependencias Dart
flutter pub get

# Ejecutar en dispositivo/emulador
flutter run
```

**Configurar URL del backend:**

En `lib/api_service.dart`, la URL se configura automáticamente según la plataforma:
- Android emulador: `http://10.0.2.2:8000`
- iOS simulador / macOS: `http://localhost:8000`
- Dispositivo físico: cambiar a tu IP local (ej: `http://192.168.1.100:8000`)

Para cambiar la IP manualmente, edita la línea correspondiente en `lib/main.dart`:
```dart
ApiService.setBaseUrl('http://TU_IP:8000');
```

## Endpoints de la API

| Método | Ruta | Auth | Descripción |
|--------|------|------|-------------|
| POST | `/api/login/` | No | Login, retorna token |
| POST | `/api/register/` | No | Registro de usuario |
| GET | `/api/pets/` | No | Listar mascotas disponibles |
| GET | `/api/pets/<id>/` | No | Detalle de mascota |
| GET | `/api/my-pets/` | Token | Mis mascotas |
| POST | `/api/pets/create/` | Token | Crear mascota |
| PUT | `/api/pets/<id>/edit/` | Token | Editar mascota |
| DELETE | `/api/pets/<id>/delete/` | Token | Eliminar mascota |
| GET | `/api/breeds/` | No | Listar razas |

**Autenticación:** Enviar header `Authorization: Token <tu_token>`

## Deploy

El proyecto se despliega en dos servicios gratuitos:
- **Vercel** → Frontend Flutter Web
- **Render** → Backend Django API

### Paso 1: Deploy del Backend en Render

1. Ir a [render.com](https://render.com) y crear cuenta con GitHub
2. Click en "New" → "Web Service"
3. Conectar el repositorio `dajaramim/pet-match`
4. Configurar:
   - **Name:** `pet-match-api`
   - **Runtime:** Python 3
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn petmatch.wsgi:application`
5. En "Environment Variables", agregar:
   - `SECRET_KEY` = (generar una clave segura)
   - `DEBUG` = `False`
   - `ALLOWED_HOSTS` = `pet-match-api.onrender.com`
6. Click "Create Web Service"

Tu backend quedará en: `https://pet-match-api.onrender.com`

Prueba que funcione:
```
https://pet-match-api.onrender.com/api/pets/
```

### Paso 2: Deploy del Frontend en Vercel

1. Ir a [vercel.com](https://vercel.com) e iniciar sesión con GitHub
2. Click en "Add New Project"
3. Importar el repositorio `dajaramim/pet-match`
4. Vercel detecta el `vercel.json` automáticamente
5. Click en "Deploy"

El `vercel.json` ya está configurado para servir `flutter_app/build/web/`.

### Paso 3: Conectar Frontend con Backend

Una vez que tengas la URL de Render, actualiza la URL del API en Flutter:

1. Editar `flutter_app/lib/api_service.dart`:
   ```dart
   static String baseUrl = 'https://pet-match-api.onrender.com';
   ```

2. Editar `flutter_app/lib/main.dart` (reemplazar la sección de configuración de URL):
   ```dart
   ApiService.setBaseUrl('https://pet-match-api.onrender.com');
   ```

3. Reconstruir Flutter Web:
   ```bash
   cd flutter_app
   flutter build web
   ```

4. Commit y push → Vercel re-despliega automáticamente.

### Crear datos iniciales en Render

Después del deploy, ve a Render → tu servicio → "Shell" tab y ejecuta:

```bash
python manage.py createsuperuser
python load_test_data.py
```

### Notas sobre el tier gratis de Render

- El servicio se apaga tras 15 minutos sin tráfico
- La primera petición después de inactividad tarda ~30 segundos (cold start)
- La base de datos SQLite se reinicia con cada deploy (los datos no persisten entre deploys)
- Para datos persistentes, usar PostgreSQL (Render ofrece PostgreSQL gratis por 90 días)

## Usuarios de prueba

| Usuario | Contraseña | Rol |
|---------|-----------|-----|
| admin | admin123 | Superusuario |
| daniel | 1234 | Usuario normal |

## Tecnologías

- **Backend:** Django 4.2, Django REST Framework, SQLite
- **Frontend Mobile/Web:** Flutter 3.11, Dart
- **Deploy:** Vercel (frontend), compatible con Railway/Render (backend)
