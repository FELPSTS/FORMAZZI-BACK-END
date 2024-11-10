from django.db import models
from django.core.exceptions import ValidationError

class certificado(models.Model):
    id = models.CharField(max_length=255, unique=True,primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    nome = models.CharField(max_length=255, unique=True)  # Nome do curso
    assinatura_Digital = models.CharField(max_length=255)  # Assinatura digital
    id_curso_pertencente = models.CharField(max_length=255)  # ID do curso pertencente
    empresa_pertencente = models.CharField(max_length=255)  # Nome da empresa pertencente
    id_empresa_pertencente = models.CharField(max_length=255)  # ID da empresa
    id_adm_responsavel = models.CharField(max_length=255)  # ID do administrador responsável
    adm_responsavel = models.CharField(max_length=255)  # Nome do administrador responsável
    id_funcionario = models.CharField(max_length=255)  # ID do funcionário
    data_emissao = models.DateField()  # Data de emissão do certificado
    status = models.CharField(max_length=50, choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')])  # Status do certificado

    def __str__(self):
        return f"Certificado de {self.nome_curso} - {self.adm_responsavel}"

    def clean(self):
        super().clean()  # Certifique-se de chamar o método `clean` da classe base
        # Adicione validações adicionais, se necessário
