from django.contrib import admin
from .models import Score, Game


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    fields = ('player', 'score', 'game')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    fields = ('name',)
