"""
"""
from django.db import models
from filmlist.models import Film


class FilmQueue(models.Model):
    """
    """
    film = models.ForeignKey(Film,
                             on_delete=models.PROTECT,
                             related_name="Queue",
                             verbose_name="Film",)

    class Meta:
        ordering = ["film"]
        verbose_name = "Film queue"
        verbose_name_plural = "Film queue"

    def __str__(self):
        return "{} ({})".format(self.film.name, self.film.year)
