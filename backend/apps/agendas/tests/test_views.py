from rest_framework import status
from .test_setup import TestSetUp
from ..models import Medico


class AgendaTestViews(TestSetUp):

    def test_listar_agendas_com_autenticacao(self):
        response = self.client.get(self.listar_agendas_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_detalhes_agendas_sem_autenticacao(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.listar_agendas_url)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
