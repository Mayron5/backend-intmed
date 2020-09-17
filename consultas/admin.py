from django.contrib import admin
from consultas.models import Consulta


class ManageConsulta(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'medico', 'dia')
    search_fields = ('dia', 'medico__nome', 'id')
    list_per_page = 20

admin.site.register(Consulta, ManageConsulta)
