from rest_framework import serializers
from .models import certificado

class certificadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = certificado
        fields = ['id', 'username','nome','assinatura_Digital','id_curso_pertencente','empresa_pertencente', 'id_empresa_pertencente','adm_responsavel','id_funcionario']
        read_only_fields = ['id']  # Se você não deseja que o campo 'id' seja alterado

    def validate_progress(self, value):
        """
        Valida o valor do progresso para garantir que esteja dentro do intervalo permitido.
        """
        if not (0 <= value <= 100):
            raise serializers.ValidationError("O progresso deve estar entre 0 e 100.")
        return value

    # Adicionalmente, se você precisar de validação personalizada ou lógica, adicione métodos aqui.
