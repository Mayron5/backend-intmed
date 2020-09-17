from django.urls import path
from django.conf.urls import include, url

from clientes.views import CriarCliente

urlpatterns = [
    path('', CriarCliente.as_view())
]
