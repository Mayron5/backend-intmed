from rest_framework import routers
from django.urls import path
from django.conf.urls import include, url
from .views import (
    listar_consultas,
    detalhes_consulta
)



urlpatterns = [
    # path('api/consultas/', include([
    #     path('', ListarConsultas.as_view()),
    #     path('<int:pk>', DetalhesConsulta.as_view()),
    # ]))
    path('api/consultas/', listar_consultas),
    path('api/consultas/<int:pk>', detalhes_consulta),
]
