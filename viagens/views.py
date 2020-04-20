from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from viagens.serializers import TravelSerialization
from viagens.models import Viagem


class TravelView(APIView):
    """
    The Travel is ApiView to managae Travels
    """

    # Set is necessary be Authenticated to access class
    permission_classes = [IsAuthenticated]

    def patch(self, request: 'Request', pk: int, format=None) -> Response:
        """
        Update Partial Travel Attributes

        Parameters:
        request (Request): Request from DRF
        pk (int): Id Travel

        """
        travel = Viagem.get_travel(request.user, pk)
        serializer = TravelSerialization(
            travel, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request: 'Request', pk: int = None, format=None) -> Response:
        """
        Return all Travels
        Parameters:
        request (Request): Request from DRF
        pk (int): Id Travel if None will return all Travel from User
        """

        if pk:
            travel = Viagem.get_travel(usuario=request.user, pk=pk)
            serializer = TravelSerialization(travel, many=False)
        else:
            travels = Viagem.get_travels(usuario=request.user)
            serializer = TravelSerialization(travels, many=True)

        return Response(serializer.data)
