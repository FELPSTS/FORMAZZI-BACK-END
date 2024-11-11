from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView
from .models import Administrador
from bson import ObjectId
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

class ADMDetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Administrador.objects.all()
    serializer_class = ADMSerializer

    def get_object(self):
        # Pega o token da URL
        token = self.kwargs.get('token')  # Pega o token diretamente da URL
        
        if not token:
            raise NotFound("Token de autenticação não fornecido.")
        
        # Buscar o Administrador usando o token
        try:
            administrador = Administrador.objects.get(token=token)
            return administrador
        except Administrador.DoesNotExist:
            raise NotFound("Administrador não encontrado para o token fornecido.")

class ADMUpdateView(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Administrador.objects.all()
    serializer_class = ADMSerializer
    lookup_field = 'token'

    def get_object(self):
        token = self.kwargs.get('token')
        if not token:
            raise NotFound("Token de autenticação não fornecido.")
        
        try:
            administrador = Administrador.objects.get(token=token)
            return administrador
        except Administrador.DoesNotExist:
            raise NotFound("Administrador não encontrado para o token fornecido.")
    
    def update(self, request, *args, **kwargs):
        administrador = self.get_object()

        # Criando uma cópia mutável de request.data
        data = request.data.copy()

        # Impede a alteração do email, mantendo o valor atual
        if 'email' in data:
            data['email'] = administrador.email

        # Valida e atualiza os dados
        serializer = self.get_serializer(administrador, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View para excluir um Administrador
class ADMDeleteView(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = ADMSerializer
    lookup_field = 'token'  # Usando o token para a consulta

    def get_object(self):
        token = self.kwargs.get('token')
        if not token:
            raise NotFound("Token de autenticação não fornecido.")
        
        try:
            administrador = Administrador.objects.get(token=token)
            return administrador
        except Administrador.DoesNotExist:
            raise NotFound("Administrador não encontrado para o token fornecido.")

    def delete(self, request, *args, **kwargs):
        # Obtém o administrador que será excluído
        administrador = self.get_object()

        # Serializa os dados do administrador para retornar na resposta
        serializer = self.get_serializer(administrador)
        data = serializer.data

        # Executa a exclusão do administrador
        administrador.delete()

        # Retorna os dados do administrador excluído
        return Response({
            "message": "Administrador excluído com sucesso.",
            "deleted_data": data
        }, status=status.HTTP_200_OK)
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
