from django.urls import path
from . import api_views

urlpatterns = [
    path('login/', api_views.api_login, name='api_login'),
    path('register/', api_views.api_register, name='api_register'),
    path('pets/', api_views.api_pet_list, name='api_pet_list'),
    path('pets/<int:pk>/', api_views.api_pet_detail, name='api_pet_detail'),
    path('my-pets/', api_views.api_my_pets, name='api_my_pets'),
    path('pets/create/', api_views.api_pet_create, name='api_pet_create'),
    path('pets/<int:pk>/edit/', api_views.api_pet_edit, name='api_pet_edit'),
    path('pets/<int:pk>/delete/', api_views.api_pet_delete, name='api_pet_delete'),
    path('breeds/', api_views.api_breeds, name='api_breeds'),
]
