from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from django.http import Http404

from backend.permissions import IsOwner
from .serializers import MedicoSerializer, EspecialidadeSerializer
from .models import Medico, Especialidade



class ListarMedicos(generics.ListAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'especialidade__especialidade']
    permission_classes = [IsAuthenticated]


class DetalhesMedico(APIView):
    def get_object(self, pk):
        try:
            return Medico.objects.get(pk=pk)
        except Medico.DoesNotExist:
            raise Http404

    @permission_classes([IsAuthenticated])
    def get(self, request, pk):
        medico = self.get_object(pk)
        serializer = MedicoSerializer(medico)
        return Response(serializer.data)


class ListarEspecialidades(generics.ListAPIView):
    queryset = Especialidade.objects.all()
    filter_backends = [SearchFilter]
    serializer_class = EspecialidadeSerializer
    search_fields = ['especialidade']
    permission_classes = [IsAuthenticated]


class DetalhesEspecialidade(APIView):
    def get_object(self, pk):
        try:
            return Especialidade.objects.get(pk=pk)
        except Especialidade.DoesNotExist:
            raise Http404

    @permission_classes([IsAuthenticated])
    def get(self, request, pk):
        especialidade = self.get_object(pk)
        serializer = EspecialidadeSerializer(especialidade)
        return Response(serializer.data)
