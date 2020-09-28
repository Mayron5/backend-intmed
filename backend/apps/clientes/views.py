from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status

from rest_framework.authtoken.models import Token

from backend.apps.clientes.serializers import ClienteSerializer
from backend.apps.clientes.models import Cliente

@api_view(['POST'])
def criar_cliente(request):
    serializer = ClienteSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        cliente = serializer.save()
        # Cliente.objects.create_user(
        #     validated_data['username'],
        #     validated_data['email'],
        #     validated_data['password']
        # )
        data['response'] = 'Cliente registrado com sucesso.'
        data['email'] = cliente.email
        data['username'] = cliente.username
        token = Token.objects.get(user=cliente).key
        data['token'] = token
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
