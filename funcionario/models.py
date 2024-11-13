from djongo import models  # Import Djongo models para integração com MongoDB
from django.contrib.auth.hashers import make_password, check_password

class Funcionario(models.Model):
    _id = models.ObjectIdField()  # Para MongoDB, o campo _id será gerado automaticamente pelo Djongo
    nome = models.CharField(max_length=255)
    empresa_pertence = models.CharField(max_length=255)
    id_empresa_pertence = models.CharField(max_length=255)
    ADM_Responsavel = models.CharField(max_length=255)
    id_ADM_Responsavel = models.CharField(max_length=255)
    token = models.CharField(max_length=100, blank=True, null=True)  # Gerado no momento de login
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'funcionario_funcionario'

    def save(self, *args, **kwargs):
        # Aqui você pode adicionar a lógica de hash da senha, se necessário
        if not self.password.startswith('pbkdf2_'):  # Evita hashear novamente se já estiver com hash
            self.password = make_password(self.password)
        super().save(*args, **kwargs)  # Salva o objeto no MongoDB
