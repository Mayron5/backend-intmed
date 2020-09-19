from django.db import models

# Create your models here.
class Especialidade(models.Model):
    especialidade = models.CharField(max_length=150)

    def __str__(self):
        return self.especialidade


class Medico(models.Model):
    crm = models.IntegerField(null=False)
    nome = models.CharField(max_length=150, null=False, blank=False)
    especialidade = models.ForeignKey(Especialidade, models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    telefone = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.nome
