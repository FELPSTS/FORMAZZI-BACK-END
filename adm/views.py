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
import uuid


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
        # Recebe os dados de login
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Verifica se os campos de username e senha foram preenchidos
        if not username or not password:
            return Response({"error": "Username e senha são obrigatórios"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Busca o administrador pelo username
            administrador = Administrador.objects.get(username=username)
            
            # Verifica se a senha está correta
            if password == administrador.password:
                # Cria um token exclusivo manualmente
                token = str(uuid.uuid4())  # Gera um UUID como token único
                administrador.token = token  # Armazena o token no modelo Administrador (ou outra estrutura)
                administrador.save()
                
                # Retorna o token como resposta ao login bem-sucedido
                return Response({"message": "Login bem-sucedido", "token": token}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
        
        except Administrador.DoesNotExist:
            return Response({"error": "Administrador não encontrado"}, status=status.HTTP_404_NOT_FOUND)

#{
  #  "username": "ADM",
 #   "password": "ADM123"
#}modelo de json
