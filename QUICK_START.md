# 🚀 Quick Start Guide - Pet Match en 5 Minutos

## Paso 1: Preparar el Ambiente (1 minuto)

```bash
# Activar ambiente virtual
env\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## Paso 2: Configurar Base de Datos (1 minuto)

```bash
# Ejecutar migraciones
python manage.py migrate

# Crear superusuario (admin)
python manage.py createsuperuser
# Ingresar:
# - Username: admin
# - Email: admin@petmatch.com
# - Password: admin123
```

## Paso 3: Cargar Datos de Prueba (1 minuto)

```bash
# Ejecutar shell de Django
python manage.py shell

# Dentro del shell, ejecutar:
exec(open('load_test_data.py').read())

# Salir (Ctrl+D o exit())
```

## Paso 4: Ejecutar Servidor (1 minuto)

```bash
python manage.py runserver
```

## Paso 5: Acceder a la Plataforma (1 minuto)

Abrir navegador en:

| Sección | URL |
|---------|-----|
| 🏠 Inicio | http://localhost:8000 |
| 🐾 Mascotas | http://localhost:8000/mascotas/ |
| 👤 Login | http://localhost:8000/login/ |
| ⚙️ Admin | http://localhost:8000/admin |

---

## 📱 Prueba Rápida

### Usuario de Prueba

```
Usuario: dueno1
Contraseña: password123
```

### Acciones para Probar

1. **Ver mascotas públicas**
   - Ir a http://localhost:8000/mascotas/
   - Ver lista y detalles

2. **Iniciar sesión**
   - Click en "Iniciar Sesión"
   - Ingresar dueno1 / password123
   - Ver "Mis Mascotas"

3. **Crear mascota**
   - Click en "+ Agregar Mascota"
   - Completar formulario
   - Subir foto (o usar placeholder)
   - Guardar

4. **Editar mascota**
   - Ir a "Mis Mascotas"
   - Click en "Editar"
   - Cambiar datos
   - Guardar

5. **Ver admin**
   - Ir a http://localhost:8000/admin
   - Login: admin / admin123
   - Ver mascotas, razas, usuarios

---

## 🔍 Estructura de Carpetas Importante

```
crud/
├── manage.py              # Comando principal de Django
├── requirements.txt       # Dependencias
├── load_test_data.py      # Cargar datos de prueba
├── petmatch/
│   └── settings.py        # Configuración (MEDIA, STATIC, etc.)
├── movies/
│   ├── models.py          # Modelos Breeds, Pets
│   ├── views.py           # Vistas CRUD
│   ├── forms.py           # Formularios
│   ├── urls.py            # Rutas
│   └── templates/         # HTML
└── media/                 # Fotos subidas
```

---

## 🐛 Solución de Problemas

### No funciona la imagen
```bash
# Crear carpeta media si no existe
mkdir media
mkdir media\pets
mkdir media\certificates
```

### Error de migraciones
```bash
# Eliminar db.sqlite3 y comenzar de nuevo
del db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

### Puerto 8000 en uso
```bash
python manage.py runserver 8080
```

### Problemas con Pillow
```bash
# Reinstalar Pillow
pip install --upgrade Pillow==8.3.2
```

---

## 📚 Próximos Pasos

1. **Explorar código**
   - Ver `movies/models.py` para entender estructura
   - Ver `movies/views.py` para lógica de negocio
   - Ver `movies/templates/` para interfaz

2. **Hacer cambios**
   - Agregar campos a modelos
   - Crear nuevas vistas
   - Personalizar templates

3. **Aprender más**
   - Leer `DEVELOPMENT_GUIDE.md`
   - Revisar `API_ENDPOINTS.md`
   - Ver `DJANGO_COMMANDS.md`

---

## ✅ Verificar que Todo Funciona

```bash
# Test 1: Base de datos
python manage.py check

# Test 2: Servidor
python manage.py runserver
# Abrir http://localhost:8000
# Debería ver la página de inicio

# Test 3: Admin
# Ir a http://localhost:8000/admin
# Debería poder iniciar sesión

# Test 4: Tests
python manage.py test movies
```

---

## 🎯 Funcionalidades Principales

| Función | Ubicación |
|---------|-----------|
| Ver mascotas | http://localhost:8000/mascotas/ |
| Crear mascota | http://localhost:8000/mascota/crear/ |
| Editar mascota | http://localhost:8000/mascota/[id]/editar/ |
| Eliminar mascota | http://localhost:8000/mascota/[id]/eliminar/ |
| Admin | http://localhost:8000/admin/ |

---

## 💡 Consejos

1. **Siempre activar venv**: `env\Scripts\activate`
2. **Backup de datos**: `python manage.py dumpdata > backup.json`
3. **Ver SQL**: `python manage.py sqlmigrate movies 0001`
4. **Debug en vistas**: `print(variable)` y revisar consola

---

## 📞 Ayuda

Si algo no funciona:

1. Revisar errores en consola
2. Buscar en `DJANGO_COMMANDS.md`
3. Ver `DEVELOPMENT_GUIDE.md`
4. Leer docs de Django 1.11

---

**¡Listo! Ya tienes Pet Match funcionando 🐾**

Cualquier duda, revisar la documentación completa incluida en el proyecto.
