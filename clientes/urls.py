from django.urls import path
from django.conf.urls import include, url

from .views import criar_cliente

urlpatterns = [
    path('api/', criar_cliente)
]
