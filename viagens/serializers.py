from rest_framework import serializers

from viagens.models import Viagem

class TravelSerialization(serializers.ModelSerializer):

    class Meta:
        model = Viagem
        fields = ['usuario', 'data_inicio', 'data_fim', 'classificacao', 'nota']