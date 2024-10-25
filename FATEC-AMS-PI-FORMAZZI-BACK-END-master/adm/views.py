from rest_framework import generics
from .models import Administrador
from .serializers import ADMSerializer

class ADMCreateView(generics.CreateAPIView):
    queryset = Administrador.objects.all()
    serializer_class = ADMSerializer

class ADMListView(generics.ListAPIView):
    queryset = Administrador.objects.all()
    serializer_class = ADMSerializer

class ADMDetailView(generics.RetrieveAPIView):
    queryset = Administrador.objects.all()
    serializer_class = ADMSerializer

class ADMUpdateView(generics.UpdateAPIView):
    queryset = Administrador.objects.all()
    serializer_class = ADMSerializer

class ADMDeleteView(generics.DestroyAPIView):
    queryset = Administrador.objects.all()
    serializer_class = ADMSerializer
