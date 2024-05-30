from django.contrib.auth.models import User  # Importa el modelo User del módulo de autenticación de Django
from rest_framework import serializers       # Importa el módulo de serializadores de Django REST framework
from .models import Note                     # Importa el modelo Note del archivo models.py en el mismo directorio

# Serializador para el modelo User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User                       # Especifica que este serializador es para el modelo User
        fields = ["id", "username", "password"]  # Campos que serán incluidos en la representación serializada
        extra_kwargs = {"password": {"write_only": True}}  # Configura el campo 'password' como de solo escritura

    def create(self, validated_data):
        print(validated_data)  # Imprime los datos validados (para depuración, puede ser removido en producción)
        user = User.objects.create_user(**validated_data)  # Crea un nuevo usuario con los datos validados
        return user  # Retorna la instancia del usuario creado

# Serializador para el modelo Note
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note  # Especifica que este serializador es para el modelo Note
        fields = ["id", "title", "content", "created_at", "author"]  # Campos que serán incluidos en la representación serializada
        extra_kwargs = {"author": {"read_only": True}}  # Configura el campo 'author' como de solo lectura
