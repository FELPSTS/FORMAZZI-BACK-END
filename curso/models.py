from django.db import models
from django.core.exceptions import ValidationError

class curso(models.Model):
    nome = models.CharField(max_length=255, unique=True)  # Adicionei o valor para max_length
    empresa_pertencente = models.CharField(max_length=255)
    id_empresa_pertencente = models.CharField(max_length=255)
    midia_intoduction = models.FileField(upload_to='midias/')  # Caminho para o diretório de uploads
    id_ref_MIDIA = models.CharField(max_length=255)
    progress = models.IntegerField()

    def __str__(self):
        return self.nome

    def clean(self):
        super().clean()  # Certifique-se de chamar o método `clean` da classe base
        if not (0 <= self.progress <= 100):
            raise ValidationError('O progresso deve estar entre 0 e 100.')

