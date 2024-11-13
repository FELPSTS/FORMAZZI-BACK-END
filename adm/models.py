from djongo import models  # Se estiver utilizando djongo para integração com MongoDB
from django.contrib.auth.hashers import make_password

class Administrador(models.Model):
    _id = models.ObjectIdField()  # Usando ObjectIdField para o MongoDB, o campo _id será gerado automaticamente
    nome = models.CharField(max_length=255)
    empresa_pertencente = models.CharField(max_length=255)
    id_empresa_pertencente = models.CharField(max_length=255)
    token = models.CharField(max_length=100, blank=True, null=True)#cria no momento de login
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'adm_administrador'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Chama o método save() da classe pai para salvar o objeto
