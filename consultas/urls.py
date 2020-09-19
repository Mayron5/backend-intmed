from rest_framework import routers
from django.urls import path
from django.conf.urls import include, url
from .views import (
    listar_consultas,
    detalhes_consulta,
    marcar_consulta
)



urlpatterns = [
    path('api/consultas/', include([
        path('', listar_consultas),
        path('', marcar_consulta),
        path('<int:pk>', detalhes_consulta),
    ]))

]
