# 🚀 Guía Rápida de Desarrollo - Pet Match

## 📖 Índice
1. [Estructura del Proyecto](#estructura-del-proyecto)
2. [Primeros Pasos](#primeros-pasos)
3. [Trabajar con Modelos](#trabajar-con-modelos)
4. [Trabajar con Vistas](#trabajar-con-vistas)
5. [Trabajar con Formularios](#trabajar-con-formularios)
6. [Agregar Nuevas Funcionalidades](#agregar-nuevas-funcionalidades)

---

## 📁 Estructura del Proyecto

```
petmatch/          # Configuración principal del proyecto
  ├── settings.py  # Configuración de Django
  ├── urls.py      # Rutas principales
  └── wsgi.py      # WSGI para servidor web

movies/            # Aplicación principal de mascotas
  ├── models.py    # Definición de datos (Breeds, Pets)
  ├── views.py     # Lógica de negocio
  ├── forms.py     # Formularios
  ├── urls.py      # Rutas de la app
  ├── admin.py     # Panel administrativo
  └── templates/   # HTML
```

---

## ⚡ Primeros Pasos

### 1. Configurar ambiente
```bash
# Activar ambiente virtual
env\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

### 2. Crear datos de prueba
```bash
python manage.py shell
```

```python
from movies.models import Breeds, Pets
from django.contrib.auth.models import User
from datetime import date

# Crear razas
labrador = Breeds.objects.create(
    name='Labrador Retriever',
    description='Perro amigable y leal',
    characteristics='Grande, energético, excelente con familias'
)

# Crear usuario
user = User.objects.create_user(
    username='dueno1',
    email='dueno@example.com',
    password='pass123'
)

# Crear mascota
pet = Pets.objects.create(
    owner=user,
    breed=labrador,
    name='Max',
    gender='M',
    birth_date=date(2020, 5, 15),
    description='Max es un labrador saludable con buen temperamento',
    is_available=True
)

print(f"Mascota creada: {pet}")
```

---

## 🗄️ Trabajar con Modelos

### Modelo Breeds (Razas)

```python
from movies.models import Breeds

# Crear una raza
breed = Breeds.objects.create(
    name='Pastor Alemán',
    description='Perro inteligente y trabajador',
    characteristics='Grande, leal, excelente para trabajo'
)

# Leer
breed = Breeds.objects.get(name='Pastor Alemán')
print(breed.description)

# Actualizar
breed.characteristics = 'Actualizado'
breed.save()

# Eliminar
breed.delete()

# Listar todas
razas = Breeds.objects.all()

# Buscar
raza = Breeds.objects.filter(name__icontains='Pastor')
```

### Modelo Pets (Mascotas)

```python
from movies.models import Pets
from datetime import date
from django.contrib.auth.models import User

# Crear mascota
user = User.objects.get(username='dueno1')
breed = Breeds.objects.get(name='Labrador Retriever')

pet = Pets.objects.create(
    owner=user,
    breed=breed,
    name='Luna',
    gender='F',
    birth_date=date(2021, 3, 10),
    description='Hembra saludable, línea de reproducción excelente',
    is_available=True
)

# Obtener edad
edad = pet.age()
print(f"{pet.name} tiene {edad} años")

# Listar mascotas de un usuario
mis_mascotas = Pets.objects.filter(owner=user)

# Mascotas disponibles
disponibles = Pets.objects.filter(is_available=True)

# Filtrar por raza
labradores = Pets.objects.filter(breed__name='Labrador Retriever')

# Búsqueda compleja
mascotas = Pets.objects.filter(
    breed__name='Labrador',
    gender='F',
    is_available=True
).select_related('owner', 'breed')

for mascota in mascotas:
    print(f"{mascota.name} - {mascota.breed.name}")
```

---

## 👁️ Trabajar con Vistas

Las vistas usan el patrón FBV (Function-Based Views) y están decoradas con `@login_required` donde es necesario.

### Vistas de Mascotas

```python
# Ver todas las mascotas (pública)
# GET /mascotas/

# Ver mis mascotas (requiere login)
# GET /mis-mascotas/

# Ver detalle de mascota (pública)
# GET /mascota/<id>/

# Crear mascota (requiere login)
# GET /mascota/crear/
# POST /mascota/crear/

# Editar mascota (requiere login + es dueño)
# GET /mascota/<id>/editar/
# POST /mascota/<id>/editar/

# Eliminar mascota (requiere login + es dueño)
# GET /mascota/<id>/eliminar/
# POST /mascota/<id>/eliminar/
```

### Agregar Nueva Vista

```python
# En movies/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pets, Breeds

@login_required
def pet_statistics(request):
    """Vista para mostrar estadísticas de mascotas"""
    total_pets = Pets.objects.filter(owner=request.user).count()
    available = Pets.objects.filter(owner=request.user, is_available=True).count()
    
    context = {
        'total_pets': total_pets,
        'available': available,
        'title': 'Estadísticas'
    }
    return render(request, 'movies/statistics.html', context)
```

### Registrar ruta

```python
# En movies/urls.py
from . import views

urlpatterns = [
    # ... otros urls
    url(r'^estadisticas/$', views.pet_statistics, name='statistics'),
]
```

---

## 📋 Trabajar con Formularios

### Usar Formularios en Vistas

```python
# En views.py
from .forms import PetsForm

@login_required
def pet_edit(request, pk):
    pet = get_object_or_404(Pets, pk=pk)
    
    if pet.owner != request.user:
        return redirect('my_pets')
    
    if request.method == 'POST':
        form = PetsForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_detail', pk=pet.pk)
    else:
        form = PetsForm(instance=pet)
    
    return render(request, 'movies/pet_form.html', {'form': form, 'pet': pet})
```

### Personalizar Formularios

```python
# En forms.py
from django import forms
from .models import Pets

class PetsForm(forms.ModelForm):
    class Meta:
        model = Pets
        fields = ['breed', 'name', 'gender', 'birth_date', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la mascota'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control'
            })
        }
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError('El nombre debe tener al menos 2 caracteres')
        return name
```

---

## ✨ Agregar Nuevas Funcionalidades

### 1. Agregar campo a Mascota

```python
# 1. Modificar models.py
from django.db import models

class Pets(models.Model):
    # ... campos existentes ...
    vacunas = models.TextField(default='', help_text='Vacunas aplicadas')

# 2. Crear migración
python manage.py makemigrations

# 3. Aplicar migración
python manage.py migrate

# 4. Actualizar formulario (forms.py)
class PetsForm(forms.ModelForm):
    class Meta:
        model = Pets
        fields = [..., 'vacunas']

# 5. Actualizar template
```

### 2. Agregar filtro avanzado

```python
# En views.py
def pet_list(request):
    pets = Pets.objects.filter(is_available=True)
    
    # Filtro por edad
    min_age = request.GET.get('min_age')
    if min_age:
        # Lógica para filtrar por edad
        pass
    
    # Filtro por género
    gender = request.GET.get('gender')
    if gender:
        pets = pets.filter(gender=gender)
    
    return render(request, 'movies/pet_list.html', {'pets': pets})
```

### 3. Agregar búsqueda por localización

```python
# 1. Agregar campo a modelo
class Pets(models.Model):
    # ... campos existentes ...
    location = models.CharField(max_length=100, default='Quilpué')

# 2. Crear migración y aplicarla
python manage.py makemigrations
python manage.py migrate

# 3. En views.py
def pet_list(request):
    pets = Pets.objects.filter(is_available=True)
    location = request.GET.get('location')
    
    if location:
        pets = pets.filter(location__icontains=location)
    
    return render(request, 'movies/pet_list.html', {'pets': pets})
```

---

## 🧪 Testing

```python
# En movies/tests.py

from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Pets, Breeds
from datetime import date

class PetsViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.breed = Breeds.objects.create(
            name='Labrador',
            description='Test'
        )

    def test_pet_list_page(self):
        """Probar que la página de mascotas carga"""
        response = self.client.get('/mascotas/')
        self.assertEqual(response.status_code, 200)

    def test_login_required(self):
        """Probar que crear mascota requiere login"""
        response = self.client.get('/mascota/crear/')
        self.assertEqual(response.status_code, 302)  # Redirect

    def test_create_pet(self):
        """Probar creación de mascota"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post('/mascota/crear/', {
            'breed': self.breed.id,
            'name': 'Max',
            'gender': 'M',
            'birth_date': '2020-01-01',
            'description': 'Test pet',
            'is_available': True
        })
        self.assertEqual(Pets.objects.count(), 1)

# Ejecutar tests
# python manage.py test movies
```

---

## 📝 Notas Importantes

- **Seguridad**: Siempre verificar que el usuario sea el dueño antes de editar/eliminar
- **Rendimiento**: Usar `select_related()` para evitar N+1 queries
- **Validación**: Validar en formularios Y en modelos
- **Testing**: Escribir tests para nuevas funcionalidades
- **Documentación**: Mantener docstrings en funciones y clases

---

## 🔗 Recursos Útiles

- [Documentación Django 1.11](https://docs.djangoproject.com/en/1.11/)
- [Django Models](https://docs.djangoproject.com/en/1.11/topics/db/models/)
- [Django Views](https://docs.djangoproject.com/en/1.11/topics/http/views/)
- [Django Forms](https://docs.djangoproject.com/en/1.11/topics/forms/)
- [Bootstrap 4](https://getbootstrap.com/docs/4.6/)

---

**Última actualización**: 2026  
**Versión**: 1.0
