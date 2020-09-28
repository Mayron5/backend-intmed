from rest_framework import routers
from django.urls import path
from django.conf.urls import include, url
from backend.apps.consultas.views import (
    listar_marcar_consultas,
    detalhes_deletar_consulta
)


urlpatterns = [
    path('api/consultas/', listar_marcar_consultas),
    path('api/consultas/<int:pk>', detalhes_deletar_consulta),
]
