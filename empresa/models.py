from django.db import models

class EMPRESA(models.Model):
    id = models.AutoField(primary_key=True)
    CNPJ = models.CharField(unique=True, max_length=255)
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.CNPJ
