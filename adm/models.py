
from django.db import models

class Administrador(models.Model):
    nome = models.CharField(max_length=255)
    empresa_pertencente = models.CharField(max_length=255)
    id_empresa_pertencente = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
