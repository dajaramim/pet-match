# 🐾 Pet Match API - Endpoints y Rutas

## 📍 URLs Disponibles

### Autenticación

| Ruta | Método | Descripción | Autenticación |
|------|--------|-------------|---------------|
| `/login/` | GET, POST | Iniciar sesión | No requerida |
| `/logout/` | GET | Cerrar sesión | Requerida |
| `/register/` | GET, POST | Registrar nuevo usuario | No requerida |

### Páginas Principales

| Ruta | Método | Descripción | Autenticación |
|------|--------|-------------|---------------|
| `/` | GET | Página de inicio | No requerida |
| `/mascotas/` | GET | Listar mascotas disponibles | No requerida |
| `/mis-mascotas/` | GET | Listar mis mascotas | Requerida |

### CRUD de Mascotas

| Ruta | Método | Descripción | Autenticación | Permisos |
|------|--------|-------------|---------------|----------|
| `/mascota/<id>/` | GET | Ver detalle de mascota | No requerida | Cualquiera |
| `/mascota/crear/` | GET, POST | Crear nueva mascota | Requerida | Usuario autenticado |
| `/mascota/<id>/editar/` | GET, POST | Editar mascota | Requerida | Dueño de mascota |
| `/mascota/<id>/eliminar/` | GET, POST | Eliminar mascota | Requerida | Dueño de mascota |

---

## 🔐 Decoradores de Seguridad

Todas las vistas de creación y edición están protegidas con:

```python
@login_required(login_url='login')
```

Esto redirige a `/login/` si el usuario no está autenticado.

---

## 📊 Parámetros de Consulta (GET)

### Filtros en `/mascotas/`

```
# Buscar por nombre
GET /mascotas/?search=Max

# Filtrar por raza
GET /mascotas/?breed=1

# Combinar filtros
GET /mascotas/?search=Max&breed=1

# Ordenar por fecha (descendente por defecto)
GET /mascotas/  # Ordenadas por -created_at
```

---

## 📨 Parámetros POST

### Crear/Editar Mascota

```python
POST /mascota/crear/
POST /mascota/<id>/editar/

# Datos requeridos
{
    'breed': 1,                              # ID de raza
    'name': 'Max',                           # Nombre (obligatorio)
    'gender': 'M',                           # 'M' o 'F'
    'birth_date': '2020-01-15',              # Formato: YYYY-MM-DD
    'description': 'Perro saludable...',     # Obligatorio
    'image': <archivo>,                      # Foto (FormData)
    'health_certificate': <archivo>,         # Certificado (opcional)
    'is_available': True                     # Boolean
}
```

### Login

```python
POST /login/

# Datos requeridos
{
    'username': 'usuario',      # Nombre de usuario
    'password': 'contraseña'    # Contraseña
}
```

### Registro

```python
POST /register/

# Datos requeridos
{
    'username': 'nuevo_usuario',
    'email': 'usuario@example.com',
    'password': 'contraseña',
    'password_confirm': 'contraseña'
}
```

---

## 📋 Respuestas

### Respuestas Exitosas (2xx)

```
GET /mascotas/
- Status: 200 OK
- Retorna: Template pet_list.html con lista de mascotas

GET /mascota/1/
- Status: 200 OK
- Retorna: Template pet_detail.html con detalles

POST /mascota/crear/
- Status: 302 Redirect
- Redirige a: /mascota/<nueva_id>/
```

### Respuestas de Error (4xx/5xx)

```
GET /mascota/999/
- Status: 404 Not Found
- Retorna: Página de error 404

GET /mascota/1/editar/  (no eres dueño)
- Status: 302 Redirect
- Redirige a: /mis-mascotas/

GET /mi-mascota/crear/  (no autenticado)
- Status: 302 Redirect
- Redirige a: /login/?next=/mascota/crear/
```

---

## 🔄 Flujos de Usuario

### Registrarse y Crear Mascota

```
1. GET /register/                    → Mostrar formulario
2. POST /register/                   → Registrar usuario
3. Redirige a /mascotas/
4. GET /mi-mascota/crear/            → Mostrar formulario (requiere login)
5. POST /mi-mascota/crear/           → Crear mascota
6. Redirige a /mascota/<id>/         → Ver mascota creada
```

### Editar Mascota

```
1. GET /mascotas/                    → Ver lista de mascotas
2. GET /mascota/<id>/                → Ver detalle
3. GET /mascota/<id>/editar/         → Mostrar formulario (solo si eres dueño)
4. POST /mascota/<id>/editar/        → Guardar cambios
5. Redirige a /mascota/<id>/         → Ver cambios
```

### Eliminar Mascota

