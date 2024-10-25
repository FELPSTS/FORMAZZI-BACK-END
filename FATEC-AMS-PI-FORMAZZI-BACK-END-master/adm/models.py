# V.1
# ATENHA-SE que essa é a models baseada em um banco de dados relaciona como SQL,
#mas nesse projeto utilizaremos um banco de dados NÃO RELACIONAL QUE SERÁ O MONGODB 
#SUA CONEXÃO JÁ ESTÁ CONFIGURADA NA SETTINGS PORÉM POR HORA ESTÁ COMMITADA E DEIXAREI COMENTARIOS PARA A IMPLEMENTAÇÃO DESTA

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
