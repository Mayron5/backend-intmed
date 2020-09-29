from rest_framework import status
from .test_setup import TestSetUp
from ..models import Cliente


class ClienteTestViews(TestSetUp):
    def test_registrar_cliente_sem_dados(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_nao_verificado(self):
        self.client.post(self.register_url, self.user_data, format='json')
        response = self.client.post(self.login_url, self.user_data,
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cliente_registrado_corretamente(self):
        response = self.client.post(self.register_url,
                                    self.user_data, format='json')

        self.assertEqual(response.data['email'], self.user_data['email'])
        self.assertEqual(response.data['username'], self.user_data['username'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
