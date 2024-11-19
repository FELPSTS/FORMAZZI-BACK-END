from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Prova
from rest_framework import generics
from .serializers import PROVASerializer
from rest_framework.permissions import AllowAny  # Permissão para qualquer usuário

class PROVAreateView(generics.CreateAPIView):
    queryset = Administrador.objects.all()
    serializer_class = PROVASerializer
    permission_classes = [AllowAny]

class PROVAListView(generics.ListAPIView):
    queryset = Administrador.objects.all()
    serializer_class = PROVASerializer
    permission_classes = [AllowAny]

class PROVADetailView(generics.detailAPIview):
    queryset = Administrador.objects.all()
    serializer_class = PROVASerializer
    permission_classes = [AllowAny]

class PROVADetailView(generics.deleteAPIview):
    queryset = Administrador.objects.all()
    serializer_class = PROVASerializer
  permission_classes = [AllowAny]
