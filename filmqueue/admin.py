"""
"""
from django.contrib import admin
from filmqueue.models import FilmQueue

class FilmQueueAdmin(admin.ModelAdmin):
    """
    """
    list_display = ["film"]

admin.site.register(FilmQueue, FilmQueueAdmin)
