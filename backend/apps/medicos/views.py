from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from rest_framework import generics
from rest_framework import status

from backend.apps.medicos.serializers import MedicoSerializer, EspecialidadeSerializer
from backend.apps.medicos.models import Medico, Especialidade


class ListarMedicos(generics.ListAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'especialidade__especialidade']
    permission_classes = [IsAuthenticated]


class ListarEspecialidades(generics.ListAPIView):
    queryset = Especialidade.objects.all()
    filter_backends = [SearchFilter]
    serializer_class = EspecialidadeSerializer
    search_fields = ['especialidade']
    permission_classes = [IsAuthenticated, ]


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detalhes_medico(request, pk):
    try:
        medico = Medico.objects.get(pk=pk)
    except Medico.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MedicoSerializer(medico)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detalhes_especialidade(request, pk):
    try:
        especialidade = Especialidade.objects.get(pk=pk)
    except Especialidade.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = EspecialidadeSerializer(especialidade)
    return Response(serializer.data, status=status.HTTP_200_OK)
