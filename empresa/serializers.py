from rest_framework import serializers
from .models import EMPRESA

class EMPRESAserializer(serializers.ModelSerializer):
    class Meta:
        model = EMPRESA
        fields = ['id', 'CNPJ', 'nome', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # Senha deve ser somente para escrita
        }
