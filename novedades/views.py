from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from novedades.serializers import NovedadesSerializer
from novedades.models import Novedades

class NovedadesView(APIView):
    def get(self, request, format=None):
        novedades = Novedades.objects.all()
        serializer = NovedadesSerializer(novedades, many=True)
        return Response(serializer.data)