from django.db import models
from medicos.models import Medico
from clientes.models import Cliente

# Create your models here.
class Consulta(models.Model):
    dia = models.DateField()
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(auto_now_add=True)
    medico = models.ForeignKey(Medico, models.CASCADE)
    cliente = models.ForeignKey(Cliente, models.CASCADE)

    def __str__(self):
        return str('Medico - ' + self.medico.nome + ' | Paciente - ' + self.cliente.username)
