from datetime import time
from django.db import models
from backend.apps.medicos.models import Medico

# Create your models here.
class Agenda(models.Model):
    medico = models.OneToOneField(Medico, models.CASCADE, primary_key=True)
    dia = models.DateField()
    def __str__(self):
        return 'Agenda do Dr. ' + self.medico.nome

class Horario(models.Model):
    HORARIO_CHOICES = (
        (time(8, 00, 00), '08:00'),
        (time(8, 30, 00), '08:30'),
        (time(9, 00, 00), '09:00'),
        (time(9, 30, 00), '09:30'),
        (time(10, 00, 00), '10:00'),
        (time(10, 30, 00), '10:30'),
        (time(11, 00, 00), '11:00'),
        (time(11, 30, 00), '11:30'),
        (time(12, 00, 00), '12:00'),
        (time(12, 30, 00), '12:30'),
        (time(13, 00, 00), '13:00'),
        (time(13, 30, 00), '13:30'),
        (time(14, 00, 00), '14:00'),
        (time(14, 30, 00), '14:30'),
        (time(15, 00, 00), '15:00'),
        (time(15, 30, 00), '15:30'),
        (time(16, 00, 00), '16:00'),
        (time(16, 30, 00), '16:30'),
        (time(17, 00, 00), '17:00'),
    )

    agenda = models.ForeignKey(Agenda, models.CASCADE)
    horario = models.TimeField(choices=HORARIO_CHOICES)
