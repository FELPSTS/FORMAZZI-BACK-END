from rest_framework import serializers
from .models import Funcionario

class funcionarioSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)  # Somente leitura

    class Meta:
        model = Funcionario
        fields = ['_id', 'nome', 'empresa_pertence', 'id_empresa_pertence', 'ADM_Responsavel', 'id_ADM_Responsavel', 'username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        administrador = Funcionario(**validated_data)
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
