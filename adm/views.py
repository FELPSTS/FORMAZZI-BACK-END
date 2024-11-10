from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .models import Administrador
from rest_framework import generics
from .serializers import ADMSerializer
from rest_framework.permissions import AllowAny  # Permissão para qualquer usuário


# View para criar um novo Administrador
class ADMCreateView(generics.CreateAPIView):
    queryset = Administrador.objects.all()
    serializer_class = ADMSerializer
    permission_classes = [AllowAny]

# View para listar todos os Administradores
class ADMListView(generics.ListAPIView):
    queryset = Administrador.objects.all()
    serializer_class = ADMSerializer
    permission_classes = [AllowAny]

# View para detalhar um Administrador
class ADMDetailView(generics.RetrieveAPIView):
    queryset = Administrador.objects.all()
    serializer_class = ADMSerializer

# View para atualizar um Administrador existente
class ADMUpdateView(generics.UpdateAPIView):
    queryset = Administrador.objects.all()
    serializer_class = ADMSerializer
    lookup_field = '_id'  # Usando _id como chave para consulta

# View para excluir um Administrador
class ADMDeleteView(generics.DestroyAPIView):
    queryset = Administrador.objects.all()
    serializer_class = ADMSerializer
    lookup_field = '_id'  # Usando _id como chave para consulta

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# View protegida, acessível apenas para usuários autenticados
class SomeView(APIView):
    permission_classes = [IsAuthenticated]  # Apenas usuários autenticados podem acessar

    def get(self, request):
        return Response({"message": "Acesso permitido!"})   

class ADMLoginView(APIView):
    permission_classes = [AllowAny]  # Permite acesso a qualquer usuário
    
    def post(self, request):
        # Pegando os dados de entrada
        username = request.data.get('username')
        password = request.data.get('password')
        
        print(f"Username recebido: {username}")
        print(f"Password recebido: {password}")
        
        # Verificando se os dados foram enviados corretamente
        if not username or not password:
            return Response({"error": "Username e senha são obrigatórios"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Busca o administrador pelo username
            administrador = Administrador.objects.get(username=username)
            
            # Verifica se a senha inserida é igual à senha armazenada
            if password == administrador.password:
                # Sucesso no login, pode retornar um token ou mensagem de sucesso
                return Response({"message": "Login bem-sucedido"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
        
        except Administrador.DoesNotExist:
            return Response({"error": "Administrador não encontrado"}, status=status.HTTP_404_NOT_FOUND)