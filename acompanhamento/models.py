from django.db import models

class Acompanhamento(models.Model):
    id = models.CharField(max_length=255, primary_key=True)  # Identificador único
    username = models.CharField(max_length=255, unique=True)
    funcionario_id = models.CharField(max_length=255, unique=True)  # ID do funcionário relacionado
    curso_id = models.CharField(max_length=255, unique=True)        # ID do curso relacionado
    tempo_no_sistema = models.IntegerField()          # Tempo total no sistema (em minutos, por exemplo)
    progresso = models.IntegerField()                 # Progresso do curso (em porcentagem, 0 a 100)
    tempo_falta = models.IntegerField()               # Tempo que falta para completar o curso (em minutos)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']  # Ordem padrão por username

