from rest_framework import serializers

from backend.apps.agendas.models import Agenda, Horario


class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ('horario', )
        depth = 1


class AgendaSerializer(serializers.ModelSerializer):
    horarios = serializers.StringRelatedField(many=True)

    class Meta:
        model = Agenda
        fields = ('id', 'medico', 'dia', 'horarios')

        depth = 2
