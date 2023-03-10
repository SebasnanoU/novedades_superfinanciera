from rest_framework import serializers

from novedades.models import Novedades

class NovedadesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Novedades
        fields = ['link', 'titulo', 'intro']