from rest_framework import generics
from .models import Acompanhamento
from .serializers import AcompanhamentoSerializer

class AcompanhamentoCreateView(generics.CreateAPIView):
    queryset = Acompanhamento.objects.all()
    serializer_class = AcompanhamentoSerializer

class AcompanhamentoListView(generics.ListAPIView):
    queryset = Acompanhamento.objects.all()
    serializer_class = AcompanhamentoSerializer

class AcompanhamentoDetailView(generics.RetrieveAPIView):
    queryset = Acompanhamento.objects.all()
    serializer_class = AcompanhamentoSerializer

class AcompanhamentoUpdateView(generics.UpdateAPIView):
    queryset = Acompanhamento.objects.all()
    serializer_class = AcompanhamentoSerializer

class AcompanhamentoDeleteView(generics.DestroyAPIView):
    queryset = Acompanhamento.objects.all()
    serializer_class = AcompanhamentoSerializer