from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from backend.apps.clientes.models import Cliente


class ManageCliente(UserAdmin):
    list_display = ('id', 'username', 'email')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'email')
    list_per_page = 20


admin.site.register(Cliente, ManageCliente)
