from circulares.models import Circulares
from rest_framework import serializers


class CircularesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Circulares
        fields = ['link', 'titulo', 'intro', 'anexo', 'fecha']