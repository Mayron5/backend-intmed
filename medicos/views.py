from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import MedicoSerializer, EspecialidadeSerializer
from .models import Medico, Especialidade



class ListarMedicos(APIView):
    def get(self, request):
        medicos = Medico.objects.all()
        serializer = MedicoSerializer(medicos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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


class ListarEspecialidades(APIView):
    def get(self, request):
        especialidades = Especialidade.objects.all()
        serializer = EspecialidadeSerializer(especialidades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
