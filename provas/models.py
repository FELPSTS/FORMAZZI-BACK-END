from djongo import models  # Se estiver utilizando djongo para integração com MongoDB
from django.contrib.auth.hashers import make_password

class PROVA(models.Model):

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Chama o método save() da classe pai para salvar o objeto
