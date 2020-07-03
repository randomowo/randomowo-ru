"""
"""
from challenges.models import FilmChallenge
from django import forms
from django.contrib import admin
from filmlist.forms import FilmAdminForm
from filmlist.forms import SeriesAdminForm
from filmlist.models import Director
from filmlist.models import Film
from filmlist.models import Series


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
        "year",
        "director",
        "is_watched",
        "is_movie",
        "episodes",
    ]

    def get_form(self, request, obj=None, **kwargs):
        if obj and obj.is_challenge:
            if "challenge_is_done" not in self.fields:
                self.fields.append("challenge_is_done")
        elif "challenge_is_done" in self.fields:
            self.fields.remove("challenge_is_done")
        return super(FilmAdmin, self).get_form(request, obj=obj, **kwargs)


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
admin.site.register(Director, DirectorAdmin)
admin.site.register(Series, SeriesAdmin)