```
1. GET /mis-mascotas/                → Ver mis mascotas
2. GET /mascota/<id>/eliminar/       → Confirmar eliminación
3. POST /mascota/<id>/eliminar/      → Eliminar
4. Redirige a /mis-mascotas/         → Volver a lista
```

---

## 🔍 Ejemplo de Uso con curl

```bash
# Registrarse
curl -X POST http://localhost:8000/register/ \
  -d "username=dueno1&email=dueno@test.com&password=pass123&password_confirm=pass123"

# Login
curl -X POST http://localhost:8000/login/ \
  -d "username=dueno1&password=pass123" \
  -c cookies.txt

# Listar mascotas
curl http://localhost:8000/mascotas/

# Ver detalle
curl http://localhost:8000/mascota/1/

# Crear mascota (con archivo)
curl -X POST http://localhost:8000/mascota/crear/ \
  -b cookies.txt \
  -F "breed=1" \
  -F "name=Max" \
  -F "gender=M" \
  -F "birth_date=2020-01-15" \
  -F "description=Perro saludable" \
  -F "image=@foto.jpg" \
  -F "is_available=true"

# Buscar mascotas
curl "http://localhost:8000/mascotas/?search=Max&breed=1"
```

---

## 📦 Tipos de Datos

### Razas (Breeds)

```json
{
  "id": 1,
  "name": "Labrador Retriever",
  "description": "Perro amigable y leal",
  "characteristics": "Grande, energético",
  "created_at": "2026-04-17T10:30:00",
  "updated_at": "2026-04-17T10:30:00"
}
```

### Mascotas (Pets)

```json
{
  "id": 1,
  "owner_id": 1,
  "breed_id": 1,
  "name": "Max",
  "gender": "M",
  "birth_date": "2020-01-15",
  "age": 6,
  "description": "Perro saludable con excelente temperamento",
  "image": "/media/pets/max_photo.jpg",
  "health_certificate": "/media/certificates/cert_1.pdf",
  "is_available": true,
  "created_at": "2026-04-17T10:30:00",
  "updated_at": "2026-04-17T10:30:00"
}
```

### Usuario (User)

```json
{
  "id": 1,
  "username": "dueno1",
  "email": "dueno@example.com",
  "first_name": "Juan",
  "last_name": "Pérez",
  "is_active": true,
  "date_joined": "2026-04-17T10:30:00"
}
```

---

## 🔗 Nombres de Rutas (URL Names)

Para usar en templates con `{% url %}` o en vistas con `reverse()`:

```python
# Autenticación
'login'              → /login/
'logout'             → /logout/
'register'           → /register/

# Páginas
'index'              → /
'pet_list'           → /mascotas/
'my_pets'            → /mis-mascotas/

# CRUD
'pet_detail'         → /mascota/<id>/
'pet_create'         → /mascota/crear/
'pet_edit'           → /mascota/<id>/editar/
'pet_delete'         → /mascota/<id>/eliminar/
```

### Uso en Templates

```html
<!-- Enlace a lista de mascotas -->
<a href="{% url 'pet_list' %}">Mascotas</a>

<!-- Enlace a detalle específico -->
<a href="{% url 'pet_detail' pet.id %}">Ver {{ pet.name }}</a>

<!-- Formulario de edición -->
<form action="{% url 'pet_edit' pet.id %}" method="post">
    ...
</form>
```

---

## ⚙️ Configuración

### settings.py

```python
# Autenticación
LOGIN_URL = 'login'              # Ruta de login
LOGIN_REDIRECT_URL = 'pet_list'  # Redirige después de login
LOGOUT_REDIRECT_URL = 'login'    # Redirige después de logout

# Archivos
MEDIA_URL = '/media/'            # URL para archivos
MEDIA_ROOT = '/path/to/media'    # Ruta de almacenamiento

# Zona horaria
TIME_ZONE = 'America/Santiago'   # Quilpué, Chile
```

---

## 🧪 Testing APIs

```bash
# Con pytest-django
pytest movies/tests.py -v

# Con Django test runner
python manage.py test movies -v 2

# Test específico
python manage.py test movies.tests.PetsViewsTestCase.test_pet_list
```

---

## 📝 Notas Técnicas

1. **CSRF Protection**: Todos los POST requieren token CSRF
2. **Session Auth**: Usa sesiones de Django (cookies)
3. **Database**: SQLite 3 por defecto
4. **Media**: Archivos en `media/pets/` y `media/certificates/`
5. **Timezone**: America/Santiago (UTC-3 o UTC-4 con DST)

---

**Última actualización**: 2026  
**Django**: 1.11.6  
**API Version**: 1.0
