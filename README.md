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

## Deploy a Vercel (Frontend Flutter Web)

El frontend Flutter Web ya está pre-compilado en `flutter_app/build/web/`.

### Opción 1: Deploy automático con GitHub

1. Ir a [vercel.com](https://vercel.com) e iniciar sesión
2. Click en "Add New Project"
3. Importar el repositorio `dajaramim/pet-match`
4. Vercel detecta el `vercel.json` automáticamente
5. Click en "Deploy"

El `vercel.json` ya está configurado para servir `flutter_app/build/web/`.

### Opción 2: Deploy manual con CLI

```bash
# Instalar Vercel CLI
npm i -g vercel

# Desde la raíz del proyecto
cd pet-match
vercel
```

### Actualizar el build web

Si modificas el código Flutter y necesitas actualizar el build:

```bash
cd flutter_app
flutter build web
```

Luego haz commit y push. Vercel re-despliega automáticamente.

### Nota sobre el backend en producción

El frontend en Vercel es solo la parte visual (Flutter Web). Para que funcione con datos reales, necesitas el backend Django corriendo en algún servidor. Opciones:

- **Railway** / **Render** / **PythonAnywhere** para el backend Django
- Actualizar `ApiService.setBaseUrl()` en el código Flutter para apuntar a la URL del backend en producción
- Reconstruir el build web con la URL correcta

## Usuarios de prueba

| Usuario | Contraseña | Rol |
|---------|-----------|-----|
| admin | admin123 | Superusuario |
| daniel | 1234 | Usuario normal |

## Tecnologías

- **Backend:** Django 4.2, Django REST Framework, SQLite
- **Frontend Mobile/Web:** Flutter 3.11, Dart
- **Deploy:** Vercel (frontend), compatible con Railway/Render (backend)
