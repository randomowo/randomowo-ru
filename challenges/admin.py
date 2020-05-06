"""
"""
from challenges.models import Challenge
from challenges.models import FilmChallenge
from django.contrib import admin


class ChallengeAdmin(admin.ModelAdmin):
    list_display = ["task"]


class FilmChallengeAdmin(admin.ModelAdmin):
    list_display = ["film"]


admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(FilmChallenge, FilmChallengeAdmin)
