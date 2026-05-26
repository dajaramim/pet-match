from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Breeds, Pets


class BreedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breeds
        fields = ['id', 'name', 'description', 'characteristics']


class PetsSerializer(serializers.ModelSerializer):
    breed_name = serializers.CharField(source='breed.name', read_only=True)
    owner_username = serializers.CharField(source='owner.username', read_only=True)
    age = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Pets
        fields = [
            'id', 'name', 'breed', 'breed_name', 'owner', 'owner_username',
            'gender', 'birth_date', 'age', 'description', 'image', 'image_url',
            'is_available', 'created_at',
        ]
        read_only_fields = ['owner']

    def get_age(self, obj):
        return obj.age()

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
