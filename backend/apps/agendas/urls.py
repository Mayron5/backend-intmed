from django.urls import path
from django.conf.urls import include, url

from backend.apps.agendas.views import listar_agendas

urlpatterns = [
    path('api/agendas', listar_agendas, name='listar_agendas')
]
