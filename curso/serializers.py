from rest_framework import serializers
from .models import curso

class cursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = curso
        fields = ['id', 'nome', 'empresa_pertencente', 'id_empresa_pertencente','id_ref_MIDIA','midia_intoduction', 'progress']
        read_only_fields = ['id']  # Se você não deseja que o campo 'id' seja alterado

    def validate_progress(self, value):
        """
        Valida o valor do progresso para garantir que esteja dentro do intervalo permitido.
        """
        if not (0 <= value <= 100):
            raise serializers.ValidationError("O progresso deve estar entre 0 e 100.")
        return value

    # Adicionalmente, se você precisar de validação personalizada ou lógica, adicione métodos aqui.
