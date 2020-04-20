from datetime import datetime

from django.test import TestCase
from django.contrib.auth.models import User

from viagens.models import Viagem, Classificacao
from viagens.serializers import TravelSerialization


class TravelSerializationTest(TestCase):
    format = '%Y-%m-%dT%H:%M:%S%z'
    data_inicio = datetime.strptime(
        '2020-02-20T12:10:00Z', format)
    data_fim = datetime.strptime(
        '2020-02-20T12:20:00Z', format)

    def setUp(self):

        self.classificacao = Classificacao.objects.create(
            classificacao='Trabalho')
        self.user = User.objects.create_user(
            username='meinreno', email='gabriel@gabriel.com',
            password='top_secret')
        self.travel = Viagem.objects.create(
            usuario=self.user,
            data_inicio=self.data_inicio,
            data_fim=self.data_fim,
            classificacao=self.classificacao)

        self.serializer = TravelSerialization(self.travel, many=False)

    def test_get_travel_serialization(self):
        response = {
            'usuario': 1,
            'data_inicio': '2020-02-20T12:10:00Z',
            'data_fim': '2020-02-20T12:20:00Z',
            'classificacao': 1,
            'nota': None}

        self.assertEqual(self.serializer.data, response)
