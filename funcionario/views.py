from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView
from .models import Funcionario
from rest_framework import generics
from .serializers import funcionarioSerializer
import uuid

# View para criar um novo Funcionario
class FUNCIONARIOCreateView(generics.CreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = funcionarioSerializer
    permission_classes = [AllowAny]

# View para listar todos os Funcionarios
class FUNCIONARIOListView(generics.ListAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = funcionarioSerializer
    permission_classes = [AllowAny]

class FUNCIONARIODetailView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Funcionario.objects.all()
    serializer_class = funcionarioSerializer

    def get_object(self):
        # Pega o token da URL
        token = self.kwargs.get('token')
        
        if not token:
            raise NotFound("Token de autenticação não fornecido.")
        
        # Buscar o Funcionario usando o token
        try:
            funcionario_obj = Funcionario.objects.get(token=token)
            return funcionario_obj
        except Funcionario.DoesNotExist:
            raise NotFound("Funcionário não encontrado para o token fornecido.")

class FUNCIONARIOUpdateView(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Funcionario.objects.all()
    serializer_class = funcionarioSerializer
    lookup_field = 'token'

    def get_object(self):
        token = self.kwargs.get('token')
        if not token:
            raise NotFound("Token de autenticação não fornecido.")
        
        try:
            funcionario_obj = Funcionario.objects.get(token=token)
            return funcionario_obj
        except Funcionario.DoesNotExist:
            raise NotFound("Funcionário não encontrado para o token fornecido.")

class FUNCIONARIODeleteView(generics.DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = funcionarioSerializer
    lookup_field = 'token'

    def get_object(self):
        token = self.kwargs.get('token')
        if not token:
            raise NotFound("Token de autenticação não fornecido.")
        
        try:
            funcionario_obj = Funcionario.objects.get(token=token)
            return funcionario_obj
        except Funcionario.DoesNotExist:
            raise NotFound("Funcionário não encontrado para o token fornecido.")

    def delete(self, request, *args, **kwargs):
        funcionario_obj = self.get_object()
        serializer = self.get_serializer(funcionario_obj)
        data = serializer.data
        funcionario_obj.delete()
        return Response({
            "message": "Funcionário excluído com sucesso.",
            "deleted_data": data
        }, status=status.HTTP_200_OK)

class FUNCIONARIOLoginView(APIView):
    permission_classes = [AllowAny]  # Permite acesso a qualquer usuário
    
    def post(self, request):
        # Recebe os dados de login
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Verifica se os campos de username e senha foram preenchidos
        if not username or not password:
            return Response({"error": "Username e senha são obrigatórios"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Busca o funcionario pelo username
            funcionario_obj = Funcionario.objects.get(username=username)
            
            # Verifica se a senha está correta
            if check_password(password, funcionario_obj.password):
                # Cria um token exclusivo manualmente
                token = str(uuid.uuid4())  # Gera um UUID como token único
                funcionario_obj.token = token  # Armazena o token no modelo Funcionario (ou outra estrutura)
                funcionario_obj.save()
                
                # Retorna o token como resposta ao login bem-sucedido
                return Response({"message": "Login bem-sucedido", "token": token}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
        
        except Funcionario.DoesNotExist:
            return Response({"error": "Funcionario não encontrado"}, status=status.HTTP_404_NOT_FOUND)
