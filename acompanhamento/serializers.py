from rest_framework import serializers
from .models import Acompanhamento

class AcompanhamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acompanhamento
        fields = ['id', 'username', 'funcionario_id', 'curso_id', 'tempo_no_sistema', 'progresso', 'tempo_falta']

    def validate_progresso(self, value):
        """
        Valida o valor do progresso para garantir que esteja dentro do intervalo permitido.
        """
        if not (0 <= value <= 100):
            raise serializers.ValidationError("O progresso deve estar entre 0 e 100.")
        return value

    # Adicionalmente, se você precisar de validação personalizada ou lógica, adicione métodos aqui.
