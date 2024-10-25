from rest_framework import generics
from .models import Modulo
from .serializers import ModuloSerializer

class ModuloCreateView(generics.CreateAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer

class ModuloListView(generics.ListAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer

class ModuloDetailView(generics.RetrieveAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer

class ModuloUpdateView(generics.UpdateAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer

class ModuloDeleteView(generics.DestroyAPIView):
    queryset = Modulo.objects.all()
    serializer_class = ModuloSerializer
