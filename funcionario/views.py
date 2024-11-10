from rest_framework import generics
from .models import funcionario
from .serializers import funcionarioSerializer

class FUNCIONARIOCreateView(generics.CreateAPIView):
    queryset = funcionario.objects.all()
    serializer_class = funcionarioSerializer

class FUNCIONARIOListView(generics.ListAPIView):
    queryset = funcionario.objects.all()
    serializer_class = funcionarioSerializer

class FUNCIONARIODetailView(generics.RetrieveAPIView):
    queryset = funcionario.objects.all()
    serializer_class = funcionarioSerializer

class FUNCIONARIOUpdateView(generics.UpdateAPIView):
    queryset = funcionario.objects.all()
    serializer_class = funcionarioSerializer

class FUNCIONARIODeleteView(generics.DestroyAPIView):
    queryset = funcionario.objects.all()
    serializer_class = funcionarioSerializer
