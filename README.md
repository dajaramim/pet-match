# Pet Match - CRUD de Mascotas para Gestión de Cruza Responsable

Prototipo funcional de un CRUD desarrollado con Django 1.11.6 para gestionar mascotas en Quilpué.

## 📋 Requisitos Técnicos Cumplidos

✅ Django 1.11.6 con patrón arquitectónico MVT  
✅ Aplicación llamada "movies" (compatibilidad profesor) con lógica Pet Match  
✅ Modelos: Breeds (Razas) y Pets (Mascotas) con relación ForeignKey  
✅ Vistas basadas en funciones (FBV) para CRUD completo  
✅ Decorador @login_required en vistas de creación y edición  
✅ Formularios: ModelForm para Pets y LoginForm para autenticación  
✅ Configuración de MEDIA y STATIC en settings.py  
✅ Soporte para Pillow (procesamiento de imágenes)  
✅ django-widget-tweaks para mejora de formularios  

## 📁 Estructura del Proyecto

```
crud/
├── manage.py
├── requirements.txt
├── petmatch/
│   ├── __init__.py
│   ├── settings.py       # Configuración del proyecto
│   ├── urls.py           # URLs principales
│   └── wsgi.py
├── movies/               # Aplicación principal
│   ├── models.py         # Modelos Breeds y Pets
│   ├── views.py          # Vistas FBV para CRUD
│   ├── forms.py          # Formularios ModelForm
│   ├── urls.py           # URLs de la app
│   ├── admin.py          # Admin personalizado
│   ├── apps.py
│   ├── tests.py
│   └── templates/
│       └── movies/
│           ├── base.html
│           ├── index.html
│           ├── login.html
│           ├── register.html
│           ├── pet_list.html
│           ├── pet_detail.html
│           ├── pet_form.html
│           └── pet_confirm_delete.html
├── media/                # Archivos subidos por usuarios
└── staticfiles/          # Archivos estáticos compilados
```

## 🚀 Instalación

### 1. Crear ambiente virtual (si no existe)
```bash
python -m venv env
env\Scripts\activate  # Windows
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Realizar migraciones
```bash
python manage.py migrate
```

### 4. Crear superusuario (admin)
```bash
python manage.py createsuperuser
```

### 5. Ejecutar servidor de desarrollo
```bash
python manage.py runserver
```

Accede a:
- **Sitio web:** http://localhost:8000
- **Admin:** http://localhost:8000/admin

## 📚 Funcionalidades

### Autenticación
- Registro de nuevos usuarios
- Login/Logout
- Protección de vistas con @login_required

### Mascotas (CRUD)
- **Listar**: Ver todas las mascotas disponibles con filtros y búsqueda
- **Ver Detalle**: Información completa de la mascota
- **Crear**: Agregar nueva mascota (requiere login)
- **Editar**: Modificar datos de mascota (solo dueño)
- **Eliminar**: Borrar mascota (solo dueño)

### Características Especiales
- Gestión de razas (Breeds)
- Información de salud y genética
- Subida de fotos
- Certificados de salud
- Cálculo automático de edad
- Filtros por raza y búsqueda

## 🗂️ Modelos de Datos

### Breeds (Razas)
- name: CharField
- description: TextField
- characteristics: TextField
- created_at: DateTimeField
- updated_at: DateTimeField

### Pets (Mascotas)
- owner: ForeignKey(User)
- breed: ForeignKey(Breeds)
- name: CharField
- gender: CharField (choices: M/F)
- birth_date: DateField
- description: TextField (salud/genética)
- image: ImageField
- health_certificate: FileField (opcional)
- is_available: BooleanField
- created_at: DateTimeField
- updated_at: DateTimeField

## 🔒 Seguridad

- Autenticación requerida para crear/editar mascotas
- Solo dueños pueden editar/eliminar sus mascotas
- CSRF protection en todos los formularios
- Validación de imágenes (máximo 5MB)
- SQL injection prevención (Django ORM)

## 🎨 Interfaz de Usuario

- Diseño responsivo con Bootstrap 4
- Navegación intuitiva
- Gradientes modernos (púrpura y azul)
- Cards interactivas con hover effects
- Formularios con validación en cliente
- Alertas y mensajes de estado

## 🧪 Testing

Ejecutar tests:
```bash
python manage.py test movies
```

## 📝 Notas

- Los archivos de usuarios se guardan en: `media/pets/` y `media/certificates/`
- Los archivos estáticos se sirven desde: `staticfiles/`
- Base de datos SQLite en: `db.sqlite3`
- Configurado para desarrollo (DEBUG=True)

## 🔧 Configuración para Producción

Cambiar en `petmatch/settings.py`:
```python
DEBUG = False
SECRET_KEY = 'usar-valor-seguro'
ALLOWED_HOSTS = ['tu-dominio.com']
```

Ejecutar:
```bash
python manage.py collectstatic
```

## 📞 Contacto & Soporte

Desarrollado para la Universidad UNAB - Quilpué, Chile
Proyecto Universitario: Pet Match - Plataforma de Cruza Responsable

---

**Versión:** 1.0  
**Django:** 1.11.6  
**Python:** 3.x  
**Última actualización:** 2026
