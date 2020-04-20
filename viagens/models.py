from typing import List

from django.http import Http404
from django.db import models
from django.contrib.auth.models import User


class Classificacao(models.Model):
    classificacao = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Classificacao"
        verbose_name_plural = "Classificacoes"

    def __str__(self):
        return self.classificacao


class Viagem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    classificacao = models.ForeignKey(Classificacao, on_delete=models.PROTECT)
    nota = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Viagem"
        verbose_name_plural = "Viagens"

    def __str__(self):
        return self.usuario.email

    @classmethod
    def get_travel(cls, usuario: 'User', pk: int) -> 'Viagem':
        """ 
        Get Travel

        Parameters:
        usuario (User): User that return from Request
        pk (int): Travel's id

        Return:
        Viagem:  Object from Model Travel
        """

        try:
            return Viagem.objects.get(usuario=usuario, pk=pk)

        except Viagem.DoesNotExist:
            raise Http404
    
    @classmethod
    def get_travels(cls, usuario: 'User') -> 'Queryset':
        """ 
        Get Travels

        Parameters:
        usuario (User): User that return from Request

        Return:
        List[Viagem]:  List of Travel from a User
        """
        travels = Viagem.objects.filter(usuario=usuario)

        if not travels:
            raise Http404

        return travels
       
