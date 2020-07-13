"""
"""
from django import forms
from django.contrib import admin

from challenges.models import FilmChallenge
from filmlist.forms import FilmAdminForm
from filmlist.forms import SeasonAdminForm
from filmlist.models import Episode
from filmlist.models import Season
from filmlist.models import Film


class FilmAdmin(admin.ModelAdmin):
    """
    """

    form = FilmAdminForm
    list_filter = [
        "is_watched",
    ]
    search_fields = [
        "title",
        "year",
    ]
    fields = [
        "title",
        "film_url",
        "director",
        "year",
        "is_watched",
        "is_movie",
    ]


class SeasonAdmin(admin.ModelAdmin):
    """
    """
    form = SeasonAdminForm
    list_display = ["number"]



class EpisodeAdmin(admin.ModelAdmin):
    """
    """

    model = Episode
    fields = [
        "season",
        "number",
        "title",
        "duration",
    ]
    list_display = ["number"]


admin.site.register(Film, FilmAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Episode, EpisodeAdmin)
