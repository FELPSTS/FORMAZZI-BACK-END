from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import PROVA
from rest_framework import generics
from .serializers import PROVASerializer
from rest_framework.permissions import AllowAny  # Permissão para qualquer usuário

class PROVACreateView(generics.CreateAPIView):
    queryset = PROVA.objects.all()
    serializer_class = PROVASerializer
    permission_classes = [AllowAny]

class PROVAListView(generics.ListAPIView):
    queryset = PROVA.objects.all()
    serializer_class = PROVASerializer
    permission_classes = [AllowAny]

class PROVADetailView(generics.detailAPIview):
    queryset = PROVA.objects.all()
    serializer_class = PROVASerializer
    permission_classes = [AllowAny]

class PROVAUpdateView(generics.deleteAPIview):
    queryset = PROVA.objects.all()
    serializer_class = PROVASerializer
    permission_classes = [AllowAny]

class PROVADeleteView(generics.deleteAPIview):
    queryset = PROVA.objects.all()
    serializer_class = PROVASerializer
    permission_classes = [AllowAny]
