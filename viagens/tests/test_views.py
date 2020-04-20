from datetime import datetime

from django.contrib.auth.models import User
from django.urls import reverse
from django.http import Http404

from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from viagens.models import Viagem, Classificacao
from viagens.views import TravelView


class TravelViewTest(APITestCase):
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

        self.factory = APIRequestFactory()

        self.view = TravelView.as_view()

    def test_get_travel_from_user(self):
        url = reverse('list-travels')

        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = self.view(request)

        self.assertEquals(response.status_code, 200)

    def test_get_travel_by_user_and_id(self):
        url = reverse('details-travel', kwargs={'pk': self.travel.id})
        request = self.factory.get(url)
        force_authenticate(request, user=self.user)
        response = self.view(request, pk=self.travel.id)

        expect_result = {'usuario': 1, 'data_inicio': '2020-02-20T12:10:00Z',
                         'data_fim': '2020-02-20T12:20:00Z', 'classificacao': 1, 'nota': None}
        self.assertEquals(response.status_code, 200)
        self.assertEquals(dict(response.data), expect_result)

    def test_update_rank_from_travel(self):
        url = reverse('details-travel', kwargs={'pk': self.travel.id})

        request = self.factory.patch(url, {'nota': 5}, format='json')

        force_authenticate(request, user=self.user)
        response = self.view(request, pk=self.travel.id)
        expect_result = {'usuario': 1, 'data_inicio': '2020-02-20T12:10:00Z',
                         'data_fim': '2020-02-20T12:20:00Z', 'classificacao': 1, 'nota': 5}
        self.assertEquals(response.status_code, 200)
        self.assertEquals(dict(response.data), expect_result)

    def test_get_travel_doesnt_exists(self):
        url = reverse('details-travel', kwargs={'pk': 25})

        request = self.factory.get(url)

        force_authenticate(request, user=self.user)
        response = self.view(request, pk=25)

        self.assertEquals(response.status_code, 404)
