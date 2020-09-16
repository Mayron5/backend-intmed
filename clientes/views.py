from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ClienteSerializer



class CriarCliente(APIView):
    def post(self, request):
        data = request.data
        serializer = ClienteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
