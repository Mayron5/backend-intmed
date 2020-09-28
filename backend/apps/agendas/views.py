from datetime import date
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins

from backend.apps.agendas.models import Agenda
from backend.apps.agendas.serializers import AgendaSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_agendas(request):
    if request.method == 'GET':
        lista_de_agenda = []
        agendas = Agenda.objects.all().order_by('-dia')
        for agenda in agendas:
            if agenda.dia >= date.today():
                lista_de_agenda.append(agenda)
        serializer = AgendaSerializer(lista_de_agenda, many=True)
        return Response(serializer.data)
