from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from adm.views import SomeView  # Importe a view SomeView

def home(request):
    return HttpResponse("BACK-END SE RODOU DEU CERTO!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Página de boas-vindas na raiz
    path('adms/', include('adm.urls')),
    path('empresa/', include('empresa.urls')),
    path('modulo/', include('modulo.urls')),
    path('curso/', include('curso.urls')),
    path('certificado/', include('certificado.urls')),
    path('funcionario/', include('funcionario.urls')),
    path('acompanhamento/', include('acompanhamento.urls')),
    path('someview/', SomeView.as_view(), name='someview')  # Corrigido aqui
]
