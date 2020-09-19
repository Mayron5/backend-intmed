from rest_framework import serializers

from medicos.serializers import MedicoSerializer
from consultas.models import Consulta

class ConsultaSerializer(serializers.ModelSerializer):
    medico = MedicoSerializer(many=False, read_only=True)
    class Meta:
        model = Consulta
        fields = ('id', 'dia', 'horario', 'data_agendamento', 'medico')
        extra_kwargs = {'cliente': {'write_only': True},
                        'agenda': {'write_only': True}}
