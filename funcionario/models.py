
from django.db import models

class funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    empresa_Pertence = models.CharField(max_length=255)
    id_empresa_pertence = models.CharField(max_length=255)
    ADM_Responsavel = models.CharField(max_length=255)
    id_ADM_Responsavel = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
