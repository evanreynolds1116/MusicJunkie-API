from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from musicapp.models import UserSpotify

class Album(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    album_artist = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100)
    album_image = models.CharField(max_length=100)
    album_rating = models.DecimalField(max_digits=3, decimal_places=1)
    album_id = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = ("album")
        verbose_name_plural = ("albums")

    def __str__(self):
        return self.album_name