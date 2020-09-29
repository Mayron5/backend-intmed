from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.urls import reverse
from faker import Faker
import datetime
import random

from backend.apps.clientes.models import Cliente
from backend.apps.medicos.models import Medico, Especialidade
from ..models import Agenda, Horario


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

        self.agenda = Agenda.objects.create(
            medico=self.medico,
            dia=datetime.datetime(2020, 12, 25),
        )

        self.horario = Horario.objects.create(
            agenda=self.agenda,
            horario=datetime.time(17, 00, 00)
        )

        self.listar_agendas_url = reverse('listar_agendas')

        self.api_authentication()

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
