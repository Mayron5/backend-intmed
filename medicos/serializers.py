from rest_framework import serializers
from medicos.models import Medico, Especialidade

class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = '__all__'


class MedicoSerializer(serializers.ModelSerializer):
    especialidade = EspecialidadeSerializer(many=False, read_only=True)
    class Meta:
        model = Medico
        fields = ['id', 'nome', 'crm', 'especialidade']
