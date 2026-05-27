#!/usr/bin/env bash
# Script de build para Render
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Crear datos iniciales si no existen
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@petmatch.com', 'admin123')
    print('Superusuario creado')
"
