"""
"""
from django.contrib import admin
from filmlist.models import Film


class FilmAdmin(admin.ModelAdmin):
    """
    """

    list_display = ["name"]


admin.site.register(Film, FilmAdmin)
