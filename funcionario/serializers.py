from rest_framework import serializers
from .models import funcionario

from rest_framework import serializers
from .models import funcionario

class funcionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = funcionario
        fields = ['id', 'nome', 'empresa_pertence', 'id_empresa_pertence', 'ADM_Responsavel', 'id_ADM_Responsavel', 'username', 'email', 'password']
    def create(self, validated_data):
        return funcionario.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance