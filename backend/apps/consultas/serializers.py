from rest_framework import serializers

from backend.apps.medicos.serializers import MedicoSerializer
from backend.apps.consultas.models import Consulta


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ('id', 'dia', 'horario', 'data_agendamento', 'medico')
        extra_kwargs = {'cliente': {'write_only': True},
                        'agenda': {'write_only': True},
                        'dia': {'read_only': True}}
        depth = 2
