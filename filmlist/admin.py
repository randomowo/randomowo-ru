"""
"""
from django import forms
from django.contrib import admin
from filmlist.forms import FilmAdminForm
from filmlist.forms import SeriesAdminForm
from filmlist.models import Actor
from filmlist.models import Director
from filmlist.models import Film
from filmlist.models import Series


class FilmAdmin(admin.ModelAdmin):
    """
    """

    form = FilmAdminForm
    fields = [
        "title",
        "year",
        "director",
        "actor",
        "rating",
        "is_watched",
        "is_movie",
        "episodes",
    ]


class ActorAdmin(admin.ModelAdmin):
    """
    """

    list_display = ["name"]


class DirectorAdmin(admin.ModelAdmin):
    """
    """

    list_display = ["name"]


class SeriesAdmin(admin.ModelAdmin):
    """
    """

    form = SeriesAdminForm
    list_display = ["film"]


admin.site.register(Film, FilmAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Series, SeriesAdmin)
