from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserSpotify(models.Model):

    display_name = models.CharField(max_length=50)
    spotify_id = models.IntegerField()
    profile_picture = models.CharField(max_length=300)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.display_name} {self.spotify_id}"

   