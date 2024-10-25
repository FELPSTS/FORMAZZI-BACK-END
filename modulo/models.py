from django.db import models

class Modulo(models.Model):
    nome = models.CharField(max_length=255)
    curso_pertencente = models.CharField(max_length=255)
    id_curso_pertencente = models.CharField(max_length=255)
    midia = models.BinaryField()

    def __str__(self):
        return self.nome
