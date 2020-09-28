"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns


from backend.apps.clientes.urls import urlpatterns as cliente_url
from backend.apps.medicos.urls import urlpatterns as medico_url
from backend.apps.consultas.urls import urlpatterns as consulta_url
from backend.apps.agendas.urls import urlpatterns as agenda_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += cliente_url
urlpatterns += medico_url
urlpatterns += consulta_url
urlpatterns += agenda_url

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])

admin.site.site_header = settings.ADMIN_SITE_HEADER
