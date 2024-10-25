from django.contrib import admin
from .models import Modulo

@admin.register(Modulo)
class ModuloAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'curso_pertencente', 'id_curso_pertencente']
