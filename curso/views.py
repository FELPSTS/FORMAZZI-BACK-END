from rest_framework import generics
from .models import Curso
from bson import ObjectId
from .serializers import cursoSerializer
from rest_framework.permissions import AllowAny 
from django.shortcuts import render
from django.http import JsonResponse
from mongoengine import Document, fields
from django.shortcuts import get_object_or_404

class cursoCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Curso.objects.all()
    serializer_class = cursoSerializer

class cursoListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Curso.objects.all()
    serializer_class = cursoSerializer

class cursoDetailView(generics.RetrieveAPIView):
    queryset = Curso.objects.all()
    serializer_class = cursoSerializer
    lookup_field = '_id'  # Usando '_id' como campo de lookup

    def get_object(self):
        # Pegando o valor de '_id' da URL e convertendo para ObjectId
        _id = self.kwargs['_id']
        try:
            return get_object_or_404(Curso, _id=ObjectId(_id))  # Usando ObjectId para consulta
        except Exception as e:
            raise Http404("Curso não encontrado")
    permission_classes = [AllowAny]
    queryset = Curso.objects.all()
    serializer_class = cursoSerializer
    lookup_field = '_id' 
    
def search_courses(request):
    nome = request.GET.get('nome', '')  # Obtém o parâmetro 'nome' da query string
    
    if nome:
        cursos = Curso.objects.filter(nome__icontains=nome)  # Filtra os cursos pelo nome
        serializer = cursoSerializer(cursos, many=True)  # Serializa os cursos encontrados
        return JsonResponse({'cursos': serializer.data})  # Retorna os cursos como resposta JSON
    
    return JsonResponse({'message': 'Nome do curso não fornecido'}, status=400)
#http://127.0.0.1:8000/curso/search-courses/?nome=(aqui o nome do curso a ser procurado)
class cursoUpdateView(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Curso.objects.all()
    serializer_class = cursoSerializer
    lookup_field = '_id'  # Usando '_id' como campo de lookup
    
    def get_object(self):
        # Obtém o curso com base no _id
        _id = self.kwargs['_id']
        try:
            return get_object_or_404(Curso, _id=ObjectId(_id))  # Procurando pelo campo _id
        except Exception:
            raise Http404("Curso não encontrado")  # Levanta erro 404 caso não encontre

# View para deletar o curso
class cursoDeleteView(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Curso.objects.all()
    serializer_class = cursoSerializer
    lookup_field = '_id'  # Usando '_id' como campo de lookup
    
    def get_object(self):
        # Obtém o curso com base no _id
        _id = self.kwargs['_id']
        try:
            return get_object_or_404(Curso, _id=ObjectId(_id))  # Procurando pelo campo _id
        except Exception:
            raise Http404("Curso não encontrado")  # Levanta erro 404 caso não encontre