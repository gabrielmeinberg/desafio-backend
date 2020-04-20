from datetime import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from django.http import Http404
from django.db.models.query import QuerySet

from viagens.models import Classificacao, Viagem


class ClassificacaoTestCase(TestCase):
    def setUp(self):
        Classificacao.objects.create(classificacao='Trabalho')

    def test_classificacao_get(self):
        """ Get Rank correctly """
        classificacao = Classificacao.objects.get(classificacao='Trabalho')

        self.assertEqual(classificacao.classificacao, 'Trabalho')


class ViagemTestCase(TestCase):

    format = '%Y-%m-%dT%H:%M:%S%z'
    data_inicio = datetime.strptime(
        '2020-02-20T12:10:00Z', format)
    data_fim = datetime.strptime(
        '2020-02-20T12:20:00Z', format)

    def setUp(self):

        classificacao = Classificacao.objects.create(classificacao='Trabalho')
        user = User.objects.create_user(
            username='meinreno', email='gabriel@gabriel.com', password='top_secret')
        User.objects.create_user(
            username='meinreno2', email='gabriel2@gabriel.com', password='top_secret')
        Viagem.objects.create(
            usuario=user,
            data_inicio=self.data_inicio,
            data_fim=self.data_fim,
            classificacao=classificacao)

    def test_viagem_get(self):
        """ Get Travel """
        travel = Viagem.objects.filter(usuario__username='meinreno').first()
        self.assertEqual(travel.classificacao.classificacao, 'Trabalho')
        self.assertEqual(travel.data_inicio, self.data_inicio)
        self.assertEqual(travel.data_fim, self.data_fim)
        self.assertEqual(travel.nota, None)

    def test_get_travels_by_user(self):
        user = User.objects.get(username='meinreno')
        travels = Viagem.get_travels(user)
        self.assertEqual(type(travels), QuerySet)
        self.assertEqual(
            travels.first().classificacao.classificacao, 'Trabalho')
        self.assertEqual(travels.first().data_inicio, self.data_inicio)
        self.assertEqual(travels.first().data_fim, self.data_fim)
        self.assertEqual(travels.first().nota, None)

    def test_get_travel_doesnt_exist(self):
        user = User.objects.get(username='meinreno2')
        with self.assertRaises(Http404):
            Viagem.get_travels(user)

    def test_get_travel_by_user_id(self):
        travel = Viagem.objects.first()

        travel_get = Viagem.get_travel(travel.usuario, travel.id)

        self.assertEqual(
            travel_get.classificacao.classificacao, 'Trabalho')
        self.assertEqual(travel_get.data_inicio, self.data_inicio)
        self.assertEqual(travel_get.data_fim, self.data_fim)
        self.assertEqual(travel_get.nota, None)

    def test_try_get_travel_from_other_user(self):
        user2 = User.objects.get(username='meinreno2')
        travel = Viagem.objects.filter(usuario__username='meinreno').first()
        with self.assertRaises(Http404):
            Viagem.get_travel(user2, travel.id)

    def test_try_get_travel_doesnt_exist(self):
        user = User.objects.get(username='meinreno')
        with self.assertRaises(Http404):
            Viagem.get_travel(user, 999)
