from rest_framework import status
from .test_setup import TestSetUp
from ..models import Medico


class MedicoTestViews(TestSetUp):

    def test_listar_medicos_com_autenticacao(self):
        response = self.client.get(self.listar_medico_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_detalhes_medico_com_autenticacao(self):
        response = self.client.get(self.detalhes_medico_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_listar_especialidades_com_autenticacao(self):
        response = self.client.get(self.listar_especialidades_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_detalhes_especialidade_com_autenticacao(self):
        response = self.client.get(self.detalhes_especialidade_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_listar_medicos_sem_autenticacao(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.listar_medico_url)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_detalhes_medico_sem_autenticacao(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.detalhes_medico_url)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_listar_especialidades_sem_autenticacao(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.listar_especialidades_url)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_detalhes_especialidade_sem_autenticacao(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.detalhes_especialidade_url)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)
