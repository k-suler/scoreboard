import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


class Game(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{} - {}".format(self.id, self.name)


class Score(models.Model):
    score = models.PositiveIntegerField(default=0)
    player = models.CharField(max_length=50)
    game = models.ForeignKey(Game, related_name='scores', on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} : {}".format(self.id, self.score, self.player)
