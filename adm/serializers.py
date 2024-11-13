from rest_framework import serializers
from .models import Administrador

class ADMSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)  # Somente leitura

    class Meta:
        model = Administrador
        fields = ['_id', 'nome', 'empresa_pertencente', 'id_empresa_pertencente', 'username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        administrador = Administrador(**validated_data)
        administrador.password = password  # Senha em texto simples
        administrador.save()
        return administrador

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if password:
            instance.password = password  # Senha em texto simples
        
        instance.save()
        return instance
