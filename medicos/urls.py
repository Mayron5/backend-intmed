from django.urls import path
from django.conf.urls import include, url

from .views import ListarMedicos, DetalhesMedico, ListarEspecialidades

urlpatterns = [
    path('medicos/', include([
        path('', ListarMedicos.as_view()),
        path('<int:pk>', DetalhesMedico.as_view())
    ])),
    path('especialidades/', ListarEspecialidades.as_view())
]
