from datetime import date
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from rest_framework import generics
from rest_framework import status

from backend.apps.agendas.models import Agenda
from backend.apps.consultas.models import Consulta
from backend.apps.clientes.models import Cliente
from backend.apps.consultas.serializers import ConsultaSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_consultas(request):
    consultas = Consulta.objects.filter(cliente=request.user)
    serializer = ConsultaSerializer(consultas, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def marcar_consulta(request):
    serializer = ConsultaSerializer(data=request.data)
    if serializer.is_valid():
        validated_data = serializer.validated_data
        agenda = Agenda.objects.get(pk=validated_data['agenda'])
        if validated_data['dia'] >= date.today():
            Consulta.objects.create(
                dia = agenda.dia,
                horario = validated_data['horario'],
                agenda = validated_data['agenda'],
                cliente = request.user.id
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalhes_consulta(request, pk):
    try:
        consulta = Consulta.objects.get(pk=pk)
    except Consulta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        if consulta.cliente == request.user:
            serializer = ConsultaSerializer(consulta)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        consulta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
