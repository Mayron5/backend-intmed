from django.urls import path
from django.conf.urls import include, url

from backend.apps.clientes.views import criar_cliente

urlpatterns = [
    path('api/', criar_cliente)
]
