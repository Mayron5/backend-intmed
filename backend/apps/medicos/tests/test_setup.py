from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.urls import reverse
from faker import Faker
import random

from backend.apps.clientes.models import Cliente

from ..models import Medico, Especialidade

ESPECIALIDADES = [
    'Pediatra',
    'Cardiologista',
    'Neurologista',
    'Nefrologista',
    'Radiologista',
    'Geral'
]


class TestSetUp(APITestCase):
    def setUp(self):
        self.fake = Faker()

        self.cliente = Cliente.objects.create_user(
            username=self.fake.email().split('@')[0],
            email=self.fake.email(),
            password=self.fake.email()
        )

        self.token = Token.objects.get(user=self.cliente)

        self.especialidade = Especialidade.objects.create(
            especialidade=random.randint(0, 5)
        )

        self.medico = Medico.objects.create(
            crm=random.randint(1000, 9999),
            nome=self.fake.first_name(),
            especialidade=self.especialidade,
            email=self.fake.email()
        )

        self.login_url = reverse('login')

        self.listar_medico_url = reverse('listar_medicos')
        self.detalhes_medico_url = reverse('detalhes_medico', kwargs={'pk': 1})
        self.listar_especialidades_url = reverse('listar_especialidades')
        self.detalhes_especialidade_url = reverse('detalhes_especialidade',
                                                  kwargs={'pk': 1})

        self.api_authentication()

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
