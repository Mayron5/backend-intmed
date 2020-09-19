from django.contrib import admin
# Register your models here.

from backend.apps.medicos.models import Especialidade, Medico


class ManageMedico(admin.ModelAdmin):
    list_display = ('id', 'nome', 'especialidade')
    display_filter = ('especialidade', )
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20


class ManageEspecialidade(admin.ModelAdmin):
    list_display = ('id', 'especialidade')
    list_display_links = ('id', 'especialidade')
    search_fields = ('especialidade',)
    list_per_page = 20


admin.site.register(Medico, ManageMedico)
admin.site.register(Especialidade, ManageEspecialidade)
