from django.contrib import admin
from backend.apps.agendas.models import Agenda, Horario


class ManageAgenda(admin.ModelAdmin):
    list_display = ('medico', 'dia')
    search_fields = ('medico__nome', 'dia')
    list_per_page = 20

class ManageHorario(admin.ModelAdmin):
    list_display = ('id', 'horario', 'agenda')
    list_per_page = 20

admin.site.register(Agenda, ManageAgenda)
admin.site.register(Horario, ManageHorario)
