from rest_framework import serializers
from .models import Curso

class cursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['_id', 'nome', 'empresa_pertencente', 'id_empresa_pertencente', 'id_ref_MIDIA', 'midia_intoduction', 'progress']
        read_only_fields = ['_id']  # Campo '_id' como somente leitura, será gerado automaticamente pelo banco de dados

    def validate_progress(self, value):
        """
        Valida o valor do progresso para garantir que esteja dentro do intervalo permitido.
        """
        if not (0 <= value <= 100):
            raise serializers.ValidationError("O progresso deve estar entre 0 e 100.")
        return value
