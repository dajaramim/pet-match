from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Pets, Breeds
from .serializers import PetsSerializer, BreedsSerializer, UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def api_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user': UserSerializer(user).data,
        })
    return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([AllowAny])
def api_register(request):
    username = request.data.get('username')
    email = request.data.get('email', '')
    password = request.data.get('password')
    password_confirm = request.data.get('password_confirm')

    if not username or not password:
        return Response({'error': 'Usuario y contraseña son requeridos'}, status=status.HTTP_400_BAD_REQUEST)
    if password != password_confirm:
        return Response({'error': 'Las contraseñas no coinciden'}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(username=username).exists():
        return Response({'error': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, email=email, password=password)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({
        'token': token.key,
        'user': UserSerializer(user).data,
    }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([AllowAny])
def api_pet_list(request):
    pets = Pets.objects.select_related('owner', 'breed').filter(is_available=True)
    breed_id = request.GET.get('breed')
    if breed_id:
        pets = pets.filter(breed_id=breed_id)
    search = request.GET.get('search')
    if search:
        pets = pets.filter(name__icontains=search)
    serializer = PetsSerializer(pets, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def api_pet_detail(request, pk):
    try:
        pet = Pets.objects.select_related('owner', 'breed').get(pk=pk)
    except Pets.DoesNotExist:
        return Response({'error': 'Mascota no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    serializer = PetsSerializer(pet, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_my_pets(request):
    pets = Pets.objects.filter(owner=request.user).select_related('breed')
    serializer = PetsSerializer(pets, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_pet_create(request):
    serializer = PetsSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def api_pet_edit(request, pk):
    try:
        pet = Pets.objects.get(pk=pk)
    except Pets.DoesNotExist:
        return Response({'error': 'Mascota no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    if pet.owner != request.user:
        return Response({'error': 'No tienes permiso'}, status=status.HTTP_403_FORBIDDEN)
    serializer = PetsSerializer(pet, data=request.data, partial=True, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_pet_delete(request, pk):
    try:
        pet = Pets.objects.get(pk=pk)
    except Pets.DoesNotExist:
        return Response({'error': 'Mascota no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    if pet.owner != request.user:
        return Response({'error': 'No tienes permiso'}, status=status.HTTP_403_FORBIDDEN)
    pet.delete()
    return Response({'message': 'Mascota eliminada'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([AllowAny])
def api_breeds(request):
    breeds = Breeds.objects.all()
    serializer = BreedsSerializer(breeds, many=True)
    return Response(serializer.data)
