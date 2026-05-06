"""
Comandos útiles para Pet Match

Ejecutar desde la carpeta raíz del proyecto
"""

# ============================================================================
# CONFIGURACIÓN INICIAL
# ============================================================================

# Crear superusuario (admin)
python manage.py createsuperuser

# Realizar migraciones
python manage.py migrate

# Ver migraciones pendientes
python manage.py showmigrations

# Crear migraciones de cambios en modelos
python manage.py makemigrations

# Revertir migraciones (cuidado)
python manage.py migrate movies 0001_initial


# ============================================================================
# SERVIDOR
# ============================================================================

# Ejecutar servidor de desarrollo
python manage.py runserver

# Ejecutar en puerto específico
python manage.py runserver 8080

# Ejecutar en IP específica
python manage.py runserver 0.0.0.0:8000


# ============================================================================
# BASE DE DATOS
# ============================================================================

# Ejecutar shell de Django
python manage.py shell

# Hacer backup de base de datos
python manage.py dumpdata > backup.json

# Restaurar base de datos
python manage.py loaddata backup.json

# Ver SQL de una operación
python manage.py sqlmigrate movies 0001


# ============================================================================
# TESTING
# ============================================================================

# Ejecutar todos los tests
python manage.py test

# Tests de una app específica
python manage.py test movies

# Tests de una clase específica
python manage.py test movies.tests.PetsTestCase

# Tests verboso
python manage.py test --verbosity=2


# ============================================================================
# ARCHIVOS ESTÁTICOS
# ============================================================================

# Recopilar archivos estáticos
python manage.py collectstatic

# Recopilar sin confirmar
python manage.py collectstatic --noinput

# Ver dónde irán los estáticos
python manage.py findstatic css/style.css


# ============================================================================
# ADMINISTRACIÓN DE DATOS
# ============================================================================

# Ejemplos de comandos en shell de Django

# python manage.py shell

# Listar todas las mascotas
from movies.models import Pets
Pets.objects.all()

# Listar mascotas disponibles
Pets.objects.filter(is_available=True)

# Crear una raza
from movies.models import Breeds
breed = Breeds.objects.create(name="Golden Retriever", description="Perro amigable")

# Buscar mascotas por dueño
from django.contrib.auth.models import User
user = User.objects.get(username='testuser')
user.pets_set.all()

# Contar mascotas disponibles
Pets.objects.filter(is_available=True).count()

# Eliminar una mascota
pet = Pets.objects.get(pk=1)
pet.delete()

# Actualizar mascota
pet = Pets.objects.get(pk=1)
pet.is_available = False
pet.save()


# ============================================================================
# OTRAS UTILIDADES
# ============================================================================

# Ver variables de entorno de Django
python manage.py diffsettings

# Validar modelos
python manage.py check

# Ver información del proyecto
python manage.py info

# Limpiar archivos estáticos sin usar
python manage.py collectstatic --clear

# Crear app nueva
python manage.py startapp nueva_app

# Crear proyecto nuevo
django-admin startproject nuevo_proyecto
