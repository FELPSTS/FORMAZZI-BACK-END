from djongo import models  # Se estiver utilizando djongo para integração com MongoDB
from django.contrib.auth.hashers import make_password

class PROVA(models.Model):
    nome = models.CharField(max_length=255)
    ID_Curso_pertencente = models.CharField(max_length=255)
    ID_funcionario = models.CharField(max_length=255)
    pertencente = FileField(upload_to='provas/')
    arquivo_prova = models.FileField(upload_to='provas/')
    progress = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    def __str__(self):
        return self.nome

    def clean(self):
        super().clean()  # Certifique-se de chamar o método `clean` da classe base
        if not (0 <= self.progress <= 100):
            raise ValidationError('O progresso deve estar entre 0 e 100.')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Chama o método save() da classe pai para salvar o objeto
