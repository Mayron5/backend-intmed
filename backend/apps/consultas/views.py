import datetime
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from rest_framework import status

from backend.apps.agendas.models import Agenda, Horario
from backend.apps.consultas.models import Consulta
from backend.apps.clientes.models import Cliente
from backend.apps.consultas.serializers import ConsultaSerializer


@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalhes_deletar_consulta(request, pk):
    try:
        consultas = Consulta.objects.filter(cliente=request.user)
        consulta = consultas.get(pk=pk)
    except Consulta.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if consulta.cliente == request.user and consulta.dia >= datetime.date.today():
            serializer = ConsultaSerializer(consulta)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Usuario nao autorizado"}, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        if consulta.dia >= datetime.date.today():
            consulta.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def listar_marcar_consultas(request):
    if request.method == 'GET':

        lista_de_consultas = []
        consultas = Consulta.objects.filter(
            cliente=request.user).order_by('-dia')
        for consulta in consultas:
            if consulta.dia >= datetime.date.today():
                lista_de_consultas.append(consulta)
        serializer = ConsultaSerializer(lista_de_consultas, many=True)
        return Response(serializer.data)

    if request.method == 'POST':

        serializer = ConsultaSerializer(data=request.data)
        try:
            if serializer.is_valid():
                validated_data = serializer.validated_data
                agenda = Agenda.objects.get(pk=request.data['agenda_id'])
                horario = Horario.objects.filter(agenda=agenda) \
                    .get(horario=validated_data['horario'])

                if (not horario.disponivel
                        and validated_data['horario'] != str(horario.horario)):

                    return Response({"message": "Horario nao disponivel"},
                                    status=status.HTTP_400_BAD_REQUEST)

                if (agenda.dia >= datetime.date.today()
                    and datetime.datetime.now().strftime("%H:%M:%S")
                        >= str(validated_data['horario'])):

                    consulta = Consulta(
                        dia=agenda.dia,
                        horario=validated_data['horario'],
                        agenda=agenda,
                        cliente=request.user,
                        medico=agenda.medico
                    )
                    horario.disponivel = False
                    horario.save()
                    consulta.save()
                    serializer = ConsultaSerializer(consulta)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response({"message": "Datas passadas nao sao validas"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message": "Erro ao agendar consulta"}, status=status.HTTP_400_BAD_REQUEST)
