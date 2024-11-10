from django.contrib import admin
from .models import ADM

@admin.register(ADM)
class ADMAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'empresa_pertencente', 'id_empresa_pertencente', 'username', 'email')
