from rest_framework import viewsets
from musics.api import serializers
from musics import models


class MusicViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MusicSerializer
    queryset = models.Music.objects.all()
