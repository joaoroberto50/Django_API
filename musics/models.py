from django.db import models
import uuid

# Create your models here.


class Music(models.Model):
    id_music = models.AutoField(
        primary_key=True,
        editable=False,
        unique=True
    )
    title = models.CharField(
        max_length=255
    )
    author = models.CharField(
        max_length=255
    )
    album = models.CharField(
        max_length=255
    )
    duration = models.IntegerField(
        default=0
    )
    year = models.IntegerField(
        default=0
    )
    genre = models.CharField(
        max_length=255
    )
    add_date = models.DateField(
        auto_now_add=True
    )
