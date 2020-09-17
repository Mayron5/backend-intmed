from django.http import Http404
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import MedicoSerializer, EspecialidadeSerializer
from .models import Medico, Especialidade



class ListarMedicos(generics.ListAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'especialidade__especialidade']


class DetalhesMedico(APIView):
    def get_object(self, pk):
        try:
            return Medico.objects.get(pk=pk)
        except Medico.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        medico = self.get_object(pk)
        serializer = MedicoSerializer(medico)
        return Response(serializer.data)


class ListarEspecialidades(generics.ListAPIView):
    queryset = Especialidade.objects.all()
    filter_backends = [SearchFilter]
    serializer_class = EspecialidadeSerializer
    search_fields = ['especialidade']


class DetalhesEspecialidade(APIView):
    def get_object(self, pk):
        try:
            return Especialidade.objects.get(pk=pk)
        except Especialidade.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        especialidade = self.get_object(pk)
        serializer = EspecialidadeSerializer(especialidade)
        return Response(serializer.data)
