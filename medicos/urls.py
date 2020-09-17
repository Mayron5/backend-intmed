from django.urls import path
from django.conf.urls import include, url

from .views import (
     ListarMedicos,
     DetalhesMedico,
     ListarEspecialidades,
     DetalhesEspecialidade
)

urlpatterns = [
    path('medicos/', include([
        path('', ListarMedicos.as_view()),
        path('<int:pk>', DetalhesMedico.as_view())
    ])),
    path('especialidades/', include([
        path('', ListarEspecialidades.as_view()),
        path('<int:pk>', DetalhesEspecialidade.as_view())
    ]))
]
