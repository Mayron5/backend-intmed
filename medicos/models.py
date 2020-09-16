from django.db import models

# Create your models here.
class Especialidade(models.Model):
    especialidade = models.CharField(max_length=150)

    def __str__(self):
        return self.especialidade

class Medico(models.Model):
    crm = models.IntegerField()
    nome = models.CharField(max_length=150)
    especialidade = models.ForeignKey(Especialidade, models.CASCADE)
    def __str__(self):
        return self.nome
