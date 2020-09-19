from rest_framework import routers
from django.urls import path
from django.conf.urls import include, url
from backend.apps.consultas.views import (
    listar_consultas,
    marcar_consulta,
    detalhes_consulta
)



urlpatterns = [
    path('api/consultas/', listar_consultas),
    path('api/consultas/', marcar_consulta),
    path('api/consultas/<int:pk>', detalhes_consulta),
]
