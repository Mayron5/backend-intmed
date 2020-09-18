from django.db import models
from medicos.models import Medico

# Create your models here.
class Agenda(models.Model):
    medico = models.ForeignKey(Medico, models.CASCADE)
    dia = models.DateField()

class Horario(models.Model):
    agenda = models.ForeignKey(Agenda, models.CASCADE)
    horario = models.TimeField()
