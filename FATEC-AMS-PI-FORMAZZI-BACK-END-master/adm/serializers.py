from rest_framework import serializers
from .models import Administrador

class ADMSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)  # O campo 'id' é somente leitura, pois é gerado pelo MongoDB
    nome = serializers.CharField(max_length=255)
    empresa_pertencente = serializers.CharField(max_length=255)
    id_empresa_pertencente = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255, write_only=True)  # Senha é somente para escrita

    def create(self, validated_data):
        # Cria uma nova instância do modelo ADM com os dados validados e salva no MongoDB
        return Administrador.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Atualiza os campos da instância existente com os dados validados e salva no MongoDB
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
