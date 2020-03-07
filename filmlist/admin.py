"""
"""
from django.contrib import admin
from filmlist.models import Actor
from filmlist.models import Director
from filmlist.models import Film
from filmlist.models import Series


class FilmAdmin(admin.ModelAdmin):
    """
    """

    list_display = ["title"]


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

    list_display = ["film"]


admin.site.register(Film, FilmAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Series, SeriesAdmin)
