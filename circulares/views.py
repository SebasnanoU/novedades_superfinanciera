from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from circulares.models import Circulares
from circulares.serializers import CircularesSerializer


class CircularesView(APIView):
    def get(self, request, format=None):
        circulares = Circulares.objects.all()
        serializer = CircularesSerializer(circulares, many=True)
        return Response(serializer.data)